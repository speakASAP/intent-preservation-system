# Coding Prompt: TASK-022 Provider Status Manager Interface

```yaml
id: PROMPT-TASK-022-provider-status-manager-interface
source_task: ../11_tasks/TASK-022-surface-provider-status-in-manager-interface.md
execution_plan: ../21_execution_plans/EP-TASK-022.md
context_package: ../13_context_packages/CP-task-022.md
status: used
```

## Role

You are an implementation agent extending the IPS manager interface with
provider safety and promotion status.

## Task

Implement TASK-022 by surfacing provider gate and promotion status in the
manager interface.

## Context

Use `../13_context_packages/CP-task-022.md` and preserve the existing static
manager interface pattern from TASK-016.

## Constraints

- Do not add real provider calls.
- Do not add credentials.
- Do not change provider safety or promotion gate logic.
- Keep provider status manager-readable.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../manager_interface/index.html`
- `../../manager_interface/styles.css`
- `../../manager_interface/app.js`
- TASK-022 governance and graph traceability documents.

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any credential values or sensitive data.

## Implementation Instructions

1. Add provider status data for the active local provider, dry-run provider
   gate, promotion status and network boundary.
2. Render manager-readable and technical provider status explanations.
3. Add provider navigation, metric and panel markup.
4. Add responsive styling that matches the existing manager interface.
5. Validate with provider and repository gates.

## Parallel Workstream Context

This prompt is for the single source-backed TASK-022
implementation/integration workstream, not a multi-agent parallel wave.

- Source parallel dispatch list:
  `WS-022-implementation-validation` from
  `../21_execution_plans/EP-TASK-022.md`.
- Objective: surface active provider status, dry-run provider safety gate
  status, provider promotion status and zero-network evidence in the existing
  static manager interface, then validate TASK-022.
- Ready-now parallel goals: none. The source-backed executable unit owns shared
  manager interface files and final validation.
- Dependency-gated goals: none for TASK-022.
- Dependencies: TASK-016 manager interface, TASK-019 provider safety gates and
  TASK-021 provider promotion thresholds.
- Owned files from source EP: `../../manager_interface/index.html`,
  `../../manager_interface/styles.css`, `../../manager_interface/app.js` and
  `../../graph/project_graph.example.yaml`.
- Blockers: none for the validated implementation. Live provider calls,
  credentials, provider gate logic changes and real provider promotion remain
  forbidden.
- Integration guidance: edit manager interface files first, update graph
  traceability after the interface scope is known, then run provider and
  repository gates. Separate thread execution is not applicable because this
  workstream owns shared UI files and final validation.
- Expected handoff output: files changed, validation evidence, blockers
  encountered or cleared, dependencies, integration notes, deviations and
  remaining documentation gaps.

## Acceptance criteria

- Manager interface shows active provider status.
- Manager interface shows dry-run provider safety gate status.
- Manager interface shows provider promotion status.
- Provider status has manager-readable and technical readouts.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 scripts/embedding_provider_gate.py --root .
python3 scripts/provider_promotion_gate.py --root . --baseline tests/fixtures/retrieval_baseline.json --candidate tests/fixtures/retrieval_candidate_dry_run.json --provider external-provider-dry-run
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-022
```

## Expected Output

The implementation agent must return files changed, tests run, validation
evidence, blockers encountered or cleared, dependencies on other workstreams,
integration notes, deviations and remaining documentation gaps.
