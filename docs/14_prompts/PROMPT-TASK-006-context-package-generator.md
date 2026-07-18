# Coding Prompt: TASK-006 Context Package Generator

```yaml
id: PROMPT-TASK-006-context-package-generator
source_task: ../11_tasks/TASK-006-generate-context-package-by-task-id.md
execution_plan: ../21_execution_plans/EP-TASK-006.md
context_package: ../13_context_packages/CP-task-006.md
status: used
```

## Role

You are an implementation agent working on a bounded context-engine task in
the Intent Preservation System.

## Task

Implement TASK-006: generate a deterministic Markdown context package for one
task id from declared task metadata and required-context links.

## Context

Use only the source material listed in `../13_context_packages/CP-task-006.md`,
especially:

- `../11_tasks/TASK-006-generate-context-package-by-task-id.md`
- `../21_execution_plans/EP-TASK-006.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-006.md`
- `../18_templates/CONTEXT_PACKAGE_TEMPLATE.md`
- `../04_systems/SYS-002-context-engine.md`
- `../05_subsystems/SUB-003-context-packager.md`

## Constraints

- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.
- Do not infer undeclared context or dependencies.
- Do not call an AI model.
- Keep generated package output deterministic.
- Use only synthetic test fixture content.

## Allowed Changes

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- TASK-006 documentation, context package, validation report and graph entries.

## Forbidden Changes

- Protected baseline documents under `../00_constitution/` and `../01_vision/`.
- Unrelated task scopes, roadmap goals or business-goal documents.
- Any prompt, fixture, report or generated package containing secrets, raw
  production data, confidential identifiers or real customer data.

## Implementation Instructions

1. Parse task metadata from a single `11_tasks/TASK-*.md` document.
2. Include the target task, upstream links, goal-impact link, execution-plan
   link, validation-report link and required-context paths.
3. Render required context package sections as Markdown.
4. Refuse to overwrite existing package output unless explicitly forced.
5. Add focused fixture tests for generation and overwrite behavior.

## Parallel Workstream Context

This prompt is a standalone single-agent prompt because `../21_execution_plans/EP-TASK-006.md` does not expose refactored parallel workstreams.

- Execution-plan status: validated.
- Parallel dispatch list: `WS-006-A` generator implementation, `WS-006-D` generated artifacts and graph links, `WS-006-V` final validation.
- Goal blockers and dependencies: `WS-006-D` depends on final generator output from `WS-006-A`; `WS-006-V` depends on implementation and artifact handoffs.
- Owned files: `../../scripts/context_package_generator.py`, `../../tests/test_context_package_generator.py`, TASK-006 documentation, context package, validation report and graph entries.
- Forbidden files: `../00_constitution/CONSTITUTION.md`, `../01_vision/VISION.md`, unrelated task scopes, roadmap goals or business-goal documents.
- Expected handoff output: files changed, validation evidence, blockers, dependencies on other workstreams, integration notes, deviations and remaining documentation gaps.

## Acceptance criteria

- The command generates a context package for a task id.
- The generated package includes target task, upstream traceability, included
  documents, excluded documents, constraints, agent prompt and validation instructions.
- The command refuses accidental overwrite unless `--force` is supplied.
- Fixture tests cover generation and overwrite safety.
- Repository validation passes.

## Validation

Run:

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-006
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
