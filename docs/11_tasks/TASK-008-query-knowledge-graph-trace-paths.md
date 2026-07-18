# TASK-008: Query knowledge graph trace paths

```yaml
id: TASK-008
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
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-008.md
execution_plan:
  - ../21_execution_plans/EP-TASK-008.md
validation_report:
  - ../12_validation/VAL-TASK-008-knowledge-graph-trace-paths.md
```

## Objective

Add a deterministic trace-path query to the repository graph extractor so a task
node can be traced to upstream Vision or Goal-like nodes.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Graph builder subsystem: `../05_subsystems/SUB-002-graph-builder.md`
- Context retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Roadmap Phase 4: `../08_roadmap/ROADMAP.md`
- Knowledge graph milestone: `../09_milestones/MS-004-knowledge-graph.md`
- Extractor foundation: `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`

## Goal Impact

This task satisfies the Phase 4 exit criterion that trace paths can be queried.
It turns extracted graph nodes and edges into an auditable trace from a task
back to upstream intent.

## Project Invariant Impact

- IPS-INV-001: trace paths must use extracted declared relationships, not
  semantic inference.
- IPS-INV-002: immutable vision and constitution documents may be read but must
  not be modified.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-008.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: tests use synthetic fixture documents only.

## Sensitive-Data Classification

Classification: none

The trace query operates on repository-local Markdown metadata and synthetic
test fixtures. No raw production data, confidential identifiers or secrets are
used.

## Contract/Schema Impact

This task extends the graph extractor CLI output with a trace-query result when
`--trace` is supplied. It does not change `../../graph/GRAPH_SCHEMA.md`.

## Replay/Determinism Impact

Trace paths must be deterministic for a fixed extracted graph. Traversal order,
returned paths and findings must be stable across repeated runs.

## Scope

- Add a reusable trace-path query function.
- Add CLI options for `--trace`, `--target-type` and `--max-depth`.
- Return deterministic trace paths and findings as JSON.
- Add fixture tests for successful trace paths and missing start nodes.

## Non-Goals

- Do not implement full graph analytics.
- Do not add orphan-task detection.
- Do not add dependency-map generation.
- Do not add vector search, embeddings or RAG.
- Do not modify protected baseline documents.

## Acceptance Criteria

- [x] A CLI command can query paths from a task id to Vision target nodes.
- [x] Trace output includes ordered node ids and traversed edges.
- [x] Missing start nodes return a structured finding.
- [x] Tests cover successful traces and missing start nodes.
- [x] Repository validation gates pass.

## Required Context

- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../graph/GRAPH_SCHEMA.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `../17_governance/PROJECT_INVARIANTS.md`

## Validation Task

Validate by running focused graph extractor tests, running a TASK-007 trace query
against the repository, and running repository validation gates.

## Required Gates

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --trace TASK-007 --target-type Vision --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-008
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-008.md`.
