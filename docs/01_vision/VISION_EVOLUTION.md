# Vision Evolution Log

## Purpose

`VISION.md` is immutable and describes the original intent of the project. Real projects still evolve. This document records approved evolution of that intent without rewriting the original vision.

This file exists to answer:

- What changed in the understanding of the product?
- Why did the change happen?
- Who approved the change?
- Which documents and implementation areas are affected?
- Does the change extend the original vision or contradict it?

## Governance Rules

1. `VISION.md` must not be modified by AI agents.
2. Any change to the project intent must be recorded here.
3. Every entry must include a reason, scope, impact, and approval status.
4. If an evolution contradicts `VISION.md`, it must be explicitly marked as a strategic pivot.
5. Downstream documents must link to the relevant evolution entry.

## Entry Template

```yaml
id: VE-YYYY-NNN
date: YYYY-MM-DD
status: proposed | approved | rejected | superseded
type: clarification | extension | constraint | pivot | deprecation
summary: Short description of the evolution
reason: Why this change is needed
original_vision_reference:
  - ../01_vision/VISION.md#section-name
affected_documents:
  - path/to/document.md
affected_systems:
  - SYS-xxx
affected_features:
  - FEAT-xxx
impact_on_business_goal: none | low | medium | high
compatibility_with_original_vision: compatible | partially-compatible | incompatible
approval:
  owner: Human owner name
  date: YYYY-MM-DD
  decision: pending | approved | rejected
```

## Evolution Entries

### VE-2026-001: Add explicit support for semantic compression

```yaml
id: VE-2026-001
date: 2026-06-05
status: approved
type: extension
summary: Add multi-level summaries for important documents so agents can consume the right amount of context.
reason: Large documentation repositories create context-window pressure. Agents need full, summary, and ultra-summary variants depending on task scope.
original_vision_reference:
  - ../01_vision/VISION.md
affected_documents:
  - ../20_semantic_compression/SEMANTIC_COMPRESSION_GUIDE.md
  - ../18_templates/SEMANTIC_COMPRESSION_TEMPLATE.md
affected_systems:
  - SYS-002
impact_on_business_goal: high
compatibility_with_original_vision: compatible
approval:
  owner: Human project owner
  date: 2026-06-05
  decision: approved
```

### VE-2026-002: Add execution plans between tasks and code

```yaml
id: VE-2026-002
date: 2026-06-05
status: approved
type: extension
summary: Add an execution-plan layer that transforms tasks into concrete implementation instructions before coding.
reason: Coding agents need a bounded, concrete, single-session plan with file-level actions, tests, validation, and rollback.
affected_documents:
  - ../21_execution_plans/EXECUTION_PLAN_GUIDE.md
  - ../18_templates/EXECUTION_PLAN_TEMPLATE.md
affected_systems:
  - SYS-002
impact_on_business_goal: high
compatibility_with_original_vision: compatible
approval:
  owner: Human project owner
  date: 2026-06-05
  decision: approved
```

### VE-2026-003: Add goal impact mapping

```yaml
id: VE-2026-003
date: 2026-06-05
status: approved
type: extension
summary: Add explicit mapping from goals to systems, features, tasks, execution plans, prompts, and validation.
reason: The system must detect orphan work and ensure every implementation task contributes to a known business or product goal.
affected_documents:
  - ../22_goal_impact/GOAL_IMPACT_MAPPING.md
  - ../18_templates/GOAL_IMPACT_TEMPLATE.md
impact_on_business_goal: high
compatibility_with_original_vision: compatible
approval:
  owner: Human project owner
  date: 2026-06-05
  decision: approved
```
