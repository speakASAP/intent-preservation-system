# EP-TASK-009: Detect Orphan Tasks From Knowledge Graph

```yaml
id: EP-TASK-009
status: validated
source_task: ../11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md
owner: knowledge-graph-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
parallelization_strategy: single_agent
project_invariant_impact: preserves
sensitive_data_classification: none
contract_schema_impact: changes
replay_determinism_impact: required
required_gates:
  - focused-tests
  - orphan-task-query
  - repository-validation
  - pre-coding
  - deployment-readiness
context_package: ../13_context_packages/CP-task-009.md
coding_prompt: ../14_prompts/PROMPT-TASK-009-orphan-task-detection.md
```

## Metadata

This execution plan implements TASK-009 and is validated by
`../12_validation/VAL-TASK-009-orphan-task-detection.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../09_milestones/MS-004-knowledge-graph.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-009.md
system: ../04_systems/SYS-002-context-engine.md
subsystem: ../05_subsystems/SUB-002-graph-builder.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan satisfies the Phase 4 requirement that orphan tasks can be detected.
It builds directly on TASK-007 graph extraction and TASK-008 trace traversal.

## Project Invariants

- IPS-INV-001: orphan results must come from extracted declared graph edges.
- IPS-INV-002: protected documents remain read-only inputs.
- IPS-INV-003: changes stay scoped to the graph extractor, tests and TASK-009
  docs.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: tests use synthetic fixture documents.

## Sensitive-Data Handling

Classification: none. The detector works over repository Markdown metadata and
synthetic fixture documents only.

## Contract Validation Plan

The CLI preserves default extraction JSON output. When `--orphan-tasks` is
supplied, it emits a JSON object with `target_types`, `max_depth`, `tasks`,
`orphan_tasks` and `findings`. Tests validate the result shape.

## Replay/Determinism Plan

The detector processes task nodes sorted by id and reuses deterministic trace
traversal. Tests validate stable orphan and non-orphan classification.

## Scope

Add orphan-task detection support to `scripts/graph_extractor.py` and focused
tests to `tests/test_graph_extractor.py`.

## Non-Goals

- No dependency-map generation.
- No semantic retrieval or vector search.
- No schema changes.

## Parallelization Plan

Parallelization strategy: `single_agent`.

TASK-009 is already validated. The executable implementation work is not split
across simultaneous agents because the orphan detector and its focused tests
share `scripts/graph_extractor.py` and `tests/test_graph_extractor.py`.
Splitting those files across agents would create shared-file merge risk without
a source-backed independent goal boundary. The plan still exposes dispatch
metadata so future agents can see that implementation and final validation are
separate workstream states.

### Ready-Now Parallel Goals

- WS-009-A: implement deterministic orphan-task detection and focused tests.
  Status: ready now for a single implementation agent in the original execution
  context; already validated by `../12_validation/VAL-TASK-009-orphan-task-detection.md`.
  Assigned files: `scripts/graph_extractor.py`,
  `tests/test_graph_extractor.py`, and TASK-009 documentation artifacts listed
  in this plan. Validation responsibility: focused graph extractor tests,
  repository orphan-task query and repository gates.

No additional ready-now parallel goal is source-backed for TASK-009.

### Dependency-Gated Goals

- WS-009-B: final integration and validation evidence review. Status:
  final integration. Dependency: WS-009-A implementation and test evidence must
  be complete. Assigned files: validation report and TASK-009 documentation
  artifacts listed in this plan.

### Blockers

- None for the validated TASK-009 implementation.
- Parallel split blocker: shared edits to `scripts/graph_extractor.py` and
  `tests/test_graph_extractor.py` make additional simultaneous implementation
  workstreams unsafe unless a future plan defines a new independent file or
  contract boundary.

### Shared Files And Merge Order

1. Merge WS-009-A implementation changes to `scripts/graph_extractor.py` and
   `tests/test_graph_extractor.py`.
2. Run WS-009-A validation commands.
3. Complete WS-009-B integration review, validation report and TASK-009
   documentation updates.

Shared files: `scripts/graph_extractor.py`, `tests/test_graph_extractor.py`,
TASK-009 documentation artifacts and `../12_validation/VAL-TASK-009-orphan-task-detection.md`.
Integration owner: `knowledge-graph-agent`.

## Files to Inspect

- `scripts/graph_extractor.py`
- `tests/test_graph_extractor.py`
- `graph/GRAPH_SCHEMA.md`
- `05_subsystems/SUB-002-graph-builder.md`
- `11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `11_tasks/TASK-008-query-knowledge-graph-trace-paths.md`

## Files to Create

- `11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`
- `21_execution_plans/EP-TASK-009.md`
- `22_goal_impact/GOAL-IMPACT-TASK-009.md`
- `13_context_packages/CP-task-009.md`
- `14_prompts/PROMPT-TASK-009-orphan-task-detection.md`
- `12_validation/VAL-TASK-009-orphan-task-detection.md`

## Files to Modify

- `scripts/graph_extractor.py`
- `tests/test_graph_extractor.py`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`
- Unrelated TASK-004 files already present in the worktree.

## Implementation Steps

1. Add a reusable orphan-task detection function that accepts an extracted graph.
2. Iterate deterministic task nodes and call trace traversal for each task.
3. Report tasks with no trace paths as orphan tasks.
4. Add CLI support for `--orphan-tasks`.
5. Add focused fixture tests.
6. Record validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-009-A | Implement deterministic orphan-task detection and tests | yes, as the only implementation workstream | knowledge-graph implementation agent | `scripts/graph_extractor.py`, `tests/test_graph_extractor.py`, TASK-009 docs listed in this plan | CLI support for `--orphan-tasks`, deterministic JSON findings and focused tests | none |
| WS-009-B | Final integration and validation evidence review | no, final integration | validation/documentation integration agent | `../12_validation/VAL-TASK-009-orphan-task-detection.md`, TASK-009 docs listed in this plan | validation evidence confirmed and docs aligned | WS-009-A complete |

Separate-thread execution is not applicable for multiple simultaneous
implementation agents because TASK-009 has one source-backed implementation
boundary and shared implementation/test files. WS-009-B should run after
WS-009-A rather than in parallel.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-009-A | none | knowledge-graph-agent | no external decision, credential or environment blocker is named by the source task | resolved |
| WS-009-B | WS-009-A implementation and validation evidence | knowledge-graph-agent | focused tests, orphan query, repository validation and gates complete | resolved |
| Additional parallel implementation split | shared edits to `scripts/graph_extractor.py` and `tests/test_graph_extractor.py` | integration owner | define a new independent file or contract boundary before assigning another simultaneous agent | not applicable |

## Parallel Dispatch List

### Goal WS-009-A: Orphan Detection Implementation

- Owner role: knowledge-graph implementation agent.
- Objective: add deterministic orphan-task detection to the graph extractor by
  identifying task nodes without trace paths to configured upstream target
  types through extracted graph edges.
- Allowed files: `scripts/graph_extractor.py`, `tests/test_graph_extractor.py`,
  `11_tasks/TASK-009-detect-orphan-tasks-from-knowledge-graph.md`,
  `21_execution_plans/EP-TASK-009.md`,
  `22_goal_impact/GOAL-IMPACT-TASK-009.md`,
  `13_context_packages/CP-task-009.md`,
  `14_prompts/PROMPT-TASK-009-orphan-task-detection.md`,
  `12_validation/VAL-TASK-009-orphan-task-detection.md`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, dependency-map implementation, vector search,
  embeddings, RAG and unrelated TASK-004 files already present in the worktree.
- Required inputs: TASK-009, TASK-007, TASK-008, graph schema, graph builder
  subsystem, project invariants, this execution plan and the context package.
- Blockers: none named by the source task.
- Validation evidence: focused graph extractor tests, repository orphan-task
  query, `npm run validate`, pre-coding gate and deployment-readiness target
  gate for TASK-009.
- Handoff output: files changed, tests run, validation evidence, blockers,
  dependencies on other workstreams, integration notes, deviations and remaining
  documentation gaps.

### Goal WS-009-B: Final Integration And Validation Review

- Owner role: validation/documentation integration agent.
- Objective: confirm WS-009-A evidence, keep TASK-009 documentation aligned and
  preserve validated status.
- Allowed files: `12_validation/VAL-TASK-009-orphan-task-detection.md` and
  TASK-009 documentation artifacts listed above.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, graph schema changes and unrelated task files.
- Required inputs: WS-009-A handoff, validation command output and TASK-009
  source chain.
- Blockers: WS-009-A must be complete before final integration review.
- Validation evidence: same gate commands listed in this plan, or recorded
  evidence in the validation report.
- Handoff output: final validation status, documentation updates, remaining
  blockers and deviations.

## Parallel Agent Handoff Prompts

### Workstream WS-009-A

You are the TASK-009 knowledge-graph implementation agent. Implement
deterministic orphan-task detection in `scripts/graph_extractor.py` and focused
coverage in `tests/test_graph_extractor.py`. Use only extracted graph nodes and
edges, reuse trace-query traversal, preserve default extraction JSON when
`--orphan-tasks` is not supplied, and do not change `graph/GRAPH_SCHEMA.md`.
Do not modify `00_constitution/CONSTITUTION.md`, `01_vision/VISION.md`,
dependency-map implementation, vector search, embeddings, RAG or unrelated
TASK-004 worktree changes. Validate with the gate commands in this plan and
return files changed, tests run, validation evidence, blockers, integration
notes, deviations and remaining documentation gaps.

### Workstream WS-009-B

You are the TASK-009 validation/documentation integration agent. Start only
after WS-009-A has returned implementation and validation evidence. Confirm the
orphan-task detector remains deterministic, the CLI report shape is documented,
the TASK-009 validation evidence is recorded, and the task, execution plan,
context package and coding prompt remain aligned. Do not modify protected
vision or constitution documents, graph schema, source code or tests unless a
new approved plan explicitly expands scope. Return final validation status,
documentation updates, blockers, deviations and remaining documentation gaps.

## Test Plan

- Test that a task tracing to Vision is not orphaned.
- Test that a task without a trace path to Vision is reported as orphaned.
- Keep existing extraction, missing-reference, determinism and trace tests
  passing.

## Validation Plan

Run focused tests, a repository orphan-task query, full repository validation
and deployment-readiness target gate for TASK-009.

## Gate Commands

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --orphan-tasks --target-type Vision --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-009
```

## Documentation Updates

Add TASK-009 task, goal-impact, context package, coding prompt and validation
report.

## Rollback Plan

Remove the orphan detection function, CLI option, TASK-009 tests and TASK-009
documentation artifacts.

## Agent Handoff Prompt

Implement TASK-009 by extending the graph extractor with deterministic orphan
task detection from extracted graph nodes and trace paths. Preserve default
extraction output and avoid dependency-map generation.

## Completion Checklist

- [x] Implementation complete
- [x] Parallelizable workstreams identified
- [x] Blockers and serial dependencies documented
- [x] Agent handoff prompts created for independent workstreams
- [x] Integration order documented
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
