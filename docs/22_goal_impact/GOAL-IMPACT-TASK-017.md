# GOAL-IMPACT-TASK-017: Local Embedding Index

```yaml
id: GOAL-IMPACT-TASK-017
artifact_type: task
artifact_id: TASK-017
artifact_path: ../11_tasks/TASK-017-implement-local-embedding-index.md
primary_goal: Advance optional RAG with a deterministic local vector index.
secondary_goals:
  - Preserve graph-first required context.
  - Keep candidate retrieval offline and auditable.
  - Reuse the existing retrieval comparison harness.
impact_level: medium
impact_description: This task adds a local embedding-style candidate mode that future semantic providers can follow.
success_metric: A local command generates embedding-index candidates that compare successfully against the retrieval baseline.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md
downstream_links:
  - ../21_execution_plans/EP-TASK-017.md
  - ../12_validation/VAL-TASK-017-local-embedding-index.md
validation_method: Run focused embedding-index tests, sample candidate generation, candidate comparison and repository gates.
status: validated
```

## Explanation

TASK-017 gives IPS a local vector index shape without external services. It
keeps mandatory graph context separate from optional suggestions and generates
candidate files that can be evaluated by the existing comparison harness.

## Evidence

- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Candidate comparison: `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- Local adapter foundation: `../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`

## Validation

The impact is validated because `local-embedding-index` candidate output is
deterministic, excludes required graph context from optional ranking and passes
the candidate comparison harness.
