# SUB-003 Context Packager

Parent system: SYS-002 Context Engine

## Purpose

Create a bounded context package for one AI execution task.

## Responsibilities

- Select the target task and upstream traceability chain.
- Include only required context documents for the task.
- Preserve constraints, validation criteria and forbidden changes.
- Exclude unrelated project material from the package.

## Inputs

- task id;
- project graph;
- token budget;
- mandatory document rules;
- optional retrieval results.

## Outputs

A context package under `13_context_packages/`.

## Inclusion rules

Always include:

- task document;
- parent feature;
- parent subsystem summary;
- parent system summary;
- relevant ADRs;
- validation criteria;
- constraints and forbidden changes.

Conditionally include:

- related tasks;
- dependency documents;
- interface contracts;
- security requirements;
- deployment notes.

Exclude:

- unrelated features;
- obsolete ADRs;
- broad documents that exceed budget unless summarized.

## Validation

The context packager is valid when a generated package names one target task,
contains its upstream traceability, includes required documents and validation
instructions, and excludes unrelated context.
