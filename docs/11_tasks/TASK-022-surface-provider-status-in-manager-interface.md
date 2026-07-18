# TASK-022: Surface provider status in manager interface

```yaml
id: TASK-022
status: validated
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../10_features/FEAT-004-manager-visibility.md
  - ../11_tasks/TASK-016-create-manager-visibility-interface.md
  - ../11_tasks/TASK-019-add-embedding-provider-safety-gates.md
  - ../11_tasks/TASK-021-add-provider-promotion-thresholds.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-022.md
execution_plan:
  - ../21_execution_plans/EP-TASK-022.md
validation_report:
  - ../12_validation/VAL-TASK-022-provider-status-manager-interface.md
```

## Objective

Surface provider safety gate and promotion status in the existing static
manager interface so managers can see whether optional retrieval providers are
safe, offline and promotable.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Manager visibility feature: `../10_features/FEAT-004-manager-visibility.md`
- Manager interface base task: `../11_tasks/TASK-016-create-manager-visibility-interface.md`
- Provider safety gates: `../11_tasks/TASK-019-add-embedding-provider-safety-gates.md`
- Provider promotion thresholds: `../11_tasks/TASK-021-add-provider-promotion-thresholds.md`

## Goal Impact

TASK-022 makes provider safety and promotion decisions visible to managers
without requiring them to inspect JSON configuration, CLI output or test
fixtures.

## Project Invariant Impact

- IPS-INV-001: provider status is shown only for optional retrieval candidates.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation is bounded to the manager interface and TASK-022
  governance artifacts.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: provider status content uses synthetic fixture and config
  metadata only.

## Sensitive-Data Classification

Classification: synthetic

The interface displays provider ids, gate status and dry-run metrics only. It
does not display credentials, raw provider payloads, production data or
customer identifiers.

## Contract/Schema Impact

No provider gate or promotion schema changes are introduced. TASK-022 consumes
the existing `../../config/embedding_provider_gates.json`,
`../../config/provider_promotion_rules.json` and
`../../tests/fixtures/retrieval_candidate_dry_run.json` meanings in a static
manager-facing readout.

## Replay/Determinism Impact

The displayed status is deterministic static content derived from the validated
provider safety and promotion artifacts.

## Scope

- Add provider safety and promotion status to `../../manager_interface/`.
- Add manager and technical explanations for provider status.
- Add provider gates to the evidence-gate list.
- Add TASK-022 governance and graph traceability artifacts.

## Non-Goals

- Do not add live provider calls.
- Do not add credentials.
- Do not promote a real external provider.
- Do not change retrieval ranking or provider gate semantics.
- Do not modify protected vision or constitution documents.

## Acceptance Criteria

- [x] Manager interface shows active provider status.
- [x] Manager interface shows dry-run provider safety gate status.
- [x] Manager interface shows provider promotion status.
- [x] Provider status has manager-readable and technical readouts.
- [x] Manager comparison mode shows graphical status rather than the technical
  evidence table.
- [x] Repository validation gates pass.

## Required Context

- `../../manager_interface/index.html`
- `../../manager_interface/styles.css`
- `../../manager_interface/app.js`
- `../../config/embedding_provider_gates.json`
- `../../config/provider_promotion_rules.json`
- `../../tests/fixtures/retrieval_candidate_dry_run.json`

## Validation Task

Validate with provider safety gate, promotion gate, repository validation,
pre-coding gate and deployment-readiness gate for TASK-022.

## Required Gates

```bash
python3 scripts/embedding_provider_gate.py --root .
python3 scripts/provider_promotion_gate.py --root . --baseline tests/fixtures/retrieval_baseline.json --candidate tests/fixtures/retrieval_candidate_dry_run.json --provider external-provider-dry-run
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-022
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-022.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-022-provider-status-manager-interface.md`.
