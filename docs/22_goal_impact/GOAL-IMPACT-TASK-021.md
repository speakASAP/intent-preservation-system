# GOAL-IMPACT-TASK-021: Provider Promotion Thresholds

```yaml
id: GOAL-IMPACT-TASK-021
artifact_type: task
artifact_id: TASK-021
artifact_path: ../11_tasks/TASK-021-add-provider-promotion-thresholds.md
primary_goal: Make provider promotion explicit and gateable.
secondary_goals:
  - Prevent ambiguous provider approval.
  - Reuse safety and comparison gates.
  - Preserve graph-first required context.
impact_level: high
impact_description: This task adds executable promotion rules before any provider candidate can be approved.
success_metric: The dry-run candidate fixture passes promotion while bad comparison, wrong mode and networked candidates fail.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-020-add-external-provider-dry-run-contract.md
downstream_links:
  - ../21_execution_plans/EP-TASK-021.md
  - ../12_validation/VAL-TASK-021-provider-promotion-thresholds.md
validation_method: Run focused promotion tests, provider promotion gate CLI and repository gates.
status: validated
```

## Explanation

TASK-021 adds a promotion gate that combines candidate comparison, provider
safety status, dry-run markers and network-call limits. This makes provider
promotion a repeatable decision instead of a manual interpretation.

## Evidence

- Promotion rules: `../../config/provider_promotion_rules.json`
- Promotion gate: `../../scripts/provider_promotion_gate.py`
- Dry-run fixture: `../../tests/fixtures/retrieval_candidate_dry_run.json`

## Validation

The impact is validated because the dry-run candidate passes promotion and
failing candidates are rejected by focused tests.
