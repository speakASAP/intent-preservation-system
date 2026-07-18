# TASK-018: Add embedding provider adapter boundary

```yaml
id: TASK-018
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
  - ../11_tasks/TASK-017-implement-local-embedding-index.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-018.md
execution_plan:
  - ../21_execution_plans/EP-TASK-018.md
validation_report:
  - ../12_validation/VAL-TASK-018-embedding-provider-adapter-boundary.md
```

## Objective

Add an explicit embedding provider adapter boundary behind the local embedding
index so future provider-backed embeddings can be introduced without changing
graph-first retrieval or the candidate comparison contract.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Optional RAG milestone: `../09_milestones/MS-005-rag-integration.md`
- Optional retrieval feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Local embedding index: `../11_tasks/TASK-017-implement-local-embedding-index.md`

## Goal Impact

TASK-018 reduces coupling between retrieval ranking and the current local hash
embedding implementation. It makes future embedding providers a bounded adapter
choice rather than a rewrite of retrieval behavior.

## Project Invariant Impact

- IPS-INV-001: provider-backed embeddings remain optional suggestions and do not
  replace mandatory graph context.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-018.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: tests use synthetic repository-local text only.

## Sensitive-Data Classification

Classification: synthetic

This task adds an adapter boundary and keeps the only implemented provider
local. It must not call external APIs, write secrets or index sensitive data.

## Contract/Schema Impact

Candidate output for `local-embedding-index` now records the selected
`embedding_provider`. Existing baseline comparison remains compatible because it
compares candidate paths, not provider internals.

## Replay/Determinism Impact

The default `local-hash` provider remains deterministic. Unknown providers are
rejected explicitly.

## Scope

- Define embedding input, result and provider boundary types.
- Move the local hash vector implementation behind the provider boundary.
- Add CLI selection for the current provider.
- Record the selected provider in embedding candidate output.
- Add focused tests for provider determinism and unsupported provider handling.

## Non-Goals

- Do not add OpenAI, local-model or other real embedding providers.
- Do not call external services.
- Do not add a vector database.
- Do not replace graph-required context.
- Do not modify protected vision or constitution documents.

## Acceptance Criteria

- [x] Embedding provider selection is explicit.
- [x] The local hash provider implements the adapter boundary.
- [x] Unknown providers fail with a clear error.
- [x] Candidate output records the selected provider.
- [x] Existing embedding candidate comparison still passes.
- [x] Repository validation gates pass.

## Required Context

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../11_tasks/TASK-017-implement-local-embedding-index.md`
- `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Validation Task

Validate with focused context-package tests, provider-selected candidate CLI
output, full repository validation, pre-coding gate and deployment-readiness
gate for TASK-018.

## Required Gates

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-018
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-018.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-018-embedding-provider-adapter-boundary.md`.
