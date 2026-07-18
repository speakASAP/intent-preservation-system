# EP-TASK-022: Provider Status Manager Interface

```yaml
id: EP-TASK-022
status: validated
source_task: ../11_tasks/TASK-022-surface-provider-status-in-manager-interface.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-022.md
coding_prompt: ../14_prompts/PROMPT-TASK-022-provider-status-manager-interface.md
validation_report: ../12_validation/VAL-TASK-022-provider-status-manager-interface.md
parallelization_strategy: single_agent
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: none
replay_determinism_impact: required
required_gates:
  - provider-safety
  - provider-promotion
  - repository-validation
  - pre-coding
  - deployment-readiness
```

## Metadata

This execution plan extends the static manager interface with provider safety
gate and promotion status.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
feature: ../10_features/FEAT-004-manager-visibility.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-022.md
provider_safety_task: ../11_tasks/TASK-019-add-embedding-provider-safety-gates.md
provider_promotion_task: ../11_tasks/TASK-021-add-provider-promotion-thresholds.md
```

## Goal Impact

The plan makes provider gate and promotion state visible in the manager
interface while preserving the existing optional retrieval boundary.

## Project Invariants

- IPS-INV-001: provider state remains optional retrieval evidence.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation is scoped to manager interface files and
  TASK-022 documentation.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: status text uses synthetic config and fixture metadata only.

## Sensitive-Data Handling

Classification: synthetic. The interface shows provider ids, dry-run status,
network-call count and gate outcomes only.

## Contract Validation Plan

Do not change provider gate schemas. Validate that the provider safety gate and
promotion gate still pass after the manager-interface update.

## Replay/Determinism Plan

Use static interface content derived from committed provider gate, promotion
rule and dry-run fixture artifacts.

## Scope

Add a provider status panel, provider metric card, navigation entry, provider
gate evidence cards and manager-mode comparison graphics to the existing static
manager interface.

## Non-Goals

- No live repository parsing.
- No external provider calls.
- No credentials.
- No promotion of a real external provider.
- No changes to provider gate logic.

## Parallelization Plan

TASK-022 is an already implemented and validated single task. The source task,
goal impact and original execution plan support one integrated implementation
and validation workstream because the manager interface files and graph
traceability are shared outputs of the same provider-status readout.

Separate parallel implementation agents are not source-supported for this task:
splitting `manager_interface/index.html`, `manager_interface/styles.css`,
`manager_interface/app.js` and `graph/project_graph.example.yaml` would create
coordination overhead without an independent goal boundary.

### Ready-Now Parallel Goals

- None. The source-backed executable unit is a single implementation and
  validation workstream for TASK-022.

### Dependency-Gated Goals

- None. TASK-022 depends on completed upstream work from TASK-016, TASK-019 and
  TASK-021, all of which are required inputs rather than additional TASK-022
  workstreams.

### Blockers

- None for the validated implementation. If the task were reopened, the agent
  must preserve the existing provider safety and promotion gate meanings and
  avoid external provider calls or credentials.

### Shared Files And Merge Order

- Shared files: `manager_interface/index.html`,
  `manager_interface/styles.css`, `manager_interface/app.js` and
  `graph/project_graph.example.yaml`.
- Merge order: single implementation agent edits the manager interface files
  first, updates graph traceability after the interface scope is known, then
  runs the provider and repository gates. No parallel merge order is applicable
  because no independent parallel workstreams are declared.

## Files to Inspect

- `manager_interface/index.html`
- `manager_interface/styles.css`
- `manager_interface/app.js`
- `config/embedding_provider_gates.json`
- `config/provider_promotion_rules.json`
- `tests/fixtures/retrieval_candidate_dry_run.json`

## Files to Create

- `11_tasks/TASK-022-surface-provider-status-in-manager-interface.md`
- `21_execution_plans/EP-TASK-022.md`
- `22_goal_impact/GOAL-IMPACT-TASK-022.md`
- `13_context_packages/CP-task-022.md`
- `14_prompts/PROMPT-TASK-022-provider-status-manager-interface.md`
- `12_validation/VAL-TASK-022-provider-status-manager-interface.md`

## Files to Modify

- `manager_interface/index.html`
- `manager_interface/styles.css`
- `manager_interface/app.js`
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Add provider status data and renderer to `manager_interface/app.js`.
2. Add provider navigation, metric and panel markup.
3. Add manager-mode comparison graphics with scorecards, arrows and drift bars.
4. Add TASK-022 governance artifacts and graph traceability.
5. Run provider and repository gates.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-022-implementation-validation | Surface provider gate and promotion status in the manager interface and validate TASK-022. | no | single implementation/integration agent | `manager_interface/index.html`, `manager_interface/styles.css`, `manager_interface/app.js`, `graph/project_graph.example.yaml`, TASK-022 governance artifacts | Manager-visible provider status, graph traceability and validation evidence | TASK-016 manager interface, TASK-019 provider safety gates and TASK-021 promotion thresholds must already exist. |

Separate Codex thread execution is not applicable because the only
source-backed TASK-022 workstream owns shared UI files and final validation.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-022-implementation-validation | TASK-016 manager interface pattern | context-engine-agent | Use the existing static manager interface structure as the extension point. | resolved |
| WS-022-implementation-validation | TASK-019 provider safety gates | context-engine-agent | Consume existing provider safety gate status without changing gate semantics. | resolved |
| WS-022-implementation-validation | TASK-021 provider promotion thresholds | context-engine-agent | Consume existing promotion thresholds without promoting a real provider. | resolved |
| WS-022-implementation-validation | External provider credentials and live calls are forbidden | implementation agent | Keep provider status static and synthetic; do not add credentials or network calls. | not applicable |

## Parallel Dispatch List

### Goal WS-022-implementation-validation: Provider Status Manager Interface

- Owner role: single implementation/integration agent.
- Objective: surface active provider, dry-run provider safety gate, promotion
  status and network-boundary evidence in the existing static manager
  interface, then validate TASK-022.
- Allowed files: `manager_interface/index.html`,
  `manager_interface/styles.css`, `manager_interface/app.js`,
  `graph/project_graph.example.yaml` and TASK-022 governance artifacts.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, provider gate logic, promotion gate logic,
  credentials and sensitive data.
- Required inputs: TASK-016 manager interface, TASK-019 provider safety gates,
  TASK-021 provider promotion thresholds,
  `config/embedding_provider_gates.json`,
  `config/provider_promotion_rules.json` and
  `tests/fixtures/retrieval_candidate_dry_run.json`.
- Blockers: none for the validated implementation; live provider calls,
  credentials and real provider promotion remain forbidden.
- Validation evidence: provider safety gate, provider promotion gate,
  `npm run validate`, pre-coding gate and deployment-readiness gate output.
- Handoff output: files changed, validation evidence, blockers encountered or
  cleared, dependencies, integration notes, deviations and remaining
  documentation gaps.

## Parallel Agent Handoff Prompts

### Workstream WS-022-implementation-validation

You are the single implementation/integration agent for TASK-022. Extend the
existing static manager interface to show active provider status, dry-run
provider safety gate status, provider promotion status and the zero-network
boundary. Use the TASK-016 manager interface pattern and consume the existing
TASK-019 and TASK-021 provider artifacts without changing their semantics.

Allowed files are `manager_interface/index.html`,
`manager_interface/styles.css`, `manager_interface/app.js`,
`graph/project_graph.example.yaml` and TASK-022 governance artifacts. Do not
modify `00_constitution/CONSTITUTION.md`, `01_vision/VISION.md`, provider gate
logic, promotion gate logic, credentials or sensitive data. Validate with the
provider safety gate, provider promotion gate, `npm run validate`, pre-coding
gate and deployment-readiness gate. Return files changed, validation evidence,
blockers, dependencies, integration notes, deviations and remaining
documentation gaps.

## Test Plan

- Open the static interface and verify provider status content exists in the
  DOM.
- Toggle Manager and Technical comparison modes and verify Manager shows visual
  graphics while Technical shows the evidence table.
- Run provider safety gate.
- Run provider promotion gate against the dry-run fixture.
- Run repository validation gates.

## Validation Plan

Run provider safety gate, provider promotion gate, `npm run validate`,
pre-coding gate and deployment-readiness gate for TASK-022.

## Gate Commands

```bash
python3 scripts/embedding_provider_gate.py --root .
python3 scripts/provider_promotion_gate.py --root . --baseline tests/fixtures/retrieval_baseline.json --candidate tests/fixtures/retrieval_candidate_dry_run.json --provider external-provider-dry-run
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-022
```

## Documentation Updates

Add TASK-022 task, goal impact, execution plan, context package, prompt and
validation report. Update the example graph with TASK-022 traceability.

## Rollback Plan

Remove TASK-022 manager-interface additions and TASK-022 governance artifacts.

## Agent Handoff Prompt

All implementation instructions are listed under Parallel Agent Handoff
Prompts. This is a single implementation/integration workstream, not a
multi-agent parallel wave.

## Completion Checklist

- [x] Implementation complete
- [x] Parallelizable workstreams identified
- [x] Blockers and serial dependencies documented
- [x] Agent handoff prompts created for independent workstreams or documented
      as not applicable
- [x] Integration order documented
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
