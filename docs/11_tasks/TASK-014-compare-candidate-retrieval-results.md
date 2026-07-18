# TASK-014: Compare candidate retrieval results

```yaml
id: TASK-014
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
  - ../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-014.md
execution_plan:
  - ../21_execution_plans/EP-TASK-014.md
validation_report:
  - ../12_validation/VAL-TASK-014-candidate-retrieval-comparison.md
```

## Objective

Add a local comparison harness for candidate retrieval outputs so future
embedding or vector-search experiments can be evaluated against the deterministic
baseline before they are considered for integration.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Optional retrieval feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Retrieval evaluation baseline: `../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`

## Goal Impact

TASK-014 creates a measurement gate for future semantic retrieval. Candidate
retrieval outputs can be compared locally, but they still cannot replace
graph-required context.

## Project Invariant Impact

- IPS-INV-001: comparison cases remain tied to task ids and expected documents.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-014.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: candidate fixtures use synthetic repository-local paths only.

## Sensitive-Data Classification

Classification: synthetic

Candidate result fixtures must contain synthetic case ids, retrieval mode names
and repository-local paths only.

## Contract/Schema Impact

This task adds a candidate comparison report with baseline case ids, candidate
paths, missing expected paths, unexpected paths and per-case pass/fail status.

## Replay/Determinism Impact

Comparison output must be deterministic for fixed baseline and candidate result
files.

## Scope

- Define a local candidate result JSON shape.
- Add comparison logic against the baseline file.
- Add a synthetic candidate fixture.
- Add focused tests for pass, fail and missing-candidate cases.

## Non-Goals

- Do not generate embeddings.
- Do not run vector search.
- Do not call external APIs.
- Do not replace graph-required context.

## Acceptance Criteria

- [x] A local command compares candidate retrieval results to a baseline file.
- [x] Reports include case-level pass/fail, missing expected paths and
  unexpected candidate paths.
- [x] Missing candidate cases produce structured findings.
- [x] Comparison output is deterministic.
- [x] Repository validation gates pass.

## Required Context

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../../tests/fixtures/retrieval_baseline.json`
- `../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`
- `../21_execution_plans/EP-TASK-013.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Validation Task

Validate with focused context-package tests, a sample candidate comparison CLI
command, full repository validation, pre-coding gate and deployment-readiness
gate for TASK-014.

## Required Gates

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-014
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-014.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-014-candidate-retrieval-comparison.md`.
