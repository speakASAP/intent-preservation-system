---
status: draft
owner: repository-owner
last_updated: YYYY-MM-DD
---

# EP-TASK-XXX: Execution Plan Title

```yaml
id: EP-TASK-XXX
status: draft | reviewed | approved | in-progress | implemented | validated | closed
source_task: ../11_tasks/TASK-XXX.md
owner: TBD
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
completeness_level: skeletal | partial | complete | validated
parallelization_strategy: single_agent | parallel_goals | blocked
project_invariant_impact: none | preserves | changes | introduces
sensitive_data_classification: none | synthetic | masked | sensitive
contract_schema_impact: none | creates | changes | validates
replay_determinism_impact: none | required | affected
required_gates:
  - pre-coding
```

## Metadata

[MISSING: add owner, status, source task, and lifecycle state]

## Upstream Traceability

[MISSING: link to vision, business case, feature, milestone, and goal impact]

## Goal Impact

[MISSING: explain the business/product goal contribution]

## Project Invariants

[MISSING: list applicable invariants and how the implementation will preserve them]

Source policy: `../17_governance/PROJECT_INVARIANTS.md`

## Sensitive-Data Handling

[MISSING: state data classification and how prompts, tests, examples, logs and reports avoid secrets or raw production data]

Source policy: `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Contract Validation Plan

[MISSING: state contract/schema impact, validation command and report evidence, or state not applicable]

| Contract or schema | Impact | Validator/command | Evidence path | Owner |
|---|---|---|---|---|
| [MISSING: artifact or not applicable] | none/create/change/validate | [MISSING: command] | [MISSING: report path] | [MISSING: owner] |

## Replay/Determinism Plan

[MISSING: state replay, idempotency or deterministic validation expectations and evidence, or state not applicable]

| Behavior | Required? | Validation method | Evidence path |
|---|---|---|---|
| Replay | yes/no/not applicable | [MISSING: method] | [MISSING: report path] |
| Idempotency | yes/no/not applicable | [MISSING: method] | [MISSING: report path] |
| Deterministic output | yes/no/not applicable | [MISSING: method] | [MISSING: report path] |

## Scope

[MISSING: define exact implementation scope]

## Non-Goals

[MISSING: define what must not be done]

## Parallelization Plan

[MISSING: state whether this plan is standalone or part of a parallel goal wave]

### Ready-Now Parallel Goals

[MISSING: list independent goals that can start immediately, their owners, assigned files, and validation responsibilities, or state none]

### Dependency-Gated Goals

[MISSING: list goals that cannot start until a dependency is completed, or state none]

### Blockers

[MISSING: list contract, approval, environment, ownership, or data blockers for this goal]

### Shared Files And Merge Order

[MISSING: list files touched by more than one goal and define merge/review order, or state none]

## Files to Inspect

[MISSING: list files the coding agent should read first]

## Files to Create

[MISSING: list new files expected]

## Files to Modify

[MISSING: list existing files allowed to change]

## Files That Must Not Be Modified

[MISSING: list protected files]

## Implementation Steps

1. [MISSING: step]

When multiple implementation steps are independent, group them by parallel wave instead of presenting a purely sequential list.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| [MISSING: workstream id] | [MISSING: goal] | yes/no/blocked | [MISSING: owner role] | [MISSING: paths] | [MISSING: deliverable] | [MISSING: dependency or none] |

[MISSING: for every ready-now parallel workstream, state whether it should be started in a separate Codex thread, or explain why separate-thread execution is not applicable]

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| [MISSING: workstream id] | [MISSING: blocker, dependency, or none] | [MISSING: agent/human/system] | [MISSING: concrete action or evidence] | open/resolved/not applicable |

## Parallel Dispatch List

### Goal [MISSING: id]: [MISSING: title]

- Owner role: [MISSING: recommended agent role]
- Objective: [MISSING: bounded objective]
- Allowed files: [MISSING: exact paths]
- Forbidden files: [MISSING: exact paths]
- Required inputs: [MISSING: documents, contracts, or prior goals]
- Blockers: [MISSING: blockers or none]
- Validation evidence: [MISSING: command or report]
- Handoff output: [MISSING: what the integration agent receives]

## Parallel Agent Handoff Prompts

### Workstream [MISSING: id]

[MISSING: bounded prompt for one agent session, including goal, allowed files, forbidden files, validation commands, expected output, and handoff notes]

## Test Plan

[MISSING: describe tests to add or run]

## Validation Plan

[MISSING: describe how to validate the completed task]

## Gate Commands

Source policy: `../23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md`

```bash
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root .
```

[MISSING: add contract, replay or integration-readiness commands when applicable]

| Gate | Required? | Command | Evidence path | Blocks next phase? |
|---|---|---|---|---|
| Pre-coding | yes/no | `python3 scripts/pre_coding_gate.py --root .` | [MISSING: report path or terminal output] | yes/no |
| Contract/schema | yes/no/not applicable | [MISSING: command] | [MISSING: report path] | yes/no |
| Replay/determinism | yes/no/not applicable | [MISSING: command] | [MISSING: report path] | yes/no |
| Integration-readiness | yes/no/not applicable | [MISSING: command] | [MISSING: report path] | yes/no |
| Deployment-readiness | yes/no | `python3 scripts/deployment_readiness_gate.py --root .` | [MISSING: report path or terminal output] | yes/no |

## Documentation Updates

[MISSING: list documentation files to update]

## Rollback Plan

[MISSING: describe how to revert safely]

## Agent Handoff Prompt

[MISSING: final integration prompt, or state that all implementation prompts are listed under Parallel Agent Handoff Prompts]

## Completion Checklist

- [ ] Implementation complete
- [ ] Parallelizable workstreams identified
- [ ] Blockers and serial dependencies documented
- [ ] Agent handoff prompts created for independent workstreams
- [ ] Integration order documented
- [ ] Tests complete
- [ ] Validation evidence collected
- [ ] Documentation updated
- [ ] Deviations documented
