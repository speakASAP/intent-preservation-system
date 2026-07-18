# TASK-004: Generate coding prompt from task metadata

```yaml
id: TASK-004
status: validated
owner: context-engine-agent
created: 2026-06-05
last_updated: 2026-06-13
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../10_features/FEAT-002-context-package-generation.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-004.md
execution_plan:
  - ../21_execution_plans/EP-TASK-004.md
validation:
  - ../12_validation/VAL-TASK-004-coding-prompt-generation.md
```

## Objective

Generate a bounded coding prompt from approved task metadata, execution plans, and context packages.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context system: `../04_systems/SYS-002-context-engine.md`
- Parent feature: `../10_features/FEAT-002-context-package-generation.md`
- Prompt guidelines: `../14_prompts/PROMPT_GUIDELINES.md`
- Coding prompt template: `../18_templates/CODING_PROMPT_TEMPLATE.md`

## Goal Impact

This task helps preserve implementation intent by giving coding agents explicit scope, constraints, acceptance criteria, validation commands, and forbidden changes.

## Scope

- Define how task metadata is converted into a coding prompt.
- Include required context, allowed changes, forbidden changes, implementation instructions, acceptance criteria, validation commands, and expected output.
- Ensure generated prompts link back to their execution plan.

## Non-Goals

- Do not call an AI model directly.
- Do not execute generated code.
- Do not bypass execution-plan approval.
- Do not modify immutable baseline documents.

## Acceptance Criteria

- The prompt structure is documented.
- Generated prompt content is traceable to approved task and execution-plan documents.
- Forbidden changes are explicit.
- Validation commands and expected output are included.

## Required Context

- `../14_prompts/PROMPT_GUIDELINES.md`
- `../18_templates/CODING_PROMPT_TEMPLATE.md`
- `../18_templates/EXECUTION_PLAN_TEMPLATE.md`
- `../13_context_packages/CP-TASK-001-example.md`
- `../04_systems/SYS-002-context-engine.md`

## Validation Task

Generate or review `../14_prompts/PROMPT-TASK-001-example.md` and confirm that it includes scope, constraints, acceptance criteria, validation commands, and upstream links.

## Execution Plan Requirement

This task requires an approved execution plan before implementation because generated prompts directly control AI coding-agent behavior.
