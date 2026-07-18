# GOAL-IMPACT-TASK-014: Candidate Retrieval Comparison

```yaml
id: GOAL-IMPACT-TASK-014
artifact_type: task
artifact_id: TASK-014
artifact_path: ../11_tasks/TASK-014-compare-candidate-retrieval-results.md
primary_goal: Compare future retrieval candidates against the deterministic optional retrieval baseline.
secondary_goals:
  - Keep semantic retrieval measurable before integration.
  - Preserve graph-first required context.
  - Keep comparison local and synthetic.
impact_level: medium
impact_description: This task adds a local candidate-comparison report for retrieval experiments.
success_metric: A local command compares candidate results with baseline expectations and reports pass or fail per case.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md
downstream_links:
  - ../21_execution_plans/EP-TASK-014.md
  - ../12_validation/VAL-TASK-014-candidate-retrieval-comparison.md
validation_method: Run focused retrieval comparison tests, sample CLI output and repository gates.
status: validated
```

## Explanation

TASK-014 lets future embedding or vector-search experiments submit candidate
retrieval outputs for local comparison against approved baseline expectations.
This keeps semantic retrieval measurable and optional.

## Evidence

- Retrieval evaluation baseline:
  `../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`

## Validation

The impact is validated because candidate comparison reports pass/fail cases
with missing and unexpected paths, and repository gates pass.
