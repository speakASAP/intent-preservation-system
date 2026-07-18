# ADR-002: Use Graph Retrieval Before RAG

Status: Accepted

## Context

The project requires durable reasoning, traceability and safe AI-assisted execution. Decisions must remain visible over time.

## Decision

Use explicit graph traversal before semantic vector retrieval.

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
