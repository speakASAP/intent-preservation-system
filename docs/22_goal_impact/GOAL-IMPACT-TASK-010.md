# GOAL-IMPACT-TASK-010: Knowledge Graph Dependency Map

```yaml
id: GOAL-IMPACT-TASK-010
artifact_type: task
artifact_id: TASK-010
artifact_path: ../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md
primary_goal: Generate deterministic dependency maps from extracted graph relationships.
secondary_goals:
  - Complete Phase 4 knowledge graph exit criteria.
  - Support graph-first context retrieval.
  - Make upstream and downstream implementation relationships reviewable.
impact_level: high
impact_description: This task adds bounded dependency-map generation on top of deterministic graph extraction.
success_metric: A local command returns deterministic upstream and downstream graph relationships for a selected node.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../05_subsystems/SUB-002-graph-builder.md
  - ../08_roadmap/ROADMAP.md
  - ../09_milestones/MS-004-knowledge-graph.md
  - ../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md
  - ../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md
  - ../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md
downstream_links:
  - ../21_execution_plans/EP-TASK-010.md
  - ../12_validation/VAL-TASK-010-dependency-map-generation.md
validation_method: Run dependency-map tests and repository validation gates.
status: validated
```

## Explanation

TASK-010 generates a bounded dependency map from extracted graph relationships.
This completes the Phase 4 knowledge graph exit criteria and supports IPS
context retrieval by making upstream and downstream relationships inspectable
without semantic inference.

## Evidence

- Roadmap Phase 4 exit criteria: `../08_roadmap/ROADMAP.md`
- Graph builder subsystem: `../05_subsystems/SUB-002-graph-builder.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Extractor foundation: `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- Trace-query support: `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- Orphan-task detection: `../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`

## Validation

The impact is valid when a repository-local command can return deterministic
dependency-map output and validation gates pass.
