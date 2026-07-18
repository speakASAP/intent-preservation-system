# Semantic Compression Guide

## Purpose

Semantic compression allows the project to keep rich documentation while giving AI agents only the amount of context they need.

Each important document may have three representations:

1. **Full document** - canonical source with all details.
2. **Summary document** - compressed but still operationally useful.
3. **Ultra-summary** - minimal intent, constraints, and links.

This is not lossy random summarization. It is structured compression that preserves decisions, constraints, traceability, and validation requirements.

Compression must never introduce intent from neighboring documents. If a summary needs architecture, ADR or roadmap context, create a separate compressed artifact for that source document instead of mixing it into the compressed vision.

## When to create compressed documents

Create compressed variants for:

- Vision documents
- Business case documents
- Architecture documents
- System and subsystem documents
- ADRs
- Roadmap documents
- Long milestone definitions
- Large validation reports
- Complex execution plans

Do not create compressed variants for very small templates unless they are repeatedly used in context packages.

## Naming convention

For a source document:

```text
06_architecture/ARCHITECTURE_OVERVIEW.md
```

Create:

```text
20_semantic_compression/summaries/ARCHITECTURE_OVERVIEW.summary.md
20_semantic_compression/ultra/ARCHITECTURE_OVERVIEW.ultra.md
```

## Compression levels

### Level 0: Full

The original document. It is the source of truth.

### Level 1: Summary

Should preserve:

- Purpose
- Scope
- Key decisions
- Constraints
- Dependencies
- Traceability links
- Validation criteria
- Open questions

Recommended content length: 10-25% of the original document, excluding required metadata.

### Level 2: Ultra-summary

Should preserve:

- One-paragraph intent
- Mandatory constraints
- Critical links
- When the full document must be read

Recommended content length: 3-8% of the original document, excluding required metadata.

## Agent usage rules

An agent should receive:

- Ultra-summary for background documents.
- Summary for directly related documents.
- Full document only for the primary task artifact or when validation requires exact wording.

## Source fidelity rules

Before editing a compressed document, an agent must read the full source document named in `source_document`.

The compressed document must:

- Preserve the source document's intent, constraints, non-goals and success criteria.
- Avoid adding decisions that are only present in architecture, ADR, roadmap or implementation documents.
- Stay meaningfully shorter than the source according to the compression level.
- Keep `fidelity_status: draft` or `fidelity_status: reviewed` unless a human explicitly approves it.

If the audit requires verbosity that conflicts with the compression limits, the audit rule is wrong and must be corrected before expanding the compressed document.

## Required metadata

Every compressed document must include:

```yaml
source_document: path/to/source.md
compression_level: summary | ultra
last_updated: YYYY-MM-DD
compression_owner: human | ai-draft | approved-ai
fidelity_status: draft | reviewed | approved
must_read_full_document_when:
  - condition one
  - condition two
```

## Completeness requirements

A compressed document is incomplete if it lacks:

- Source document path
- Compression level
- Summary of purpose
- Preserved constraints
- Traceability links
- Conditions for reading the full document

## Validation checklist

- Does the summary preserve the original intent?
- Are all non-negotiable constraints retained?
- Are links to upstream and downstream artifacts retained?
- Could an agent misunderstand the system if it reads only this summary?
- Does the ultra-summary clearly say when the full document is required?
- Is every major claim traceable to the source document named in `source_document`?
- Does the content length stay within the recommended range for its compression level?
