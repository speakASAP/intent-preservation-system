#!/usr/bin/env python3
"""Provider candidate promotion gate."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.context_package_generator import compare_candidate_retrieval
from scripts.embedding_provider_gate import run_gate as run_embedding_provider_gate


RULES_PATH = "config/provider_promotion_rules.json"
REPORT_PATH = "reports/validation/ips-provider-promotion-gate.json"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _finding(kind: str, provider_id: str, message: str) -> dict[str, str]:
    return {
        "type": kind,
        "provider": provider_id,
        "message": message,
    }


def _load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def _promotion_rule(root: Path, rules_path: str, provider_id: str) -> tuple[dict[str, Any], list[dict[str, str]]]:
    rules_file = root / rules_path
    if not rules_file.is_file():
        return {}, [_finding("missing_promotion_rules", provider_id, f"Missing {rules_path}.")]
    rules = _load_json(rules_file)
    providers = rules.get("providers")
    if not isinstance(providers, list):
        return {}, [_finding("invalid_promotion_rules", provider_id, "providers must be a list.")]
    for item in providers:
        if isinstance(item, dict) and str(item.get("id")) == provider_id:
            return item, []
    return {}, [_finding("missing_provider_rule", provider_id, "Provider has no promotion rule.")]


def _unexpected_path_count(comparison: dict[str, Any]) -> int:
    count = 0
    for case in comparison.get("cases", []):
        if isinstance(case, dict):
            unexpected = case.get("unexpected_candidate_paths")
            if isinstance(unexpected, list):
                count += len(unexpected)
    return count


def run_gate(
    root: Path,
    *,
    baseline_path: Path,
    candidate_path: Path,
    provider_id: str,
    rules_path: str = RULES_PATH,
) -> dict[str, Any]:
    root = root.resolve()
    findings: list[dict[str, str]] = []
    rule, rule_findings = _promotion_rule(root, rules_path, provider_id)
    findings.extend(rule_findings)
    candidate = _load_json(candidate_path)
    comparison = compare_candidate_retrieval(baseline_path, candidate_path)
    provider_gate = run_embedding_provider_gate(root)

    total_cases = int(comparison.get("total_cases", 0))
    passed_cases = int(comparison.get("passed_cases", 0))
    failed_cases = int(comparison.get("failed_cases", 0))
    pass_rate = passed_cases / total_cases if total_cases else 0.0
    unexpected_paths = _unexpected_path_count(comparison)
    candidate_mode = str(candidate.get("retrieval_mode") or "")

    if rule:
        required_mode = str(rule.get("required_candidate_mode") or "")
        if required_mode and candidate_mode != required_mode:
            findings.append(
                _finding(
                    "candidate_mode_mismatch",
                    provider_id,
                    f"Candidate mode {candidate_mode} does not match required mode {required_mode}.",
                )
            )
        min_pass_rate = float(rule.get("min_pass_rate", 1.0))
        if pass_rate < min_pass_rate:
            findings.append(
                _finding(
                    "pass_rate_below_threshold",
                    provider_id,
                    f"Pass rate {pass_rate:.3f} is below threshold {min_pass_rate:.3f}.",
                )
            )
        max_failed_cases = int(rule.get("max_failed_cases", 0))
        if failed_cases > max_failed_cases:
            findings.append(
                _finding(
                    "failed_cases_above_threshold",
                    provider_id,
                    f"Failed cases {failed_cases} exceed threshold {max_failed_cases}.",
                )
            )
        max_unexpected_paths = int(rule.get("max_unexpected_paths", 0))
        if unexpected_paths > max_unexpected_paths:
            findings.append(
                _finding(
                    "unexpected_paths_above_threshold",
                    provider_id,
                    f"Unexpected paths {unexpected_paths} exceed threshold {max_unexpected_paths}.",
                )
            )
        if bool(rule.get("require_provider_gate_pass")) and provider_gate["status"] != "pass":
            findings.append(
                _finding(
                    "provider_gate_failed",
                    provider_id,
                    "Embedding provider safety gate must pass before promotion.",
                )
            )
        if bool(rule.get("require_dry_run")) and candidate.get("dry_run") is not True:
            findings.append(
                _finding(
                    "dry_run_required",
                    provider_id,
                    "Provider candidate must be marked dry_run true.",
                )
            )
        if bool(rule.get("require_zero_network_calls")) and int(candidate.get("network_calls", -1)) != 0:
            findings.append(
                _finding(
                    "zero_network_calls_required",
                    provider_id,
                    "Provider candidate must report network_calls 0.",
                )
            )

    report: dict[str, Any] = {
        "schema_version": "1.0.0",
        "created_at": _utc_now(),
        "gate": "provider_promotion",
        "root": str(root),
        "provider": provider_id,
        "rules_path": rules_path,
        "baseline_path": baseline_path.as_posix(),
        "candidate_path": candidate_path.as_posix(),
        "from_stage": rule.get("from_stage") if rule else None,
        "to_stage": rule.get("to_stage") if rule else None,
        "status": "fail" if findings else "pass",
        "metrics": {
            "total_cases": total_cases,
            "passed_cases": passed_cases,
            "failed_cases": failed_cases,
            "pass_rate": pass_rate,
            "unexpected_paths": unexpected_paths,
            "candidate_mode": candidate_mode,
            "dry_run": bool(candidate.get("dry_run")),
            "network_calls": int(candidate.get("network_calls", -1)),
        },
        "provider_gate": {
            "status": provider_gate["status"],
            "report_path": provider_gate.get("report_path"),
        },
        "comparison": comparison,
        "findings": findings,
        "next_step": "provider_candidate_promotable" if not findings else "fix_provider_promotion_findings",
    }

    output_path = root / REPORT_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report["report_path"] = REPORT_PATH
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the IPS provider promotion gate.")
    parser.add_argument("--root", required=True, help="Repository root.")
    parser.add_argument("--baseline", required=True, help="Retrieval baseline JSON path.")
    parser.add_argument("--candidate", required=True, help="Candidate retrieval JSON path.")
    parser.add_argument("--provider", required=True, help="Provider id to evaluate.")
    parser.add_argument("--rules", default=RULES_PATH, help="Promotion rules path relative to root.")
    args = parser.parse_args()

    report = run_gate(
        Path(args.root),
        baseline_path=Path(args.baseline),
        candidate_path=Path(args.candidate),
        provider_id=args.provider,
        rules_path=args.rules,
    )
    print(f"{report['status'].upper()} provider_promotion_gate report={report['report_path']}")
    if report["status"] != "pass":
        print(json.dumps({"findings": report["findings"], "metrics": report["metrics"]}, indent=2, sort_keys=True))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
