from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path


from scripts.provider_promotion_gate import run_gate


class ProviderPromotionGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="ips-provider-promotion-gate-test-"))
        self.write(
            "docs/23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md",
            "# Embedding Provider Safety Gates\n\nContent.\n",
        )
        self.write_json(
            "config/embedding_provider_gates.json",
            {
                "schema_version": "1.0.0",
                "active_provider": "external-provider-dry-run",
                "providers": [
                    {
                        "id": "external-provider-dry-run",
                        "status": "approved",
                        "environment": "offline",
                        "credential_mode": "none",
                        "allows_external_network": False,
                        "dry_run": True,
                        "allowed_data_classifications": ["none", "synthetic"],
                        "human_review_required": True,
                        "data_boundary_document": "../docs/23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md",
                    }
                ],
            },
        )
        self.write_json(
            "config/provider_promotion_rules.json",
            {
                "schema_version": "1.0.0",
                "providers": [
                    {
                        "id": "external-provider-dry-run",
                        "from_stage": "experimental",
                        "to_stage": "approved_candidate",
                        "required_candidate_mode": "external-provider-dry-run",
                        "min_pass_rate": 1.0,
                        "max_failed_cases": 0,
                        "max_unexpected_paths": 0,
                        "require_provider_gate_pass": True,
                        "require_dry_run": True,
                        "require_zero_network_calls": True,
                    }
                ],
            },
        )
        self.baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            {
                "cases": [
                    {
                        "id": "dry-run-support",
                        "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"],
                    }
                ]
            },
        )
        self.candidate = self.write_json(
            "tests/fixtures/retrieval_candidate_dry_run.json",
            {
                "retrieval_mode": "external-provider-dry-run",
                "embedding_provider": "external-provider-dry-run",
                "dry_run": True,
                "network_calls": 0,
                "cases": [
                    {
                        "id": "dry-run-support",
                        "returned_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"],
                        "dry_run": True,
                    }
                ],
            },
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def write(self, rel: str, text: str) -> Path:
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_json(self, rel: str, data: dict[str, object]) -> Path:
        return self.write(rel, json.dumps(data))

    def test_provider_promotion_gate_passes_dry_run_candidate(self) -> None:
        report = run_gate(
            self.tmp,
            baseline_path=self.baseline,
            candidate_path=self.candidate,
            provider_id="external-provider-dry-run",
        )

        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["from_stage"], "experimental")
        self.assertEqual(report["to_stage"], "approved_candidate")
        self.assertEqual(report["metrics"]["pass_rate"], 1.0)
        self.assertEqual(report["metrics"]["network_calls"], 0)

    def test_provider_promotion_gate_fails_failed_comparison(self) -> None:
        candidate = self.write_json(
            "tests/fixtures/bad_candidate.json",
            {
                "retrieval_mode": "external-provider-dry-run",
                "embedding_provider": "external-provider-dry-run",
                "dry_run": True,
                "network_calls": 0,
                "cases": [
                    {
                        "id": "dry-run-support",
                        "returned_optional_paths": ["docs/06_architecture/WRONG.md"],
                        "dry_run": True,
                    }
                ],
            },
        )

        report = run_gate(
            self.tmp,
            baseline_path=self.baseline,
            candidate_path=candidate,
            provider_id="external-provider-dry-run",
        )

        finding_types = {finding["type"] for finding in report["findings"]}
        self.assertEqual(report["status"], "fail")
        self.assertIn("pass_rate_below_threshold", finding_types)
        self.assertIn("failed_cases_above_threshold", finding_types)
        self.assertIn("unexpected_paths_above_threshold", finding_types)

    def test_provider_promotion_gate_requires_dry_run_and_zero_network(self) -> None:
        candidate = self.write_json(
            "tests/fixtures/network_candidate.json",
            {
                "retrieval_mode": "external-provider-dry-run",
                "embedding_provider": "external-provider-dry-run",
                "dry_run": False,
                "network_calls": 1,
                "cases": [
                    {
                        "id": "dry-run-support",
                        "returned_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"],
                    }
                ],
            },
        )

        report = run_gate(
            self.tmp,
            baseline_path=self.baseline,
            candidate_path=candidate,
            provider_id="external-provider-dry-run",
        )

        finding_types = {finding["type"] for finding in report["findings"]}
        self.assertEqual(report["status"], "fail")
        self.assertIn("dry_run_required", finding_types)
        self.assertIn("zero_network_calls_required", finding_types)

    def test_provider_promotion_gate_requires_candidate_mode(self) -> None:
        candidate = self.write_json(
            "tests/fixtures/wrong_mode_candidate.json",
            {
                "retrieval_mode": "local-embedding-index",
                "embedding_provider": "external-provider-dry-run",
                "dry_run": True,
                "network_calls": 0,
                "cases": [
                    {
                        "id": "dry-run-support",
                        "returned_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"],
                    }
                ],
            },
        )

        report = run_gate(
            self.tmp,
            baseline_path=self.baseline,
            candidate_path=candidate,
            provider_id="external-provider-dry-run",
        )

        self.assertEqual(report["status"], "fail")
        self.assertIn("candidate_mode_mismatch", {finding["type"] for finding in report["findings"]})


if __name__ == "__main__":
    unittest.main()
