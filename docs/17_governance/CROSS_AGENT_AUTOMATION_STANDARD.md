# Cross-Agent Automation Standard

## Purpose

This standard defines how AI agents, automation jobs, and background worker sessions must coordinate work across company repositories. It is agent-neutral and applies to Codex, Claude Code, Copilot, Cursor, and other AI coding agents.

## Required Operating Model

Every repository using this standard must preserve the chain:

```text
Vision -> Goal Impact -> System -> Feature -> Task -> Execution Plan -> Coding Prompt -> Code -> Validation
```

Agents must separate work into these roles:

1. Readiness scanner: classifies goals as ready now, dependency-gated, blocked, active elsewhere, complete, or needs owner input.
2. Worker agent: implements one bounded goal or workstream with explicit allowed files, forbidden files, validation evidence, and handoff output.
3. Worker monitor: tracks active workers, extracts safe handoff facts, and detects shared-file conflicts.
4. Integration validator: validates completed worker batches, separates current-task failures from known validation debt, and records final integration evidence.

One conversation or automation may perform more than one role only when the work is small and no parallel workstream is active. When workers are active, integration must not race worker-owned files.

## Repo-Local Discovery

Each repository should expose the same agent entry points:

- `AGENTS.md` or equivalent root agent instructions.
- Planning/status files such as `TASKS.md`, `STATE.json`, `docs/orchestrator/STATUS.md`, `docs/orchestrator/PLAN.md`, or repo-specific equivalents.
- A validation-debt ledger at `docs/orchestrator/VALIDATION_DEBT.md`, `docs/intent-preservation/VALIDATION_DEBT.md`, or the nearest project-standard docs location.
- Execution plans with a parallel execution section when work can be split.

Agents must read repository-local instructions before relying on memory from prior conversations.

## Parallel Work Rules

Execution plans must define:

- objective;
- scope;
- owner role;
- allowed files;
- forbidden files;
- expected output;
- dependencies;
- blockers;
- validation evidence;
- handoff notes;
- shared files or contracts;
- integration owner;
- validation owner;
- merge order.

Do not assign parallel agents to edit the same file, public contract, schema, migration, generated index, deployment file, or status artifact unless the plan defines one integration owner and a conflict-resolution order.

## Validation Debt

Known repo-wide or out-of-scope validation failures must be recorded in a validation-debt ledger instead of being rediscovered in every session.

Validation debt does not excuse current-task failures. A failure is current-task blocking when it touches files changed by the task, names the active task/goal/module, violates the task acceptance criteria, or was introduced by the current work.

## Remote Repository Rules

For remote repositories:

- Work in the remote repository path specified by the project, such as `/home/ssf/Documents/Github/<repository>`.
- Do not mirror remote repository contents into local user directories.
- Deploy only under pre-existing, human-approved project or ecosystem policy.
  The policy must identify the permitted actor or automation, environment,
  service scope, queue/manual path and allowed circumstances. An agent cannot
  create or weaken the authorization it relies on during the current task.
- Keep command output sanitized. Do not print secrets, token values, raw production data, private customer evidence, or confidential identifiers.

## Agent Final Report

Every agent must report:

- role performed;
- files changed;
- documents created;
- validation commands and results;
- known validation debt used or created;
- active blockers with `[MISSING: ...]` or `[UNKNOWN: ...]`;
- deviations from scope;
- next concrete action.

Next step: Apply this standard through repository-local agent instructions and validation-debt ledgers.
