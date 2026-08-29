from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAFFOLDER = ROOT / "scripts" / "scaffold_project_adoption.py"
VALIDATOR = ROOT / "scripts" / "validate_adoption_profile.py"
sys.path.insert(0, str(ROOT))

from scripts.validate_adoption_profile import markdown_sections, unresolved_document_lines  # noqa: E402


class ProjectAdoptionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="ips-adoption-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def scaffold(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCAFFOLDER),
                "--root",
                str(self.tmp),
                "--project",
                "example-service",
                "--repository",
                "https://github.com/speakASAP/example-service",
                "--standard-revision",
                "0123456789abcdef",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_scaffolder_creates_complete_non_destructive_document_set(self) -> None:
        first = self.scaffold()
        self.assertEqual(first.returncode, 0, first.stderr)

        profile = json.loads((self.tmp / "ips-adoption.json").read_text(encoding="utf-8"))
        self.assertEqual(profile["project"]["name"], "example-service")
        self.assertEqual(profile["artifacts"]["readme"], "README.md")
        self.assertEqual(profile["artifacts"]["claude"], "CLAUDE.md")

        for relative_path in profile["artifacts"].values():
            self.assertTrue((self.tmp / relative_path).is_file(), relative_path)

        business = self.tmp / "BUSINESS.md"
        business.write_text("# Existing approved business intent\n", encoding="utf-8")
        second = self.scaffold()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(
            business.read_text(encoding="utf-8"),
            "# Existing approved business intent\n",
        )
        self.assertIn("kept existing: BUSINESS.md", second.stdout)

    def test_validator_requires_readme_artifact(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)

        profile_path = self.tmp / "ips-adoption.json"
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
        del profile["artifacts"]["readme"]
        profile_path.write_text(json.dumps(profile), encoding="utf-8")

        validation = subprocess.run(
            [sys.executable, str(VALIDATOR), "--root", str(self.tmp)],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(validation.returncode, 0)
        self.assertIn("missing artifact keys: readme", validation.stdout)

    def complete_profile_integrations(self) -> None:
        profile_path = self.tmp / "ips-adoption.json"
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
        for review in profile["integrationReview"]:
            if review["capability"] in {"logging", "docs-rag", "monitoring"}:
                for field in ("contract", "configuration", "failureMode", "validation"):
                    if "REPLACE_ME" in str(review.get(field, "")):
                        review[field] = f"Concrete {field}"
            else:
                review.update(
                    {
                        "decision": "not-applicable",
                        "reason": "The example service does not use this capability",
                    }
                )
        profile_path.write_text(json.dumps(profile), encoding="utf-8")

    def validate(self, phase: str = "deployment") -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--root",
                str(self.tmp),
                "--phase",
                phase,
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def complete_documents(self, complete_validation: bool = True) -> None:
        profile = json.loads((self.tmp / "ips-adoption.json").read_text(encoding="utf-8"))
        for key, relative_path in profile["artifacts"].items():
            path = self.tmp / relative_path
            if key == "state":
                path.write_text(
                    json.dumps(
                        {
                            "schemaVersion": 1,
                            "project": "example-service",
                            "lifecycle": "onboarding",
                            "health": "not-deployed",
                            "activeTask": "TASK-001-bootstrap-service",
                            "lastUpdated": "2026-08-29",
                            "deployment": {"status": "not-started"},
                            "blockers": [],
                            "followUps": [],
                        }
                    )
                    + "\n",
                    encoding="utf-8",
                )
                continue
            if key == "bootstrapValidation" and not complete_validation:
                continue

            text = path.read_text(encoding="utf-8")
            text = re.sub(
                r"\[(?:MISSING|UNKNOWN):\s*([^\]]+)\]",
                lambda match: f"Resolved project-specific requirement: {match.group(1).strip()}.",
                text,
            )
            text = text.replace("[MISSING]", "Resolved project-specific decision.")
            text = re.sub(r"(?mi)^status:.*$", "status: approved", text)
            text = re.sub(r"(?mi)^completeness_level:.*$", "completeness_level: complete", text)
            text = re.sub(r"\bTBD\b", "Resolved owner", text)
            text = text.replace("YYYY-MM-DD", "2026-08-29")
            text = text.replace("- None.", "- No completed work exists before bootstrap validation.")
            if complete_validation:
                deployment_statuses = {
                    "bootstrapTask": "completed",
                    "bootstrapExecutionPlan": "implemented",
                    "bootstrapValidation": "validated",
                }
                if key in deployment_statuses:
                    text = re.sub(r"(?mi)^status:.*$", f"status: {deployment_statuses[key]}", text)
            if key in {"business", "constitution", "vision"}:
                text = re.sub(r"(?mi)^Approved by:.*$", "Approved by: Sergej Stasok", text)
                text = re.sub(
                    r"(?mi)^Approval evidence:.*$",
                    "Approval evidence: owner-confirmation:2026-08-29",
                    text,
                )
            path.write_text(text, encoding="utf-8")

    def test_fresh_scaffold_fails_until_project_documents_are_completed(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.complete_profile_integrations()

        validation = self.validate("planning")

        self.assertNotEqual(validation.returncode, 0)
        self.assertIn("unresolved placeholders", validation.stdout)
        self.assertIn("requires human-approved status", validation.stdout)

    def test_planning_allows_draft_validation_evidence_only(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.complete_profile_integrations()
        self.complete_documents(complete_validation=False)

        planning = self.validate("planning")
        deployment = self.validate("deployment")

        self.assertEqual(planning.returncode, 0, planning.stdout + planning.stderr)
        self.assertNotEqual(deployment.returncode, 0)
        self.assertIn("bootstrapValidation", deployment.stdout)

    def test_completed_document_set_passes_deployment_validation(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.complete_profile_integrations()
        self.complete_documents()

        validation = self.validate("deployment")

        self.assertEqual(validation.returncode, 0, validation.stdout + validation.stderr)
        self.assertIn("valid for deployment", validation.stdout)
        self.assertIn("16 capabilities reviewed", validation.stdout)

    def test_validator_requires_human_approval_evidence(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.complete_profile_integrations()
        self.complete_documents()
        business = self.tmp / "BUSINESS.md"
        business.write_text(
            business.read_text(encoding="utf-8").replace(
                "Approved by: Sergej Stasok",
                "Approved by: Copilot Agent",
            ),
            encoding="utf-8",
        )

        validation = self.validate()

        self.assertNotEqual(validation.returncode, 0)
        self.assertIn("requires a concrete human approver", validation.stdout)

    def test_validator_requires_durable_approval_evidence(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.complete_profile_integrations()
        self.complete_documents()
        vision = self.tmp / "docs/01_vision/VISION.md"
        vision.write_text(
            vision.read_text(encoding="utf-8").replace(
                "Approval evidence: owner-confirmation:2026-08-29",
                "Approval evidence: approved",
            ),
            encoding="utf-8",
        )

        validation = self.validate()

        self.assertNotEqual(validation.returncode, 0)
        self.assertIn("requires durable approval evidence", validation.stdout)

    def test_validator_rejects_non_object_state(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.complete_profile_integrations()
        self.complete_documents()
        (self.tmp / "STATE.json").write_text("[]\n", encoding="utf-8")

        validation = self.validate()

        self.assertNotEqual(validation.returncode, 0)
        self.assertIn("state must contain a JSON object", validation.stdout)

    def test_deployment_rejects_planning_only_task_status(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.complete_profile_integrations()
        self.complete_documents()
        task = self.tmp / "docs/11_tasks/TASK-001-bootstrap-service.md"
        task.write_text(
            task.read_text(encoding="utf-8").replace(
                "status: completed",
                "status: approved",
            ),
            encoding="utf-8",
        )

        validation = self.validate("deployment")

        self.assertNotEqual(validation.returncode, 0)
        self.assertIn("bootstrapTask status must be one of: completed, validated", validation.stdout)

    def test_validator_rejects_invalid_state_fields(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.complete_profile_integrations()
        self.complete_documents()
        state_path = self.tmp / "STATE.json"
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state.update(
            {
                "schemaVersion": None,
                "lifecycle": None,
                "deployment": None,
                "blockers": None,
                "followUps": None,
            }
        )
        state_path.write_text(json.dumps(state), encoding="utf-8")

        validation = self.validate()

        self.assertNotEqual(validation.returncode, 0)
        self.assertIn("state schemaVersion must be 1", validation.stdout)
        self.assertIn("state deployment must contain a concrete status", validation.stdout)

    def test_validator_rejects_generic_document_stub(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.complete_profile_integrations()
        self.complete_documents()
        (self.tmp / "SYSTEM.md").write_text(
            "# System\n\nstatus: approved\ncompleteness_level: complete\n\nContent.\n",
            encoding="utf-8",
        )

        validation = self.validate()

        self.assertNotEqual(validation.returncode, 0)
        self.assertIn("artifact system missing required section", validation.stdout)

    def test_marker_scanner_masks_examples_but_not_real_markers(self) -> None:
        text = "\n".join(
            [
                "Use `[MISSING: fact]` when blocked.",
                "```text",
                "[MISSING: fenced example]",
                "```",
                "Owner: [MISSING: owner] (format: `[MISSING: ...]`)",
                "```yaml",
                "owner: \"[MISSING: yaml owner]\"",
                "```",
            ]
        )

        self.assertEqual(unresolved_document_lines(text), [5, 7])

    def test_section_scanner_ignores_fenced_markdown_examples(self) -> None:
        text = "\n".join(
            [
                "```markdown",
                "## Purpose",
                "Concrete but fenced example content.",
                "```",
                "## Real section",
                "Concrete real section content.",
            ]
        )

        self.assertEqual(markdown_sections(text), {"real section": "Concrete real section content."})

    def test_validator_rejects_noncanonical_artifact_path(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)
        profile_path = self.tmp / "ips-adoption.json"
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
        profile["artifacts"]["readme"] = "../README.md"
        profile_path.write_text(json.dumps(profile), encoding="utf-8")

        validation = self.validate()

        self.assertNotEqual(validation.returncode, 0)
        self.assertIn("artifact readme must use canonical path README.md", validation.stdout)

    def test_scaffold_uses_lightweight_adoption_gate_paths(self) -> None:
        result = self.scaffold()
        self.assertEqual(result.returncode, 0, result.stderr)

        plan = (self.tmp / "docs/21_execution_plans/EP-TASK-001-bootstrap-service.md").read_text(
            encoding="utf-8"
        )
        vision = (self.tmp / "docs/01_vision/VISION.md").read_text(encoding="utf-8")

        self.assertIn(
            "python3 ../intent-preservation-system/scripts/validate_adoption_profile.py",
            plan,
        )
        self.assertNotIn("python3 scripts/deployment_readiness_gate.py", plan)
        self.assertIn("../00_constitution/CONSTITUTION.md", vision)
        self.assertNotIn("upstream:\n  - ../../BUSINESS.md", vision)


if __name__ == "__main__":
    unittest.main()
