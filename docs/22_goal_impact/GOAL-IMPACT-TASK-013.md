# GOAL-IMPACT-TASK-013: Retrieval Evaluation Baseline

```yaml
id: GOAL-IMPACT-TASK-013
artifact_type: task
artifact_id: TASK-013
artifact_path: ../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md
primary_goal: Create a deterministic baseline for evaluating optional retrieval quality.
secondary_goals:
  - Make future semantic retrieval measurable.
  - Preserve graph-first required context.
  - Keep evaluation local and synthetic.
impact_level: medium
impact_description: This task adds baseline evaluation before embedding or vector-search work.
success_metric: A local command evaluates retrieval cases and reports pass or fail with missing and unexpected documents.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-012-harden-optional-local-retrieval.md
downstream_links:
  - ../21_execution_plans/EP-TASK-013.md
  - ../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md
validation_method: Run focused retrieval evaluation tests, sample CLI output and repository gates.
status: validated
```

## Explanation

TASK-013 adds a deterministic benchmark for optional retrieval. This lets future
embedding or vector-search changes prove that they improve supporting context
without weakening graph-required context.

## Evidence

- Hardened local retrieval: `../11_tasks/TASK-012-harden-optional-local-retrieval.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`

## Validation

The impact is validated because local evaluation reports pass/fail cases with
expected, returned, missing and unexpected documents, and repository gates pass.
