# Prompt Guidelines

## Prompt principles

Every coding prompt must be:

- small;
- bounded;
- traceable;
- testable;
- explicit about constraints;
- clear about forbidden changes;
- scoped to one parallel-safe workstream when the execution plan exposes independent workstreams.

## Prompt structure

```text
Role
Task
Context
Constraints
Allowed files
Forbidden changes
Acceptance criteria
Validation steps
Output format
```

When a plan contains parallel workstreams, generate one prompt per independent workstream plus a separate integration prompt when needed. Each workstream prompt must name blockers, dependencies, allowed files, forbidden files, validation steps and the expected handoff output for the integration agent. If thread-management tools are available, ready-now workstream prompts should be started in separate Codex threads.

## Anti-patterns

Avoid prompts like:

- Build the whole backend.
- Implement everything from the plan.
- Refactor the app.
- Make it production ready.

Prefer prompts like:

- Add parser support for YAML front matter in Markdown files.
- Implement validation for missing ADR trace links.
- Generate context package metadata for one task id.
