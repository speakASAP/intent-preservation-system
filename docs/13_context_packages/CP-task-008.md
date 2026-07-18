# Context Package: TASK-008

## Target task

TASK-008: `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../05_subsystems/SUB-002-graph-builder.md -> ../09_milestones/MS-004-knowledge-graph.md -> TASK-008
```

## Included documents

- `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- `../21_execution_plans/EP-TASK-008.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-008.md`
- `../12_validation/VAL-TASK-008-knowledge-graph-trace-paths.md`
- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../graph/GRAPH_SCHEMA.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `../17_governance/PROJECT_INVARIANTS.md`

## Excluded documents

- Orphan-task detection and dependency-map implementation details are excluded.
- Vector search, embeddings and optional RAG documents are excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Use extracted graph edges only.
- Keep trace output deterministic.
- Preserve default extractor output when trace mode is not requested.
- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.

## Parallel execution context

- Execution plan: `../21_execution_plans/EP-TASK-008.md`
- Plan status: validated.
- Parallelization status: `EP-TASK-008.md` includes Parallel Execution Strategy, Goal Blockers And Dependencies, Parallel Dispatch List and Parallel Agent Handoff Prompts.
- Ready-now workstreams: `WS-008-A` implements deterministic trace-path query support.
- Dependency-gated workstreams: `WS-008-D` updates TASK-008 artifacts and graph links; `WS-008-V` validates after implementation and artifact handoffs.
- Integration owner and merge order: validation agent integrates after `WS-008-A`, then `WS-008-D`, then `WS-008-V`.

## Agent prompt

Implement TASK-008 by adding deterministic trace-path querying to the graph
extractor. Return structured paths and findings as JSON.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --trace TASK-007 --target-type Vision --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-008
```
