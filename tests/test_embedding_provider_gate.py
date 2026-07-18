from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path


from scripts.embedding_provider_gate import run_gate


class EmbeddingProviderGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="ips-embedding-provider-gate-test-"))
        self.write(
            "docs/23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md",
            "# Embedding Provider Safety Gates\n\nContent.\n",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def write(self, rel: str, text: str) -> None:
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def write_config(self, data: dict[str, object]) -> None:
        self.write("config/embedding_provider_gates.json", json.dumps(data))

    def valid_config(self) -> dict[str, object]:
        return {
            "schema_version": "1.0.0",
            "active_provider": "local-hash",
            "providers": [
                {
                    "id": "local-hash",
                    "status": "approved",
                    "environment": "local",
                    "credential_mode": "none",
                    "allows_external_network": False,
                    "allowed_data_classifications": ["none", "synthetic"],
                    "human_review_required": False,
                    "data_boundary_document": "../docs/23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md",
                }
            ],
        }

    def test_embedding_provider_gate_passes_local_provider(self) -> None:
        self.write_config(self.valid_config())

        report = run_gate(self.tmp)

        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["active_provider"], "local-hash")
        self.assertEqual(report["provider_count"], 1)
        self.assertEqual(report["findings"], [])

    def test_embedding_provider_gate_rejects_missing_registry(self) -> None:
        report = run_gate(self.tmp)

        self.assertEqual(report["status"], "fail")
        self.assertEqual(report["findings"][0]["type"], "missing_provider_registry")

    def test_embedding_provider_gate_rejects_unknown_active_provider(self) -> None:
        config = self.valid_config()
        config["active_provider"] = "external"
        self.write_config(config)

        report = run_gate(self.tmp)

        self.assertEqual(report["status"], "fail")
        self.assertIn("unknown_active_provider", {finding["type"] for finding in report["findings"]})

    def test_embedding_provider_gate_rejects_credential_values(self) -> None:
        config = self.valid_config()
        provider = config["providers"][0]  # type: ignore[index]
        provider["credential_mode"] = "env_reference"  # type: ignore[index]
        provider["credential_reference"] = "sk-this-is-a-secret-value"  # type: ignore[index]
        self.write_config(config)

        report = run_gate(self.tmp)

        self.assertEqual(report["status"], "fail")
        self.assertIn("credential_value_detected", {finding["type"] for finding in report["findings"]})

    def test_embedding_provider_gate_rejects_sensitive_classification(self) -> None:
        config = self.valid_config()
        provider = config["providers"][0]  # type: ignore[index]
        provider["allowed_data_classifications"] = ["synthetic", "sensitive"]  # type: ignore[index]
        self.write_config(config)

        report = run_gate(self.tmp)

        self.assertEqual(report["status"], "fail")
        self.assertIn("sensitive_classification_not_allowed", {finding["type"] for finding in report["findings"]})

    def test_embedding_provider_gate_requires_external_provider_review(self) -> None:
        config = self.valid_config()
        provider = config["providers"][0]  # type: ignore[index]
        provider["id"] = "external-provider"  # type: ignore[index]
        provider["status"] = "draft"  # type: ignore[index]
        provider["environment"] = "controlled_external"  # type: ignore[index]
        provider["credential_mode"] = "env_reference"  # type: ignore[index]
        provider["credential_reference"] = "ENV:EMBEDDING_PROVIDER_API_KEY"  # type: ignore[index]
        provider["allows_external_network"] = True  # type: ignore[index]
        provider["human_review_required"] = False  # type: ignore[index]
        config["active_provider"] = "external-provider"
        self.write_config(config)

        report = run_gate(self.tmp)

        finding_types = {finding["type"] for finding in report["findings"]}
        self.assertEqual(report["status"], "fail")
        self.assertIn("external_provider_not_approved", finding_types)
        self.assertIn("external_provider_requires_human_review", finding_types)

    def test_embedding_provider_gate_accepts_offline_dry_run_provider(self) -> None:
        config = self.valid_config()
        config["active_provider"] = "external-provider-dry-run"
        config["providers"].append(  # type: ignore[union-attr]
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
        )
        self.write_config(config)

        report = run_gate(self.tmp)

        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["active_provider"], "external-provider-dry-run")

    def test_embedding_provider_gate_rejects_networked_dry_run_provider(self) -> None:
        config = self.valid_config()
        config["active_provider"] = "external-provider-dry-run"
        config["providers"].append(  # type: ignore[union-attr]
            {
                "id": "external-provider-dry-run",
                "status": "approved",
                "environment": "controlled_external",
                "credential_mode": "env_reference",
                "credential_reference": "ENV:EMBEDDING_PROVIDER_API_KEY",
                "allows_external_network": True,
                "dry_run": True,
                "allowed_data_classifications": ["none", "synthetic"],
                "human_review_required": True,
                "data_boundary_document": "../docs/23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md",
            }
        )
        self.write_config(config)

        report = run_gate(self.tmp)

        finding_types = {finding["type"] for finding in report["findings"]}
        self.assertEqual(report["status"], "fail")
        self.assertIn("dry_run_requires_offline_environment", finding_types)
        self.assertIn("dry_run_requires_no_credentials", finding_types)
        self.assertIn("dry_run_requires_no_network", finding_types)


if __name__ == "__main__":
    unittest.main()
