# TASK-002: Detect missing traceability fields

```yaml
id: TASK-002
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
  - ../22_goal_impact/GOAL-IMPACT-TASK-002.md
execution_plan:
  - ../21_execution_plans/EP-TASK-002.md
```

## Objective

Detect documents that do not clearly link implementation work back to upstream features, systems, business goals, and vision.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Audit system: `../04_systems/SYS-003-audit-engine.md`
- Parent feature: `../10_features/FEAT-001-documentation-audit.md`
- Documentation standard: `../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`

## Goal Impact

This task reduces concept drift by ensuring that AI agents can follow a trace path from low-level artifacts back to approved intent.

## Scope

This task must be small enough for one AI-agent session.

- Define traceability fields required for tasks, execution plans, goal impact records, and context packages.
- Report documents with missing upstream links.
- Report documents with missing goal impact links.
- Include remediation guidance that points to the correct template.

## Non-Goals

- Do not infer business goals from unrelated prose.
- Do not modify protected baseline documents.
- Do not implement graph traversal yet.
- Do not integrate with Jira, Confluence, or remote Git hosting.

## Acceptance Criteria

- The audit identifies task documents without upstream links.
- The audit identifies execution plans without upstream traceability.
- The audit identifies missing goal impact fields.
- Findings include enough path-level detail for an AI agent to repair the document.

## Required Context

- `../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `../22_goal_impact/GOAL_IMPACT_MAPPING.md`
- `../18_templates/TASK_TEMPLATE.md`
- `../18_templates/EXECUTION_PLAN_TEMPLATE.md`
- `../18_templates/GOAL_IMPACT_TEMPLATE.md`

## Validation Task

Create or use a sample task without upstream links, run the strict audit, and confirm that the report identifies the traceability gap.

## Execution Plan Requirement

This task requires an execution plan before implementation because it changes audit behavior and affects downstream context generation.
