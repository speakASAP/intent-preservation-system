# GOAL-IMPACT-TASK-020: External Provider Dry-Run Contract

```yaml
id: GOAL-IMPACT-TASK-020
artifact_type: task
artifact_id: TASK-020
artifact_path: ../11_tasks/TASK-020-add-external-provider-dry-run-contract.md
primary_goal: Validate the external-provider pathway without data movement.
secondary_goals:
  - Preserve graph-first required context.
  - Prove provider safety gates before real integrations.
  - Reuse candidate comparison before provider rollout.
impact_level: medium
impact_description: This task adds a dry-run provider candidate mode that validates shape and gates without network calls.
success_metric: Dry-run candidate output passes provider gates and candidate comparison while reporting zero network calls.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-019-add-embedding-provider-safety-gates.md
downstream_links:
  - ../21_execution_plans/EP-TASK-020.md
  - ../12_validation/VAL-TASK-020-external-provider-dry-run-contract.md
validation_method: Run focused dry-run tests, provider gate CLI, dry-run candidate CLI and repository gates.
status: validated
```

## Explanation

TASK-020 creates a safe rehearsal path for future external embedding providers.
It checks provider registry rules and candidate comparison behavior while
avoiding network calls and repository document text reads.

## Evidence

- Provider registry: `../../config/embedding_provider_gates.json`
- Provider gate: `../../scripts/embedding_provider_gate.py`
- Candidate generator: `../../scripts/context_package_generator.py`

## Validation

The impact is validated because dry-run output is marked as dry-run, reports
zero network calls and passes existing candidate comparison.
