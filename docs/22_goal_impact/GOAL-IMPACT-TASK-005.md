# GOAL-IMPACT-TASK-005: Safe Draft Remediation

```yaml
id: GOAL-IMPACT-TASK-005
artifact_type: task
artifact_id: TASK-005
artifact_path: ../11_tasks/TASK-005-propose-and-generate-missing-document-drafts.md
primary_goal: Preserve human control while remediating incomplete documentation.
secondary_goals:
  - Turn audit findings into reviewable draft updates.
  - Prevent AI agents from inventing goals or silently changing protected intent.
impact_level: high
impact_description: This task provides a controlled path from audit findings to template-based document repair.
success_metric: Draft-generation proposals list intended file changes and require approval before writing.
upstream_links:
  - ../01_vision/VISION.md
  - ../00_constitution/CONSTITUTION.md
downstream_links:
  - ../21_execution_plans/EP-TASK-005.md
  - ../12_validation/VAL-TASK-005-safe-draft-remediation.md
validation_method: Run the workflow against a temporary repository with a missing required section and verify approval gating.
status: validated
```

## Explanation

TASK-005 keeps remediation aligned with the constitution by making missing
information explicit, deriving draft content only from approved upstream
documents, and requiring human approval before writes.

## Evidence

- Constitution AI-agent rules: `../00_constitution/CONSTITUTION.md`
- Audit feature: `../10_features/FEAT-001-documentation-audit.md`
- Agent gap filling rules: `../23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`
- Execution plan: `../21_execution_plans/EP-TASK-005.md`

## Validation

The impact is valid when draft remediation proposes changes without writing
them, preserves existing content, and inserts explicit missing-information
markers when approved upstream sources are insufficient.
