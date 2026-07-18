# GOAL-IMPACT-TASK-011: Optional RAG Retrieval Contract

```yaml
id: GOAL-IMPACT-TASK-011
artifact_type: task
artifact_id: TASK-011
artifact_path: ../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md
primary_goal: Add safe optional retrieval without weakening graph-first context.
secondary_goals:
  - Start Phase 5 optional RAG integration.
  - Preserve mandatory graph context as the source of truth.
  - Make optional supporting context inspectable and deterministic.
impact_level: high
impact_description: This task defines the contract and first deterministic implementation slice for optional retrieval suggestions.
success_metric: A local command returns required graph context separately from optional suggestions with stable reason metadata.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-006-generate-context-package-by-task-id.md
  - ../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md
downstream_links:
  - ../21_execution_plans/EP-TASK-011.md
  - ../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md
validation_method: Run retrieval tests, repository validation gates and TASK-011 deployment-readiness gate.
status: validated
```

## Explanation

TASK-011 exists so Phase 5 can add semantic or keyword-assisted retrieval
without making vector similarity authoritative. It turns optional RAG into a
bounded contract: mandatory documents come from graph traversal, while optional
suggestions are separately labeled, ranked and justified.

## Evidence

- Context engine retrieval strategy: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture optional context section:
  `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Phase 5 roadmap: `../08_roadmap/ROADMAP.md`
- Optional RAG milestone: `../09_milestones/MS-005-rag-integration.md`
- Optional RAG feature: `../10_features/FEAT-003-optional-rag-retrieval.md`

## Validation

The impact is validated because TASK-011 produces deterministic optional
suggestions for a task id, keeps required graph context separate, and passes the
repository validation gates without sensitive-data findings.
