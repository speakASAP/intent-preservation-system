# GOAL-IMPACT-TASK-018: Embedding Provider Adapter Boundary

```yaml
id: GOAL-IMPACT-TASK-018
artifact_type: task
artifact_id: TASK-018
artifact_path: ../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md
primary_goal: Make embedding providers swappable behind the optional retrieval contract.
secondary_goals:
  - Preserve graph-first required context.
  - Keep the default provider deterministic and local.
  - Reuse candidate comparison gates for future providers.
impact_level: medium
impact_description: This task separates provider selection from optional vector retrieval behavior.
success_metric: Candidate generation can select the local provider explicitly and still pass comparison gates.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-017-implement-local-embedding-index.md
downstream_links:
  - ../21_execution_plans/EP-TASK-018.md
  - ../12_validation/VAL-TASK-018-embedding-provider-adapter-boundary.md
validation_method: Run focused provider boundary tests, sample provider-selected candidate generation and repository gates.
status: validated
```

## Explanation

TASK-018 prepares optional RAG for real embedding providers by making provider
selection explicit. The current implementation remains local and deterministic,
but the retrieval code now depends on a provider boundary instead of directly on
the hash vector implementation.

## Evidence

- Local embedding index: `../11_tasks/TASK-017-implement-local-embedding-index.md`
- Candidate comparison: `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`

## Validation

The impact is validated because provider-selected candidate generation remains
compatible with the existing comparison gates and unsupported providers fail
explicitly.
