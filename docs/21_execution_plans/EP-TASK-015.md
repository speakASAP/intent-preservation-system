# EP-TASK-015: Local Semantic Candidate Adapter

```yaml
id: EP-TASK-015
status: validated
source_task: ../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-015.md
coding_prompt: ../14_prompts/PROMPT-TASK-015-local-semantic-candidate-adapter.md
validation_report: ../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md
parallelization_strategy: parallel_goals
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: validates
replay_determinism_impact: required
required_gates:
  - focused-tests
  - candidate-generation
  - candidate-comparison
  - repository-validation
  - pre-coding
  - deployment-readiness
```

## Metadata

This execution plan defined a local candidate adapter shape before real
embedding or vector-search integration and has been validated by
`../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-015.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan creates a candidate adapter contract future semantic providers can
reuse while keeping the current implementation deterministic and local.

## Project Invariants

- IPS-INV-001: candidate output remains traceable to baseline case ids.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation stays bounded to local candidate generation.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: candidate fixtures use synthetic repository-local data only.

## Sensitive-Data Handling

Classification: synthetic. The adapter reads repository Markdown and baseline
fixtures only.

## Contract Validation Plan

Generate TASK-014-compatible candidate JSON with `retrieval_mode` and `cases`
containing `id` and `returned_optional_paths`.

| Contract or schema | Impact | Validator/command | Evidence path | Owner |
|---|---|---|---|---|
| TASK-014 candidate comparison result shape | validates | `python3 scripts/context_package_generator.py --root . --compare-retrieval-candidate tests/fixtures/retrieval_baseline.json --candidate-results tests/fixtures/retrieval_candidate.json --pretty` | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` | context-engine-agent |

## Replay/Determinism Plan

Use deterministic token overlap and stable path tie-breaking. Tests compare
repeated output.

| Behavior | Required? | Validation method | Evidence path |
|---|---|---|---|
| Replay | yes | Generate candidate results from the fixed baseline fixture and compare through TASK-014 harness. | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` |
| Idempotency | yes | Run focused context-package tests against deterministic candidate output. | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` |
| Deterministic output | yes | Tests compare repeated output from deterministic token overlap and stable path tie-breaking. | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` |

## Scope

Add local semantic-style candidate generation to
`scripts/context_package_generator.py` and focused tests.

## Non-Goals

- No embeddings.
- No vector database.
- No external API calls.
- No graph-required context replacement.

## Parallelization Plan

TASK-015 is validated, so no implementation dispatch remains open. For replay,
audit, or future re-execution, the work decomposes into parallel goals after
the TASK-014 candidate comparison contract and baseline fixture are read:

- local candidate adapter implementation;
- focused tests and comparison compatibility validation;
- final documentation, gate execution and validation evidence update.

The final documentation and gate workstream is integration-owned because it
records evidence from the implementation and test workstreams.

### Ready-Now Parallel Goals

For a re-execution of this validated plan, these goals can start immediately
after the shared inputs listed below are read.

| Goal | Owner role | Allowed files | Validation responsibility | Status |
|---|---|---|---|---|
| WS-015-A local adapter implementation | context-engine implementation agent | `scripts/context_package_generator.py` | Candidate generation CLI emits TASK-014-compatible JSON from `tests/fixtures/retrieval_baseline.json`. | validated |
| WS-015-B focused tests and comparison compatibility | context-engine test agent | `tests/test_context_package_generator.py` | `python3 -m unittest tests.test_context_package_generator` and TASK-014 comparison command. | validated |

### Dependency-Gated Goals

| Goal | Dependency | Owner role | Status |
|---|---|---|---|
| WS-015-C final documentation and gate integration | Requires outputs from WS-015-A and WS-015-B. | integration and validation agent | validated |

### Blockers

No current blockers remain for TASK-015 because implementation and validation
are complete. During re-execution, WS-015-C is dependency-gated on validation
evidence from WS-015-A and WS-015-B.

### Shared Files And Merge Order

| Shared file or contract | Workstreams | Integration owner | Merge/review order |
|---|---|---|---|
| TASK-014 candidate result shape: `retrieval_mode`, `cases`, `id`, `returned_optional_paths` | WS-015-A, WS-015-B, WS-015-C | context-engine-agent | Confirm contract in WS-015-A, validate in WS-015-B, record evidence in WS-015-C. |
| `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` | WS-015-C | context-engine-agent | Update only after WS-015-A and WS-015-B evidence is available. |
| TASK-015 documentation set | WS-015-C | context-engine-agent | Update after implementation and test changes are merged. |

## Files to Inspect

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `tests/fixtures/retrieval_baseline.json`
- `11_tasks/TASK-014-compare-candidate-retrieval-results.md`

## Files to Create

- TASK-015 documentation, context package, prompt and validation report.

## Files to Modify

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `graph/project_graph.example.yaml`
- TASK-015 documents after validation.

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

Parallel wave 1:

1. WS-015-A: add local candidate generation from baseline cases.
2. WS-015-A: use deterministic token overlap over candidate document titles and bodies.
3. WS-015-A: return TASK-014-compatible candidate result JSON.
4. WS-015-A: add CLI support.
5. WS-015-B: add focused tests for successful candidate generation,
   comparison compatibility and deterministic output.

Integration wave:

6. WS-015-B: validate generated candidates through candidate comparison.
7. WS-015-C: run repository gates and update validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-015-A | Implement deterministic local candidate generation and CLI support. | yes, for re-execution | context-engine implementation agent | `scripts/context_package_generator.py` | TASK-014-compatible candidate JSON generation from baseline cases. | Shared TASK-014 candidate result shape. |
| WS-015-B | Add and run focused tests plus candidate comparison compatibility checks. | yes, for re-execution after reading shared contract | context-engine test agent | `tests/test_context_package_generator.py` | Passing focused tests and comparison evidence. | Candidate CLI behavior from WS-015-A for final validation. |
| WS-015-C | Integrate evidence, run repository gates and update TASK-015 documentation. | no, dependency-gated final integration | integration and validation agent | TASK-015 documentation, context package, prompt and validation report | Validated documentation and gate evidence. | WS-015-A and WS-015-B outputs. |

Separate Codex thread execution is not required for the current repository state
because TASK-015 is already validated. If this plan is replayed, WS-015-A and
WS-015-B should be opened in separate Codex threads, then WS-015-C should run
after both handoffs are available.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-015-A | TASK-014 candidate comparison shape and baseline fixture must be preserved. | context-engine implementation agent | Read TASK-014, EP-TASK-014 and `tests/fixtures/retrieval_baseline.json` before editing. | resolved |
| WS-015-B | Final comparison validation depends on candidate CLI behavior from WS-015-A. | context-engine test agent | Add focused tests and run comparison after WS-015-A is available. | resolved |
| WS-015-C | Final documentation and gates depend on implementation and test evidence. | integration and validation agent | Record evidence in TASK-015 validation artifacts after WS-015-A and WS-015-B pass. | resolved |

## Parallel Dispatch List

### Goal WS-015-A: Local Candidate Adapter Implementation

- Owner role: context-engine implementation agent
- Objective: add deterministic local semantic-style candidate generation from a
  baseline file without embeddings, vector databases or external API calls.
- Allowed files: `scripts/context_package_generator.py`
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, external provider integration files, vector database
  configuration and production data fixtures.
- Required inputs: TASK-015, EP-TASK-015, TASK-014, EP-TASK-014,
  `tests/fixtures/retrieval_baseline.json` and TASK-014 candidate result shape.
- Blockers: none currently; preserve the TASK-014 candidate result fields.
- Validation evidence: candidate generation CLI output from
  `python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --pretty`.
- Handoff output: implementation summary, generated candidate output evidence,
  dependencies for tests and deviations.

### Goal WS-015-B: Focused Tests And Comparison Compatibility

- Owner role: context-engine test agent
- Objective: prove candidate generation is deterministic and compatible with
  TASK-014 comparison.
- Allowed files: `tests/test_context_package_generator.py`
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, production data fixtures and external service mocks.
- Required inputs: TASK-015, EP-TASK-015, TASK-014, EP-TASK-014,
  `tests/fixtures/retrieval_baseline.json`, candidate CLI behavior from
  WS-015-A.
- Blockers: final comparison evidence depends on WS-015-A candidate generation.
- Validation evidence: `python3 -m unittest tests.test_context_package_generator`
  and the TASK-014 comparison command.
- Handoff output: test summary, comparison evidence, unresolved failures and
  deviations.

### Goal WS-015-C: Final Documentation And Gate Integration

- Owner role: integration and validation agent
- Objective: update TASK-015 documentation and validation evidence after
  implementation and tests pass.
- Allowed files: TASK-015 documentation, context package, prompt and validation
  report.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, source code and tests unless reporting a required
  deviation.
- Required inputs: handoffs from WS-015-A and WS-015-B.
- Blockers: dependency-gated on implementation and test evidence.
- Validation evidence: `npm run validate`,
  `python3 scripts/pre_coding_gate.py --root .` and
  `python3 scripts/deployment_readiness_gate.py --root . --target TASK-015`.
- Handoff output: files changed, validation evidence, remaining blockers,
  deviations and remaining documentation gaps.

## Parallel Agent Handoff Prompts

### Workstream WS-015-A

You are the TASK-015 local candidate adapter implementation agent. Work only in
`scripts/context_package_generator.py`. Read TASK-015, EP-TASK-015, TASK-014,
EP-TASK-014 and `tests/fixtures/retrieval_baseline.json`. Add deterministic
local semantic-style candidate generation from baseline cases, using repository
Markdown and stable token-overlap ordering. Return TASK-014-compatible JSON with
`retrieval_mode`, `cases`, `id` and `returned_optional_paths`. Do not add
embeddings, vector databases, external API calls, production data or changes to
protected vision and constitution files. Validate by running the candidate
generation CLI and hand off files changed, generated output evidence,
dependencies for tests, blockers and deviations.

### Workstream WS-015-B

You are the TASK-015 focused test and comparison agent. Work only in
`tests/test_context_package_generator.py`. Read TASK-015, EP-TASK-015, TASK-014,
EP-TASK-014 and `tests/fixtures/retrieval_baseline.json`. Add tests proving
successful candidate generation, TASK-014 comparison compatibility and
deterministic repeated output. Do not modify protected vision and constitution
files, production data fixtures or external service mocks. Validate with
`python3 -m unittest tests.test_context_package_generator` and the TASK-014
comparison command after WS-015-A is available. Hand off test evidence,
comparison evidence, blockers and deviations.

### Workstream WS-015-C

You are the TASK-015 integration and validation agent. Start only after
WS-015-A and WS-015-B handoffs are available. Update TASK-015 documentation,
context package, prompt and validation report with implementation, test and gate
evidence. Do not modify source code or tests unless reporting a required
deviation. Run `npm run validate`, `python3 scripts/pre_coding_gate.py --root .`
and `python3 scripts/deployment_readiness_gate.py --root . --target TASK-015`.
Return files changed, documents created, remaining missing-information markers,
validation evidence, blockers, dependencies, integration notes and deviations.

## Test Plan

- Test candidate generation returns expected case ids.
- Test candidate output compares successfully against the fixture baseline.
- Test deterministic output.

## Validation Plan

Run focused tests, sample candidate generation CLI, candidate comparison CLI,
`npm run validate`, pre-coding gate and deployment-readiness gate for TASK-015.

## Gate Commands

Source policy: `../23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md`

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --pretty
python3 scripts/context_package_generator.py --root . --compare-retrieval-candidate tests/fixtures/retrieval_baseline.json --candidate-results tests/fixtures/retrieval_candidate.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-015
```

| Gate | Required? | Command | Evidence path | Blocks next phase? |
|---|---|---|---|---|
| Focused tests | yes | `python3 -m unittest tests.test_context_package_generator` | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` | yes |
| Candidate generation | yes | `python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --pretty` | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` | yes |
| Contract/schema | yes | `python3 scripts/context_package_generator.py --root . --compare-retrieval-candidate tests/fixtures/retrieval_baseline.json --candidate-results tests/fixtures/retrieval_candidate.json --pretty` | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` | yes |
| Repository validation | yes | `npm run validate` | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` | yes |
| Pre-coding | yes | `python3 scripts/pre_coding_gate.py --root .` | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` | yes |
| Deployment-readiness | yes | `python3 scripts/deployment_readiness_gate.py --root . --target TASK-015` | `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md` | yes |

## Documentation Updates

Update TASK-015 task, goal impact, execution plan and validation report after
implementation.

## Rollback Plan

Remove local candidate generation code, tests and TASK-015 validation status
updates.

## Agent Handoff Prompt

Implement TASK-015 by adding deterministic local candidate generation compatible
with TASK-014 comparison. Preserve graph-first context and avoid embeddings,
vector search and external API calls.

For parallel re-execution, use the workstream-specific prompts in
`Parallel Agent Handoff Prompts`. Use this general handoff only when assigning
the full task to one agent.

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
