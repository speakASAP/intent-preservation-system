from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.strict_doc_audit import apply_remediation_plan, audit, remediation_plan_for  # noqa: E402


class StrictDocAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="ips-audit-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def write(self, rel: str, text: str) -> None:
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def write_baseline(self) -> None:
        for rel in [
            "docs/00_constitution/CONSTITUTION.md",
            "docs/01_vision/VISION_EVOLUTION.md",
            "docs/02_business_case/BUSINESS_CASE.md",
            "docs/03_domain_model/GLOSSARY.md",
            "docs/03_domain_model/CORE_ENTITIES.md",
            "docs/06_architecture/ARCHITECTURE_OVERVIEW.md",
            "docs/08_roadmap/ROADMAP.md",
            "docs/12_validation/VALIDATION_PYRAMID.md",
            "docs/15_audits/AUDIT_CHECKLIST.md",
            "docs/23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md",
            "docs/09_milestones/MS-001.md",
        ]:
            self.write(rel, f"# {Path(rel).stem}\n\nContent.\n")
        self.write(
            "docs/01_vision/VISION.md",
            "# VISION\n\n"
            + " ".join(
                [
                    "The system preserves original intent through traceable documents, bounded execution plans, validation evidence and graph-based context retrieval."
                ]
                * 20
            )
            + "\n",
        )
        self.write(
            "docs/04_systems/SYS-001.md",
            "# SYS-001\n\n## Purpose\nContent.\n\n## Responsibilities\nContent.\n\n## Validation\nContent.\n",
        )
        self.write(
            "docs/05_subsystems/SUB-001.md",
            "# SUB-001\n\n## Purpose\nContent.\n\n## Responsibilities\nContent.\n\n## Inputs\nContent.\n\n## Outputs\nContent.\n\n## Validation\nContent.\n",
        )
        self.write(
            "docs/07_decisions/ADR-001.md",
            "# ADR-001\n\nStatus: Accepted\n\n## Context\nContent.\n\n## Decision\nContent.\n\n## Consequences\nContent.\n\n## Validation\nContent.\n",
        )
        self.write(
            "docs/10_features/FEAT-001.md",
            "# FEAT-001\n\n## Goal\nContent.\n\n## Acceptance criteria\nContent.\n\n## Traceability\nContent.\n\n## Validation\nContent.\n",
        )

    def write_task_chain(self, plan_status: str = "reviewed") -> None:
        self.write(
            "docs/11_tasks/TASK-001.md",
            f"""# TASK-001

```yaml
id: TASK-001
status: completed
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

## Goal Impact
Content.

## Scope
Content.

## Non-Goals
Content.

## Acceptance Criteria
Content.

## Required Context
Content.

## Validation Task
Content.

## Execution Plan Requirement
Content.
""",
        )
        self.write(
            "docs/21_execution_plans/EP-TASK-001.md",
            f"""# EP-TASK-001

## Metadata

```yaml
id: EP-TASK-001
status: {plan_status}
source_task: ../11_tasks/TASK-001.md
```

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-001.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-001.md
```

## Goal Impact
Content.

## Scope
Content.

## Non-Goals
Content.

## Files to Inspect
Content.

## Files to Create
Content.

## Files to Modify
Content.

## Files That Must Not Be Modified
Content.

## Implementation Steps
Content.

## Test Plan
Content.

## Validation Plan
Content.

## Documentation Updates
Content.

## Rollback Plan
Content.

## Agent Handoff Prompt
Content.

## Completion Checklist
- [x] Done.
""",
        )
        self.write(
            "docs/22_goal_impact/GOAL-IMPACT-TASK-001.md",
            """# GOAL-IMPACT-TASK-001

```yaml
id: GOAL-IMPACT-TASK-001
artifact_type: task
artifact_id: TASK-001
artifact_path: ../11_tasks/TASK-001.md
primary_goal: Preserve intent.
impact_level: high
upstream_links:
  - ../01_vision/VISION.md
  - ../00_constitution/CONSTITUTION.md
status: reviewed
```

## Explanation
Content.

## Evidence
Content.

## Validation
Content.
""",
        )
        self.write(
            "docs/13_context_packages/CP-TASK-001.md",
            "# Context Package: TASK-001\n\n## Target task\nTASK-001: `../11_tasks/TASK-001.md`.\n\n## Upstream traceability\n`../01_vision/VISION.md` -> `../10_features/FEAT-001.md` -> `../11_tasks/TASK-001.md`\n\n## Included documents\n- `../01_vision/VISION.md`\n- `../10_features/FEAT-001.md`\n- `../11_tasks/TASK-001.md`\n\n## Excluded documents\nContent.\n\n## Constraints\nContent.\n\n## Agent prompt\nContent.\n\n## Validation instructions\nContent.\n",
        )
        self.write(
            "docs/14_prompts/PROMPT-TASK-001.md",
            "# Prompt\n\n## Role\nContent.\n\n## Task\nTASK-001.\n\n## Context\nContent.\n\n## Constraints\nContent.\n\n## Acceptance criteria\nContent.\n\n## Validation\nContent.\n",
        )
        self.write(
            "docs/12_validation/VAL-TASK-001.md",
            "# Validation\n\n## Summary\nTASK-001 validated.\n\n## Upstream goal\nContent.\n\n## Criteria checked\nContent.\n\n## Issues found\nNone.\n\n## Recommendation\nPass.\n\n## Traceability confirmation\nContent.\n",
        )
        self.write(
            "docs/20_semantic_compression/summaries/VISION.summary.md",
            """---
source_document: ../../01_vision/VISION.md
compression_level: summary
last_updated: 2026-06-08
compression_owner: test
fidelity_status: reviewed
must_read_full_document_when: changing goals
---

# Vision Summary

Intent remains traceable.
Context stays bounded.
Validation proves alignment.
""",
        )
        self.write(
            "docs/20_semantic_compression/ultra/VISION.ultra.md",
            """---
source_document: ../../01_vision/VISION.md
compression_level: ultra
last_updated: 2026-06-08
compression_owner: test
fidelity_status: reviewed
must_read_full_document_when: changing goals
---

# Vision Ultra

Intent.
Trace.
Validate.
""",
        )
        self.write(
            "graph/project_graph.example.yaml",
            """nodes:
  - id: GOAL-001
    type: Goal
    path: ../docs/01_vision/VISION.md
  - id: ADR-001
    type: ADR
    path: ../docs/07_decisions/ADR-001.md
  - id: FEAT-001
    type: Feature
    path: ../docs/10_features/FEAT-001.md
  - id: TASK-001
    type: Task
    path: ../docs/11_tasks/TASK-001.md
  - id: EP-TASK-001
    type: ExecutionPlan
    path: ../docs/21_execution_plans/EP-TASK-001.md
  - id: PROMPT-TASK-001
    type: CodingPrompt
    path: ../docs/14_prompts/PROMPT-TASK-001.md
  - id: CP-TASK-001
    type: ContextPackage
    path: ../docs/13_context_packages/CP-TASK-001.md
  - id: VAL-TASK-001
    type: ValidationReport
    path: ../docs/12_validation/VAL-TASK-001.md
edges:
  - from: TASK-001
    type: implements
    to: FEAT-001
  - from: TASK-001
    type: impacts_goal
    to: GOAL-001
  - from: EP-TASK-001
    type: derives_from
    to: TASK-001
  - from: EP-TASK-001
    type: generates
    to: PROMPT-TASK-001
  - from: EP-TASK-001
    type: constrained_by
    to: ADR-001
  - from: PROMPT-TASK-001
    type: included_in_context
    to: CP-TASK-001
  - from: VAL-TASK-001
    type: validates
    to: TASK-001
""",
        )

    def test_complete_chain_passes(self) -> None:
        self.write_baseline()
        self.write_task_chain()

        report = audit(self.tmp)

        self.assertEqual(report["status"], "PASS")

    def test_complete_context_package_passes_contract_checks(self) -> None:
        self.write_baseline()
        self.write_task_chain()

        report = audit(self.tmp)

        result = next(
            item for item in report["results"] if item["path"] == "docs/13_context_packages/CP-TASK-001.md"
        )
        self.assertEqual(result["type"], "CONTEXT_PACKAGE")
        self.assertTrue(result["ok"])
        self.assertFalse(
            [
                item
                for item in report["findings"]
                if item["path"] == "docs/13_context_packages/CP-TASK-001.md"
            ]
        )

    def test_missing_task_heading_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        task = self.tmp / "docs/11_tasks/TASK-001.md"
        task.write_text(task.read_text(encoding="utf-8").replace("## Scope\nContent.\n\n", ""), encoding="utf-8")

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any(item["type"] == "missing_section" for item in report["findings"]))

    def test_remediation_plan_maps_missing_section_to_template(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        task = self.tmp / "docs/11_tasks/TASK-001.md"
        before = task.read_text(encoding="utf-8")
        task.write_text(before.replace("## Scope\nContent.\n\n", ""), encoding="utf-8")

        report = audit(self.tmp)
        actions = remediation_plan_for(report)

        self.assertTrue(
            any(
                action["action"] == "append_missing_section"
                and action["path"] == "docs/11_tasks/TASK-001.md"
                and action["section"] == "Scope"
                and action["template"] == "docs/18_templates/TASK_TEMPLATE.md"
                and action["writes_file"]
                for action in actions
            )
        )
        self.assertEqual(task.read_text(encoding="utf-8"), before.replace("## Scope\nContent.\n\n", ""))

    def test_apply_remediation_preserves_existing_content_and_adds_missing_section(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        self.write(
            "docs/18_templates/TASK_TEMPLATE.md",
            "# TASK-XXX\n\n## Scope\n\n[MISSING: define what is included]\n",
        )
        task = self.tmp / "docs/11_tasks/TASK-001.md"
        task.write_text(
            task.read_text(encoding="utf-8").replace("## Scope\nContent.\n\n", ""),
            encoding="utf-8",
        )
        report = audit(self.tmp)

        changed = apply_remediation_plan(self.tmp, remediation_plan_for(report))

        remediated = task.read_text(encoding="utf-8")
        self.assertIn("## Objective\nContent.", remediated)
        self.assertIn("## Scope\n\n[MISSING: define what is included]", remediated)
        self.assertIn("docs/11_tasks/TASK-001.md", changed)

    def test_apply_remediation_replaces_placeholder_section_body(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        self.write(
            "docs/18_templates/TASK_TEMPLATE.md",
            "# TASK-XXX\n\n## Scope\n\n[MISSING: define what is included]\n",
        )
        task = self.tmp / "docs/11_tasks/TASK-001.md"
        task.write_text(
            task.read_text(encoding="utf-8").replace("## Scope\nContent.", "## Scope\nTBD"),
            encoding="utf-8",
        )
        report = audit(self.tmp)

        changed = apply_remediation_plan(self.tmp, remediation_plan_for(report))

        remediated = task.read_text(encoding="utf-8")
        self.assertIn("## Scope\n\n[MISSING: define what is included]", remediated)
        self.assertIn("## Non-Goals\nContent.", remediated)
        self.assertIn("docs/11_tasks/TASK-001.md", changed)

    def test_missing_document_group_recommendation_is_proposal_only(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        shutil.rmtree(self.tmp / "docs/05_subsystems")

        report = audit(self.tmp)
        actions = remediation_plan_for(report)

        self.assertTrue(
            any(
                action["action"] == "proposal_only"
                and action["path"] == "docs/05_subsystems"
                and action["template"] == "docs/18_templates/SUBSYSTEM_TEMPLATE.md"
                and not action["writes_file"]
                for action in actions
            )
        )

    def test_broken_reference_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        task = self.tmp / "docs/11_tasks/TASK-001.md"
        task.write_text(task.read_text(encoding="utf-8") + "\n`../missing.md`\n", encoding="utf-8")

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any(item["type"] == "broken_reference" for item in report["findings"]))

    def test_prompt_from_draft_plan_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain(plan_status="draft")

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any(item["type"] == "prompt_from_unapproved_plan" for item in report["findings"]))

    def test_task_without_goal_impact_link_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        task = self.tmp / "docs/11_tasks/TASK-001.md"
        task.write_text(
            task.read_text(encoding="utf-8").replace(
                "goal_impact:\n  - ../22_goal_impact/GOAL-IMPACT-TASK-001.md\n",
                "",
            ),
            encoding="utf-8",
        )

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any(
                item["type"] == "missing_metadata" and item["section"] == "goal_impact"
                for item in report["findings"]
            )
        )

    def test_execution_plan_without_traceability_field_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        plan = self.tmp / "docs/21_execution_plans/EP-TASK-001.md"
        plan.write_text(
            plan.read_text(encoding="utf-8").replace("feature: ../10_features/FEAT-001.md\n", ""),
            encoding="utf-8",
        )

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any(
                item["type"] == "missing_traceability_field" and item["section"] == "feature"
                for item in report["findings"]
            )
        )

    def test_goal_impact_without_upstream_links_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        goal_impact = self.tmp / "docs/22_goal_impact/GOAL-IMPACT-TASK-001.md"
        goal_impact.write_text(
            goal_impact.read_text(encoding="utf-8").replace(
                "upstream_links:\n  - ../01_vision/VISION.md\n  - ../00_constitution/CONSTITUTION.md\n",
                "",
            ),
            encoding="utf-8",
        )

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any(
                item["type"] == "missing_traceability_field" and item["section"] == "upstream_links"
                for item in report["findings"]
            )
        )

    def test_context_package_without_target_task_path_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        package = self.tmp / "docs/13_context_packages/CP-TASK-001.md"
        package.write_text(
            package.read_text(encoding="utf-8")
            .replace("TASK-001: `../11_tasks/TASK-001.md`.", "TASK-001.")
            .replace("- `../11_tasks/TASK-001.md`\n", ""),
            encoding="utf-8",
        )

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any(
                item["type"] == "missing_traceability_link" and item["section"] == "Target task"
                for item in report["findings"]
            )
        )

    def test_context_package_without_target_task_id_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        package = self.tmp / "docs/13_context_packages/CP-TASK-001.md"
        package.write_text(
            package.read_text(encoding="utf-8").replace(
                "TASK-001: `../11_tasks/TASK-001.md`.",
                "Content.",
            ),
            encoding="utf-8",
        )

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any(
                item["type"] == "missing_traceability_field" and item["section"] == "Target task"
                for item in report["findings"]
            )
        )

    def test_context_package_without_validation_instructions_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        package = self.tmp / "docs/13_context_packages/CP-TASK-001.md"
        package.write_text(
            package.read_text(encoding="utf-8").replace("## Validation instructions\nContent.\n", ""),
            encoding="utf-8",
        )

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any(
                item["type"] == "missing_section" and item["section"] == "Validation instructions"
                for item in report["findings"]
            )
        )

    def test_context_package_with_broken_included_document_fails(self) -> None:
        self.write_baseline()
        self.write_task_chain()
        package = self.tmp / "docs/13_context_packages/CP-TASK-001.md"
        package.write_text(
            package.read_text(encoding="utf-8").replace(
                "- `../10_features/FEAT-001.md`\n",
                "- ../10_features/FEAT-999.md\n",
            ),
            encoding="utf-8",
        )

        report = audit(self.tmp)

        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any(
                item["type"] == "broken_reference"
                and item["path"] == "docs/13_context_packages/CP-TASK-001.md"
                and item["section"] == "../10_features/FEAT-999.md"
                for item in report["findings"]
            )
        )


if __name__ == "__main__":
    unittest.main()
