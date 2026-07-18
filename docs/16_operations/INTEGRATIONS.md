# Integrations

## Jira

Recommended role: execution tracking mirror.

Do not use Jira as the primary knowledge store. Generate Jira epics and tasks from repository files.

## Confluence

Recommended role: human-readable publishing layer.

Do not use Confluence as the canonical source of truth in the MVP. Publish Markdown snapshots if needed.

## RAG

Recommended role: secondary retrieval.

Use RAG to discover optional supporting context, not to decide mandatory task context.

## GitHub Actions

Recommended role: documentation quality gate.

Possible checks:

- protected files modified;
- missing traceability;
- missing validation;
- missing ADR references.

## AI coding CLI

Recommended role: executor.

The CLI should receive generated prompts and context packages, not the whole repository.
