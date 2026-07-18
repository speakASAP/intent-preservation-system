# EP-TASK-007: Extract Knowledge Graph from Repository Documents

```yaml
id: EP-TASK-007
status: validated
source_task: ../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md
owner: knowledge-graph-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-007.md
coding_prompt: ../14_prompts/PROMPT-TASK-007-knowledge-graph-extraction.md
```

## Metadata

This execution plan defines the implementation boundary for TASK-007 and is
validated by `../12_validation/VAL-TASK-007-knowledge-graph-extraction.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../09_milestones/MS-004-knowledge-graph.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-007.md
system: ../04_systems/SYS-002-context-engine.md
subsystem: ../05_subsystems/SUB-002-graph-builder.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The implementation creates the first executable Phase 4 graph-builder step. It
allows later tasks to query trace paths, detect orphan tasks and build dependency
maps from repository documents instead of hand-maintained graph examples alone.

## Project Invariants

- IPS-INV-001: relationships must come from declared document metadata or
  explicit links, not guessed semantic similarity.
- IPS-INV-002: protected vision and constitution documents are read-only inputs.
- IPS-INV-003: code changes must stay inside this execution plan.
- IPS-INV-004: validation evidence must be captured in a TASK-007 validation
  report before closure.
- IPS-INV-005: fixtures and reports must use synthetic data only.

## Sensitive-Data Handling

Classification: none. The extractor operates on repository Markdown and tests
use synthetic fixture documents. The implementation must not copy real customer,
supplier, mailbox, attachment, export or production records into examples,
logs, tests or validation reports.

## Contract Validation Plan

TASK-007 creates an executable extraction mapping aligned with
`../../graph/GRAPH_SCHEMA.md`. The first implementation should expose a structured
JSON-compatible graph object with `nodes`, `edges` and `findings` collections.
Fixture tests must validate node fields, edge fields, stable ordering and broken
reference findings. Any required schema change must be reported as a deviation
instead of silently editing `../../graph/GRAPH_SCHEMA.md`.

## Replay/Determinism Plan

Sort input paths, extracted nodes, extracted edges and findings before output.
Fixture tests must run extraction twice over the same fixture tree and assert
identical serialized output.

## Scope

Implement a dependency-free repository graph extractor that scans Markdown
documents, classifies known IPS artifact types, extracts declared metadata links,
normalizes repository-relative references and emits deterministic structured
output.

## Non-Goals

- No graph query API.
- No path traversal beyond producing extracted edges.
- No vector retrieval or embeddings.
- No generated context packages or coding prompts.
- No modification of immutable vision or constitution files.

## Files to Inspect

- `scripts/strict_doc_audit.py`
- `graph/GRAPH_SCHEMA.md`
- `graph/project_graph.example.yaml`
- `04_systems/SYS-002-context-engine.md`
- `05_subsystems/SUB-002-graph-builder.md`
- `06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `07_decisions/ADR-002-use-graph-retrieval-before-rag.md`

## Files to Create

- scripts/graph_extractor.py
- tests/test_graph_extractor.py
- 12_validation/VAL-TASK-007-knowledge-graph-extraction.md
- 13_context_packages/CP-task-007.md
- 14_prompts/PROMPT-TASK-007-knowledge-graph-extraction.md

## Files to Modify

- `package.json`
- `graph/project_graph.example.yaml`
- `11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `21_execution_plans/EP-TASK-007.md`

Only modify `graph/project_graph.example.yaml` if implementation evidence needs
to register TASK-007 artifacts or if validation proves the graph example is out
of sync with the new task.

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`
- Unrelated task, execution-plan, prompt, context-package or validation files
  outside TASK-007 scope.

## Implementation Steps

1. Reuse the document classification and metadata parsing approach from
   `scripts/strict_doc_audit.py` where practical.
2. Define graph extraction data structures for nodes, edges and findings.
3. Scan Markdown files in deterministic path order while excluding generated,
   cache and dependency directories.
4. Create nodes for known IPS artifact types using document id metadata when
   present and stable file-derived ids otherwise.
5. Extract edges from declared metadata fields and section links that represent
   traceability relationships in `../../graph/GRAPH_SCHEMA.md`.
6. Normalize links to repository-relative paths and report missing references as
   findings.
7. Add a CLI that accepts `--root` and prints deterministic JSON output.
8. Add fixture tests for node extraction, edge extraction, broken references and
   replay determinism.
9. Add validation evidence in a TASK-007 validation report.
10. Run required gates and document any deviations.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-007-A | Implement deterministic graph extraction and CLI | yes, as the only implementation workstream | knowledge-graph implementation agent | `scripts/graph_extractor.py`; `tests/test_graph_extractor.py` | Extracted nodes, edges, findings and deterministic tests | none |
| WS-007-D | Add TASK-007 docs, prompt, context package and graph entries | no, dependency-gated | documentation/graph agent | TASK-007 artifacts under `12_validation/`, `13_context_packages/`, `14_prompts/`, `graph/project_graph.example.yaml`, and TASK-007 plan/task files | Traceable TASK-007 documentation chain | WS-007-A behavior |
| WS-007-V | Final validation and gate evidence | no, final integration | validation agent | TASK-007 validation report | Command evidence and readiness recommendation | WS-007-A and WS-007-D complete |

WS-007-A may run in a separate Codex thread before implementation is complete.
WS-007-D and WS-007-V are dependency-gated because graph documentation and
validation depend on the extractor contract.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-007-A | No open blocker recorded | knowledge-graph implementation agent | Preserve `graph/GRAPH_SCHEMA.md` unless a deviation is approved | resolved |
| WS-007-D | Requires final extractor fields and findings | documentation/graph agent | Register artifacts after WS-007-A handoff | dependency-gated |
| WS-007-V | Requires implementation and documentation evidence | validation agent | Run gates and update validation report | dependency-gated |

## Parallel Dispatch List

### Goal WS-007-A: Knowledge Graph Extraction

- Owner role: knowledge-graph implementation agent.
- Objective: implement deterministic graph extraction from declared IPS metadata
  and links.
- Allowed files: `scripts/graph_extractor.py`; `tests/test_graph_extractor.py`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, `graph/GRAPH_SCHEMA.md` unless reporting a deviation,
  unrelated artifacts and secrets/raw production data.
- Required inputs: TASK-007, this plan, `graph/GRAPH_SCHEMA.md` and ADR-002.
- Blockers: none open.
- Validation evidence: `python3 -m unittest tests.test_graph_extractor`.
- Handoff output: code/test changes, extracted contract notes, tests run,
  blockers and deviations.

### Goal WS-007-D: TASK-007 Artifact Chain

- Owner role: documentation/graph agent.
- Objective: preserve the TASK-007 context, prompt, validation and graph chain.
- Allowed files: TASK-007 artifacts listed in this plan and
  `graph/project_graph.example.yaml`.
- Forbidden files: protected vision/constitution files, schema changes and
  unrelated task artifacts.
- Required inputs: WS-007-A handoff.
- Blockers: WS-007-A final contract.
- Validation evidence: strict audit and graph artifact review.
- Handoff output: documentation/graph changes, blockers and deviations.

### Goal WS-007-V: Final Validation

- Owner role: validation agent.
- Objective: validate TASK-007 extraction behavior and record evidence.
- Allowed files: `12_validation/VAL-TASK-007-knowledge-graph-extraction.md`.
- Forbidden files: protected files and implementation files unless reporting a
  validation defect.
- Required inputs: WS-007-A and WS-007-D handoffs.
- Blockers: implementation and artifact chain complete.
- Validation evidence: focused graph tests, `npm run validate`, pre-coding gate
  and deployment-readiness gate for TASK-007.
- Handoff output: validation evidence and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-007-A

You are the TASK-007 knowledge-graph implementation agent. Implement
deterministic extraction of nodes, edges and findings from declared IPS
metadata. Modify only `scripts/graph_extractor.py` and focused tests unless a
deviation is reported. Return files changed, contract notes, tests run,
blockers and deviations.

### Workstream WS-007-D

You are the TASK-007 documentation/graph agent. After WS-007-A, update only the
TASK-007 artifact chain and graph example entries needed to preserve
traceability. Return files changed, evidence, blockers and deviations.

### Workstream WS-007-V

You are the TASK-007 validation agent. After implementation and artifact updates,
run graph tests, repository validation, pre-coding gate and deployment-readiness
gate for TASK-007. Record evidence and readiness recommendation.

## Test Plan

- Unit test document classification for task, execution plan, goal-impact,
  prompt, context package and validation report fixture files.
- Unit test edge extraction from `upstream`, `goal_impact`, `execution_plan`,
  `source_task`, prompt context and validation report references.
- Unit test unresolved reference findings.
- Unit test deterministic serialized output across repeated runs.

## Validation Plan

Run focused unit tests first, then run full repository validation. The task can
close only after a TASK-007 validation report records command output, invariant
evidence, sensitive-data handling and any deviations.

## Gate Commands

```bash
python3 -m unittest tests.test_graph_extractor
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-007
```

## Documentation Updates

- Add a TASK-007 validation report after implementation.
- Add a TASK-007 context package and coding prompt to preserve the implementation
  handoff chain.
- Update `../../graph/project_graph.example.yaml` with TASK-007 implementation
  artifacts once they exist.
- Document any schema gap as a deviation rather than editing
  `../../graph/GRAPH_SCHEMA.md` inside this task.

## Rollback Plan

Remove scripts/graph_extractor.py, tests/test_graph_extractor.py, the
TASK-007 validation report and any TASK-007 graph-example additions. Leave the
task, goal-impact record and execution plan in draft state unless a reviewer
explicitly retires them.

## Agent Handoff Prompt

Implement TASK-007 using this plan. Build a deterministic, dependency-free
extractor for graph nodes and edges from IPS Markdown documents. Preserve
declared traceability, report unresolved links, avoid schema changes unless
documented as deviations, and do not modify protected baseline documents.

## Completion Checklist

- [x] Implementation complete
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
