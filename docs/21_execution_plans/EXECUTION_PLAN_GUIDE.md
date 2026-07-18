# Execution Plan Guide

## Purpose

An execution plan sits between a task and code. It converts a task into concrete, bounded implementation goals that can be executed by one coding agent or split into parallel agent sessions when dependencies allow. A coordination plan may group multiple execution plans into parallel goal waves, but each executable goal remains owned by one agent session.

The flow is:

```text
Goal -> Feature -> Task -> Execution Plan -> Coding Prompt -> Code -> Validation Report
```

## Why execution plans are required

A task often says what should be done. A coding agent also needs to know:

- Which files to create
- Which files to modify
- Which files must not be touched
- Which tests to add or update
- Which acceptance criteria must be proven
- What dependencies are required
- How to roll back if the result is wrong
- What documentation must be updated after coding

Without this layer, coding prompts become too vague and agents improvise.

## Required sections

Every execution plan must include:

1. Metadata
2. Upstream traceability
3. Goal impact
4. Scope
5. Non-goals
6. Files to inspect
7. Files to create
8. Files to modify
9. Files that must not be modified
10. Implementation steps
11. Parallel execution strategy
12. Goal blockers and dependencies
13. Parallel dispatch list
14. Test plan
15. Validation plan
16. Documentation updates
17. Rollback plan
18. Agent handoff prompt
19. Completion checklist

Operational execution plans must also declare:

- applicable project invariants;
- sensitive-data handling;
- contract validation plan;
- replay/determinism plan;
- gate commands.

Use the generic operational policy names unless a repository defines stricter local equivalents:

- `17_governance/PROJECT_INVARIANTS.md`
- `23_documentation_contracts/SENSITIVE_DATA_POLICY.md`
- `23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md`

## Execution plan status lifecycle

```text
draft -> reviewed -> approved -> in-progress -> implemented -> validated -> closed
```

Only approved execution plans should be converted into coding prompts.

## Parallel-first rule

An execution plan should be decomposed into goal workstreams that one AI coding agent can complete in one focused session.

If multiple workstreams can be started without waiting for each other, the plan must make that explicit so they can be assigned to different agents and executed in parallel. When the executing environment supports Codex thread creation, ready-now parallel workstreams should be launched in separate threads so the plan's parallelism is actually used.

Split the plan if:

- It touches unrelated subsystems.
- It requires more than one independent validation strategy.
- It contains more than one primary goal.
- It requires broad refactoring plus feature implementation.

## Parallel dispatch rule

Every execution plan must include a parallel execution assessment and a handoff-ready Parallel Dispatch List:

- Identify each independently startable goal or workstream.
- State the owner role or recommended agent type for each workstream.
- List allowed files, forbidden files and expected outputs per workstream.
- Mark whether the workstream can start immediately, must wait for another workstream, or is blocked.
- Name blockers with the exact missing decision, dependency, credential, environment, file or validation evidence.
- State whether the workstream should be opened as its own Codex thread, or explain why separate-thread execution is not applicable.
- Define merge or integration order when parallel workstreams touch shared contracts, public APIs, schemas, generated artifacts or the same files.
- Identify the final integration and validation workstream, even when all implementation workstreams can run in parallel.

Prefer several small handoff prompts over one broad prompt. If two workstreams touch the same file, shared schema or public contract, they are not parallel until the plan defines an integration owner and conflict-resolution order.

The Parallel Dispatch List must be suitable for assigning directly to multiple agents. For each item include goal id, objective, allowed files, forbidden files, required inputs, blockers, validation evidence and expected handoff output.

## Agent rules

A coding agent may:

- Implement only the approved scope.
- Modify only files listed in the plan unless it explicitly reports a required deviation.
- Add tests required by the plan.
- Update documentation listed by the plan.

A coding agent must not:

- Change the original vision.
- Change ADRs.
- Expand scope without approval.
- Skip validation.
- Mark the plan completed without evidence.

## Validation of execution plans

Before coding starts, validate that:

- The plan links to a task.
- The task links to a feature or milestone.
- The feature links to a goal.
- Parallelizable workstreams and serial dependencies are declared.
- Blockers are explicit and assigned to either a prerequisite workstream or a human decision.
- Acceptance criteria are measurable.
- Required files are known or discovery steps are defined.
- Parallel-ready goals, dependency-gated goals, blockers, and shared-file merge order are explicit when the work can be split across agents.
- Tests are explicit.
- Rollback is possible.
- Applicable invariants and data-protection requirements are explicit.
- Contract/schema impact and replay/determinism impact are explicit.
- Required gates can be run locally.
- Gate evidence paths or terminal-output expectations are named before work starts.

## AI-cycle artifacts

Use AI-cycle review artifacts for work that touches contracts, data-bearing examples, production workflows, deployment readiness or cross-system behavior.

Recommended sequence:

```text
execution plan
  -> AI cycle plan review
  -> data-protection review
  -> contract review when applicable
  -> executor report
  -> cycle summary
```

Templates live in `18_templates/`:

- `AI_CYCLE_PLAN_REVIEW_TEMPLATE.md`
- `AI_CYCLE_DATA_PROTECTION_REVIEW_TEMPLATE.md`
- `AI_CYCLE_CONTRACT_REVIEW_TEMPLATE.md`
- `AI_CYCLE_EXECUTOR_REPORT_TEMPLATE.md`
- `AI_CYCLE_SUMMARY_TEMPLATE.md`
