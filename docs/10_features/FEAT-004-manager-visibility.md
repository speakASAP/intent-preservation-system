# FEAT-004 Manager Visibility Interface

Parent system: SYS-002 Context Engine

## Goal

Provide a basic manager-facing web interface that makes IPS traceability,
retrieval comparison and validation status visible without requiring managers
to read the repository structure.

## User story

As a manager reviewing an AI-assisted delivery effort, I want to see how the
original intent connects to tasks, prompts, comparisons and gates so I can
understand progress and risk at a glance.

## Acceptance criteria

- The interface shows the IPS chain from vision through validation.
- The interface explains retrieval comparison in business-readable terms.
- The interface separates manager readout from implementation details.
- The interface is static and local, with no external services or sensitive
  data.
- The interface can be opened through a simple local web server.
- Visual verification confirms the page is readable on desktop and mobile.

## Dependencies

- `../01_vision/VISION.md`
- `../04_systems/SYS-002-context-engine.md`
- `../07_decisions/ADR-001-use-markdown-and-git-as-source-of-truth.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../10_features/FEAT-002-context-package-generation.md`
- `../10_features/FEAT-003-optional-rag-retrieval.md`
- `../12_validation/VALIDATION_PYRAMID.md`

## Traceability

Vision goal: preserve project intent by making the trace from original goals to
validated work easier to inspect and explain.

## Validation

Validate with repository governance gates, local static serving and visual
inspection of desktop and mobile viewports.
