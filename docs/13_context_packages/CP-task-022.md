# Context Package: TASK-022

## Target task

TASK-022: `../11_tasks/TASK-022-surface-provider-status-in-manager-interface.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-004-manager-visibility.md -> TASK-022
```

## Included documents

- `../11_tasks/TASK-022-surface-provider-status-in-manager-interface.md`
- `../21_execution_plans/EP-TASK-022.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-022.md`
- `../12_validation/VAL-TASK-022-provider-status-manager-interface.md`
- `../11_tasks/TASK-016-create-manager-visibility-interface.md`
- `../11_tasks/TASK-019-add-embedding-provider-safety-gates.md`
- `../11_tasks/TASK-021-add-provider-promotion-thresholds.md`
- `../../manager_interface/index.html`
- `../../manager_interface/styles.css`
- `../../manager_interface/app.js`
- `../../config/embedding_provider_gates.json`
- `../../config/provider_promotion_rules.json`
- `../../tests/fixtures/retrieval_candidate_dry_run.json`

## Excluded documents

- Provider credentials are excluded.
- Real external provider outputs are excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Do not add live external provider calls.
- Do not add credentials.
- Do not change provider gate or promotion gate semantics.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Agent prompt

Implement TASK-022 by surfacing provider gate and promotion status in the
manager interface.

## Parallel dispatch and blockers

- Parallelization source: `../21_execution_plans/EP-TASK-022.md`.
- Execution model in source EP: single implementation/integration workstream,
  not a multi-agent parallel wave.
- Parallel dispatch list: `WS-022-implementation-validation` surfaces active
  provider status, dry-run provider safety gate status, provider promotion
  status and zero-network evidence in the existing static manager interface,
  then validates TASK-022.
- Ready-now parallel goals: none. The source-backed executable unit owns shared
  manager interface files and final validation.
- Dependency-gated goals: none. TASK-016, TASK-019 and TASK-021 are completed
  required inputs rather than additional TASK-022 workstreams.
- Blockers: none for the validated implementation. Live provider calls,
  credentials, provider gate logic changes and real provider promotion remain
  forbidden.
- Allowed files for the workstream: `../../manager_interface/index.html`,
  `../../manager_interface/styles.css`, `../../manager_interface/app.js`,
  `../../graph/project_graph.example.yaml` and TASK-022 governance artifacts.
- Shared-file merge order: edit manager interface files first, update graph
  traceability after the interface scope is known, then run provider and
  repository gates. Separate thread execution is not applicable.
- Handoff output: files changed, validation evidence, blockers encountered or
  cleared, dependencies, integration notes, deviations and remaining
  documentation gaps.

## Validation instructions

Run:

```bash
python3 scripts/embedding_provider_gate.py --root .
python3 scripts/provider_promotion_gate.py --root . --baseline tests/fixtures/retrieval_baseline.json --candidate tests/fixtures/retrieval_candidate_dry_run.json --provider external-provider-dry-run
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-022
```
