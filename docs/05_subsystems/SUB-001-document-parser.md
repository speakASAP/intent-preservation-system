# SUB-001 Document Parser

Parent system: SYS-001 Knowledge Repository

## Purpose

Parse Markdown files and extract structured metadata for indexing, graph generation and audits.

## Responsibilities

- Read Markdown front matter.
- Extract headings.
- Extract trace links.
- Extract validation criteria.
- Extract dependencies.
- Detect missing required sections.

## Inputs

- Markdown documents.
- YAML front matter.
- folder conventions.

## Outputs

- normalized document metadata;
- graph nodes and edges;
- audit findings.

## Validation

The parser is valid when it can extract metadata from all template-based documents without manual intervention.
