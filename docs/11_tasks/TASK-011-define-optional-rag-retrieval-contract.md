# TASK-011: Define optional RAG retrieval contract

```yaml
id: TASK-011
status: validated
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../09_milestones/MS-005-rag-integration.md
  - ../10_features/FEAT-003-optional-rag-retrieval.md
  - ../11_tasks/TASK-006-generate-context-package-by-task-id.md
  - ../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-011.md
execution_plan:
  - ../21_execution_plans/EP-TASK-011.md
validation_report:
  - ../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md
```

## Objective

Define and implement a deterministic optional retrieval contract that can attach
bounded semantic or keyword suggestions to a task without replacing mandatory
graph context.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Context retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Phase 5 milestone: `../09_milestones/MS-005-rag-integration.md`
- Optional RAG feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Context package generator: `../11_tasks/TASK-006-generate-context-package-by-task-id.md`
- Dependency map foundation: `../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md`

## Goal Impact

TASK-011 starts Phase 5 by making optional retrieval safe and inspectable. It
preserves graph-first intent by separating required documents from optional
suggestions and by requiring deterministic reason metadata for every suggestion.

## Project Invariant Impact

- IPS-INV-001: optional suggestions must keep traceability to the target task
  and must not replace upstream graph links.
- IPS-INV-002: immutable vision and constitution documents may be read but must
  not be modified.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-011.md`.
- IPS-INV-004: validation evidence must be recorded before closure.
- IPS-INV-005: fixtures and reports use repository documentation and synthetic
  examples only.

## Sensitive-Data Classification

Classification: none

The first implementation works over repository-local Markdown documents and
synthetic test fixtures. It must not index secrets, raw production data,
confidential identifiers or real customer data.

## Contract/Schema Impact

This task defines a new optional retrieval report contract with separate
`required_context`, `optional_suggestions` and `findings` sections. It may add a
CLI command or flag, but it must not change existing context-package or graph
extractor default output.

## Replay/Determinism Impact

Optional retrieval output must be deterministic for a fixed repository state,
task id, query terms and scoring rules. Ties must use stable path ordering.

## Scope

- Define an optional retrieval report shape.
- Implement a local deterministic keyword-based fallback for the first slice.
- Keep semantic/vector embedding support out of this slice unless it is purely
  contract documentation.
- Separate mandatory graph context from optional suggestions.
- Add tests with synthetic fixtures.

## Non-Goals

- Do not call external embedding APIs.
- Do not add a vector database.
- Do not replace graph traversal.
- Do not include secrets or raw production data in fixtures or reports.
- Do not modify protected vision or constitution documents.

## Acceptance Criteria

- [x] A local command can produce optional suggestions for a task id.
- [x] Output separates required graph context from optional suggestions.
- [x] Each suggestion includes path, reason, score or rank, and retrieval mode.
- [x] Existing graph and context-package outputs remain backward compatible.
- [x] Tests cover deterministic ordering, no-suggestion output and missing task
  findings.
- [x] Repository validation gates pass.

## Required Context

- `../04_systems/SYS-002-context-engine.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../10_features/FEAT-003-optional-rag-retrieval.md`
- `../11_tasks/TASK-006-generate-context-package-by-task-id.md`
- `../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md`
- `../../scripts/context_package_generator.py`
- `../../scripts/graph_extractor.py`
- `../../tests/test_context_package_generator.py`
- `../../tests/test_graph_extractor.py`
- `../17_governance/PROJECT_INVARIANTS.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Validation Task

Validate by running focused retrieval tests, a repository sample retrieval
command, the strict documentation audit, the pre-coding gate and the
deployment-readiness gate for TASK-011.

## Required Gates

```bash
python3 -m unittest discover -s tests
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-011
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-011.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md`.
