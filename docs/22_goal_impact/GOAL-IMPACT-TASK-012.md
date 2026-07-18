# GOAL-IMPACT-TASK-012: Harden Optional Local Retrieval

```yaml
id: GOAL-IMPACT-TASK-012
artifact_type: task
artifact_id: TASK-012
artifact_path: ../11_tasks/TASK-012-harden-optional-local-retrieval.md
primary_goal: Make local optional retrieval more auditable before semantic retrieval is introduced.
secondary_goals:
  - Preserve graph-first required context.
  - Improve report transparency.
  - Keep Phase 5 retrieval deterministic and local.
impact_level: medium
impact_description: This task improves optional retrieval scoring metadata, filtering and report summaries.
success_metric: Optional retrieval reports explain ranking and filtering decisions while validation gates pass.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md
downstream_links:
  - ../21_execution_plans/EP-TASK-012.md
  - ../12_validation/VAL-TASK-012-harden-optional-local-retrieval.md
validation_method: Run focused retrieval tests, sample CLI output and repository gates.
status: validated
```

## Explanation

TASK-012 improves the local optional retrieval layer so future embedding work
has a deterministic baseline to compare against. It keeps required graph context
separate while making optional suggestion scores easier to audit.

## Evidence

- TASK-011 optional retrieval contract:
  `../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`

## Validation

The impact is validated because reports include scoring metadata, minimum-score
filtering works, required context remains separate, and repository validation
gates pass.
