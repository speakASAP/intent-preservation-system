# FEAT-002 Context Package Generation

Parent system: SYS-002 Context Engine

## Goal

Generate minimal context packages for individual AI-agent tasks.

## User story

As a developer, I want each AI agent to receive only the context needed for its task so that quality improves and token waste decreases.

## Acceptance criteria

- A package can be generated from a task id.
- The package includes upstream system context.
- The package includes relevant ADRs.
- The package includes validation criteria.
- The package excludes unrelated documents.
- The package contains a final prompt.

## Traceability

Vision goal: AI agents receive minimal but sufficient context, with graph-based
retrieval used before semantic fallback.

## Validation

Generate a package for a sample task and verify that all required context is present.
