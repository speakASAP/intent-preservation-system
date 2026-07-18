# Coding Prompt: TASK-012 Harden Optional Local Retrieval

```yaml
id: PROMPT-TASK-012-harden-optional-local-retrieval
source_task: ../11_tasks/TASK-012-harden-optional-local-retrieval.md
execution_plan: ../21_execution_plans/EP-TASK-012.md
context_package: ../13_context_packages/CP-task-012.md
status: used
```

## Role

You are an implementation agent hardening local optional retrieval for IPS.

## Task

Implement TASK-012: add auditable score metadata, scan summary and
minimum-score filtering to deterministic optional keyword retrieval.

## Context

Use `../13_context_packages/CP-task-012.md` and preserve the TASK-011 optional
retrieval contract.

## Constraints

- Do not add embeddings, vector search or external API calls.
- Do not replace graph-required context.
- Preserve existing TASK-011 report fields.
- Keep output deterministic.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- TASK-012 validation documentation.

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any fixture, prompt or report containing secrets or raw production data.

## Implementation Instructions

1. Add score component details to suggestions.
2. Add report-level query terms and scan summary.
3. Add minimum-score filtering to the function and CLI.
4. Preserve required context and optional suggestions as separate fields.
5. Add focused tests and run validation gates.

## Parallel Workstream Context

- Prompt type: implementation prompt derived from a source execution plan that
  now exposes refactored parallel dispatch metadata.
- Source blocker: none; `../21_execution_plans/EP-TASK-012.md` includes
  Parallel Dispatch List, Goal Blockers And Dependencies and Parallel Agent
  Handoff Prompts.
- Dependencies: use the serial dependencies and files listed in the execution
  plan; `WS-012-A` must preserve TASK-011 compatibility, and
  `WS-012-D`/`WS-012-V` depend on the implementation handoff.
- Owned files: `WS-012-A` owns implementation/test files; `WS-012-D` owns
  TASK-012 artifact and graph updates; `WS-012-V` owns final validation evidence.
- Expected handoff: return validation evidence, remaining blockers,
  dependencies on other agent workstreams and integration notes.

## Acceptance criteria

- Optional suggestions include score component metadata.
- Reports include query terms and scan summary metadata.
- CLI supports minimum-score filtering.
- Existing TASK-011 report fields remain available.
- Tests cover scoring metadata, filtering and deterministic ordering.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-012
```

## Expected Output

The implementation agent must return:

- Files changed.
- Documents created.
- Missing sections filled.
- Remaining missing-information markers.
- Validation evidence.
- Blockers encountered or cleared.
- Dependencies on other agent workstreams.
- Integration or merge notes.
- Deviations from plan.
