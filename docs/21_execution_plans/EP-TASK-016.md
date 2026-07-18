# EP-TASK-016: Manager Visibility Interface

```yaml
id: EP-TASK-016
status: validated
source_task: ../11_tasks/TASK-016-create-manager-visibility-interface.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
parallelization_strategy: parallel_goals
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: none
replay_determinism_impact: required
required_gates:
  - unit-tests
  - repository-validation
  - pre-coding
  - deployment-readiness
context_package: ../13_context_packages/CP-task-016.md
coding_prompt: ../14_prompts/PROMPT-TASK-016-manager-visibility-interface.md
validation_report: ../12_validation/VAL-TASK-016-manager-visibility-interface.md
```

## Metadata

This execution plan defines a small static web interface for managers to inspect
IPS traceability, retrieval comparison and validation status.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
system: ../04_systems/SYS-002-context-engine.md
feature: ../10_features/FEAT-004-manager-visibility.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-016.md
adr:
  - ../07_decisions/ADR-001-use-markdown-and-git-as-source-of-truth.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan converts IPS status into a manager-readable interface while preserving
the repository as the source of truth.

## Project Invariants

- IPS-INV-001: the dashboard represents the full Vision to Validation chain.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation is bounded to static interface assets and TASK-016
  governance documents.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: visible data is synthetic and repository-local.

## Sensitive-Data Handling

Classification: synthetic. The page uses local project status examples and
must not expose secrets, raw production data or customer identifiers.

## Contract Validation Plan

Confirm that no IPS schema, retrieval JSON contract or validation gate contract
is changed.

## Replay/Determinism Plan

Keep the interface static and deterministic. JavaScript state is local to the
browser and derived from hardcoded repository status examples.

## Scope

Add `manager_interface/index.html`, `manager_interface/styles.css` and
`manager_interface/app.js`.

## Non-Goals

- No backend.
- No production connection.
- No live document parser.
- No generated data from sensitive sources.

## Parallelization Plan

This task can be decomposed into parallel goal workstreams because the original
scope separates governance documents, static interface files and graph
traceability. Final validation is a dependency-gated integration workstream
because it requires the interface, graph entries and documentation to be present.

### Ready-Now Parallel Goals

- WS-016-A Governance chain documents: create or update TASK-016 governance
  documents and keep the Vision to Validation chain explicit.
- WS-016-B Static manager interface: create the local HTML, CSS and JavaScript
  interface under `manager_interface/`.
- WS-016-C Graph traceability entry: update `graph/project_graph.example.yaml`
  with TASK-016 feature, task, plan, prompt, context package and validation
  nodes.

### Dependency-Gated Goals

- WS-016-D Final validation and evidence: run local serving, browser checks,
  unit tests, repository validation, pre-coding gate and deployment-readiness
  gate after WS-016-A, WS-016-B and WS-016-C are complete.

### Blockers

- No approval, credential, production data or external environment blocker is
  identified in the source task, goal impact, context package or prompt.
- WS-016-D is blocked until the ready-now workstreams produce their files.

### Shared Files And Merge Order

- No ready-now workstream should edit the same implementation file.
- Merge order: WS-016-A governance documents first, WS-016-B interface files
  second, WS-016-C graph traceability third, WS-016-D validation evidence last.
- Integration owner: `context-engine-agent`, matching the execution-plan owner.

## Files to Inspect

- `10_features/FEAT-003-optional-rag-retrieval.md`
- `11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`
- `12_validation/VALIDATION_PYRAMID.md`
- `graph/project_graph.example.yaml`

## Files to Create

- `10_features/FEAT-004-manager-visibility.md`
- `11_tasks/TASK-016-create-manager-visibility-interface.md`
- `21_execution_plans/EP-TASK-016.md`
- `22_goal_impact/GOAL-IMPACT-TASK-016.md`
- `13_context_packages/CP-task-016.md`
- `14_prompts/PROMPT-TASK-016-manager-visibility-interface.md`
- `12_validation/VAL-TASK-016-manager-visibility-interface.md`
- `manager_interface/index.html`
- `manager_interface/styles.css`
- `manager_interface/app.js`

## Files to Modify

- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

Parallel wave 1:

1. WS-016-A: Add TASK-016 governance documents.
2. WS-016-B: Add the static manager interface.
3. WS-016-C: Update the project graph with feature, task, plan, prompt, context
   package and validation nodes.

Final integration wave:

1. WS-016-D: Serve the interface locally and verify desktop and mobile
   viewports.
2. WS-016-D: Run repository validation gates.
3. WS-016-D: Update validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-016-A | Create TASK-016 governance and derived planning documents. | yes | Context-engine documentation agent | `10_features/FEAT-004-manager-visibility.md`, `11_tasks/TASK-016-create-manager-visibility-interface.md`, `21_execution_plans/EP-TASK-016.md`, `22_goal_impact/GOAL-IMPACT-TASK-016.md`, `13_context_packages/CP-task-016.md`, `14_prompts/PROMPT-TASK-016-manager-visibility-interface.md`, `12_validation/VAL-TASK-016-manager-visibility-interface.md` | Source-backed governance chain for TASK-016. | none |
| WS-016-B | Create the static manager-facing interface. | yes | Frontend implementation agent | `manager_interface/index.html`, `manager_interface/styles.css`, `manager_interface/app.js` | Local static dashboard for traceability, retrieval comparison and validation status. | none |
| WS-016-C | Add graph traceability for TASK-016 artifacts. | yes | Graph documentation agent | `graph/project_graph.example.yaml` | Graph entries for feature, task, plan, prompt, context package and validation nodes. | none |
| WS-016-D | Integrate and validate TASK-016. | dependency-gated | Validation and integration agent | `12_validation/VAL-TASK-016-manager-visibility-interface.md`, validation terminal output | Local browser evidence and passing gate evidence. | WS-016-A, WS-016-B and WS-016-C complete |

Ready-now workstreams WS-016-A, WS-016-B and WS-016-C should be started in
separate Codex threads when thread-management tools are available. WS-016-D
should remain in the integration thread because it depends on merged outputs.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-016-A | None identified in source artifacts. | Context-engine documentation agent | Create source-backed governance documents without modifying protected vision or constitution files. | resolved |
| WS-016-B | None identified in source artifacts. | Frontend implementation agent | Create static local interface without backend, production connection or sensitive data. | resolved |
| WS-016-C | None identified in source artifacts. | Graph documentation agent | Add traceability nodes and edges after TASK-016 artifact paths are known. | resolved |
| WS-016-D | Depends on WS-016-A, WS-016-B and WS-016-C. | Validation and integration agent | Run local serving, browser checks and required gates, then record validation evidence. | resolved |

## Parallel Dispatch List

### Goal WS-016-A: Governance Chain Documents

- Owner role: Context-engine documentation agent.
- Objective: Create TASK-016 governance documents that preserve the Vision to
  Validation chain and describe manager visibility scope.
- Allowed files: `10_features/FEAT-004-manager-visibility.md`,
  `11_tasks/TASK-016-create-manager-visibility-interface.md`,
  `21_execution_plans/EP-TASK-016.md`,
  `22_goal_impact/GOAL-IMPACT-TASK-016.md`,
  `13_context_packages/CP-task-016.md`,
  `14_prompts/PROMPT-TASK-016-manager-visibility-interface.md`,
  `12_validation/VAL-TASK-016-manager-visibility-interface.md`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, backend services, production integrations and files
  containing secrets, customer data or raw production data.
- Required inputs: TASK-016 upstream links, goal impact, feature scope,
  validation pyramid, TASK-014 and TASK-015 context.
- Blockers: none identified in source artifacts.
- Validation evidence: documentation chain can be inspected and later validated
  by repository validation gates.
- Handoff output: list of governance files created or updated and remaining
  documentation gaps.

### Goal WS-016-B: Static Manager Interface

- Owner role: Frontend implementation agent.
- Objective: Create the local static manager-facing page for IPS status,
  traceability, retrieval comparison and validation evidence.
- Allowed files: `manager_interface/index.html`,
  `manager_interface/styles.css`, `manager_interface/app.js`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, backend services, production integrations and files
  containing secrets, customer data or raw production data.
- Required inputs: context package, execution plan, TASK-016 acceptance
  criteria, validation pyramid, TASK-014 and TASK-015 retrieval context.
- Blockers: none identified in source artifacts.
- Validation evidence: local static server response and desktop/mobile browser
  inspection in WS-016-D.
- Handoff output: interface files and notes about responsive behavior.

### Goal WS-016-C: Graph Traceability Entry

- Owner role: Graph documentation agent.
- Objective: Add TASK-016 graph entries for feature, task, execution plan,
  context package, coding prompt and validation report.
- Allowed files: `graph/project_graph.example.yaml`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, unrelated task files and source code.
- Required inputs: paths from TASK-016 governance documents and execution plan.
- Blockers: none identified in source artifacts.
- Validation evidence: repository validation in WS-016-D.
- Handoff output: graph diff and traceability notes.

### Goal WS-016-D: Final Validation And Evidence

- Owner role: Validation and integration agent.
- Objective: Validate the integrated TASK-016 interface, graph and documentation
  against the acceptance criteria and required gates.
- Allowed files: `12_validation/VAL-TASK-016-manager-visibility-interface.md`
  and terminal validation evidence.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, backend services, production integrations and files
  containing secrets, customer data or raw production data.
- Required inputs: completed WS-016-A, WS-016-B and WS-016-C outputs.
- Blockers: WS-016-A, WS-016-B and WS-016-C must be complete.
- Validation evidence: local static serving, desktop and mobile browser
  inspection, unit tests, repository validation, pre-coding gate and
  deployment-readiness gate for TASK-016.
- Handoff output: validation report with files changed, gates run, evidence and
  deviations.

## Parallel Agent Handoff Prompts

### Workstream WS-016-A

You are the TASK-016 governance-chain documentation agent. Create or update only
the TASK-016 governance and derived planning documents listed for WS-016-A.
Preserve the Vision to Validation chain, use only repository-local synthetic
examples and do not modify `00_constitution/CONSTITUTION.md` or
`01_vision/VISION.md`. Return files changed, documents created, missing
sections filled, remaining missing markers, validation notes, blockers and
deviations.

### Workstream WS-016-B

You are the TASK-016 frontend implementation agent. Create only
`manager_interface/index.html`, `manager_interface/styles.css` and
`manager_interface/app.js`. Build a static local manager-facing interface that
shows IPS status, traceability, retrieval comparison and validation evidence in
manager-readable language. Do not add a backend, production connection, live
document parser, secrets, customer data or raw production data. Return files
changed, responsive behavior notes, validation notes, blockers and deviations.

### Workstream WS-016-C

You are the TASK-016 graph traceability agent. Update only
`graph/project_graph.example.yaml` with TASK-016 feature, task, execution plan,
context package, coding prompt and validation report entries. Do not modify
protected vision or constitution files, unrelated task files or source code.
Return files changed, graph entries added, validation notes, blockers and
deviations.

### Workstream WS-016-D

You are the TASK-016 validation and integration agent. After WS-016-A,
WS-016-B and WS-016-C are complete, serve the static interface locally, inspect
desktop and mobile layouts, run the required gates and update only
`12_validation/VAL-TASK-016-manager-visibility-interface.md` with evidence.
Return files changed, tests run, validation evidence, blockers cleared,
integration notes and deviations.

## Test Plan

- Static server returns `manager_interface/index.html`.
- Browser inspection confirms readable desktop layout.
- Browser inspection confirms readable mobile layout.
- Repository gates pass.

## Validation Plan

Run local static serving, browser visual checks, unit tests, repository
validation, pre-coding gate and deployment-readiness gate for TASK-016.

## Gate Commands

```bash
python3 -m unittest discover -s tests
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-016
```

## Documentation Updates

Update TASK-016 task, goal impact, execution plan and validation report after
implementation.

## Rollback Plan

Remove the TASK-016 governance documents, manager interface files and graph
entries.

## Agent Handoff Prompt

Implement TASK-016 by adding a static manager-facing interface that explains IPS
traceability, retrieval comparison and validation status without changing
protected source-of-truth documents.

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
