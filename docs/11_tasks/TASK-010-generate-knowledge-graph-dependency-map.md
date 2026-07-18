# TASK-010: Generate knowledge graph dependency map

```yaml
id: TASK-010
status: validated
owner: knowledge-graph-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../05_subsystems/SUB-002-graph-builder.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../08_roadmap/ROADMAP.md
  - ../09_milestones/MS-004-knowledge-graph.md
  - ../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md
  - ../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md
  - ../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-010.md
execution_plan:
  - ../21_execution_plans/EP-TASK-010.md
validation_report:
  - ../12_validation/VAL-TASK-010-dependency-map-generation.md
```

## Objective

Add deterministic dependency-map generation to the graph extractor so a caller
can inspect upstream and downstream graph relationships around a selected node.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Graph builder subsystem: `../05_subsystems/SUB-002-graph-builder.md`
- Context retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Roadmap Phase 4: `../08_roadmap/ROADMAP.md`
- Knowledge graph milestone: `../09_milestones/MS-004-knowledge-graph.md`
- Extractor foundation: `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- Trace-query support: `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- Orphan-task detection: `../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`

## Goal Impact

This task satisfies the Phase 4 exit criterion that a dependency map is
generated. It turns extracted graph relationships into a bounded, deterministic
map that can support context retrieval and implementation review.

## Project Invariant Impact

- IPS-INV-001: dependency maps must use extracted declared relationships.
- IPS-INV-002: immutable vision and constitution documents may be read but must
  not be modified.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-010.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: tests use synthetic fixture documents only.

## Sensitive-Data Classification

Classification: none

The dependency map operates on repository-local Markdown metadata and synthetic
test fixtures. No raw production data, confidential identifiers or secrets are
used.

## Contract/Schema Impact

This task extends the graph extractor CLI with an explicit dependency-map report
when `--dependency-map NODE_ID` is supplied. It does not change default
extraction output or `../../graph/GRAPH_SCHEMA.md`.

## Replay/Determinism Impact

Dependency-map output must be deterministic for a fixed extracted graph. Node
ordering, edge ordering and missing-start findings must be stable across
repeated runs.

## Scope

- Add a reusable dependency-map function.
- Add a CLI option for `--dependency-map NODE_ID`.
- Reuse `--max-depth` for bounded traversal.
- Return deterministic upstream and downstream nodes and edges as JSON.
- Add fixture tests for successful maps and missing start nodes.

## Non-Goals

- Do not add vector search, embeddings or RAG.
- Do not infer semantic dependencies from prose.
- Do not change the graph schema.
- Do not modify protected baseline documents.

## Acceptance Criteria

- [x] A CLI command can generate a dependency map for a task id.
- [x] The map includes upstream and downstream relationships from extracted
  edges.
- [x] Missing start nodes return a structured finding.
- [x] Tests cover successful maps and missing start nodes.
- [x] Repository validation gates pass.

## Required Context

- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../graph/GRAPH_SCHEMA.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- `../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`
- `../17_governance/PROJECT_INVARIANTS.md`

## Validation Task

Validate by running focused graph extractor tests, running a dependency-map
query against the repository, and running repository validation gates.

## Required Gates

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --dependency-map TASK-010 --max-depth 2 --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-010
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-010.md`.
