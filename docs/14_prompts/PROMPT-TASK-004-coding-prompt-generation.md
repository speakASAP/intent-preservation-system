# Coding Prompt: TASK-004 Coding Prompt Generation

```yaml
id: PROMPT-TASK-004-coding-prompt-generation
source_task: ../11_tasks/TASK-004-generate-coding-prompt-from-task-metadata.md
execution_plan: ../21_execution_plans/EP-TASK-004.md
context_package: ../13_context_packages/CP-TASK-001-example.md
status: used
```

## Role

You are an implementation agent working on a bounded context-engine task in the Intent Preservation System.

## Task

Implement TASK-004: add strict documentation-audit readiness checks for coding prompts generated from task metadata, execution plans and context packages.

## Context

Use only the source material declared by TASK-004 and EP-TASK-004:

- `../11_tasks/TASK-004-generate-coding-prompt-from-task-metadata.md`
- `../21_execution_plans/EP-TASK-004.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-004.md`
- `../14_prompts/PROMPT_GUIDELINES.md`
- `../18_templates/CODING_PROMPT_TEMPLATE.md`
- `../18_templates/EXECUTION_PLAN_TEMPLATE.md`
- `../13_context_packages/CP-TASK-001-example.md`
- `../04_systems/SYS-002-context-engine.md`

## Constraints

- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.
- Do not call AI models.
- Do not execute generated implementation code.
- Do not approve execution plans automatically.
- Preserve approval gating for prompts derived from execution plans.

## Allowed Changes

- `../../scripts/strict_doc_audit.py`
- Focused strict-audit fixture tests for coding prompt readiness.
- Prompt examples if readiness metadata changes.
- TASK-004 validation documentation.
- `../../graph/project_graph.example.yaml` when graph edges are needed for prompt traceability.

## Forbidden Changes

- Protected baseline documents under `../00_constitution/` and `../01_vision/`.
- Unrelated task, feature, system, business-goal, or ADR decisions.
- Any prompt, test, report, or example content containing secrets, raw production data, confidential identifiers, or real customer data.

## Implementation Instructions

1. Classify `14_prompts/PROMPT-*.md` artifacts as coding prompts.
2. Enforce required prompt sections for role, task, context, constraints, acceptance criteria and validation.
3. Detect coding prompts derived from draft or missing execution plans.
4. Validate graph edges from execution plans to generated prompts.
5. Validate graph edges from prompt artifacts to their context packages.
6. Add focused fixture coverage for reviewed plans, draft plans, missing prompt sections and missing context-package graph edges.

## Parallel Workstream Context

This prompt is a standalone single-agent prompt because `../21_execution_plans/EP-TASK-004.md` does not expose refactored parallel workstreams.

- Execution-plan status: validated.
- Parallel dispatch list: `WS-004-A` prompt readiness audit, `WS-004-D` prompt documentation alignment if needed, `WS-004-V` validation evidence.
- Goal blockers and dependencies: `WS-004-D` depends on final readiness behavior from `WS-004-A`; `WS-004-V` depends on implementation and documentation handoffs.
- Owned files: `../../scripts/strict_doc_audit.py`, focused prompt-readiness tests, TASK-004 validation documentation, and prompt examples if readiness metadata changes.
- Forbidden files: `../00_constitution/CONSTITUTION.md`, `../01_vision/VISION.md`, unrelated task, feature, system, business-goal or ADR documents.
- Expected handoff output: files changed, validation evidence, blockers, dependencies on other workstreams, integration notes, deviations and remaining documentation gaps.

## Acceptance criteria

- The prompt structure is documented.
- Generated prompt content is traceable to approved task and execution-plan documents.
- Forbidden changes are explicit.
- Validation commands and expected output are included.
- Strict audit rejects prompts derived from draft execution plans.
- Strict audit validates required prompt graph connectivity.

## Validation

Run the narrowest relevant fixture tests, then run:

```bash
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root .
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
