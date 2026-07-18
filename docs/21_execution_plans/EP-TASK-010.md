# EP-TASK-010: Generate Knowledge Graph Dependency Map

```yaml
id: EP-TASK-010
status: validated
source_task: ../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md
owner: knowledge-graph-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-010.md
coding_prompt: ../14_prompts/PROMPT-TASK-010-dependency-map-generation.md
```

## Metadata

This execution plan implements TASK-010 and is validated by
`../12_validation/VAL-TASK-010-dependency-map-generation.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../09_milestones/MS-004-knowledge-graph.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-010.md
system: ../04_systems/SYS-002-context-engine.md
subsystem: ../05_subsystems/SUB-002-graph-builder.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan satisfies the Phase 4 requirement that a dependency map can be
generated. It builds directly on graph extraction, trace traversal and
orphan-task detection.

## Project Invariants

- IPS-INV-001: dependency maps must come from extracted declared graph edges.
- IPS-INV-002: protected documents remain read-only inputs.
- IPS-INV-003: changes stay scoped to the graph extractor, tests and TASK-010
  docs.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: tests use synthetic fixture documents.

## Sensitive-Data Handling

Classification: none. The map works over repository Markdown metadata and
synthetic fixture documents only.

## Contract Validation Plan

The CLI preserves default extraction JSON output. When `--dependency-map` is
supplied, it emits a JSON object with `start`, `max_depth`, `nodes`, `edges` and
`findings`. Tests validate the result shape.

## Replay/Determinism Plan

The map traversal uses sorted incoming and outgoing edges and returns sorted
nodes and edges. Tests validate deterministic output.

## Scope

Add dependency-map support to `scripts/graph_extractor.py` and focused tests to
`tests/test_graph_extractor.py`.

## Non-Goals

- No semantic dependency inference from prose.
- No semantic retrieval or vector search.
- No schema changes.

## Files to Inspect

- `scripts/graph_extractor.py`
- `tests/test_graph_extractor.py`
- `graph/GRAPH_SCHEMA.md`
- `05_subsystems/SUB-002-graph-builder.md`
- `11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- `11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`

## Files to Create

- `11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md`
- `21_execution_plans/EP-TASK-010.md`
- `22_goal_impact/GOAL-IMPACT-TASK-010.md`
- `13_context_packages/CP-task-010.md`
- `14_prompts/PROMPT-TASK-010-dependency-map-generation.md`
- `12_validation/VAL-TASK-010-dependency-map-generation.md`

## Files to Modify

- `scripts/graph_extractor.py`
- `tests/test_graph_extractor.py`
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`
- Unrelated TASK-004 files already present in the worktree.

## Implementation Steps

1. Add a reusable dependency-map function that accepts an extracted graph and a
   start node id.
2. Build deterministic outgoing and incoming adjacency indexes.
3. Traverse upstream and downstream relationships up to max depth.
4. Return structured node, edge and finding data.
5. Add CLI support for `--dependency-map NODE_ID`.
6. Add focused fixture tests.
7. Record validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-010-A | Implement deterministic dependency-map generation | yes, as the only implementation workstream | knowledge-graph implementation agent | `scripts/graph_extractor.py`; `tests/test_graph_extractor.py` | Dependency-map CLI/report behavior and tests | none |
| WS-010-D | Add TASK-010 artifact chain and graph entries | no, dependency-gated | documentation/graph agent | TASK-010 artifacts and `graph/project_graph.example.yaml` | Traceable documentation chain | WS-010-A complete |
| WS-010-V | Final validation and readiness evidence | no, final integration | validation agent | `12_validation/VAL-TASK-010-dependency-map-generation.md` | Gate evidence and readiness recommendation | WS-010-A and WS-010-D complete |

WS-010-A can run in a separate Codex thread before implementation is complete.
WS-010-D and WS-010-V are dependency-gated because artifact updates and
validation depend on the final dependency-map contract.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-010-A | TASK-007 through TASK-009 graph behavior must exist | knowledge-graph implementation agent | Build maps from extracted declared graph edges only | resolved |
| WS-010-D | Requires final dependency-map behavior | documentation/graph agent | Register TASK-010 artifacts after WS-010-A | dependency-gated |
| WS-010-V | Requires implementation and artifact evidence | validation agent | Run gates and update validation report | dependency-gated |

## Parallel Dispatch List

### Goal WS-010-A: Dependency Map Generation

- Owner role: knowledge-graph implementation agent.
- Objective: add deterministic upstream/downstream dependency-map generation
  from extracted graph relationships.
- Allowed files: `scripts/graph_extractor.py`; `tests/test_graph_extractor.py`.
- Forbidden files: protected vision/constitution files, schema changes,
  unrelated TASK-004 files and artifacts containing secrets or raw production
  data.
- Required inputs: TASK-010, this plan, TASK-007 extraction, TASK-008 trace and
  TASK-009 orphan behavior.
- Blockers: graph extraction/query behavior must be available.
- Validation evidence: focused graph tests and sample dependency-map CLI output.
- Handoff output: code/test changes, CLI behavior, tests run, blockers and
  deviations.

### Goal WS-010-D: TASK-010 Artifact Chain

- Owner role: documentation/graph agent.
- Objective: add or update TASK-010 task, goal-impact, context package, prompt,
  validation report and graph entries after WS-010-A.
- Allowed files: TASK-010 artifacts and `graph/project_graph.example.yaml`.
- Forbidden files: protected vision/constitution files and implementation files
  unless reporting a deviation.
- Required inputs: WS-010-A handoff.
- Blockers: final dependency-map behavior from WS-010-A.
- Validation evidence: strict audit and graph artifact review.
- Handoff output: documentation/graph changes, blockers and deviations.

### Goal WS-010-V: Final Validation

- Owner role: validation agent.
- Objective: validate TASK-010 behavior and record readiness evidence.
- Allowed files: `12_validation/VAL-TASK-010-dependency-map-generation.md`.
- Forbidden files: protected files and implementation files unless a validation
  defect is reported.
- Required inputs: WS-010-A and WS-010-D handoffs.
- Blockers: implementation and artifact chain complete.
- Validation evidence: graph tests, sample dependency-map query,
  `npm run validate`, pre-coding gate and deployment-readiness gate for TASK-010.
- Handoff output: validation evidence and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-010-A

You are the TASK-010 knowledge-graph implementation agent. Extend
`scripts/graph_extractor.py` with deterministic dependency-map generation and
focused tests. Preserve default extraction output and avoid semantic inference.
Return files changed, CLI behavior, tests run, blockers and deviations.

### Workstream WS-010-D

You are the TASK-010 documentation/graph agent. After WS-010-A, update only the
TASK-010 artifact chain and graph entries needed for traceability. Return files
changed, evidence, blockers and deviations.

### Workstream WS-010-V

You are the TASK-010 validation agent. After implementation and artifacts, run
graph tests, a sample dependency-map query, repository validation, pre-coding
gate and deployment-readiness gate for TASK-010. Record evidence and readiness.

## Test Plan

- Test that a task dependency map includes upstream goal/plan relationships and
  downstream validation relationships.
- Test missing start-node findings.
- Test deterministic output.
- Keep existing extraction, trace and orphan tests passing.

## Validation Plan

Run focused tests, a repository dependency-map query, full repository validation
and deployment-readiness target gate for TASK-010.

## Gate Commands

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --dependency-map TASK-010 --max-depth 2 --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-010
```

## Documentation Updates

Add TASK-010 task, goal-impact, context package, coding prompt, validation
report and graph-example entries.

## Rollback Plan

Remove the dependency-map function, CLI option, TASK-010 tests and TASK-010
documentation artifacts. Restore graph-example entries for TASK-010 only.

## Agent Handoff Prompt

Implement TASK-010 by extending the graph extractor with deterministic
dependency-map generation from extracted graph relationships. Preserve default
extraction output and avoid semantic dependency inference.

## Completion Checklist

- [x] Implementation complete
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
