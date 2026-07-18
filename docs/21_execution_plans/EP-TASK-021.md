# EP-TASK-021: Provider Promotion Thresholds

```yaml
id: EP-TASK-021
status: validated
source_task: ../11_tasks/TASK-021-add-provider-promotion-thresholds.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-021.md
coding_prompt: ../14_prompts/PROMPT-TASK-021-provider-promotion-thresholds.md
validation_report: ../12_validation/VAL-TASK-021-provider-promotion-thresholds.md
parallelization_strategy: single_agent
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: validates
replay_determinism_impact: required
required_gates:
  - focused-promotion-tests
  - provider-promotion-gate
  - provider-safety-gate
  - repository-validate
  - pre-coding
  - deployment-readiness
```

## Metadata

This execution plan adds provider promotion rules and a promotion gate.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-021.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
dry_run_contract: ../11_tasks/TASK-020-add-external-provider-dry-run-contract.md
```

## Goal Impact

The plan makes provider promotion criteria machine-checkable before any real
external provider is used.

## Project Invariants

- IPS-INV-001: promotion applies only to optional retrieval candidates.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation is bounded to promotion rules, gate script, tests
  and TASK-021 docs.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: promotion fixtures are synthetic and path-only.

## Sensitive-Data Handling

Classification: synthetic. Promotion rules and fixtures do not contain
credential values, raw production data or real customer data.

## Contract Validation Plan

Validate candidate mode, pass rate, failed cases, unexpected paths, provider
safety gate status, dry-run marker and network-call count.

## Replay/Determinism Plan

Use static baseline, candidate and promotion rule JSON inputs.

## Scope

Add provider promotion rules, dry-run candidate fixture, promotion gate, focused
tests, typecheck coverage and TASK-021 graph/governance documents.

## Non-Goals

- No real provider promotion.
- No provider network calls.
- No credentials.
- No retrieval ranking change.

## Parallelization Plan

This is an already implemented and validated single task. The source-backed
implementation surface is one promotion-gate slice: promotion rules, dry-run
fixture, gate logic, focused tests, typecheck coverage, graph traceability and
validation evidence. No independent parallel workstreams are source-supported
because splitting the rule config, gate script, fixture and tests would create
shared behavioral ownership without a separate contract or schema boundary.

### Ready-Now Parallel Goals

No multi-agent ready-now goals are source-supported for this task.

| Goal | Status | Owner role | Assigned files | Validation responsibility |
| --- | --- | --- | --- | --- |
| TASK-021-IMPL | ready now, single implementation/integration workstream | context-engine implementation agent | `config/provider_promotion_rules.json`, `scripts/provider_promotion_gate.py`, `tests/test_provider_promotion_gate.py`, `tests/fixtures/retrieval_candidate_dry_run.json`, `package.json`, `graph/project_graph.example.yaml`, TASK-021 documentation | focused promotion tests, promotion gate CLI, provider safety gate CLI, repository validation, pre-coding gate and deployment-readiness gate |

### Dependency-Gated Goals

No additional dependency-gated goals are source-supported. TASK-021 depends on
the completed TASK-020 external provider dry-run contract as an input, not as a
parallel workstream owned by this plan.

### Blockers

No open blockers remain. The TASK-020 dry-run contract, synthetic baseline
fixture and provider safety gate are required inputs and were available for the
validated implementation.

### Shared Files And Merge Order

No parallel merge order is required because the plan has one implementation and
integration owner. If replayed as a coding task, merge the single workstream in
this order:

1. Promotion rules and dry-run fixture.
2. Promotion gate and focused tests.
3. `package.json` validation coverage.
4. `graph/project_graph.example.yaml` and TASK-021 documentation.
5. Validation report evidence.

## Files to Inspect

- `scripts/context_package_generator.py`
- `scripts/embedding_provider_gate.py`
- `tests/fixtures/retrieval_baseline.json`
- `tests/fixtures/retrieval_candidate_dry_run.json`

## Files to Create

- `config/provider_promotion_rules.json`
- `scripts/provider_promotion_gate.py`
- `tests/test_provider_promotion_gate.py`
- TASK-021 task, goal impact, execution plan, context package, prompt and
  validation report.

## Files to Modify

- `package.json`
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Add promotion rule config.
2. Add dry-run candidate fixture.
3. Add promotion gate.
4. Add focused pass and fail tests.
5. Add typecheck coverage.
6. Update graph traceability.
7. Run repository gates.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| TASK-021-IMPL | Implement and validate provider promotion thresholds as one cohesive promotion-gate slice. | no; single-agent workstream only | context-engine implementation agent | `config/provider_promotion_rules.json`, `scripts/provider_promotion_gate.py`, `tests/test_provider_promotion_gate.py`, `tests/fixtures/retrieval_candidate_dry_run.json`, `package.json`, `graph/project_graph.example.yaml`, TASK-021 task, goal impact, execution plan, context package, prompt and validation report | promotion rules, executable promotion gate, dry-run fixture, focused tests, graph traceability and validation evidence | TASK-020 dry-run contract input |
| TASK-021-FINAL | Final integration and validation for the same single workstream. | no; final validation follows implementation | context-engine validation owner | validation commands and TASK-021 validation report | validation evidence and handoff summary | TASK-021-IMPL complete |

Separate Codex threads are not applicable for this execution plan because only
one implementation/integration workstream is source-supported. Running multiple
agents against the same rule config, gate script, fixture and tests would create
unnecessary file conflicts without additional validated scope.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| TASK-021-IMPL | TASK-020 external provider dry-run contract | context-engine agent | Use TASK-020 dry-run mode, safety and zero-network requirements as required inputs. | resolved |
| TASK-021-IMPL | Synthetic baseline and candidate fixtures | context-engine agent | Use static fixture JSON only; no production data, credentials or real provider outputs. | resolved |
| TASK-021-FINAL | Completed implementation workstream | context-engine validation owner | Run focused tests, provider gates and repository gates; record validation evidence. | resolved |

## Parallel Dispatch List

### Goal TASK-021-IMPL: Provider promotion thresholds implementation and validation

- Owner role: context-engine implementation and validation agent.
- Objective: add provider promotion thresholds and comparison rules so dry-run
  and future provider candidates can be promoted only after passing configured
  safety, comparison, dry-run and zero-network gates.
- Allowed files: `config/provider_promotion_rules.json`,
  `scripts/provider_promotion_gate.py`, `tests/test_provider_promotion_gate.py`,
  `tests/fixtures/retrieval_candidate_dry_run.json`, `package.json`,
  `graph/project_graph.example.yaml`, TASK-021 task, goal impact, execution
  plan, context package, prompt and validation report.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, credential files, real provider outputs, unrelated
  task ranges and unrelated architecture or ADR documents.
- Required inputs: TASK-021 task, GOAL-IMPACT-TASK-021, TASK-020 external
  provider dry-run contract, static retrieval baseline fixture and provider
  safety gate behavior.
- Blockers: none open; TASK-020 dry-run contract dependency is resolved.
- Validation evidence: focused promotion tests, provider promotion gate CLI,
  provider safety gate CLI, `npm run validate`, pre-coding gate and
  deployment-readiness gate for TASK-021.
- Handoff output: files changed, tests run, validation evidence, blockers
  encountered or cleared, integration notes, deviations and remaining
  documentation gaps.

## Parallel Agent Handoff Prompts

### Workstream TASK-021-IMPL

You are the TASK-021 provider promotion thresholds implementation and
validation agent for the Intent Preservation System. Work from
`../13_context_packages/CP-task-021.md` and preserve graph-first retrieval.

Objective: add provider promotion thresholds and comparison rules so a provider
candidate can graduate from experimental to approved candidate only after
passing configured safety, comparison, dry-run and zero-network gates.

Allowed files: `../../config/provider_promotion_rules.json`,
`../../scripts/provider_promotion_gate.py`,
`../../tests/test_provider_promotion_gate.py`,
`../../tests/fixtures/retrieval_candidate_dry_run.json`, `../../package.json`,
`../../graph/project_graph.example.yaml`, TASK-021 task, goal impact, execution
plan, context package, prompt and validation report.

Forbidden files: `../00_constitution/CONSTITUTION.md`,
`../01_vision/VISION.md`, credential files, real provider outputs, unrelated
task ranges and unrelated architecture or ADR documents.

Required inputs: TASK-020 external provider dry-run contract, TASK-021 task,
GOAL-IMPACT-TASK-021, static retrieval baseline fixture and provider safety
gate behavior.

Blockers: none open. Do not split this workstream across agents unless a future
plan creates independent ownership boundaries.

Validation commands:

```bash
python3 -m unittest tests.test_provider_promotion_gate
python3 scripts/provider_promotion_gate.py --root . --baseline tests/fixtures/retrieval_baseline.json --candidate tests/fixtures/retrieval_candidate_dry_run.json --provider external-provider-dry-run
python3 scripts/embedding_provider_gate.py --root .
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-021
```

Expected handoff output: files changed, tests run, validation evidence, blockers
encountered or cleared, dependencies, integration notes, deviations and
remaining documentation gaps.

## Test Plan

- Promotion gate passes dry-run candidate.
- Promotion gate fails failed comparison.
- Promotion gate fails missing dry-run or nonzero network calls.
- Promotion gate fails candidate mode mismatch.

## Validation Plan

Run focused promotion tests, promotion gate CLI, provider gate CLI,
`npm run validate`, pre-coding gate and deployment-readiness gate for TASK-021.

## Gate Commands

```bash
python3 -m unittest tests.test_provider_promotion_gate
python3 scripts/provider_promotion_gate.py --root . --baseline tests/fixtures/retrieval_baseline.json --candidate tests/fixtures/retrieval_candidate_dry_run.json --provider external-provider-dry-run
python3 scripts/embedding_provider_gate.py --root .
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-021
```

## Documentation Updates

Update TASK-021 task, goal impact, execution plan and validation report after
implementation.

## Rollback Plan

Remove promotion rules, promotion gate, dry-run candidate fixture, tests and
TASK-021 graph and governance documents.

## Agent Handoff Prompt

Implement TASK-021 by adding provider promotion thresholds and comparison rules
for dry-run and future provider candidates.

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
