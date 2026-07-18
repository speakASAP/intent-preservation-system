# EP-TASK-008: Query Knowledge Graph Trace Paths

```yaml
id: EP-TASK-008
status: validated
source_task: ../11_tasks/TASK-008-query-knowledge-graph-trace-paths.md
owner: knowledge-graph-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-008.md
coding_prompt: ../14_prompts/PROMPT-TASK-008-knowledge-graph-trace-paths.md
```

## Metadata

This execution plan implements TASK-008 and is validated by
`../12_validation/VAL-TASK-008-knowledge-graph-trace-paths.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../09_milestones/MS-004-knowledge-graph.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-008.md
system: ../04_systems/SYS-002-context-engine.md
subsystem: ../05_subsystems/SUB-002-graph-builder.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan satisfies the Phase 4 requirement that graph trace paths can be
queried. It builds directly on TASK-007 extraction output.

## Project Invariants

- IPS-INV-001: query results must come from extracted declared graph edges.
- IPS-INV-002: protected documents remain read-only inputs.
- IPS-INV-003: changes stay scoped to the graph extractor and TASK-008 docs.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: tests use synthetic fixture documents.

## Sensitive-Data Handling

Classification: none. The query works over repository Markdown metadata and
synthetic fixture documents only.

## Contract Validation Plan

The CLI preserves the default extraction JSON output. When `--trace` is
supplied, it emits a JSON object with `start`, `target_types`, `paths` and
`findings`. Tests validate the result shape.

## Replay/Determinism Plan

Breadth-first traversal uses sorted outgoing edges and returns sorted paths.
Tests validate deterministic output indirectly through the existing repeated
serialization test and direct trace assertions.

## Scope

Add trace-path query support to `scripts/graph_extractor.py` and focused tests
to `tests/test_graph_extractor.py`.

## Non-Goals

- No orphan-task detection.
- No dependency-map generation.
- No semantic retrieval or vector search.
- No schema changes.

## Files to Inspect

- `scripts/graph_extractor.py`
- `tests/test_graph_extractor.py`
- `graph/GRAPH_SCHEMA.md`
- `05_subsystems/SUB-002-graph-builder.md`
- `11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`

## Files to Create

- `11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`
- `21_execution_plans/EP-TASK-008.md`
- `22_goal_impact/GOAL-IMPACT-TASK-008.md`
- `13_context_packages/CP-task-008.md`
- `14_prompts/PROMPT-TASK-008-knowledge-graph-trace-paths.md`
- `12_validation/VAL-TASK-008-knowledge-graph-trace-paths.md`

## Files to Modify

- `scripts/graph_extractor.py`
- `tests/test_graph_extractor.py`
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`
- Unrelated TASK-004 files already present in the worktree.

## Implementation Steps

1. Add a trace-path data structure for traversed edges.
2. Build deterministic adjacency from extracted graph edges.
3. Traverse breadth-first from the requested start node to target node types.
4. Return structured findings for missing start nodes or missing paths.
5. Add CLI arguments for trace mode.
6. Add focused fixture tests.
7. Record validation evidence and graph links.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-008-A | Implement deterministic trace-path query support | yes, as the only implementation workstream | knowledge-graph implementation agent | `scripts/graph_extractor.py`; `tests/test_graph_extractor.py` | Trace query CLI behavior and focused tests | none |
| WS-008-D | Add TASK-008 artifact chain and graph entries | no, dependency-gated | documentation/graph agent | TASK-008 artifacts and `graph/project_graph.example.yaml` | Traceable documentation chain | WS-008-A complete |
| WS-008-V | Final validation and readiness evidence | no, final integration | validation agent | `12_validation/VAL-TASK-008-knowledge-graph-trace-paths.md` | Gate evidence and readiness recommendation | WS-008-A and WS-008-D complete |

WS-008-A can run in a separate Codex thread before implementation is complete.
WS-008-D and WS-008-V are serial because docs and validation depend on the trace
query contract.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-008-A | TASK-007 extractor must exist | knowledge-graph implementation agent | Build trace traversal on extracted declared edges only | resolved |
| WS-008-D | Requires final trace CLI/report behavior | documentation/graph agent | Register TASK-008 artifacts after WS-008-A | dependency-gated |
| WS-008-V | Requires implementation and artifact evidence | validation agent | Run gates and update validation report | dependency-gated |

## Parallel Dispatch List

### Goal WS-008-A: Trace Path Queries

- Owner role: knowledge-graph implementation agent.
- Objective: add deterministic trace queries from a start node to target node
  types while preserving default extraction output.
- Allowed files: `scripts/graph_extractor.py`; `tests/test_graph_extractor.py`.
- Forbidden files: protected vision/constitution files, schema changes,
  unrelated TASK-004 files and artifacts containing secrets or raw production
  data.
- Required inputs: TASK-008, this plan and TASK-007 extractor behavior.
- Blockers: TASK-007 extractor availability.
- Validation evidence: focused graph extractor tests and a TASK-007 trace query.
- Handoff output: code/test changes, CLI behavior, tests run, blockers and
  deviations.

### Goal WS-008-D: TASK-008 Artifact Chain

- Owner role: documentation/graph agent.
- Objective: add or update TASK-008 task, goal-impact, context package, prompt,
  validation report and graph entries after WS-008-A.
- Allowed files: TASK-008 artifacts and `graph/project_graph.example.yaml`.
- Forbidden files: protected vision/constitution files and implementation files
  unless reporting a deviation.
- Required inputs: WS-008-A handoff.
- Blockers: final trace behavior from WS-008-A.
- Validation evidence: strict audit and graph artifact review.
- Handoff output: documentation/graph changes, blockers and deviations.

### Goal WS-008-V: Final Validation

- Owner role: validation agent.
- Objective: validate TASK-008 behavior and record readiness evidence.
- Allowed files: `12_validation/VAL-TASK-008-knowledge-graph-trace-paths.md`.
- Forbidden files: protected files and implementation files unless a validation
  defect is reported.
- Required inputs: WS-008-A and WS-008-D handoffs.
- Blockers: implementation and artifact chain complete.
- Validation evidence: graph tests, sample trace query, `npm run validate`,
  pre-coding gate and deployment-readiness gate for TASK-008.
- Handoff output: validation evidence and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-008-A

You are the TASK-008 knowledge-graph implementation agent. Extend
`scripts/graph_extractor.py` with deterministic trace-path query support and
focused tests. Preserve default extraction output and avoid schema changes.
Return files changed, CLI behavior, tests run, blockers and deviations.

### Workstream WS-008-D

You are the TASK-008 documentation/graph agent. After WS-008-A, update only the
TASK-008 artifact chain and graph entries needed for traceability. Return files
changed, evidence, blockers and deviations.

### Workstream WS-008-V

You are the TASK-008 validation agent. After implementation and artifacts, run
graph tests, a sample trace query, repository validation, pre-coding gate and
deployment-readiness gate for TASK-008. Record evidence and readiness.

## Test Plan

- Test a successful task-to-vision trace.
- Test missing start-node findings.
- Keep existing extraction, missing-reference and determinism tests passing.

## Validation Plan

Run the focused tests, a repository TASK-007 trace query, full repository
validation and deployment-readiness target gate for TASK-008.

## Gate Commands

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --trace TASK-007 --target-type Vision --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-008
```

## Documentation Updates

Add TASK-008 task, goal-impact, context package, coding prompt, validation
report and graph-example entries.

## Rollback Plan

Remove the trace query functions, CLI options, TASK-008 tests and TASK-008
documentation artifacts. Restore graph-example entries for TASK-008 only.

## Agent Handoff Prompt

Implement TASK-008 by extending the graph extractor with deterministic trace
path queries from a start node to target node types. Preserve default extraction
output and avoid unrelated graph analytics.

## Completion Checklist

- [x] Implementation complete
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
