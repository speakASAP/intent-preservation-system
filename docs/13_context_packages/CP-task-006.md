# Context Package: TASK-006

## Target task

TASK-006: `../11_tasks/TASK-006-generate-context-package-by-task-id.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../05_subsystems/SUB-003-context-packager.md -> ../10_features/FEAT-002-context-package-generation.md -> TASK-006
```

## Included documents

- `../11_tasks/TASK-006-generate-context-package-by-task-id.md`
- `../01_vision/VISION.md`
- `../04_systems/SYS-002-context-engine.md`
- `../05_subsystems/SUB-003-context-packager.md`
- `../10_features/FEAT-002-context-package-generation.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-006.md`
- `../21_execution_plans/EP-TASK-006.md`
- `../12_validation/VAL-TASK-006-context-package-generator.md`
- `../13_context_packages/README.md`
- `../18_templates/CONTEXT_PACKAGE_TEMPLATE.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`
- `../17_governance/PROJECT_INVARIANTS.md`

## Excluded documents

- Unrelated tasks, execution plans and validation reports are excluded.
- Raw production data, secrets, confidential identifiers and real customer data are excluded.

## Constraints

- Preserve original task scope and upstream traceability.
- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.
- Use only synthetic or repository-local fixture data.
- Keep generated outputs deterministic and auditable.

## Parallel execution context

- Execution plan: `../21_execution_plans/EP-TASK-006.md`
- Plan status: validated.
- Parallelization status: `EP-TASK-006.md` includes Parallel Execution Strategy, Goal Blockers And Dependencies, Parallel Dispatch List and Parallel Agent Handoff Prompts.
- Ready-now workstreams: `WS-006-A` implements the deterministic context-package generator.
- Dependency-gated workstreams: `WS-006-D` generates artifacts and graph links; `WS-006-V` validates after implementation and artifact handoffs.
- Integration owner and merge order: validation agent integrates after `WS-006-A`, then `WS-006-D`, then `WS-006-V`.

## Agent prompt

Implement TASK-006 using the included documents. Preserve the declared scope, non-goals, acceptance criteria and required gates from the task and execution plan.

## Validation instructions

Acceptance criteria from the source task:

- The command generates a context package for a task id.
- The generated package includes target task, upstream traceability, included
  documents, excluded documents, constraints, agent prompt and validation instructions.
- The command refuses accidental overwrite unless `--force` is supplied.
- Fixture tests cover generation and overwrite safety.
- Repository validation passes.

Run the narrowest relevant tests, then run:

```bash
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-006
```
