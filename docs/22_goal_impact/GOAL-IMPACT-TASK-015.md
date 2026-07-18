# GOAL-IMPACT-TASK-015: Local Semantic Candidate Adapter

```yaml
id: GOAL-IMPACT-TASK-015
artifact_type: task
artifact_id: TASK-015
artifact_path: ../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md
primary_goal: Create a local candidate adapter shape for future semantic retrieval.
secondary_goals:
  - Keep candidate retrieval non-authoritative.
  - Preserve graph-first required context.
  - Avoid external services while defining the adapter contract.
impact_level: medium
impact_description: This task adds deterministic local candidate generation compatible with retrieval comparison.
success_metric: A local command generates candidate results that can be compared against the retrieval baseline.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-014-compare-candidate-retrieval-results.md
downstream_links:
  - ../21_execution_plans/EP-TASK-015.md
  - ../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md
validation_method: Run focused candidate adapter tests, sample CLI output, candidate comparison and repository gates.
status: validated
```

## Explanation

TASK-015 creates a local adapter shape for candidate semantic retrieval. It
does not add embeddings or external services; it only emits candidate files that
the TASK-014 comparison harness can evaluate.

## Evidence

- Candidate comparison: `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`

## Validation

The impact is validated because the adapter emits deterministic candidate files
compatible with the comparison harness and repository gates pass.
