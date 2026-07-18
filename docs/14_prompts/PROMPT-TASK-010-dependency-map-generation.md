# Coding Prompt: TASK-010 Dependency Map Generation

```yaml
id: PROMPT-TASK-010-dependency-map-generation
source_task: ../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md
execution_plan: ../21_execution_plans/EP-TASK-010.md
context_package: ../13_context_packages/CP-task-010.md
status: used
```

## Role

You are an implementation agent working on Phase 4 knowledge-graph dependency
map generation for Intent Preservation System.

## Task

Implement TASK-010: generate bounded upstream and downstream dependency maps
from extracted graph relationships.

## Context

Use the context package at `../13_context_packages/CP-task-010.md`, especially:

- `../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md`
- `../21_execution_plans/EP-TASK-010.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-010.md`
- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../graph/GRAPH_SCHEMA.md`

## Constraints

- Use extracted graph nodes and edges only.
- Keep default extraction output unchanged.
- Keep output deterministic.
- Do not infer semantic dependencies from prose.
- Do not implement vector search, embeddings or RAG.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../graph/project_graph.example.yaml`
- TASK-010 documentation and graph-example entries.

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Pre-existing TASK-004 worktree changes.
- Any prompt, fixture or report containing secrets or raw production data.

## Implementation Instructions

1. Add deterministic dependency-map traversal over extracted graph edges.
2. Include upstream outgoing relationships and downstream incoming
   relationships.
3. Support `--dependency-map NODE_ID` and `--max-depth`.
4. Return structured nodes, edges and findings.
5. Add tests for successful maps, missing start nodes and deterministic output.

## Parallel Workstream Context

- Prompt type: implementation prompt derived from a source execution plan that
  now exposes refactored parallel dispatch metadata.
- Source blocker: none; `../21_execution_plans/EP-TASK-010.md` includes
  Parallel Dispatch List, Goal Blockers And Dependencies and Parallel Agent
  Handoff Prompts.
- Dependencies: use the serial dependencies and files listed in the execution
  plan; `WS-010-A` depends on existing graph extraction/query behavior, and
  `WS-010-D`/`WS-010-V` depend on the implementation handoff.
- Owned files: `WS-010-A` owns implementation/test files; `WS-010-D` owns
  TASK-010 artifact and graph updates; `WS-010-V` owns final validation evidence.
- Expected handoff: return validation evidence, remaining blockers,
  dependencies on other agent workstreams and integration notes.

## Acceptance criteria

- A CLI command can generate a dependency map for a task id.
- The map includes upstream and downstream relationships from extracted edges.
- Missing start nodes return a structured finding.
- Tests cover successful maps and missing start nodes.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --dependency-map TASK-010 --max-depth 2 --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-010
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
