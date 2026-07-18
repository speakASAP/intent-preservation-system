# Coding Prompt: TASK-009 Orphan Task Detection

```yaml
id: PROMPT-TASK-009-orphan-task-detection
source_task: ../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md
execution_plan: ../21_execution_plans/EP-TASK-009.md
context_package: ../13_context_packages/CP-task-009.md
status: used
```

## Role

You are an implementation agent working on Phase 4 knowledge-graph orphan-task
detection for Intent Preservation System.

## Task

Implement TASK-009: detect task nodes that cannot trace to upstream target node
types through extracted graph edges.

## Context

Use the context package at `../13_context_packages/CP-task-009.md`, especially:

- `../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`
- `../21_execution_plans/EP-TASK-009.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-009.md`
- `../13_context_packages/CP-task-009.md`
- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../graph/GRAPH_SCHEMA.md`

## Constraints

- Use extracted graph nodes and edges only.
- Reuse trace-query traversal for upstream checks.
- Keep default extraction output unchanged.
- Keep output deterministic.
- Do not implement dependency maps, vector search, embeddings or RAG.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- TASK-009 documentation and graph-example entries.

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Pre-existing TASK-004 worktree changes.
- Any prompt, fixture or report containing secrets or raw production data.

## Implementation Request

1. Add deterministic orphan-task detection over extracted graph data.
2. Classify a task as orphaned when no trace path reaches the configured target
   node types within max depth.
3. Add `--orphan-tasks` CLI support.
4. Add focused tests for orphan and non-orphan tasks.

## Parallel Workstream Context

- Prompt type: WS-009-A single-agent implementation prompt from the refactored
  execution plan.
- Parallelization strategy: `single_agent`; no additional simultaneous
  implementation workstream is source-backed because the detector and tests
  share `../../scripts/graph_extractor.py` and `../../tests/test_graph_extractor.py`.
- Dependencies: none for WS-009-A. WS-009-B final integration and validation
  review starts only after implementation and validation evidence are complete.
- Owned files: use `Allowed Changes` above. Shared implementation/test files
  are owned by WS-009-A before WS-009-B validation review.
- Expected handoff: return validation evidence, blockers encountered or
  cleared, dependencies on WS-009-B, integration notes and deviations.

## Acceptance criteria

- A CLI command can report orphan tasks from the extracted graph.
- Tasks with a trace path to Vision are not reported as orphaned.
- Tasks without a trace path to configured target types are reported with
  structured findings.
- Tests cover orphan and non-orphan task detection.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --orphan-tasks --target-type Vision --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-009
```

## Expected Output

The implementation agent must return:

- Files changed.
- Documents created.
- Missing sections filled.
- Remaining missing-information markers.
- Validation evidence.
- Blockers encountered or cleared.
- Dependencies on other agent workstreams.
- Integration or merge notes.
- Deviations from plan.
