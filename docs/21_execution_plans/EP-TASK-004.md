# EP-TASK-004: Generate Coding Prompt From Task Metadata

## Metadata

```yaml
id: EP-TASK-004
status: validated
source_task: ../11_tasks/TASK-004-generate-coding-prompt-from-task-metadata.md
owner: context-engine-agent
created: 2026-06-08
last_updated: 2026-06-13
completeness_level: validated
validation_report: ../12_validation/VAL-TASK-004-coding-prompt-generation.md
```

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-002-context-package-generation.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-004.md
```

## Goal Impact

This plan prevents coding prompts from bypassing task intent, execution-plan
scope and validation requirements.

## Scope

Define prompt readiness checks and ensure prompt artifacts derive only from
reviewed or approved execution plans.

## Non-Goals

- Do not call AI models.
- Do not execute generated code.
- Do not approve execution plans automatically.

## Files to Inspect

- `14_prompts/PROMPT_GUIDELINES.md`
- `18_templates/CODING_PROMPT_TEMPLATE.md`
- `21_execution_plans/*.md`

## Files to Create

- Fixture tests for prompts generated from draft plans.

## Files to Modify

- `scripts/strict_doc_audit.py`
- Prompt examples if readiness metadata changes.

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Classify prompt artifacts.
2. Enforce required prompt sections.
3. Detect prompts associated with draft or missing execution plans.
4. Validate graph edges from execution plans to prompts and prompts to context packages.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-004-A | Implement prompt readiness and section checks | yes, as the only implementation workstream | context-engine audit agent | `scripts/strict_doc_audit.py`; prompt-readiness tests under `tests/` | Deterministic prompt audit findings and tests | none |
| WS-004-D | Align prompt examples or guidance if readiness metadata changes | no, dependency-gated | prompt documentation agent | `14_prompts/`; `18_templates/CODING_PROMPT_TEMPLATE.md` | Prompt docs/examples aligned to implemented checks | WS-004-A final behavior |
| WS-004-V | Validate TASK-004 and record evidence | no, final integration | validation agent | `12_validation/VAL-TASK-004-coding-prompt-generation.md` | Validation evidence and readiness recommendation | WS-004-A and WS-004-D if needed |

Separate-thread execution is only appropriate for WS-004-A before implementation
is complete. WS-004-D starts only when WS-004-A changes metadata semantics.
WS-004-V remains the final integration workstream.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-004-A | No open blocker recorded | context-engine audit agent | Preserve approval gating for draft execution plans | resolved |
| WS-004-D | Requires final prompt readiness behavior | prompt documentation agent | Update docs/examples only if behavior changes | dependency-gated |
| WS-004-V | Requires implementation and documentation evidence | validation agent | Run gates and update validation evidence | dependency-gated |

## Parallel Dispatch List

### Goal WS-004-A: Prompt Readiness Audit

- Owner role: context-engine audit agent.
- Objective: enforce prompt section requirements and prevent prompts from being
  treated as ready when their execution plan is draft or missing.
- Allowed files: `scripts/strict_doc_audit.py`; focused tests under `tests/`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, unrelated validated artifacts, and artifacts
  containing secrets or raw production data.
- Required inputs: TASK-004, this plan, `14_prompts/PROMPT_GUIDELINES.md`,
  `18_templates/CODING_PROMPT_TEMPLATE.md` and `21_execution_plans/*.md`.
- Blockers: none open.
- Validation evidence: focused prompt-readiness tests and strict audit output.
- Handoff output: files changed, findings format, tests run, blockers and
  deviations.

### Goal WS-004-D: Prompt Documentation Alignment

- Owner role: prompt documentation agent.
- Objective: align prompt examples and templates with final readiness metadata
  only if WS-004-A changes the contract.
- Allowed files: relevant files under `14_prompts/`;
  `18_templates/CODING_PROMPT_TEMPLATE.md`.
- Forbidden files: protected vision/constitution files and implementation files
  unless reporting a deviation.
- Required inputs: WS-004-A handoff.
- Blockers: WS-004-A final behavior.
- Validation evidence: documentation diff review and strict audit output.
- Handoff output: documentation changes, blockers and deviations.

### Goal WS-004-V: Validation Evidence

- Owner role: validation agent.
- Objective: verify TASK-004 behavior and preserve validation evidence.
- Allowed files: `12_validation/VAL-TASK-004-coding-prompt-generation.md`.
- Forbidden files: protected vision/constitution files and implementation files
  unless a validation defect is reported.
- Required inputs: WS-004-A handoff and WS-004-D handoff if used.
- Blockers: implementation complete; documentation complete if needed.
- Validation evidence: strict audit, pre-coding gate and deployment-readiness
  gate output.
- Handoff output: validation report update and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-004-A

You are the TASK-004 context-engine audit agent. Implement prompt readiness
checks that derive from reviewed execution plans and required prompt sections.
Modify only `scripts/strict_doc_audit.py` and focused tests under `tests/`.
Preserve protected vision and constitution files. Return files changed, tests
run, findings format, blockers and deviations.

### Workstream WS-004-D

You are the TASK-004 prompt documentation agent. After WS-004-A, update prompt
examples or `18_templates/CODING_PROMPT_TEMPLATE.md` only if readiness metadata
changed. Return documentation changes, evidence, blockers and deviations.

### Workstream WS-004-V

You are the TASK-004 validation agent. After implementation and any
documentation updates, run strict audit and gate commands, then update
`12_validation/VAL-TASK-004-coding-prompt-generation.md` with evidence and a
readiness recommendation.

## Test Plan

- Test prompt from reviewed plan.
- Test prompt from draft plan.
- Test prompt with missing required sections.
- Test missing context package edge.

## Validation Plan

Run fixture tests and strict audit.

## Documentation Updates

Update prompt guidance if readiness rules change.

## Rollback Plan

Revert audit code, tests and prompt documentation updates for this task.

## Agent Handoff Prompt

Implement TASK-004 using this execution plan. Preserve approval gating and do
not generate prompts from draft execution plans.

## Completion Checklist

- [x] Prompt section checks implemented.
- [x] Draft-plan prompt check implemented.
- [x] Graph prompt edges validated.
- [x] Validation report created.
