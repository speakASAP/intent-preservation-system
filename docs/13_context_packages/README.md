# Context Packages

This folder stores generated packages for AI agents.

A context package is not the whole project. It is a carefully selected task-specific bundle.

## Package naming

```text
CP-TASK-001-create-required-document-audit-rules.md
```

## Required sections

Every context package must include these top-level sections in this order:

1. `# Context Package: <TASK-ID>`
2. `## Target task`
3. `## Upstream traceability`
4. `## Included documents`
5. `## Excluded documents`
6. `## Constraints`
7. `## Agent prompt`
8. `## Validation instructions`

The title is the package metadata. It must identify the target task and should
match the task identifier used in the package filename.

`## Included documents` must list the bounded source documents, contracts,
validation reports or implementation files the agent is expected to use.
`## Excluded documents` must state relevant exclusions so the package remains
task-specific and does not invite scope creep.

## Optional sections

Context packages may include additional task-specific sections when the source
execution plan or task contract requires them. Common optional sections include:

- `## Parallel execution context`
- `## Parallel dispatch status`
- `## Parallel dispatch and blockers`

Optional sections must not replace or rename the required sections.

## Compatibility notes

Existing `CP-*.md` files that use `# Context Package: <TASK-ID>` as the title
already satisfy the package metadata requirement. Existing packages may retain
their optional parallel-planning section names as long as all required sections
above remain present and non-empty.
