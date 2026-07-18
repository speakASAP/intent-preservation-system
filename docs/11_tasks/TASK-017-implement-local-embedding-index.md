# TASK-017: Implement local embedding index

```yaml
id: TASK-017
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
  - ../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-017.md
execution_plan:
  - ../21_execution_plans/EP-TASK-017.md
validation_report:
  - ../12_validation/VAL-TASK-017-local-embedding-index.md
```

## Objective

Add a deterministic local embedding-style index for optional retrieval
candidates so Phase 5 can move from token-overlap candidate generation toward a
vector-search shape without external services.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Optional RAG milestone: `../09_milestones/MS-005-rag-integration.md`
- Optional retrieval feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Local semantic adapter: `../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`

## Goal Impact

TASK-017 advances optional RAG by introducing a local vector index contract that
future embedding providers can replace or extend while preserving graph-first
required context.

## Project Invariant Impact

- IPS-INV-001: optional vector candidates must not replace mandatory graph
  context.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-017.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: tests and reports use synthetic repository-local documents only.

## Sensitive-Data Classification

Classification: synthetic

The local index scans repository Markdown and synthetic test fixtures. It must
not call external embedding providers or index secrets, confidential
identifiers, raw production data or real customer data.

## Contract/Schema Impact

This task adds a candidate mode named `local-embedding-index` and a local
embedding report with index metadata. Existing keyword retrieval and
`local-semantic-token-overlap` candidate output remain backward compatible.

## Replay/Determinism Impact

The index uses deterministic hashed token vectors and stable path tie-breaking.
For a fixed repository state, baseline file and query, generated candidates are
repeatable.

## Scope

- Add a deterministic local vector index over repository Markdown.
- Add local embedding retrieval report output.
- Add candidate generation mode for `local-embedding-index`.
- Add focused tests for index exclusion, report shape, comparison compatibility
  and determinism.
- Update TASK-017 governance and graph traceability.

## Non-Goals

- Do not call external embedding APIs.
- Do not add a vector database.
- Do not replace graph-required context.
- Do not index sensitive data.
- Do not modify protected vision or constitution documents.

## Acceptance Criteria

- [x] A local embedding-style index can be built deterministically.
- [x] Required graph context is excluded from optional candidate ranking.
- [x] Candidate generation supports `local-embedding-index`.
- [x] Generated embedding candidates compare through the TASK-014 harness.
- [x] Focused tests cover deterministic output and report metadata.
- [x] Repository validation gates pass.

## Required Context

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../../tests/fixtures/retrieval_baseline.json`
- `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Validation Task

Validate with focused context-package tests, generated embedding candidate CLI
output, candidate comparison, full repository validation, pre-coding gate and
deployment-readiness gate for TASK-017.

## Required Gates

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-017
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-017.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-017-local-embedding-index.md`.
