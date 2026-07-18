# TASK-003: Create context package schema

```yaml
id: TASK-003
status: validated
owner: context-engine-agent
created: 2026-06-05
last_updated: 2026-06-12
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../10_features/FEAT-002-context-package-generation.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-003.md
execution_plan:
  - ../21_execution_plans/EP-TASK-003.md
validation_report:
  - ../12_validation/VAL-TASK-003-context-package-schema.md
```

## Objective

Create the schema for generated context packages that provide bounded, relevant input to AI coding agents.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context system: `../04_systems/SYS-002-context-engine.md`
- Parent feature: `../10_features/FEAT-002-context-package-generation.md`
- Context package template: `../18_templates/CONTEXT_PACKAGE_TEMPLATE.md`

## Goal Impact

This task supports reliable AI implementation by ensuring agents receive minimal but sufficient context instead of manually assembled, inconsistent prompts.

## Scope

- Define required context package fields.
- Include target task, upstream traceability, required documents, constraints, agent prompt, and validation instructions.
- Support future generation from graph-based retrieval.
- Keep the schema readable as Markdown.

## Non-Goals

- Do not implement semantic retrieval.
- Do not build a vector database.
- Do not generate coding prompts directly.
- Do not change task or feature scope.

## Acceptance Criteria

- The context package schema is documented.
- Required sections are clear enough for AI generation.
- The schema links back to the source task and upstream artifacts.
- Validation instructions are included in every package.

## Required Context

- `../13_context_packages/README.md`
- `../18_templates/CONTEXT_PACKAGE_TEMPLATE.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../04_systems/SYS-002-context-engine.md`
- `../05_subsystems/SUB-003-context-packager.md`

## Validation Task

Generate or review `../13_context_packages/CP-TASK-001-example.md` and confirm that it contains target task, traceability, included documents, constraints, prompt, and validation instructions.

## Execution Plan Requirement

This task requires an approved execution plan before implementation because it defines a reusable artifact contract for AI agents.
