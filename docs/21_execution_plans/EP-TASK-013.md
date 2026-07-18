# EP-TASK-013: Retrieval Evaluation Baseline

```yaml
id: EP-TASK-013
status: validated
source_task: ../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
parallelization_strategy: parallel_goals
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: creates
replay_determinism_impact: required
context_package: ../13_context_packages/CP-task-013.md
coding_prompt: ../14_prompts/PROMPT-TASK-013-retrieval-evaluation-baseline.md
validation_report: ../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md
required_gates:
  - focused-context-package-tests
  - retrieval-baseline-cli
  - repository-validation
  - pre-coding
  - deployment-readiness
```

## Metadata

This execution plan defined a bounded retrieval evaluation baseline before any
semantic retrieval implementation. TASK-013 is validated, and evidence is
recorded in
`../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-013.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
prior_task: ../11_tasks/TASK-012-harden-optional-local-retrieval.md
validation_report: ../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md
```

## Goal Impact

The plan makes optional retrieval quality measurable with a deterministic local
baseline before embeddings are introduced. This supports the TASK-013 goal of
preventing semantic retrieval from becoming an unmeasured black box while graph
required context remains separate.

## Project Invariants

- IPS-INV-001: evaluation cases remain traceable to task ids and expected
  documents.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation stays bounded to local evaluation under this
  execution plan.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: baseline fixtures use synthetic repository-local data only.

Source policy: `../17_governance/PROJECT_INVARIANTS.md`

## Sensitive-Data Handling

Classification: synthetic. Baseline fixtures use synthetic task ids, queries and
repository-local paths only. Prompts, tests, examples, logs and reports must not
contain secrets, raw production data, confidential identifiers or real customer
data.

Source policy: `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Contract Validation Plan

TASK-013 creates a JSON-compatible retrieval evaluation report contract with
case-level pass/fail results, expected documents, returned documents, missing
documents, unexpected documents and findings.

| Contract or schema | Impact | Validator/command | Evidence path | Owner |
|---|---|---|---|---|
| Retrieval evaluation report | creates | `python3 -m unittest tests.test_context_package_generator` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | context-engine-agent |
| Baseline evaluation CLI output | validates | `python3 scripts/context_package_generator.py --root . --evaluate-retrieval tests/fixtures/retrieval_baseline.json --pretty` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | context-engine-agent |

## Replay/Determinism Plan

Evaluation output must be deterministic for a fixed baseline file and repository
state. Baseline cases and returned paths are sorted deterministically, and tests
compare repeated output.

| Behavior | Required? | Validation method | Evidence path |
|---|---|---|---|
| Replay | yes | Re-run the same baseline file against the same repository state. | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` |
| Idempotency | yes | Re-run the evaluator without changing repository data. | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` |
| Deterministic output | yes | `test_evaluate_retrieval_baseline_is_deterministic` compares repeated output. | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` |

## Scope

- Define a local baseline JSON shape.
- Add retrieval evaluation support to `scripts/context_package_generator.py`.
- Add CLI support for evaluating a baseline file.
- Add a synthetic baseline fixture.
- Add focused tests for pass, fail and missing-task cases.
- Record validation evidence for TASK-013.

## Non-Goals

- No embeddings.
- No vector database.
- No external API calls.
- No graph-required context replacement.
- No changes to protected vision or constitution documents.

## Parallelization Plan

This plan can be decomposed into parallel-safe workstreams with one final
integration and validation owner. The implementation is already validated; if it
is replayed or audited, use the workstreams below instead of a single broad
implementation session.

### Ready-Now Parallel Goals

- WS-013A, retrieval evaluator and CLI: can start immediately because it owns
  `scripts/context_package_generator.py` and preserves TASK-012 retrieval
  behavior.
- WS-013C, documentation scaffolding: can start immediately as draft
  documentation from TASK-013, GOAL-IMPACT-TASK-013, the context package and the
  coding prompt. It must not mark final validation complete until WS-013D.

### Dependency-Gated Goals

- WS-013B, tests and synthetic fixture: depends on WS-013A's baseline JSON shape
  and evaluation result fields.
- WS-013D, final integration and validation: depends on WS-013A, WS-013B and
  WS-013C handoff evidence.

### Blockers

- No remaining blockers are recorded for the validated TASK-013 implementation.
- During a re-run, WS-013B is blocked until WS-013A confirms the baseline JSON
  shape and report fields.
- WS-013D is blocked until focused tests, sample CLI output, repository
  validation, pre-coding gate and deployment-readiness gate evidence are
  available.

### Shared Files And Merge Order

- `scripts/context_package_generator.py`: owned by WS-013A.
- `tests/test_context_package_generator.py`: owned by WS-013B.
- `tests/fixtures/retrieval_baseline.json`: owned by WS-013B.
- `graph/project_graph.example.yaml`: owned by WS-013B.
- TASK-013 documentation files: draft updates owned by WS-013C, final status and
  evidence updates owned by WS-013D.

Merge order:

1. Merge WS-013A evaluator and CLI changes.
2. Merge WS-013B tests, synthetic fixture and graph example updates after
   confirming the evaluator contract.
3. Merge WS-013C draft documentation.
4. Merge WS-013D final validation evidence and status updates.

## Files to Inspect

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `11_tasks/TASK-012-harden-optional-local-retrieval.md`
- `21_execution_plans/EP-TASK-012.md`
- `12_validation/VAL-TASK-012-harden-optional-local-retrieval.md`
- `23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Files to Create

- `tests/fixtures/retrieval_baseline.json`
- `22_goal_impact/GOAL-IMPACT-TASK-013.md`
- `13_context_packages/CP-task-013.md`
- `14_prompts/PROMPT-TASK-013-retrieval-evaluation-baseline.md`
- `12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md`

## Files to Modify

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `graph/project_graph.example.yaml`
- `11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`
- `21_execution_plans/EP-TASK-013.md`
- TASK-013 documentation after validation.

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`
- Files containing secrets, raw production data, confidential identifiers or real
  customer data.

## Implementation Steps

Parallel wave 1:

1. WS-013A defines baseline case parsing in
   `scripts/context_package_generator.py`.
2. WS-013A runs optional retrieval for each baseline case.
3. WS-013A compares expected paths against returned optional suggestion paths.
4. WS-013A returns case-level pass/fail, missing paths and unexpected paths.
5. WS-013A adds CLI support for baseline evaluation.
6. WS-013C prepares TASK-013 draft documentation from approved source artifacts.

Parallel wave 2:

1. WS-013B adds a synthetic baseline fixture after WS-013A confirms the baseline
   JSON shape.
2. WS-013B adds focused tests for passing, failing, missing-task and
   deterministic-output cases.

Final integration wave:

1. WS-013D runs validation gates.
2. WS-013D updates validation evidence and final TASK-013 documentation status.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-013A | Add deterministic retrieval evaluator and CLI mode. | yes | Context engine implementation agent | `scripts/context_package_generator.py` | Evaluator and CLI support for baseline evaluation. | None |
| WS-013B | Add synthetic fixture and focused tests. | dependency-gated | Test and fixture agent | `tests/test_context_package_generator.py`, `tests/fixtures/retrieval_baseline.json`, `graph/project_graph.example.yaml` | Passing/failing/missing-task/determinism tests and synthetic baseline data. | WS-013A baseline JSON shape and report fields |
| WS-013C | Prepare TASK-013 documentation and prompt artifacts. | yes | Documentation agent | `11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`, `22_goal_impact/GOAL-IMPACT-TASK-013.md`, `13_context_packages/CP-task-013.md`, `14_prompts/PROMPT-TASK-013-retrieval-evaluation-baseline.md`, `21_execution_plans/EP-TASK-013.md` | Draft traceable TASK-013 documentation and prompt artifacts. | Final validation status waits for WS-013D |
| WS-013D | Integrate, validate and record evidence. | final integration | Validation owner | `11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`, `21_execution_plans/EP-TASK-013.md`, `22_goal_impact/GOAL-IMPACT-TASK-013.md`, `12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | Validation evidence, final status updates and deviations. | WS-013A, WS-013B and WS-013C |

Ready-now workstreams WS-013A and WS-013C should be started in separate Codex
threads when thread-management tools are available. WS-013B should start after
WS-013A hands off the baseline JSON shape and report fields. WS-013D remains in
the integration thread.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-013A | None recorded. | context-engine-agent | Preserve graph-first retrieval and avoid embeddings, vector search and external APIs. | resolved |
| WS-013B | Depends on baseline JSON shape and report fields. | test and fixture agent | Receive WS-013A handoff or inspect merged evaluator contract. | resolved |
| WS-013C | Final validated status depends on gate evidence. | documentation agent | Keep draft documentation traceable until WS-013D records evidence. | resolved |
| WS-013D | Depends on WS-013A, WS-013B and WS-013C outputs. | validation owner | Run required gates and update validation report/status fields. | resolved |

## Parallel Dispatch List

### Goal WS-013A: Retrieval Evaluator And CLI

- Owner role: context engine implementation agent.
- Objective: Add deterministic optional retrieval baseline evaluation and CLI
  support to `scripts/context_package_generator.py`.
- Allowed files: `scripts/context_package_generator.py`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, embedding provider files, vector database files,
  external API integrations and files containing secrets or raw production data.
- Required inputs: TASK-013, EP-TASK-013, TASK-012, EP-TASK-012,
  VAL-TASK-012 and the sensitive-data policy.
- Blockers: none recorded.
- Validation evidence: focused tests and sample baseline CLI output collected by
  WS-013D.
- Handoff output: baseline JSON shape, report fields, CLI flag behavior and any
  deviations.

### Goal WS-013B: Synthetic Fixture And Focused Tests

- Owner role: test and fixture agent.
- Objective: Add synthetic baseline data and tests for pass, fail, missing-task
  and deterministic-output cases.
- Allowed files: `tests/test_context_package_generator.py`,
  `tests/fixtures/retrieval_baseline.json`,
  `graph/project_graph.example.yaml`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, production data, secrets and external API fixtures.
- Required inputs: WS-013A baseline JSON shape and report fields, TASK-013 and
  the sensitive-data policy.
- Blockers: dependency on WS-013A contract handoff.
- Validation evidence: `python3 -m unittest tests.test_context_package_generator`.
- Handoff output: fixture path, test names, pass/fail evidence and any
  determinism findings.

### Goal WS-013C: Documentation And Prompt Drafts

- Owner role: documentation agent.
- Objective: Prepare traceable TASK-013 documentation, context package and
  coding prompt content without inventing validation evidence.
- Allowed files: `11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`,
  `21_execution_plans/EP-TASK-013.md`,
  `22_goal_impact/GOAL-IMPACT-TASK-013.md`,
  `13_context_packages/CP-task-013.md`,
  `14_prompts/PROMPT-TASK-013-retrieval-evaluation-baseline.md`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, ADRs and unrelated task files.
- Required inputs: TASK-013, GOAL-IMPACT-TASK-013, CP-task-013,
  PROMPT-TASK-013 and EP-TASK-013.
- Blockers: final validation status waits for WS-013D evidence.
- Validation evidence: documentation diff reviewed by WS-013D and repository
  gates.
- Handoff output: list of documentation updates, remaining markers and any
  source gaps.

### Goal WS-013D: Final Integration And Validation

- Owner role: integration and validation owner.
- Objective: Merge workstreams, run gates and record TASK-013 validation
  evidence.
- Allowed files: `11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`,
  `21_execution_plans/EP-TASK-013.md`,
  `22_goal_impact/GOAL-IMPACT-TASK-013.md`,
  `12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, ADRs, unrelated task files, production data and
  secrets.
- Required inputs: WS-013A, WS-013B and WS-013C handoff outputs.
- Blockers: cannot start until implementation, fixture/tests and draft docs are
  complete.
- Validation evidence: focused tests, sample CLI output, `npm run validate`,
  pre-coding gate and deployment-readiness gate.
- Handoff output: final validation report, final status updates, deviations and
  remaining blockers.

## Parallel Agent Handoff Prompts

### Workstream WS-013A

You are the WS-013A context engine implementation agent for TASK-013. Work only
on `scripts/context_package_generator.py`. Add deterministic optional retrieval
baseline evaluation and CLI support using synthetic repository-local inputs.
Preserve TASK-012 graph-first behavior. Do not add embeddings, vector search,
external API calls, secrets or production data. Return the baseline JSON shape,
report fields, CLI behavior, files changed, validation run if any, blockers and
deviations for the integration owner.

### Workstream WS-013B

You are the WS-013B test and fixture agent for TASK-013. After WS-013A confirms
the baseline JSON shape and report fields, update only
`tests/test_context_package_generator.py`,
`tests/fixtures/retrieval_baseline.json` and
`graph/project_graph.example.yaml`. Use synthetic data only. Add focused tests
for passing, failing, missing-task and deterministic-output cases. Run
`python3 -m unittest tests.test_context_package_generator` when possible and
return evidence, fixture paths, test names, blockers and deviations.

### Workstream WS-013C

You are the WS-013C documentation agent for TASK-013. Prepare traceable TASK-013
documentation from TASK-013, EP-TASK-013, GOAL-IMPACT-TASK-013, CP-task-013 and
PROMPT-TASK-013. Do not change protected vision, constitution, ADRs or
unrelated task files. Do not invent validation evidence. Leave final validated
status to WS-013D. Return files changed, missing markers, blockers and
handoff notes.

### Workstream WS-013D

You are the WS-013D final integration and validation owner for TASK-013. Merge
WS-013A, WS-013B and WS-013C outputs, run focused context-package tests, sample
baseline CLI output, `npm run validate`, `python3 scripts/pre_coding_gate.py
--root .` and `python3 scripts/deployment_readiness_gate.py --root . --target
TASK-013`. Update final TASK-013 validation evidence and status documents only
after evidence is available. Return files changed, validation evidence, blockers,
dependencies, integration notes and deviations.

## Test Plan

- Test a passing baseline case.
- Test a failing baseline case.
- Test missing task findings.
- Test deterministic evaluation output.

## Validation Plan

Run focused tests, sample baseline evaluation CLI, `npm run validate`,
pre-coding gate and deployment-readiness gate for TASK-013.

## Gate Commands

Source policy: `../23_documentation_contracts/OPERATIONAL_GATE_STANDARD.md`

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --evaluate-retrieval tests/fixtures/retrieval_baseline.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-013
```

| Gate | Required? | Command | Evidence path | Blocks next phase? |
|---|---|---|---|---|
| Focused context-package tests | yes | `python3 -m unittest tests.test_context_package_generator` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | yes |
| Retrieval baseline CLI | yes | `python3 scripts/context_package_generator.py --root . --evaluate-retrieval tests/fixtures/retrieval_baseline.json --pretty` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | yes |
| Repository validation | yes | `npm run validate` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | yes |
| Pre-coding | yes | `python3 scripts/pre_coding_gate.py --root .` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | yes |
| Contract/schema | yes | `python3 -m unittest tests.test_context_package_generator` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | yes |
| Replay/determinism | yes | `python3 -m unittest tests.test_context_package_generator` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | yes |
| Integration-readiness | yes | `npm run validate` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | yes |
| Deployment-readiness | yes | `python3 scripts/deployment_readiness_gate.py --root . --target TASK-013` | `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md` | yes |

## Documentation Updates

- Update TASK-013 task metadata and acceptance criteria after validation.
- Update GOAL-IMPACT-TASK-013 status after validation.
- Update EP-TASK-013 status and evidence after validation.
- Create or update CP-task-013.
- Create or update PROMPT-TASK-013.
- Create VAL-TASK-013 with validation evidence.

## Rollback Plan

Remove evaluation code, tests, fixture and TASK-013 validation status updates.
Keep protected vision and constitution documents unchanged.

## Agent Handoff Prompt

Use the workstream-specific prompts under `Parallel Agent Handoff Prompts`.
WS-013D owns final integration, validation evidence and status updates.

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
