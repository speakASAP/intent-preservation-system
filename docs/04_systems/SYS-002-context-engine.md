# SYS-002 Context Engine

## Purpose

The Context Engine generates minimal, sufficient context packages for AI agents.

## Responsibilities

- Identify the target task.
- Resolve traceability chain.
- Retrieve related systems, subsystems, features and ADRs.
- Include validation criteria.
- Exclude irrelevant documents.
- Generate final coding prompts.

## Retrieval strategy

The engine should use a hybrid model:

1. Graph traversal for mandatory context.
2. Keyword search for exact terms.
3. Vector search for semantic support.
4. Human overrides for sensitive or ambiguous tasks.

## Why graph first

Semantic similarity does not guarantee relevance. A vector search may find text that sounds related but miss critical ADRs or upstream goals. The graph defines required context explicitly.

## Context package structure

```text
context-package.md
metadata.yaml
included-documents/
prompt.md
validation.md
```

## Validation

A context package is valid when:

- it references exactly one task;
- it includes upstream feature, subsystem and system context;
- it includes relevant ADRs;
- it includes acceptance criteria;
- it excludes unrelated documents;
- it fits within a target token budget.
