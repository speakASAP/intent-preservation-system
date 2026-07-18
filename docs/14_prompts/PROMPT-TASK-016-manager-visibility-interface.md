# Coding Prompt: TASK-016 Manager Visibility Interface

```yaml
id: PROMPT-TASK-016-manager-visibility-interface
source_task: ../11_tasks/TASK-016-create-manager-visibility-interface.md
execution_plan: ../21_execution_plans/EP-TASK-016.md
context_package: ../13_context_packages/CP-task-016.md
status: used
```

## Role

You are an implementation agent adding a static manager-facing interface for the
Intent Preservation System.

## Task

Implement TASK-016: create a basic web page that shows IPS status, traceability,
retrieval comparison and validation evidence in language understandable by
managers.

## Context

Use `../13_context_packages/CP-task-016.md` and preserve the repository as the
source of truth.

## Constraints

- Do not modify protected vision or constitution documents.
- Do not add a backend service.
- Do not connect to production systems.
- Do not include secrets, customer data or raw production data.
- Keep the page responsive and readable on desktop and mobile.

## Allowed Changes

- `../../manager_interface/index.html`
- `../../manager_interface/styles.css`
- `../../manager_interface/app.js`
- TASK-016 governance and validation documentation.
- `../../graph/project_graph.example.yaml`

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any prompt, fixture, report or page content containing sensitive data.

## Implementation Instructions

1. Add a static interface with overview, traceability, retrieval comparison and
   validation sections.
2. Explain the IPS chain in manager-readable language.
3. Include interactive comparison mode controls using local JavaScript only.
4. Keep the visual design restrained, readable and responsive.
5. Validate with local serving, visual checks and repository gates.

## Parallel Workstream Context

- Prompt type: validated historical implementation prompt with resolved
  parallel workstream context from
  `../21_execution_plans/EP-TASK-016.md`.
- Ready-now workstreams: WS-016-A governance chain documents, WS-016-B static
  manager interface and WS-016-C graph traceability entry.
- Dependency-gated workstream: WS-016-D final validation and evidence after
  WS-016-A, WS-016-B and WS-016-C complete.
- Dependencies: WS-016-A, WS-016-B and WS-016-C have no source-identified
  approval, credential, production data or external environment blocker;
  WS-016-D depends on their completed outputs.
- Owned files: use `Allowed Changes` above, split by the execution plan's
  `Parallel Dispatch List` and `Shared Files And Merge Order`.
- Expected handoff: return validation evidence, remaining blockers,
  dependencies on other agent workstreams and integration notes.

## Acceptance criteria

- Managers can open a basic web page and see the IPS status.
- The page shows traceability from vision to validation.
- The page shows how baseline and candidate retrieval are compared.
- The page explains manager-relevant risks and next checks.
- The page is responsive and visually verified.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest discover -s tests
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-016
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
