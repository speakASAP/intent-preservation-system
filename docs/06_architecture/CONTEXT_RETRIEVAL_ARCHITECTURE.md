# Context Retrieval Architecture

## Problem

AI agents need relevant context, but large projects contain too much documentation to fit into a single prompt.

## Solution

Use context retrieval based on explicit traceability plus semantic enrichment.

## Retrieval pipeline

```text
Task ID
  -> Load task metadata
  -> Follow graph to feature
  -> Follow graph to subsystem
  -> Follow graph to system
  -> Include relevant ADRs
  -> Include validation rules
  -> Add dependency docs
  -> Optionally run vector search
  -> Summarize oversized docs
  -> Generate context package
```

## Mandatory context

Mandatory context is determined by graph links, not by semantic similarity.

## Optional context

Optional context may be retrieved through:

- embedding search;
- keyword search;
- file path conventions;
- human-specified includes.

## Token budget strategy

1. Include full task and acceptance criteria.
2. Include full relevant ADRs if short.
3. Include summaries of high-level documents.
4. Include exact interface contracts.
5. Exclude broad unrelated docs.

## Failure mode prevention

| Failure | Prevention |
|---|---|
| Missing ADR | Required graph edge check |
| Too much context | Token budget enforcement |
| Wrong semantic match | Graph-first retrieval |
| Stale document | Audit timestamp and review status |
| Scope creep | Vision and non-goal inclusion |
