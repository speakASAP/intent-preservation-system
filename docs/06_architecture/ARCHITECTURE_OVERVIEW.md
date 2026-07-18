# Architecture Overview

## Architectural style

The recommended architecture is modular and file-first.

```text
Markdown Repository
      ↓
Document Parser
      ↓
Knowledge Graph Builder
      ↓
Audit Engine
      ↓
Context Engine
      ↓
Prompt Generator
      ↓
AI Coding Agent
      ↓
Validation Engine
```

## Storage choices

### Required

- Git repository.
- Markdown files.
- YAML front matter.

### Optional

- SQLite for local indexes.
- Vector database for semantic retrieval.
- Graph database for large projects.
- Jira integration for task status.
- Confluence export for human browsing.

## Recommended MVP architecture

Start with:

- local Markdown repo;
- Python or TypeScript CLI;
- JSON graph file;
- simple audit script;
- generated context packages.

Avoid starting with a heavy SaaS stack.

## RAG role

RAG should be secondary. The first retrieval mechanism must be traceability graph traversal. RAG can supplement the package with semantically related documents.

## Atlassian role

Jira can mirror execution tasks. Confluence can publish human-readable docs. Neither should be the canonical source of truth in the first version.

## Security model

- Protected folders for immutable documents.
- Git branch protection.
- CODEOWNERS for review enforcement.
- Audit checks in CI.
- Explicit AI write restrictions.
