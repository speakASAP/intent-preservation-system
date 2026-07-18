# TASK-009: Detect orphan tasks from knowledge graph

```yaml
id: TASK-009
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
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-009.md
execution_plan:
  - ../21_execution_plans/EP-TASK-009.md
validation_report:
  - ../12_validation/VAL-TASK-009-orphan-task-detection.md
```

## Objective

Add deterministic orphan-task detection to the graph extractor by identifying
task nodes that cannot trace to upstream intent through extracted graph edges.

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

## Goal Impact

This task satisfies the Phase 4 exit criterion that orphan tasks are detected.
It builds on graph extraction and trace-query support so work can be checked
against upstream intent without semantic inference.

## Project Invariant Impact

- IPS-INV-001: orphan detection must use extracted declared relationships.
- IPS-INV-002: immutable vision and constitution documents may be read but must
  not be modified.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-009.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: tests use synthetic fixture documents only.

## Sensitive-Data Classification

Classification: none

The orphan detector operates on repository-local Markdown metadata and
synthetic test fixtures. No raw production data, confidential identifiers or
secrets are used.

## Contract/Schema Impact

This task extends the graph extractor CLI with an explicit orphan-task report
when `--orphan-tasks` is supplied. It does not change default extraction output
or `../../graph/GRAPH_SCHEMA.md`.

## Replay/Determinism Impact

The orphan-task report must be deterministic for a fixed extracted graph. Task
ordering, trace traversal and findings must be stable across repeated runs.

## Scope

- Add a reusable orphan-task detection function.
- Add a CLI option for `--orphan-tasks`.
- Reuse trace-query target type and max-depth options.
- Return deterministic orphan-task findings as JSON.
- Add fixture tests for orphan and non-orphan tasks.

## Non-Goals

- Do not add dependency-map generation.
- Do not add vector search, embeddings or RAG.
- Do not change the graph schema.
- Do not modify protected baseline documents.

## Acceptance Criteria

- [x] A CLI command can report orphan tasks from the extracted graph.
- [x] Tasks with a trace path to Vision are not reported as orphaned.
- [x] Tasks without a trace path to configured target types are reported with
  structured findings.
- [x] Tests cover orphan and non-orphan task detection.
- [x] Repository validation gates pass.

## Required Context

- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../graph/GRAPH_SCHEMA.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- `../17_governance/PROJECT_INVARIANTS.md`

## Validation Task

Validate by running focused graph extractor tests, running an orphan-task query
against the repository, and running repository validation gates.

## Required Gates

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --orphan-tasks --target-type Vision --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-009
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-009.md`.
