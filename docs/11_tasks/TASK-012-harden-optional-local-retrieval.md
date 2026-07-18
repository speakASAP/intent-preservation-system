# TASK-012: Harden optional local retrieval

```yaml
id: TASK-012
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
  - ../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-012.md
execution_plan:
  - ../21_execution_plans/EP-TASK-012.md
validation_report:
  - ../12_validation/VAL-TASK-012-harden-optional-local-retrieval.md
```

## Objective

Improve the deterministic local optional retrieval contract so results are more
auditable before any embedding or vector-search work begins.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Phase 5 milestone: `../09_milestones/MS-005-rag-integration.md`
- Optional retrieval feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Optional retrieval contract: `../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md`

## Goal Impact

TASK-012 strengthens the safe local retrieval layer by adding more transparent
ranking and report metadata. This makes future semantic retrieval easier to
compare without allowing it to replace graph-required context.

## Project Invariant Impact

- IPS-INV-001: optional retrieval remains traceable to a target task and
  separates required context from suggestions.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-012.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: tests use synthetic fixtures and repository-local documents only.

## Sensitive-Data Classification

Classification: none

The implementation scans repository-local Markdown and synthetic test fixtures.
It must not introduce secrets, raw production data or confidential identifiers.

## Contract/Schema Impact

This task extends the optional retrieval JSON report with auditable scoring
metadata. Existing required fields from TASK-011 must remain backward
compatible.

## Replay/Determinism Impact

Ranking must remain deterministic for a fixed repository state, query and score
configuration. Tie-breaking must use stable path ordering.

## Scope

- Add transparent score component metadata.
- Add report-level query and scan summary metadata.
- Add minimum-score filtering.
- Keep required graph context excluded from optional suggestions by default.
- Add focused tests for scoring, filtering and compatibility.

## Non-Goals

- Do not add embeddings.
- Do not add a vector database.
- Do not call external APIs.
- Do not replace graph-required context.
- Do not modify immutable vision or constitution documents.

## Acceptance Criteria

- [x] Optional suggestions include score component metadata.
- [x] Reports include query terms and scan summary metadata.
- [x] CLI supports minimum-score filtering.
- [x] Existing TASK-011 report fields remain available.
- [x] Tests cover scoring metadata, filtering and deterministic ordering.
- [x] Repository validation gates pass.

## Required Context

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md`
- `../21_execution_plans/EP-TASK-011.md`
- `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md`
- `../17_governance/PROJECT_INVARIANTS.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Validation Task

Validate with focused context-package tests, sample optional retrieval CLI
output, full repository validation, the pre-coding gate and deployment-readiness
gate for TASK-012.

## Required Gates

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-012
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-012.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-012-harden-optional-local-retrieval.md`.
