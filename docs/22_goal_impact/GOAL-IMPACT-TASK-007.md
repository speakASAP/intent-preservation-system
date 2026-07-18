# GOAL-IMPACT-TASK-007: Knowledge Graph Extraction from Repository Documents

```yaml
id: GOAL-IMPACT-TASK-007
artifact_type: task
artifact_id: TASK-007
artifact_path: ../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md
primary_goal: Build a graph representation of project knowledge for graph-first context retrieval.
secondary_goals:
  - Enable trace-path queries in later Phase 4 tasks.
  - Enable orphan-task and dependency-map validation in later Phase 4 tasks.
  - Reduce reliance on hand-maintained graph examples.
impact_level: high
impact_description: This task starts Phase 4 by extracting graph nodes and edges from declared repository document metadata.
success_metric: A local command emits deterministic nodes, edges and findings from repository Markdown fixtures.
upstream_links:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../05_subsystems/SUB-002-graph-builder.md
  - ../08_roadmap/ROADMAP.md
  - ../09_milestones/MS-004-knowledge-graph.md
downstream_links:
  - ../21_execution_plans/EP-TASK-007.md
validation_method: Run graph extractor fixture tests and repository validation gates after implementation.
status: draft
```

## Explanation

TASK-007 supports the graph-first retrieval decision by making repository
traceability executable. It creates the extraction foundation required before
later Phase 4 work can query graph paths, detect orphan tasks or generate a
dependency map.

## Evidence

- Roadmap Phase 4 exit criteria: `../08_roadmap/ROADMAP.md`
- Graph builder subsystem: `../05_subsystems/SUB-002-graph-builder.md`
- Graph schema: `../../graph/GRAPH_SCHEMA.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`

## Validation

The impact is valid when TASK-007 produces deterministic graph extraction
output from repository documents and records validation evidence without
weakening traceability, data-handling or immutable-document invariants.
