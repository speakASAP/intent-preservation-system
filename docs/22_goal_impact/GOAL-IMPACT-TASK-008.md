# GOAL-IMPACT-TASK-008: Knowledge Graph Trace Path Queries

```yaml
id: GOAL-IMPACT-TASK-008
artifact_type: task
artifact_id: TASK-008
artifact_path: ../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md
primary_goal: Query graph trace paths from implementation work back to upstream intent.
secondary_goals:
  - Advance Phase 4 knowledge graph exit criteria.
  - Support deterministic context retrieval from graph relationships.
  - Prepare for orphan-task detection.
impact_level: high
impact_description: This task adds the first query capability on top of extracted graph nodes and edges.
success_metric: A local command returns deterministic trace paths from a task id to Vision target nodes.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../05_subsystems/SUB-002-graph-builder.md
  - ../08_roadmap/ROADMAP.md
  - ../09_milestones/MS-004-knowledge-graph.md
downstream_links:
  - ../21_execution_plans/EP-TASK-008.md
  - ../12_validation/VAL-TASK-008-knowledge-graph-trace-paths.md
validation_method: Run trace query tests and repository validation gates.
status: validated
```

## Explanation

TASK-008 turns extracted graph data into a queryable trace path. This supports
IPS intent preservation by allowing task work to be checked against upstream
Vision or Goal-like nodes before later orphan detection and dependency mapping.

## Evidence

- Roadmap Phase 4 exit criteria: `../08_roadmap/ROADMAP.md`
- Graph builder subsystem: `../05_subsystems/SUB-002-graph-builder.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Extractor foundation: `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`

## Validation

The impact is valid when a repository-local command can return deterministic
trace paths from a task id to upstream Vision target nodes and validation gates
pass.
