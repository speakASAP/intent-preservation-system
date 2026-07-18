# GOAL-IMPACT-TASK-009: Orphan Task Detection

```yaml
id: GOAL-IMPACT-TASK-009
artifact_type: task
artifact_id: TASK-009
artifact_path: ../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md
primary_goal: Detect implementation tasks that cannot trace back to upstream intent.
secondary_goals:
  - Advance Phase 4 knowledge graph exit criteria.
  - Support deterministic governance checks before coding.
  - Reuse extracted graph and trace-query capabilities.
impact_level: high
impact_description: This task adds orphan-task detection on top of deterministic graph extraction and trace traversal.
success_metric: A local command returns a deterministic report of task nodes without upstream trace paths.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../05_subsystems/SUB-002-graph-builder.md
  - ../08_roadmap/ROADMAP.md
  - ../09_milestones/MS-004-knowledge-graph.md
  - ../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md
  - ../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md
downstream_links:
  - ../21_execution_plans/EP-TASK-009.md
  - ../12_validation/VAL-TASK-009-orphan-task-detection.md
validation_method: Run orphan detection tests and repository validation gates.
status: validated
```

## Explanation

TASK-009 uses the extracted graph and trace-query traversal to identify task
nodes that do not reach upstream intent. This supports IPS intent preservation
by making orphan implementation work visible before it enters later delivery
steps.

## Evidence

- Roadmap Phase 4 exit criteria: `../08_roadmap/ROADMAP.md`
- Graph builder subsystem: `../05_subsystems/SUB-002-graph-builder.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Extractor foundation: `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- Trace-query support: `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`

## Validation

The impact is valid when a repository-local command can return deterministic
orphan-task findings and validation gates pass.
