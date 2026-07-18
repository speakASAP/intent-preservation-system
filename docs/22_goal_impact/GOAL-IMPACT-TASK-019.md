# GOAL-IMPACT-TASK-019: Embedding Provider Safety Gates

```yaml
id: GOAL-IMPACT-TASK-019
artifact_type: task
artifact_id: TASK-019
artifact_path: ../11_tasks/TASK-019-add-embedding-provider-safety-gates.md
primary_goal: Prevent unsafe embedding provider rollout.
secondary_goals:
  - Make credential handling explicit.
  - Make provider environment boundaries explicit.
  - Block sensitive data classification for provider-backed retrieval.
impact_level: high
impact_description: This task adds machine-checkable provider safety gates before external embedding providers are implemented.
success_metric: Provider registry and gate tests pass while unsafe provider configurations fail.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md
  - ../23_documentation_contracts/SENSITIVE_DATA_POLICY.md
downstream_links:
  - ../21_execution_plans/EP-TASK-019.md
  - ../12_validation/VAL-TASK-019-embedding-provider-safety-gates.md
validation_method: Run focused provider gate tests, provider gate CLI and repository gates.
status: validated
```

## Explanation

TASK-019 makes future embedding provider work safer by requiring a provider
registry and a gate that checks credentials, environments, external network use
and data classifications before provider-backed retrieval is enabled.

## Evidence

- Provider policy: `../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- Provider registry: `../../config/embedding_provider_gates.json`
- Provider gate: `../../scripts/embedding_provider_gate.py`
- Provider gate tests: `../../tests/test_embedding_provider_gate.py`

## Validation

The impact is validated because the current local provider passes and unsafe
configurations fail in focused tests.
