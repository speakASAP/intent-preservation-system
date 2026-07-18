# TASK-001: Create required-document audit rules

```yaml
id: TASK-001
status: validated
owner: documentation-audit-agent
created: 2026-06-05
last_updated: 2026-06-08
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-003-audit-engine.md
  - ../10_features/FEAT-001-documentation-audit.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-001-example.md
execution_plan:
  - ../21_execution_plans/EP-TASK-001-example.md
```

## Objective

Create local required-document audit rules for repositories that use the Intent Preservation System folder structure.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Audit system: `../04_systems/SYS-003-audit-engine.md`
- Parent feature: `../10_features/FEAT-001-documentation-audit.md`
- Goal impact record: `../22_goal_impact/GOAL-IMPACT-TASK-001-example.md`

## Goal Impact

This task makes documentation completeness machine-checkable before coding tasks are assigned to AI agents. It supports the vision outcome that existing projects can be analyzed, improved, and validated against original intent.

## Scope

- Define required baseline documents for this repository structure.
- Detect missing required document groups.
- Detect missing or placeholder required sections in auditable artifacts.
- Produce machine-readable JSON and management-readable Markdown output.
- Provide template-based recommendations for missing draft documents or sections.

## Non-Goals

- Do not audit arbitrary repository structures.
- Do not implement a web interface.
- Do not clone remote repositories.
- Do not modify immutable vision or constitution documents.

## Acceptance Criteria

- The audit runs locally without external dependencies.
- Missing required files and document groups are reported.
- Missing required sections are reported with severity and recommendation.
- The output can be consumed by humans, AI agents, and CI jobs.
- The repository can use the audit against itself.

## Required Context

- `../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `../15_audits/AUDIT_CHECKLIST.md`
- `../18_templates/TASK_TEMPLATE.md`
- `../18_templates/AUDIT_REPORT_TEMPLATE.md`
- `../04_systems/SYS-003-audit-engine.md`

## Validation Task

Run `python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues` from the repository root and confirm that incomplete documents are reported with actionable recommendations.

## Execution Plan Requirement

This task must not be converted into a coding prompt until an approved execution plan exists in `../21_execution_plans/`.
