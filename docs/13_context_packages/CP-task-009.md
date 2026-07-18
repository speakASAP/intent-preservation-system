# Context Package: TASK-009

## Target task

TASK-009: `../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../05_subsystems/SUB-002-graph-builder.md -> ../09_milestones/MS-004-knowledge-graph.md -> TASK-009
```

## Included documents

- `../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`
- `../21_execution_plans/EP-TASK-009.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-009.md`
- `../12_validation/VAL-TASK-009-orphan-task-detection.md`
- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../graph/GRAPH_SCHEMA.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- `../17_governance/PROJECT_INVARIANTS.md`

## Excluded documents

- Dependency-map implementation details are excluded.
- Vector search, embeddings and optional RAG documents are excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Use extracted graph edges only.
- Reuse trace-query support for upstream path checks.
- Keep orphan detection output deterministic.
- Preserve default extractor output when orphan mode is not requested.
- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.

## Parallel dispatch status

- Source execution plan: `../21_execution_plans/EP-TASK-009.md`
- Parallelization strategy: `single_agent`.
- Dispatch readiness: the execution plan now defines WS-009-A as the single
  ready implementation workstream and WS-009-B as final integration and
  validation review.
- Derived prompt treatment: use the coding prompt as the WS-009-A
  implementation prompt; WS-009-B starts only after implementation and
  validation evidence are available.
- Blockers: no source task blocker is named for WS-009-A. Additional
  simultaneous implementation workstreams are blocked by shared edits to
  `../../scripts/graph_extractor.py` and `../../tests/test_graph_extractor.py` unless
  a future plan defines an independent file or contract boundary.
- Integration owner: `knowledge-graph-agent`.

## Agent prompt

Implement TASK-009 by adding deterministic orphan-task detection to the graph
extractor. Return structured task and finding data as JSON.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --orphan-tasks --target-type Vision --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-009
```
