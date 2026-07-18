# Context Package: TASK-001

## Target task

TASK-001: `../11_tasks/TASK-001-create-required-document-audit-rules.md`

## Upstream traceability

```text
VISION -> SYS-003 Audit Engine -> FEAT-001 Documentation Audit -> TASK-001
```

## Included documents

- `01_vision/VISION.md`
- `04_systems/SYS-003-audit-engine.md`
- `10_features/FEAT-001-documentation-audit.md`
- `11_tasks/TASK-001-create-required-document-audit-rules.md`
- `12_validation/VALIDATION_REPORT_TEMPLATE.md`

## Excluded documents

- Semantic compression outputs are excluded because this package uses the full source documents.
- Unrelated feature, task, and prompt documents are excluded.

## Constraints

- Do not modify vision.
- Do not implement unrelated audit categories.
- Output must support future automation.

## Parallel execution context

- Execution plan: `../21_execution_plans/EP-TASK-001-example.md`
- Plan status: reviewed.
- Parallelization status: `EP-TASK-001-example.md` includes Parallel Execution Strategy, Goal Blockers And Dependencies, Parallel Dispatch List and Parallel Agent Handoff Prompts.
- Ready-now workstreams: `WS-001-A` implements required-section audit rules; `WS-001-D` may start after final audit rule names are available.
- Dependency-gated workstreams: `WS-001-V` runs after implementation and documentation handoffs are complete.
- Integration owner and merge order: validation agent integrates after `WS-001-A`, then `WS-001-D`, then `WS-001-V`.

## Agent prompt

You are implementing TASK-001. Use only the included context. Create required-document audit rules that check for the presence of baseline project documentation. Preserve traceability and produce validation instructions.

## Validation instructions

Verify that the rules detect missing constitution, vision, business case, systems, subsystems, ADRs, roadmap, milestones, features, tasks and validation documents.
