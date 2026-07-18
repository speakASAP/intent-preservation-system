# TASK-006: Generate context package by task id

```yaml
id: TASK-006
status: validated
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../05_subsystems/SUB-003-context-packager.md
  - ../10_features/FEAT-002-context-package-generation.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-006.md
execution_plan:
  - ../21_execution_plans/EP-TASK-006.md
validation_report:
  - ../12_validation/VAL-TASK-006-context-package-generator.md
```

## Objective

Implement a deterministic local command that generates a Markdown context
package for one task id from declared task metadata and required-context links.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context system: `../04_systems/SYS-002-context-engine.md`
- Context packager subsystem: `../05_subsystems/SUB-003-context-packager.md`
- Parent feature: `../10_features/FEAT-002-context-package-generation.md`
- Context package schema task: `../11_tasks/TASK-003-create-context-package-schema.md`

## Goal Impact

This task advances Phase 3 by moving from a documented context-package schema
to a repeatable local generator that can create a package for a target task.

## Project Invariant Impact

- IPS-INV-001: generated packages must preserve traceability to upstream task metadata.
- IPS-INV-002: immutable vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows this execution plan and validation evidence.
- IPS-INV-005: generated packages must exclude secrets, raw production data and confidential identifiers.

## Sensitive-Data Classification

Classification: none

The generator uses repository-local Markdown metadata only. Tests use synthetic
task ids and fixture text.

## Contract/Schema Impact

This task materializes the existing context-package Markdown schema. It does
not change the schema required by TASK-003.

## Replay/Determinism Impact

The generator must be deterministic for a fixed task document and repository
state. Re-running with `--force` should produce the same package text.

## Scope

- Add a dependency-free CLI that accepts `--task TASK-XXX`.
- Resolve a single task document from `11_tasks/`.
- Include the task, upstream documents, goal-impact record, execution plan,
  validation report and required-context links.
- Render the required context package sections as Markdown.
- Refuse to overwrite an existing package unless explicitly forced.

## Non-Goals

- Do not implement vector retrieval.
- Do not infer undeclared dependencies.
- Do not call an AI model.
- Do not modify immutable vision or constitution documents.

## Acceptance Criteria

- The command generates a context package for a task id.
- The generated package includes target task, upstream traceability, included
  documents, excluded documents, constraints, agent prompt and validation instructions.
- The command refuses accidental overwrite unless `--force` is supplied.
- Fixture tests cover generation and overwrite safety.
- Repository validation passes.

## Required Context

- `../13_context_packages/README.md`
- `../18_templates/CONTEXT_PACKAGE_TEMPLATE.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../04_systems/SYS-002-context-engine.md`
- `../05_subsystems/SUB-003-context-packager.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`
- `../17_governance/PROJECT_INVARIANTS.md`

## Validation Task

Run generator fixture tests, generate `../13_context_packages/CP-task-006.md`
from this task, and run the strict audit, pre-coding gate and deployment-readiness gate.

## Required Gates

```bash
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-006
```

## Execution Plan Requirement

This task requires an execution plan because it creates generated artifacts
used by downstream AI agents.
