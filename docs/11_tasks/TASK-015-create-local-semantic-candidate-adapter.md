# TASK-015: Create local semantic candidate adapter

```yaml
id: TASK-015
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
  - ../11_tasks/TASK-014-compare-candidate-retrieval-results.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-015.md
execution_plan:
  - ../21_execution_plans/EP-TASK-015.md
validation_report:
  - ../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md
```

## Objective

Create a local semantic-style candidate adapter that emits candidate retrieval
result files for the comparison harness without adding embeddings, vector
databases or external API calls.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Optional retrieval feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Candidate comparison: `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`

## Goal Impact

TASK-015 creates the adapter shape future embedding providers can follow while
keeping the implementation local, deterministic and non-authoritative.

## Project Invariant Impact

- IPS-INV-001: candidate output remains tied to baseline cases and task ids.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-015.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: fixtures and candidate reports use synthetic repository-local
  paths only.

## Sensitive-Data Classification

Classification: synthetic

The adapter reads repository-local Markdown and synthetic baseline fixtures. It
must not call external services or write sensitive data.

## Contract/Schema Impact

This task adds a candidate generation report compatible with TASK-014 candidate
comparison. It may include adapter metadata, but returned candidate paths must
remain compatible.

## Replay/Determinism Impact

Candidate generation must be deterministic for a fixed baseline file and
repository state.

## Scope

- Add local semantic-style candidate generation from a baseline file.
- Use deterministic token overlap against document titles and bodies.
- Return candidate result JSON compatible with TASK-014.
- Add focused tests and validate through the comparison harness.

## Non-Goals

- Do not generate embeddings.
- Do not add vector databases.
- Do not call external APIs.
- Do not replace graph-required context.

## Acceptance Criteria

- [x] A local command generates candidate retrieval results from a baseline file.
- [x] Candidate output is compatible with TASK-014 comparison.
- [x] Candidate generation is deterministic.
- [x] Tests cover successful candidate generation and comparison compatibility.
- [x] Repository validation gates pass.

## Required Context

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../../tests/fixtures/retrieval_baseline.json`
- `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `../21_execution_plans/EP-TASK-014.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Validation Task

Validate with focused context-package tests, generated candidate CLI output,
candidate comparison CLI output, full repository validation, pre-coding gate and
deployment-readiness gate for TASK-015.

## Required Gates

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-015
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-015.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md`.
