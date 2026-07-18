# GOAL-IMPACT-TASK-016: Manager Visibility Interface

```yaml
id: GOAL-IMPACT-TASK-016
artifact_type: task
artifact_id: TASK-016
artifact_path: ../11_tasks/TASK-016-create-manager-visibility-interface.md
primary_goal: Make IPS traceability and validation understandable for managers.
secondary_goals:
  - Show the Vision to Validation chain in one view.
  - Explain retrieval comparison without implementation jargon.
  - Keep the interface local, static and free of sensitive data.
impact_level: medium
impact_description: This task adds a basic manager-facing dashboard for IPS status, comparison and validation evidence.
success_metric: A manager can open the local page and understand traceability, comparison results and validation status without reading source folders first.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../07_decisions/ADR-001-use-markdown-and-git-as-source-of-truth.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../10_features/FEAT-004-manager-visibility.md
downstream_links:
  - ../21_execution_plans/EP-TASK-016.md
  - ../12_validation/VAL-TASK-016-manager-visibility-interface.md
validation_method: Run local browser verification, repository validation, pre-coding gate and deployment-readiness gate.
status: validated
```

## Explanation

TASK-016 makes IPS easier to inspect by presenting the main governance chain,
retrieval comparison and validation evidence in a simple web page. It helps
managers see whether work is traceable, whether retrieval candidates improve
context and whether required gates have passed.

## Evidence

- Manager visibility feature: `../10_features/FEAT-004-manager-visibility.md`
- Validation report: `../12_validation/VAL-TASK-016-manager-visibility-interface.md`
- Static interface: `../../manager_interface/index.html`

## Validation

The impact is validated because the interface renders locally, remains static
and passes repository governance gates.
