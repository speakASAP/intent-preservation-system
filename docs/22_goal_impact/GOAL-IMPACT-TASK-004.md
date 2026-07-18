# GOAL-IMPACT-TASK-004: Coding Prompt Generation

```yaml
id: GOAL-IMPACT-TASK-004
artifact_type: task
artifact_id: TASK-004
artifact_path: ../11_tasks/TASK-004-generate-coding-prompt-from-task-metadata.md
primary_goal: Preserve task intent inside generated AI coding prompts.
secondary_goals:
  - Prevent prompts from bypassing approved execution plans.
  - Keep validation commands and forbidden changes visible.
impact_level: high
impact_description: This task ensures generated prompts remain derived from approved task, plan and context-package artifacts.
success_metric: Prompt artifacts include traceable scope, constraints, acceptance criteria, validation commands and expected output.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
downstream_links:
  - ../21_execution_plans/EP-TASK-004.md
validation_method: Review generated prompt examples against prompt guidelines and approved execution-plan metadata.
status: validated
```

## Explanation

TASK-004 protects downstream implementation by ensuring AI coding prompts carry
the task scope, constraints and validation requirements rather than free-form
instructions.

## Evidence

- Vision outcome: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Prompt guidelines: `../14_prompts/PROMPT_GUIDELINES.md`
- Execution plan: `../21_execution_plans/EP-TASK-004.md`

## Validation

The impact is valid when prompt generation refuses unapproved execution plans
and generated prompts retain required traceability and validation content.
