# ADR-001: Use Markdown and Git as Source of Truth

Status: Accepted

## Context

The project requires durable reasoning, traceability and safe AI-assisted execution. Decisions must remain visible over time.

## Decision

Use a file-based Markdown repository under Git as the canonical source of truth.

## Alternatives considered

1. Ad hoc documentation.
2. SaaS-first documentation.
3. Chat-only memory.
4. Pure vector search.

## Consequences

Positive:

- improves auditability;
- supports repeatable context generation;
- reduces loss of intent.

Negative:

- requires discipline;
- requires templates and review process;
- may feel heavier during early prototyping.

## Validation

This decision is valid if it improves traceability and reduces context loss without blocking implementation speed excessively.
