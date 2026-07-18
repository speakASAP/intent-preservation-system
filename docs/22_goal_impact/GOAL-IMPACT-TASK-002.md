# GOAL-IMPACT-TASK-002: Missing Traceability Detection

```yaml
id: GOAL-IMPACT-TASK-002
artifact_type: task
artifact_id: TASK-002
artifact_path: ../11_tasks/TASK-002-detect-missing-traceability-fields.md
primary_goal: Preserve project intent by detecting artifacts that lack upstream traceability.
secondary_goals:
  - Reduce concept drift during AI-assisted implementation.
  - Make remediation paths explicit for incomplete documents.
impact_level: high
impact_description: This task ensures low-level artifacts cannot silently disconnect from approved project goals.
success_metric: Strict audit reports missing upstream, goal-impact and execution-plan links with actionable file paths.
upstream_links:
  - ../01_vision/VISION.md
  - ../00_constitution/CONSTITUTION.md
downstream_links:
  - ../21_execution_plans/EP-TASK-002.md
validation_method: Run fixture tests and strict audit cases with missing traceability metadata.
status: validated
```

## Explanation

TASK-002 exists to make broken traceability visible before AI agents receive
implementation work. It supports the constitutional rule that every artifact
must contain trace links and that audits must reveal broken traceability.

## Evidence

- Vision outcome: `../01_vision/VISION.md`
- Constitution traceability rule: `../00_constitution/CONSTITUTION.md`
- Audit feature: `../10_features/FEAT-001-documentation-audit.md`
- Execution plan: `../21_execution_plans/EP-TASK-002.md`

## Validation

The impact is valid when strict audit findings identify missing upstream,
goal-impact and execution-plan links for task-like artifacts.
