# Coding Prompt: TASK-008 Knowledge Graph Trace Paths

```yaml
id: PROMPT-TASK-008-knowledge-graph-trace-paths
source_task: ../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md
execution_plan: ../21_execution_plans/EP-TASK-008.md
context_package: ../13_context_packages/CP-task-008.md
status: used
```

## Role

You are an implementation agent working on Phase 4 knowledge-graph query
support in the Intent Preservation System.

## Task

Implement TASK-008: query deterministic trace paths from a graph start node to
upstream target node types.

## Context

Use the context package at `../13_context_packages/CP-task-008.md`, especially:

- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- `../21_execution_plans/EP-TASK-008.md`
- `../05_subsystems/SUB-002-graph-builder.md`

## Constraints

- Preserve default extractor JSON output unless `--trace` is supplied.
- Use extracted declared graph edges only.
- Keep traversal deterministic.
- Do not implement orphan detection, dependency maps, vector search or RAG.
- Do not modify protected baseline documents.

## Allowed Changes

- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- TASK-008 documentation and graph-example entries.

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Pre-existing TASK-004 worktree changes.
- Any prompt, fixture or report containing secrets or raw production data.

## Implementation Instructions

1. Add deterministic trace traversal over extracted graph edges.
2. Support CLI options for start node, target node type and max depth.
3. Return structured paths with node ids and traversed edges.
4. Return structured findings for missing start nodes or missing paths.
5. Add tests for successful trace and missing start behavior.

## Parallel Workstream Context

This prompt is a standalone single-agent prompt because `../21_execution_plans/EP-TASK-008.md` does not expose refactored parallel workstreams.

- Execution-plan status: validated.
- Parallel dispatch list: `WS-008-A` trace-path query implementation, `WS-008-D` TASK-008 artifact chain, `WS-008-V` final validation.
- Goal blockers and dependencies: `WS-008-A` depends on TASK-007 extractor behavior; `WS-008-D` and `WS-008-V` depend on implementation handoff.
- Owned files: `../../scripts/graph_extractor.py`, `../../tests/test_graph_extractor.py`, TASK-008 documentation and graph-example entries.
- Forbidden files: `../00_constitution/CONSTITUTION.md`, `../01_vision/VISION.md`, pre-existing TASK-004 worktree changes, and any prompt, fixture or report containing secrets or raw production data.
- Expected handoff output: files changed, validation evidence, blockers, dependencies on other workstreams, integration notes, deviations and remaining documentation gaps.

## Acceptance criteria

- A CLI command can query paths from a task id to Vision target nodes.
- Trace output includes ordered node ids and traversed edges.
- Missing start nodes return a structured finding.
- Tests cover successful traces and missing start nodes.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --trace TASK-007 --target-type Vision --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-008
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
