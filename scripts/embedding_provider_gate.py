#!/usr/bin/env python3
"""Embedding provider credential, environment and sensitive-data gate."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CONFIG_PATH = "config/embedding_provider_gates.json"
REPORT_PATH = "reports/validation/ips-embedding-provider-gate.json"
ALLOWED_ENVIRONMENTS = {"local", "controlled_external", "offline"}
ALLOWED_CREDENTIAL_MODES = {"none", "env_reference", "secret_manager_reference"}
ALLOWED_CLASSIFICATIONS = {"none", "synthetic", "masked"}
SECRET_VALUE_RE = re.compile(
    r"(?i)(sk-[A-Za-z0-9_-]{12,}|[A-Za-z0-9_./+=:-]{24,})"
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _finding(kind: str, provider_id: str, message: str) -> dict[str, str]:
    return {
        "type": kind,
        "provider": provider_id,
        "message": message,
    }


def _looks_like_secret(value: str) -> bool:
    if not value:
        return False
    if value.startswith(("ENV:", "SECRET:", "example.", "https://example.invalid/")):
        return False
    return bool(SECRET_VALUE_RE.search(value))


def _provider_findings(root: Path, provider: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    provider_id = str(provider.get("id") or "")
    if not provider_id:
        findings.append(_finding("missing_provider_id", "", "Provider entry must declare an id."))
        provider_id = "<missing>"

    environment = str(provider.get("environment") or "")
    if environment not in ALLOWED_ENVIRONMENTS:
        findings.append(
            _finding(
                "invalid_environment",
                provider_id,
                f"Environment must be one of {sorted(ALLOWED_ENVIRONMENTS)}.",
            )
        )

    credential_mode = str(provider.get("credential_mode") or "")
    if credential_mode not in ALLOWED_CREDENTIAL_MODES:
        findings.append(
            _finding(
                "invalid_credential_mode",
                provider_id,
                f"Credential mode must be one of {sorted(ALLOWED_CREDENTIAL_MODES)}.",
            )
        )

    credential_reference = str(provider.get("credential_reference") or "")
    if credential_mode == "none" and credential_reference:
        findings.append(
            _finding(
                "credential_reference_not_allowed",
                provider_id,
                "Providers with credential_mode none must not declare credential references.",
            )
        )
    if credential_mode != "none" and not credential_reference:
        findings.append(
            _finding(
                "missing_credential_reference",
                provider_id,
                "Credentialed providers must declare an environment or secret-manager reference.",
            )
        )
    if _looks_like_secret(credential_reference):
        findings.append(
            _finding(
                "credential_value_detected",
                provider_id,
                "Provider registry must store references only, not credential values.",
            )
        )

    classifications = provider.get("allowed_data_classifications")
    if not isinstance(classifications, list) or not classifications:
        findings.append(
            _finding(
                "missing_allowed_classifications",
                provider_id,
                "Provider must declare allowed data classifications.",
            )
        )
    else:
        for item in classifications:
            classification = str(item)
            if classification == "sensitive":
                findings.append(
                    _finding(
                        "sensitive_classification_not_allowed",
                        provider_id,
                        "Embedding providers must not be approved for sensitive data in IPS artifacts.",
                    )
                )
            elif classification not in ALLOWED_CLASSIFICATIONS:
                findings.append(
                    _finding(
                        "invalid_data_classification",
                        provider_id,
                        f"Classification {classification} is not allowed.",
                    )
                )

    allows_external_network = bool(provider.get("allows_external_network"))
    dry_run = bool(provider.get("dry_run"))
    if dry_run:
        if environment != "offline":
            findings.append(
                _finding(
                    "dry_run_requires_offline_environment",
                    provider_id,
                    "Dry-run providers must use environment offline.",
                )
            )
        if credential_mode != "none":
            findings.append(
                _finding(
                    "dry_run_requires_no_credentials",
                    provider_id,
                    "Dry-run providers must not declare credentials.",
                )
            )
        if allows_external_network:
            findings.append(
                _finding(
                    "dry_run_requires_no_network",
                    provider_id,
                    "Dry-run providers must not allow external network access.",
                )
            )
        if provider.get("human_review_required") is not True:
            findings.append(
                _finding(
                    "dry_run_requires_human_review",
                    provider_id,
                    "Dry-run providers require human_review_required true.",
                )
            )

    if allows_external_network:
        if provider.get("status") != "approved_external":
            findings.append(
                _finding(
                    "external_provider_not_approved",
                    provider_id,
                    "External providers require status approved_external.",
                )
            )
        if provider.get("human_review_required") is not True:
            findings.append(
                _finding(
                    "external_provider_requires_human_review",
                    provider_id,
                    "External providers require human_review_required true.",
                )
            )
        if credential_mode == "none":
            findings.append(
                _finding(
                    "external_provider_requires_credentials",
                    provider_id,
                    "External providers must declare a credential reference mode.",
                )
            )

    boundary = str(provider.get("data_boundary_document") or "")
    if not boundary:
        findings.append(
            _finding(
                "missing_data_boundary_document",
                provider_id,
                "Provider must declare a data boundary document.",
            )
        )
    else:
        boundary_path = (root / boundary.removeprefix("../")).resolve()
        try:
            boundary_path.relative_to(root.resolve())
        except ValueError:
            findings.append(
                _finding(
                    "data_boundary_outside_root",
                    provider_id,
                    "Data boundary document must stay inside the repository.",
                )
            )
        if not boundary_path.is_file():
            findings.append(
                _finding(
                    "missing_data_boundary_file",
                    provider_id,
                    "Data boundary document does not exist.",
                )
            )

    return findings


def run_gate(root: Path, config_path: str = CONFIG_PATH) -> dict[str, Any]:
    root = root.resolve()
    config_file = root / config_path
    findings: list[dict[str, str]] = []
    providers: list[dict[str, Any]] = []
    active_provider = ""

    if not config_file.is_file():
        findings.append(_finding("missing_provider_registry", "", f"Missing {config_path}."))
    else:
        config = json.loads(config_file.read_text(encoding="utf-8"))
        active_provider = str(config.get("active_provider") or "")
        raw_providers = config.get("providers")
        if isinstance(raw_providers, list):
            providers = [provider for provider in raw_providers if isinstance(provider, dict)]
        else:
            findings.append(_finding("invalid_provider_registry", "", "providers must be a list."))

        provider_ids = {str(provider.get("id")) for provider in providers}
        if not active_provider:
            findings.append(_finding("missing_active_provider", "", "active_provider must be declared."))
        elif active_provider not in provider_ids:
            findings.append(
                _finding(
                    "unknown_active_provider",
                    active_provider,
                    "active_provider must match a declared provider id.",
                )
            )

        for provider in providers:
            findings.extend(_provider_findings(root, provider))

    report: dict[str, Any] = {
        "schema_version": "1.0.0",
        "created_at": _utc_now(),
        "gate": "embedding_provider",
        "root": str(root),
        "config_path": config_path,
        "active_provider": active_provider,
        "provider_count": len(providers),
        "status": "fail" if findings else "pass",
        "findings": findings,
        "next_step": "embedding_provider_review_passed" if not findings else "fix_embedding_provider_gate_findings",
    }

    output_path = root / REPORT_PATH
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report["report_path"] = REPORT_PATH
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the IPS embedding provider safety gate.")
    parser.add_argument("--root", required=True, help="Repository root.")
    parser.add_argument("--config", default=CONFIG_PATH, help="Provider registry path relative to root.")
    args = parser.parse_args()

    report = run_gate(Path(args.root), config_path=args.config)
    print(f"{report['status'].upper()} embedding_provider_gate report={report['report_path']}")
    if report["status"] != "pass":
        print(json.dumps({"findings": report["findings"]}, indent=2, sort_keys=True))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
