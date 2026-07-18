# Context Package: TASK-010

## Target task

TASK-010: `../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../05_subsystems/SUB-002-graph-builder.md -> ../09_milestones/MS-004-knowledge-graph.md -> TASK-010
```

## Included documents

- `../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md`
- `../21_execution_plans/EP-TASK-010.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-010.md`
- `../12_validation/VAL-TASK-010-dependency-map-generation.md`
- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../graph/GRAPH_SCHEMA.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- `../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`
- `../17_governance/PROJECT_INVARIANTS.md`

## Excluded documents

- Vector search, embeddings and optional RAG documents are excluded.
- Semantic dependency inference from prose is excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Use extracted graph edges only.
- Keep dependency-map output deterministic.
- Preserve default extractor output when dependency-map mode is not requested.
- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.

## Parallel dispatch status

- Source execution plan: `../21_execution_plans/EP-TASK-010.md`
- Dispatch readiness: [MISSING: source execution plan does not include a
  `Parallel Dispatch List` or `Parallel Agent Handoff Prompts` section after the
  parallel-agent execution-plan refactor.]
- Derived prompt treatment: use the coding prompt as a single-agent
  implementation prompt until the execution plan is refactored with explicit
  workstream ownership.
- Blockers: [MISSING: workstream owners, per-workstream allowed files,
  per-workstream forbidden files, blockers, validation evidence and handoff
  outputs.]

## Agent prompt

Implement TASK-010 by adding deterministic dependency-map generation to the
graph extractor. Return structured node, edge and finding data as JSON.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --dependency-map TASK-010 --max-depth 2 --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-010
```
