# Goal Impact Mapping

## Purpose

Goal Impact Mapping ensures that every system, feature, task, execution plan, and coding prompt contributes to a known product or business goal.

It prevents orphan work: tasks that consume time but do not support the original project intent.

## Core principle

Every implementation artifact must answer:

> Why does this exist?

The answer must point upward to a goal, business case, vision element, milestone, or approved vision evolution entry.

## Traceability chain

Preferred chain:

```text
Vision / Business Goal
  -> System
  -> Subsystem
  -> Feature
  -> Task
  -> Execution Plan
  -> Coding Prompt
  -> Code Change
  -> Validation Report
```

## Impact levels

Use these levels:

```yaml
impact_level: critical | high | medium | low | none
```

Definitions:

- `critical`: Without this work, a core project goal cannot be achieved.
- `high`: Strongly supports a core goal.
- `medium`: Useful but not central.
- `low`: Nice-to-have or supporting work.
- `none`: No known goal impact; should be removed, deferred, or justified.

## Required fields for every goal impact record

```yaml
id: GOAL-IMPACT-xxx
artifact_type: system | subsystem | feature | task | execution-plan | prompt | code-change | validation-report
artifact_id: ID or path
primary_goal: Goal ID or document section
secondary_goals:
  - optional goal
impact_level: critical | high | medium | low | none
impact_description: Explanation of contribution
success_metric: How the impact will be observed
upstream_links:
  - path/to/upstream.md
downstream_links:
  - path/to/downstream.md
validation_method: How contribution will be validated
status: draft | reviewed | approved
```

## Orphan work rule

If `impact_level: none`, the artifact must not proceed to implementation unless one of the following is true:

- It is required technical maintenance.
- It is required security work.
- It is required documentation repair.
- It is explicitly approved by a human owner.

## Agent behavior

If an agent sees a task without goal impact mapping, it must not assume the impact. It must create a gap report or add a draft goal impact record if enough information is available.

## Audit questions

- Does every feature map to a system goal?
- Does every task map to a feature or milestone?
- Does every execution plan map to a task?
- Does every coding prompt map to an execution plan?
- Are there tasks with no business or product impact?
- Are critical goals missing downstream implementation artifacts?
