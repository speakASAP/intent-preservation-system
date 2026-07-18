# GOAL-IMPACT-TASK-006: Context Package Generation by Task Id

```yaml
id: GOAL-IMPACT-TASK-006
artifact_type: task
artifact_id: TASK-006
artifact_path: ../11_tasks/TASK-006-generate-context-package-by-task-id.md
primary_goal: Generate bounded AI-agent context packages deterministically from task metadata.
secondary_goals:
  - Reduce manual context assembly.
  - Preserve traceability from package output back to task, feature and system intent.
impact_level: high
impact_description: This task turns the context-package schema into a runnable local generation workflow.
success_metric: A local command can generate an audit-valid context package for a task id without inferred or unrelated context.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
downstream_links:
  - ../21_execution_plans/EP-TASK-006.md
  - ../12_validation/VAL-TASK-006-context-package-generator.md
validation_method: Run fixture tests, generate a TASK-006 context package, and run repository validation gates.
status: validated
```

## Explanation

TASK-006 supports the vision requirement that AI agents receive minimal but
sufficient context. It avoids ad hoc prompt assembly by generating packages
from explicit task metadata and required-context declarations.

## Evidence

- Vision outcome: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Context packager subsystem: `../05_subsystems/SUB-003-context-packager.md`
- Context package schema validation: `../12_validation/VAL-TASK-003-context-package-schema.md`

## Validation

The impact is valid when a repository-local command generates an audit-valid
context package for a task id and validation gates pass.
