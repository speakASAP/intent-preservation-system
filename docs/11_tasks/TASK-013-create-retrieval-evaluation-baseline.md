# TASK-013: Create retrieval evaluation baseline

```yaml
id: TASK-013
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
  - ../11_tasks/TASK-012-harden-optional-local-retrieval.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-013.md
execution_plan:
  - ../21_execution_plans/EP-TASK-013.md
validation_report:
  - ../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md
```

## Objective

Create a deterministic local evaluation baseline for optional retrieval so
future embedding or vector-search work can be compared against expected
graph-safe supporting documents.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Optional retrieval feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Hardened local retrieval: `../11_tasks/TASK-012-harden-optional-local-retrieval.md`

## Goal Impact

TASK-013 prevents future semantic retrieval from becoming an unmeasured black
box. It creates a deterministic benchmark that records whether retrieval returns
expected supporting documents while graph-required context remains separate.

## Project Invariant Impact

- IPS-INV-001: evaluation cases stay tied to task ids and expected documents.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-013.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: baseline fixtures use synthetic repository-local data only.

## Sensitive-Data Classification

Classification: synthetic

Evaluation fixtures must contain only synthetic task ids, queries and expected
document paths. No secrets, raw production data or confidential identifiers are
allowed.

## Contract/Schema Impact

This task adds a retrieval evaluation report contract with case-level pass/fail
results, expected documents, returned documents, missing documents and
unexpected documents.

## Replay/Determinism Impact

Evaluation output must be deterministic for a fixed baseline file and repository
state.

## Scope

- Define a local baseline JSON shape.
- Add an evaluation function and CLI mode.
- Add a synthetic baseline fixture.
- Add focused tests for pass, fail and missing-task cases.

## Non-Goals

- Do not add embeddings.
- Do not add vector search.
- Do not call external APIs.
- Do not replace graph-required context.

## Acceptance Criteria

- [x] A local command evaluates retrieval cases from a JSON baseline file.
- [x] Reports include case-level pass/fail, expected, returned, missing and
  unexpected documents.
- [x] Missing task cases produce structured findings.
- [x] Evaluation output is deterministic.
- [x] Repository validation gates pass.

## Required Context

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../11_tasks/TASK-012-harden-optional-local-retrieval.md`
- `../21_execution_plans/EP-TASK-012.md`
- `../12_validation/VAL-TASK-012-harden-optional-local-retrieval.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Validation Task

Validate with focused context-package tests, a sample baseline evaluation CLI
command, full repository validation, pre-coding gate and deployment-readiness
gate for TASK-013.

## Required Gates

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-013
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-013.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md`.
