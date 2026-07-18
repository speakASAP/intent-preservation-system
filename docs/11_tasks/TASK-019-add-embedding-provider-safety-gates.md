# TASK-019: Add embedding provider safety gates

```yaml
id: TASK-019
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
  - ../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md
  - ../23_documentation_contracts/SENSITIVE_DATA_POLICY.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-019.md
execution_plan:
  - ../21_execution_plans/EP-TASK-019.md
validation_report:
  - ../12_validation/VAL-TASK-019-embedding-provider-safety-gates.md
```

## Objective

Add explicit credential, environment and sensitive-data gates for future
embedding providers before any external provider implementation is introduced.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Optional RAG milestone: `../09_milestones/MS-005-rag-integration.md`
- Optional retrieval feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Provider adapter boundary: `../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md`
- Sensitive data policy: `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Goal Impact

TASK-019 prevents unsafe provider rollout by making provider approval,
credential references, environment boundaries and data classification rules
machine-checkable.

## Project Invariant Impact

- IPS-INV-001: provider-backed retrieval remains optional and gated.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-019.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: provider registry examples contain no secrets or production data.

## Sensitive-Data Classification

Classification: synthetic

The provider registry contains only provider ids and references. It must not
contain credential values, raw production data or real customer data.

## Contract/Schema Impact

This task adds `config/embedding_provider_gates.json` and a validation report
schema emitted by `scripts/embedding_provider_gate.py`. It does not change
retrieval candidate comparison semantics.

## Replay/Determinism Impact

The gate is deterministic for a fixed provider registry and repository state.

## Scope

- Add an embedding provider safety policy document.
- Add a provider registry for the current local provider.
- Add a dependency-free embedding provider gate script.
- Add tests for registry pass, missing registry, unknown active provider,
  credential values, sensitive classification and external review requirements.
- Add the new gate to repository typecheck coverage.
- Update TASK-019 governance and graph traceability.

## Non-Goals

- Do not implement an external embedding provider.
- Do not add real credentials.
- Do not add a secret manager integration.
- Do not change graph-required context behavior.
- Do not modify protected vision or constitution documents.

## Acceptance Criteria

- [x] Provider registry exists without secrets.
- [x] Credential mode rules are machine-checkable.
- [x] Environment and external-network rules are machine-checkable.
- [x] Sensitive classification is rejected for embedding providers.
- [x] Gate tests cover passing and failing provider configurations.
- [x] Repository validation gates pass.

## Required Context

- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`
- `../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md`
- `../../scripts/embedding_provider_gate.py`
- `../../tests/test_embedding_provider_gate.py`
- `../../config/embedding_provider_gates.json`

## Validation Task

Validate with focused provider gate tests, the provider gate CLI, full
repository validation, pre-coding gate and deployment-readiness gate for
TASK-019.

## Required Gates

```bash
python3 -m unittest tests.test_embedding_provider_gate
python3 scripts/embedding_provider_gate.py --root .
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-019
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-019.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-019-embedding-provider-safety-gates.md`.
