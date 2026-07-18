# EP-TASK-020: External Provider Dry-Run Contract

```yaml
id: EP-TASK-020
status: validated
source_task: ../11_tasks/TASK-020-add-external-provider-dry-run-contract.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-020.md
coding_prompt: ../14_prompts/PROMPT-TASK-020-external-provider-dry-run-contract.md
validation_report: ../12_validation/VAL-TASK-020-external-provider-dry-run-contract.md
parallelization_strategy: single_agent
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: validates
replay_determinism_impact: required
required_gates:
  - focused-tests
  - provider-gate
  - dry-run-candidate-cli
  - repository-validation
  - pre-coding
  - deployment-readiness
```

## Metadata

This execution plan adds a dry-run contract for future external embedding
providers.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-020.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
provider_gates: ../11_tasks/TASK-019-add-embedding-provider-safety-gates.md
```

## Goal Impact

The plan validates provider flow shape before any real external provider can
receive repository text.

## Project Invariants

- IPS-INV-001: dry-run retrieval remains optional.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation is bounded to dry-run provider config, generator
  mode, tests and TASK-020 docs.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: dry-run fixtures are synthetic and path-only.

## Sensitive-Data Handling

Classification: synthetic. Dry-run candidate output uses baseline fixture paths
only and does not read repository document body text.

## Contract Validation Plan

Validate output keys `retrieval_mode`, `embedding_provider`, `dry_run`,
`network_calls` and candidate `returned_optional_paths` through focused tests
and the existing comparison harness.

## Replay/Determinism Plan

Use baseline fixture expectations to produce deterministic dry-run candidates.

## Scope

Modify provider registry, provider safety gate, context package generator and
focused tests. Add TASK-020 governance and graph traceability.

## Non-Goals

- No real external provider.
- No credentials.
- No network calls.
- No repository text transmission.

## Parallelization Plan

TASK-020 is an already implemented and validated single task. The source-backed
scope crosses provider configuration, provider safety policy, candidate
generation, focused tests, graph traceability and validation evidence for one
contract. No independent implementation workstream is source-supported because
splitting the provider gate, generator mode and compatibility tests would create
shared contract and validation-order coupling.

Separate-thread parallel execution is not applicable for the original
implementation. The source-backed dispatch is a single implementation and
integration workstream with one validation owner.

### Ready-Now Parallel Goals

- WS-020-IMPLEMENTATION-INTEGRATION: ready now as a single-agent implementation,
  integration and validation workstream.

No additional ready-now parallel goals are source-supported.

### Dependency-Gated Goals

- Real external provider integration: dependency-gated on future approved work
  outside TASK-020, including credentials, provider-specific contracts and
  data-movement review.

### Blockers

- No blockers remain for TASK-020; the validation report records the task as
  accepted and validated.
- Future real-provider work is blocked by a separate approved execution plan,
  provider credentials, external API contract review and sensitive-data review.

### Shared Files And Merge Order

The TASK-020 implementation touched files that share one contract surface:
provider registry, provider safety policy, provider gate, candidate generator,
focused tests and graph traceability. Because only one source-backed workstream
exists, there is no parallel merge order.

If future maintenance splits the work, merge order must be:

1. Provider registry and safety policy.
2. Provider gate behavior.
3. Candidate generator dry-run mode.
4. Focused tests and validation evidence.
5. Graph traceability and TASK-020 documentation.

## Files to Inspect

- `config/embedding_provider_gates.json`
- `23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- `scripts/embedding_provider_gate.py`
- `scripts/context_package_generator.py`
- `tests/test_embedding_provider_gate.py`
- `tests/test_context_package_generator.py`

## Files to Create

- TASK-020 task, goal impact, execution plan, context package, prompt and
  validation report.

## Files to Modify

- `config/embedding_provider_gates.json`
- `23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- `scripts/embedding_provider_gate.py`
- `scripts/context_package_generator.py`
- `tests/test_embedding_provider_gate.py`
- `tests/test_context_package_generator.py`
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

Single-agent workstream WS-020-IMPLEMENTATION-INTEGRATION:

1. Add dry-run provider registry entry.
2. Add dry-run provider safety rules.
3. Add dry-run candidate generation mode.
4. Add focused tests for dry-run pass and failure behavior.
5. Validate dry-run CLI output.
6. Update graph traceability.
7. Run repository gates.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-020-IMPLEMENTATION-INTEGRATION | Add and validate the offline external-provider dry-run contract. | no; single source-backed workstream | context-engine implementation and validation agent | `config/embedding_provider_gates.json`; `23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`; `scripts/embedding_provider_gate.py`; `scripts/context_package_generator.py`; `tests/test_embedding_provider_gate.py`; `tests/test_context_package_generator.py`; `graph/project_graph.example.yaml`; TASK-020 documentation and validation artifacts | Dry-run provider registry, gate rules, candidate mode, focused tests, graph traceability and validation evidence | none |

Separate Codex thread execution is not applicable because the only
source-backed workstream owns shared contract behavior and final validation.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-020-IMPLEMENTATION-INTEGRATION | TASK-019 provider safety gates must exist before dry-run provider validation. | context-engine-agent | Use `../11_tasks/TASK-019-add-embedding-provider-safety-gates.md` and existing provider gate files as inputs. | resolved |
| WS-020-IMPLEMENTATION-INTEGRATION | Real external provider calls, credentials and repository text transmission are outside this task. | future integration owner | Create a separate approved execution plan before real provider work. | not applicable to TASK-020 |

## Parallel Dispatch List

### Goal WS-020-IMPLEMENTATION-INTEGRATION: External Provider Dry-Run Contract

- Owner role: context-engine implementation and validation agent.
- Objective: add a dry-run external provider contract that validates provider
  configuration, candidate result shape and comparison compatibility without
  network calls or repository text transmission.
- Allowed files: `config/embedding_provider_gates.json`,
  `23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`,
  `scripts/embedding_provider_gate.py`, `scripts/context_package_generator.py`,
  `tests/test_embedding_provider_gate.py`,
  `tests/test_context_package_generator.py`, `graph/project_graph.example.yaml`
  and TASK-020 task, goal-impact, execution-plan, context-package, prompt and
  validation documents.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, credential files, production data and unrelated task
  ranges.
- Required inputs: TASK-020 task, GOAL-IMPACT-TASK-020, TASK-019 provider
  safety gates, provider registry, provider safety policy, provider gate,
  context package generator, focused tests and retrieval baseline fixture.
- Blockers: none for validated TASK-020; future real-provider work requires a
  separate approved plan and data-protection review.
- Validation evidence: focused unittest command, provider gate CLI, dry-run
  candidate CLI, `npm run validate`, pre-coding gate and deployment-readiness
  gate, as recorded in
  `../12_validation/VAL-TASK-020-external-provider-dry-run-contract.md`.
- Handoff output: files changed, tests run, validation evidence, blockers or
  dependencies, integration notes, deviations and remaining documentation gaps.

## Parallel Agent Handoff Prompts

### Workstream WS-020-IMPLEMENTATION-INTEGRATION

You are the context-engine implementation and validation agent for TASK-020.
Implement the external-provider dry-run contract only. Use the TASK-020 task,
goal-impact document, execution plan and context package as source material.
Modify only the allowed files listed for this workstream. Do not modify
`00_constitution/CONSTITUTION.md`, `01_vision/VISION.md`, credential files,
production data or unrelated task ranges.

Add the offline dry-run provider registry entry, dry-run provider safety rules,
dry-run candidate generation mode, focused tests and graph traceability. The
dry-run output must identify `external-provider-dry-run`, set `dry_run: true`,
report `network_calls: 0` and compare through the existing candidate harness
without reading repository document body text.

Validate with focused tests, provider gate CLI, dry-run candidate CLI,
repository validation, pre-coding gate and deployment-readiness gate. Return
files changed, validation evidence, blockers, dependencies, integration notes,
deviations and remaining documentation gaps.

## Test Plan

- Provider gate accepts offline dry-run provider.
- Provider gate rejects networked or credentialed dry-run provider.
- Dry-run candidate output compares against baseline.
- Dry-run candidate output does not require repository document text.

## Validation Plan

Run focused tests, provider gate, dry-run candidate CLI, `npm run validate`,
pre-coding gate and deployment-readiness gate for TASK-020.

## Gate Commands

```bash
python3 -m unittest tests.test_context_package_generator tests.test_embedding_provider_gate
python3 scripts/embedding_provider_gate.py --root .
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode external-provider-dry-run --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-020
```

## Documentation Updates

Update TASK-020 task, goal impact, execution plan, context package, coding
prompt and validation report after implementation.

## Rollback Plan

Remove dry-run provider registry entry, gate rules, candidate mode, tests and
TASK-020 graph and governance documents.

## Agent Handoff Prompt

Final integration handoff is the single source-backed workstream prompt listed
under Parallel Agent Handoff Prompts.

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
