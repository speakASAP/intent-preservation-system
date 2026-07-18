# TASK-021: Add provider promotion thresholds

```yaml
id: TASK-021
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
  - ../11_tasks/TASK-020-add-external-provider-dry-run-contract.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-021.md
execution_plan:
  - ../21_execution_plans/EP-TASK-021.md
validation_report:
  - ../12_validation/VAL-TASK-021-provider-promotion-thresholds.md
```

## Objective

Add provider comparison thresholds and promotion rules so a provider candidate
can graduate from experimental to approved candidate only after passing safety,
comparison and dry-run requirements.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Optional RAG milestone: `../09_milestones/MS-005-rag-integration.md`
- Optional retrieval feature: `../10_features/FEAT-003-optional-rag-retrieval.md`
- Dry-run contract: `../11_tasks/TASK-020-add-external-provider-dry-run-contract.md`

## Goal Impact

TASK-021 prevents ambiguous provider adoption by making promotion thresholds
explicit and executable.

## Project Invariant Impact

- IPS-INV-001: promoted providers remain optional retrieval candidates.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-021.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: promotion fixtures contain only synthetic paths and no sensitive
  data.

## Sensitive-Data Classification

Classification: synthetic

Promotion rules and fixtures use provider ids, thresholds and synthetic path
fixtures only.

## Contract/Schema Impact

This task adds `config/provider_promotion_rules.json` and
`scripts/provider_promotion_gate.py`. It does not change retrieval comparison
case semantics.

## Replay/Determinism Impact

Promotion results are deterministic for a fixed baseline, candidate result file
and promotion rule set.

## Scope

- Add provider promotion rule config.
- Add dry-run candidate fixture.
- Add provider promotion gate.
- Add focused pass and fail tests.
- Add the gate to typecheck coverage.
- Update TASK-021 governance and graph traceability.

## Non-Goals

- Do not promote any real external provider.
- Do not add network calls.
- Do not add credentials.
- Do not change graph-required context behavior.
- Do not modify protected vision or constitution documents.

## Acceptance Criteria

- [x] Promotion rules define required mode, pass rate and failure thresholds.
- [x] Promotion gate checks provider safety gate status.
- [x] Promotion gate checks dry-run and zero-network requirements.
- [x] Promotion gate rejects failed comparisons and wrong candidate modes.
- [x] Promotion gate passes the dry-run candidate fixture.
- [x] Repository validation gates pass.

## Required Context

- `../../config/provider_promotion_rules.json`
- `../../tests/fixtures/retrieval_candidate_dry_run.json`
- `../../scripts/provider_promotion_gate.py`
- `../../tests/test_provider_promotion_gate.py`
- `../../scripts/context_package_generator.py`
- `../../scripts/embedding_provider_gate.py`

## Validation Task

Validate with focused promotion tests, provider promotion gate CLI, provider
safety gate CLI, full repository validation, pre-coding gate and
deployment-readiness gate for TASK-021.

## Required Gates

```bash
python3 -m unittest tests.test_provider_promotion_gate
python3 scripts/provider_promotion_gate.py --root . --baseline tests/fixtures/retrieval_baseline.json --candidate tests/fixtures/retrieval_candidate_dry_run.json --provider external-provider-dry-run
python3 scripts/embedding_provider_gate.py --root .
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-021
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-021.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-021-provider-promotion-thresholds.md`.
