# EP-TASK-019: Embedding Provider Safety Gates

```yaml
id: EP-TASK-019
status: validated
source_task: ../11_tasks/TASK-019-add-embedding-provider-safety-gates.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-019.md
coding_prompt: ../14_prompts/PROMPT-TASK-019-embedding-provider-safety-gates.md
validation_report: ../12_validation/VAL-TASK-019-embedding-provider-safety-gates.md
parallelization_strategy: single_agent
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: validates
replay_determinism_impact: required
required_gates:
  - provider-gate-tests
  - provider-gate-cli
  - repository-validate
  - pre-coding
  - deployment-readiness
```

## Metadata

This execution plan adds safety gates for future embedding providers.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-019.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
sensitive_data_policy: ../23_documentation_contracts/SENSITIVE_DATA_POLICY.md
```

## Goal Impact

The plan adds executable safety checks before any real embedding provider can be
introduced.

## Project Invariants

- IPS-INV-001: provider-backed retrieval remains optional.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation is bounded to provider safety policy, registry,
  gate script, tests and TASK-019 docs.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: registry examples use references only and no secrets.

## Sensitive-Data Handling

Classification: synthetic. The registry stores provider ids and references
only. It does not store credential values.

## Contract Validation Plan

Validate the provider registry through `scripts/embedding_provider_gate.py`.
Reject sensitive classification, credential-looking values and unapproved
external providers.

## Replay/Determinism Plan

The gate reads static JSON and repository-local documents, then writes a
deterministic JSON report for the same input state.

## Scope

Add provider safety policy, registry, gate script, tests, typecheck coverage and
TASK-019 governance documents.

## Non-Goals

- No external provider implementation.
- No real credentials.
- No secret manager integration.
- No retrieval contract change.

## Parallelization Plan

This is an already implemented and validated single task. The source-backed
scope is one implementation/integration workstream for provider safety gates.
No independent parallel workstreams are supported because the policy, registry,
gate script, tests, package validation hook and graph traceability form one
shared validation surface.

### Ready-Now Parallel Goals

None. The only source-supported goal is `WS-019`, a standalone
implementation/integration workstream that owns the complete TASK-019 safety
gate slice and has already been validated.

### Dependency-Gated Goals

None. TASK-019 depends on the completed TASK-018 provider adapter boundary and
the sensitive-data policy context, both of which are listed as upstream inputs.
No later TASK-019 workstream is gated behind another parallel workstream.

### Blockers

No open blockers remain. Historical dependencies were:

- TASK-018 provider adapter boundary available as
  `../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md`.
- Sensitive-data handling rules available as
  `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`.
- Validation evidence recorded in
  `../12_validation/VAL-TASK-019-embedding-provider-safety-gates.md`.

### Shared Files And Merge Order

No multi-agent merge order is required. If this plan were re-run, `WS-019`
would be the sole owner and integration owner for:

- `23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- `config/embedding_provider_gates.json`
- `scripts/embedding_provider_gate.py`
- `tests/test_embedding_provider_gate.py`
- `package.json`
- `graph/project_graph.example.yaml`
- TASK-019 task, goal impact, execution plan, context package, prompt and
  validation report

## Files to Inspect

- `23_documentation_contracts/SENSITIVE_DATA_POLICY.md`
- `scripts/pre_coding_gate.py`
- `scripts/deployment_readiness_gate.py`
- `11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md`

## Files to Create

- `23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- `config/embedding_provider_gates.json`
- `scripts/embedding_provider_gate.py`
- `tests/test_embedding_provider_gate.py`
- TASK-019 task, goal impact, execution plan, context package, prompt and
  validation report.

## Files to Modify

- `package.json`
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Add provider safety policy.
2. Add local provider registry with no credentials.
3. Add dependency-free provider gate.
4. Add focused tests for pass and fail cases.
5. Add the new gate to typecheck coverage.
6. Update graph traceability.
7. Run repository gates and update validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-019 | Implement and validate the complete embedding provider safety gate slice. | No; standalone single-agent workstream. | Context engine implementation agent. | `23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`, `config/embedding_provider_gates.json`, `scripts/embedding_provider_gate.py`, `tests/test_embedding_provider_gate.py`, `package.json`, `graph/project_graph.example.yaml`, TASK-019 governance and validation artifacts. | Provider safety policy, registry, deterministic gate, tests, validation hook, graph traceability and validation report. | None beyond upstream TASK-018 and sensitive-data policy inputs. |

Separate Codex thread dispatch is not applicable for TASK-019 because the
source-supported work is one validated workstream with shared files and one
validation owner.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-019 | TASK-018 provider adapter boundary. | Context engine agent. | Read `../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md` before implementing provider gates. | resolved |
| WS-019 | Sensitive-data policy. | Context engine agent. | Apply `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`; keep registry examples synthetic and secret-free. | resolved |
| WS-019 | Provider safety validation evidence. | Context engine agent. | Run focused tests, provider gate CLI, repository validation, pre-coding gate and deployment-readiness gate. | resolved |

## Parallel Dispatch List

### Goal WS-019: Embedding Provider Safety Gates

- Owner role: context engine implementation and validation agent.
- Objective: implement the complete TASK-019 provider safety gate slice while
  preserving optional graph-first retrieval and preventing unsafe external
  provider rollout.
- Allowed files:
  `23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`,
  `config/embedding_provider_gates.json`,
  `scripts/embedding_provider_gate.py`,
  `tests/test_embedding_provider_gate.py`, `package.json`,
  `graph/project_graph.example.yaml`, TASK-019 task, goal impact, execution
  plan, context package, prompt and validation report.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, real credential stores, production data samples and
  unrelated task artifacts.
- Required inputs: TASK-019 task, GOAL-IMPACT-TASK-019, TASK-018 provider
  adapter boundary, sensitive-data policy and graph-first retrieval ADR.
- Blockers: none open; TASK-018 and sensitive-data policy dependencies are
  resolved inputs.
- Validation evidence: `python3 -m unittest tests.test_embedding_provider_gate`,
  `python3 scripts/embedding_provider_gate.py --root .`, `npm run validate`,
  `python3 scripts/pre_coding_gate.py --root .` and
  `python3 scripts/deployment_readiness_gate.py --root . --target TASK-019`.
- Handoff output: files changed, tests run, validation evidence, blockers,
  integration notes, deviations and remaining documentation gaps.

## Parallel Agent Handoff Prompts

### Workstream WS-019

You are the TASK-019 context engine implementation agent for the Intent
Preservation System. Implement the complete embedding provider safety gate
slice from `../21_execution_plans/EP-TASK-019.md`.

Allowed files are
`../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`,
`../../config/embedding_provider_gates.json`,
`../../scripts/embedding_provider_gate.py`,
`../../tests/test_embedding_provider_gate.py`, `../../package.json`,
`../../graph/project_graph.example.yaml` and TASK-019 governance/validation
artifacts. Do not modify `../00_constitution/CONSTITUTION.md`,
`../01_vision/VISION.md`, unrelated task artifacts, credential stores or
production data samples.

Read TASK-019, GOAL-IMPACT-TASK-019, TASK-018 provider adapter boundary,
`../23_documentation_contracts/SENSITIVE_DATA_POLICY.md` and
`../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`. Add the provider
safety policy, local provider registry, dependency-free deterministic gate,
focused pass/fail tests, validation hook and graph traceability. Validate with
focused tests, provider gate CLI, `npm run validate`, pre-coding gate and
deployment-readiness gate for TASK-019. Return changed files, validation
evidence, blockers, integration notes, deviations and remaining documentation
gaps.

## Test Plan

- Provider gate passes local provider config.
- Provider gate fails missing registry.
- Provider gate fails unknown active provider.
- Provider gate fails credential values.
- Provider gate fails sensitive classification.
- Provider gate fails unapproved external network provider.

## Validation Plan

Run focused gate tests, provider gate CLI, `npm run validate`, pre-coding gate
and deployment-readiness gate for TASK-019.

## Gate Commands

```bash
python3 -m unittest tests.test_embedding_provider_gate
python3 scripts/embedding_provider_gate.py --root .
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-019
```

## Documentation Updates

Update TASK-019 task, goal impact, execution plan and validation report after
implementation.

## Rollback Plan

Remove provider safety policy, registry, gate script, tests and TASK-019 graph
and governance documents.

## Agent Handoff Prompt

Implement TASK-019 by adding credential, environment and sensitive-data gates
for future embedding providers.

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
