from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.deployment_readiness_gate import run_gate as run_deployment_gate  # noqa: E402
from scripts.pre_coding_gate import run_gate as run_pre_coding_gate  # noqa: E402


class OperationalGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="ips-gate-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def write(self, rel: str, text: str) -> None:
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def write_pre_coding_baseline(self) -> None:
        self.write("docs/00_constitution/CONSTITUTION.md", "# Constitution\n\nContent.\n")
        self.write("docs/01_vision/VISION.md", "# Vision\n\nContent.\n")
        self.write(
            "docs/17_governance/PROJECT_INVARIANTS.md",
            "# Project Invariants\n\n## Purpose\nContent.\n",
        )
        self.write(
            "docs/11_tasks/TASK-001.md",
            """# TASK-001

```yaml
id: TASK-001
status: draft
upstream:
  - ../10_features/FEAT-001.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-001.md
execution_plan:
  - ../21_execution_plans/EP-TASK-001.md
```

## Objective
Content.

## Upstream Links
`../10_features/FEAT-001.md`
""",
        )
        self.write(
            "docs/21_execution_plans/EP-TASK-001.md",
            """# EP-TASK-001

## Metadata

```yaml
id: EP-TASK-001
status: draft
source_task: ../11_tasks/TASK-001.md
```

## Validation Plan
Run the local gate scripts and focused tests.
""",
        )

    def test_pre_coding_gate_passes_with_required_operational_inputs(self) -> None:
        self.write_pre_coding_baseline()

        report = run_pre_coding_gate(self.tmp)

        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["project_invariants"]["status"], "pass")
        self.assertEqual(report["sensitive_data_findings"], [])
        self.assertTrue((self.tmp / report["report_path"]).is_file())

    def test_pre_coding_gate_fails_on_missing_validation_plan(self) -> None:
        self.write_pre_coding_baseline()
        plan = self.tmp / "docs/21_execution_plans/EP-TASK-001.md"
        plan.write_text(plan.read_text(encoding="utf-8").replace("## Validation Plan\nRun the local gate scripts and focused tests.\n", ""), encoding="utf-8")

        report = run_pre_coding_gate(self.tmp)

        self.assertEqual(report["status"], "fail")
        self.assertEqual(
            report["execution_plans"]["missing_validation_plan"],
            ["docs/21_execution_plans/EP-TASK-001.md"],
        )

    def test_pre_coding_gate_scans_env_files_for_secret_assignments(self) -> None:
        self.write_pre_coding_baseline()
        key_name = "ACCESS_" + "TOKEN"
        token_value = "abc123" + "456789xyz"
        self.write(".env", f"{key_name}={token_value}\n")

        report = run_pre_coding_gate(self.tmp)

        self.assertEqual(report["status"], "fail")
        self.assertTrue(
            any(item["path"] == ".env" and item["pattern"] == "secret_assignment" for item in report["sensitive_data_findings"])
        )

    def test_deployment_gate_reports_unresolved_markers_and_requires_validation_target(self) -> None:
        self.write("docs/12_validation/VAL-TASK-001.md", "# Validation\n\nTASK-001 passed.\n")
        self.write("docs/11_tasks/TASK-001.md", "# Task\n\n[MISSING: human decision]\n")

        with patch(
            "scripts.deployment_readiness_gate.run_pre_coding_gate",
            return_value={"status": "pass", "report_path": "reports/validation/pre.json"},
        ):
            with patch(
                "scripts.deployment_readiness_gate.run_strict_doc_audit",
                return_value={"status": "PASS", "score": 100, "findings_count": 0},
            ):
                report = run_deployment_gate(self.tmp, target="TASK-001")

        self.assertEqual(report["status"], "pass")
        self.assertEqual(report["validation_reports"]["matching_reports"], ["docs/12_validation/VAL-TASK-001.md"])
        self.assertEqual(len(report["unresolved_markers"]), 1)
        self.assertEqual(report["unresolved_markers"][0]["path"], "docs/11_tasks/TASK-001.md")

    def test_deployment_gate_fails_when_protected_intent_file_is_modified(self) -> None:
        self.write("docs/00_constitution/CONSTITUTION.md", "# Constitution\n\nOriginal.\n")
        self.write("docs/01_vision/VISION.md", "# Vision\n\nOriginal.\n")
        self.write("docs/12_validation/VAL-TASK-001.md", "# Validation\n\nTASK-001 passed.\n")
        subprocess.run(["git", "init"], cwd=self.tmp, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.tmp, check=True)
        subprocess.run(["git", "config", "user.name", "Gate Test"], cwd=self.tmp, check=True)
        subprocess.run(["git", "add", "."], cwd=self.tmp, check=True)
        subprocess.run(["git", "commit", "-m", "baseline"], cwd=self.tmp, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.write("docs/01_vision/VISION.md", "# Vision\n\nChanged.\n")

        with patch(
            "scripts.deployment_readiness_gate.run_pre_coding_gate",
            return_value={"status": "pass", "report_path": "reports/validation/pre.json"},
        ):
            with patch(
                "scripts.deployment_readiness_gate.run_strict_doc_audit",
                return_value={"status": "PASS", "score": 100, "findings_count": 0},
            ):
                report = run_deployment_gate(self.tmp, target="TASK-001")

        self.assertEqual(report["status"], "fail")
        self.assertEqual(report["protected_files"]["changed_files"], ["docs/01_vision/VISION.md"])


if __name__ == "__main__":
    unittest.main()
