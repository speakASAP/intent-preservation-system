# EP-TASK-005: Propose and Generate Missing Document Drafts

## Metadata

```yaml
id: EP-TASK-005
status: validated
source_task: ../11_tasks/TASK-005-propose-and-generate-missing-document-drafts.md
owner: documentation-audit-agent
created: 2026-06-08
last_updated: 2026-06-12
context_package: ../13_context_packages/CP-TASK-005-safe-draft-remediation.md
coding_prompt: ../14_prompts/PROMPT-TASK-005-safe-draft-remediation.md
```

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-001-documentation-audit.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-005.md
```

## Goal Impact

This plan supports controlled remediation of incomplete documentation while
preserving human review and immutable source-of-truth boundaries.

## Scope

Define the safe draft-generation workflow and audit recommendations that map
missing artifacts to templates.

## Non-Goals

- Do not modify immutable documents.
- Do not invent new project goals.
- Do not write files without explicit approval.
- Do not implement a web interface.

## Files to Inspect

- `scripts/strict_doc_audit.py`
- `18_templates/*.md`
- `23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`

## Files to Create

- Fixture tests for draft-generation recommendations.

## Files to Modify

- `scripts/strict_doc_audit.py`
- Remediation workflow documentation if added.

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Keep audit findings mapped to remediation templates.
2. Ensure recommendations do not write files directly.
3. Require explicit approval before future draft-generation workflows write files.
4. Preserve existing content when missing sections are added.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-005-A | Implement safe remediation recommendations | yes, as the only implementation workstream | documentation-audit agent | `scripts/strict_doc_audit.py`; focused tests under `tests/` | Template-mapped recommendations that do not write files | none |
| WS-005-D | Document approval-gated remediation workflow if added | no, dependency-gated | documentation agent | remediation workflow documentation listed by WS-005-A | Workflow docs preserving explicit approval | WS-005-A behavior |
| WS-005-V | Validate TASK-005 and record evidence | no, final integration | validation agent | `12_validation/VAL-TASK-005-safe-draft-remediation.md` if present or TASK-005 validation report | Validation evidence and readiness recommendation | WS-005-A and WS-005-D if needed |

Separate-thread execution is useful only for WS-005-A before implementation is
complete. Documentation and validation are dependency-gated because they depend
on the final recommendation behavior.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-005-A | No open blocker recorded | documentation-audit agent | Keep remediation approval-gated and non-mutating by default | resolved |
| WS-005-D | Requires final remediation workflow behavior | documentation agent | Update docs only if a workflow is added or changed | dependency-gated |
| WS-005-V | Requires implementation and documentation evidence | validation agent | Run gates and update validation evidence | dependency-gated |

## Parallel Dispatch List

### Goal WS-005-A: Safe Draft Remediation Recommendations

- Owner role: documentation-audit agent.
- Objective: map missing documentation findings to templates without writing
  files or inventing missing source information.
- Allowed files: `scripts/strict_doc_audit.py`; focused tests under `tests/`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, generated drafts without approval, and artifacts
  containing secrets or raw production data.
- Required inputs: TASK-005, this plan, templates under `18_templates/` and
  `23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`.
- Blockers: none open.
- Validation evidence: tests proving recommendations are template-mapped,
  audit execution performs no writes, and missing markers are preserved.
- Handoff output: files changed, recommendation examples, tests run, blockers
  and deviations.

### Goal WS-005-D: Remediation Workflow Documentation

- Owner role: documentation agent.
- Objective: document the approval-gated remediation workflow only if WS-005-A
  adds or changes one.
- Allowed files: remediation workflow documentation identified by WS-005-A.
- Forbidden files: protected vision/constitution files and implementation files
  unless reporting a deviation.
- Required inputs: WS-005-A handoff.
- Blockers: WS-005-A final behavior.
- Validation evidence: documentation review and strict audit output.
- Handoff output: documentation changes, blockers and deviations.

### Goal WS-005-V: Validation Evidence

- Owner role: validation agent.
- Objective: verify safe draft remediation behavior and record evidence.
- Allowed files: TASK-005 validation report under `12_validation/`.
- Forbidden files: protected vision/constitution files and WS-005-A files unless
  a validation defect is reported.
- Required inputs: WS-005-A handoff and WS-005-D handoff if used.
- Blockers: implementation complete; documentation complete if needed.
- Validation evidence: focused tests, strict audit, pre-coding gate and
  deployment-readiness gate output.
- Handoff output: validation report update and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-005-A

You are the TASK-005 documentation-audit agent. Implement safe remediation
recommendations that map findings to templates without writing files by default.
Do not modify protected vision or constitution files, generate drafts without
approval, or invent missing source information. Return files changed, tests run,
recommendation examples, blockers and deviations.

### Workstream WS-005-D

You are the TASK-005 documentation agent. After WS-005-A, document the
approval-gated remediation workflow only if behavior changed. Return
documentation changes, validation evidence, blockers and deviations.

### Workstream WS-005-V

You are the TASK-005 validation agent. After implementation and any
documentation updates, run focused tests, strict audit and gate commands, then
record TASK-005 validation evidence and readiness recommendation.

## Test Plan

- Test missing section recommendations.
- Test missing document recommendations.
- Test no writes occur during audit.
- Test missing information markers are preserved.

## Validation Plan

Run fixture tests and strict audit.

## Documentation Updates

Update audit or operations docs when a draft-generation command is implemented.

## Rollback Plan

Revert audit recommendation changes, tests and workflow documentation for this task.

## Agent Handoff Prompt

Implement TASK-005 using this execution plan. Keep the workflow approval-gated
and do not modify protected baseline documents.

## Completion Checklist

- [x] Remediation recommendations remain template mapped.
- [x] Audit performs no file writes.
- [x] Approval-gated workflow documented or implemented.
- [x] Validation report created.
