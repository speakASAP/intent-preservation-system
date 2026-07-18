# TASK-020: Add external provider dry-run contract

```yaml
id: TASK-020
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
  - ../11_tasks/TASK-019-add-embedding-provider-safety-gates.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-020.md
execution_plan:
  - ../21_execution_plans/EP-TASK-020.md
validation_report:
  - ../12_validation/VAL-TASK-020-external-provider-dry-run-contract.md
```

## Objective

Add a dry-run external provider contract that validates provider configuration,
candidate result shape and comparison compatibility without network calls or
repository text transmission.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Optional RAG milestone: `../09_milestones/MS-005-rag-integration.md`
- Optional retrieval feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Provider safety gates: `../11_tasks/TASK-019-add-embedding-provider-safety-gates.md`

## Goal Impact

TASK-020 lets IPS test the external-provider pathway safely before introducing
real provider calls. It proves the provider gate, candidate output shape and
comparison harness can work together without data movement.

## Project Invariant Impact

- IPS-INV-001: dry-run candidates remain optional and non-authoritative.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-020.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: dry-run output uses synthetic baseline fixture expectations only.

## Sensitive-Data Classification

Classification: synthetic

Dry-run candidate generation uses baseline fixture paths and does not read,
send or persist repository document text.

## Contract/Schema Impact

This task adds candidate mode `external-provider-dry-run`. Dry-run output
includes `dry_run: true`, `embedding_provider: external-provider-dry-run` and
`network_calls: 0`.

## Replay/Determinism Impact

Dry-run output is deterministic for a fixed baseline file because it derives
candidate paths from baseline expectations.

## Scope

- Add `external-provider-dry-run` to provider registry.
- Add dry-run provider safety rules.
- Add dry-run candidate mode.
- Add tests proving dry-run comparison compatibility and no document text
  dependency.
- Update TASK-020 governance and graph traceability.

## Non-Goals

- Do not implement real external embedding calls.
- Do not add credentials.
- Do not read repository document text for dry-run candidates.
- Do not change graph-required context behavior.
- Do not modify protected vision or constitution documents.

## Acceptance Criteria

- [x] Dry-run provider registry entry passes provider safety gate.
- [x] Dry-run candidate generation emits expected output shape.
- [x] Dry-run candidate output reports zero network calls.
- [x] Dry-run candidate output compares through the existing harness.
- [x] Tests prove dry-run does not require repository document text.
- [x] Repository validation gates pass.

## Required Context

- `../../config/embedding_provider_gates.json`
- `../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- `../../scripts/embedding_provider_gate.py`
- `../../scripts/context_package_generator.py`
- `../../tests/test_embedding_provider_gate.py`
- `../../tests/test_context_package_generator.py`

## Validation Task

Validate with focused provider/retrieval tests, provider gate CLI, dry-run
candidate CLI, full repository validation, pre-coding gate and
deployment-readiness gate for TASK-020.

## Required Gates

```bash
python3 -m unittest tests.test_context_package_generator tests.test_embedding_provider_gate
python3 scripts/embedding_provider_gate.py --root .
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode external-provider-dry-run --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-020
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-020.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-020-external-provider-dry-run-contract.md`.
