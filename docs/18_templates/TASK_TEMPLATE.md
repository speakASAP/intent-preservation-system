# TASK-XXX: Title

```yaml
id: TASK-XXX
status: draft | reviewed | approved | blocked | completed
owner: TBD
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
completeness_level: skeletal | partial | complete | validated
upstream:
  - ../10_features/FEAT-XXX.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-XXX.md
execution_plan:
  - ../21_execution_plans/EP-TASK-XXX.md
project_invariant_impact: none | preserves | changes | introduces
sensitive_data_classification: none | synthetic | masked | sensitive
contract_schema_impact: none | creates | changes | validates
replay_determinism_impact: none | required | affected
parallel_workstream_context: standalone | ready-now | dependency-gated | final-integration
required_gates:
  - pre-coding
```

## Objective

[MISSING: describe the specific outcome this task must produce]

## Upstream Links

[MISSING: link to feature, milestone, system, vision/evolution if relevant]

## Goal Impact

[MISSING: explain why this task matters and link to goal impact record]

## Project Invariant Impact

[MISSING: list applicable project invariants from ../17_governance/PROJECT_INVARIANTS.md or state not applicable with reason]

## Sensitive-Data Classification

Classification: none | synthetic | masked | sensitive

[MISSING: explain whether the task uses data-bearing examples, logs, fixtures or reports and how they will comply with ../23_documentation_contracts/SENSITIVE_DATA_POLICY.md]

## Contract/Schema Impact

[MISSING: state whether the task creates, changes or validates contracts, schemas, APIs, examples or structured artifacts]

## Replay/Determinism Impact

[MISSING: state whether replay, idempotency or deterministic validation applies]

## Scope

[MISSING: define what is included]

## Non-Goals

[MISSING: define what is excluded]

## Acceptance Criteria

- [ ] [MISSING: measurable criterion]

## Required Context

[MISSING: list documents required by the agent]

## Validation Task

[MISSING: define how completion will be validated]

## Required Gates

[MISSING: list required pre-coding, contract, replay, integration-readiness or deployment-readiness gates]

| Gate | Required? | Command or evidence path | Blocks on |
|---|---|---|---|
| Pre-coding | yes/no | [MISSING: command or report path] | [MISSING: missing traceability, invariant, data, contract or validation evidence] |
| Contract/schema | yes/no/not applicable | [MISSING: command or report path] | [MISSING: contract or example validation failure] |
| Replay/determinism | yes/no/not applicable | [MISSING: command or report path] | [MISSING: replay, idempotency or deterministic validation failure] |
| Integration-readiness | yes/no/not applicable | [MISSING: command or report path] | [MISSING: dependency, shared-file or merge blocker] |
| Deployment-readiness | yes/no/not applicable | [MISSING: command or report path] | [MISSING: unresolved validation or gate failure] |

## Parallel Workstream Context

[MISSING: state whether this task is standalone, a ready-now parallel workstream, dependency-gated, blocked or final integration]

- Owner role: [MISSING: owner role]
- Allowed files: [MISSING: exact paths or not applicable]
- Forbidden files: [MISSING: protected paths]
- Dependencies: [MISSING: upstream workstreams, decisions, credentials, files or none]
- Expected handoff output: [MISSING: validation evidence, changed sections, blockers and next action]

## Execution Plan Requirement

This task must not be converted into a coding prompt until an approved execution plan exists.
