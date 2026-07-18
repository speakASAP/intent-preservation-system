# EP-TASK-011: Optional RAG Retrieval Contract

```yaml
id: EP-TASK-011
status: validated
source_task: ../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
parallelization_strategy: single_agent
project_invariant_impact: preserves
sensitive_data_classification: none
contract_schema_impact: creates
replay_determinism_impact: required
required_gates:
  - unit-tests
  - repository-validation
  - pre-coding
  - deployment-readiness
context_package: ../13_context_packages/CP-task-011.md
coding_prompt: ../14_prompts/PROMPT-TASK-011-optional-rag-retrieval-contract.md
validation_report: ../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md
```

## Metadata

This execution plan defined the first Phase 5 implementation slice for
TASK-011 and has been validated by
`../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-011.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan starts Phase 5 by introducing a safe optional retrieval contract. It
keeps graph traversal mandatory and makes semantic or keyword suggestions
explicitly optional, explainable and deterministic.

## Project Invariants

- IPS-INV-001: required context must remain traceable through graph links.
- IPS-INV-002: protected vision and constitution documents are read-only.
- IPS-INV-003: implementation must follow this execution plan and remain
  bounded to optional retrieval.
- IPS-INV-004: validation evidence must be added before closure.
- IPS-INV-005: tests and reports must avoid secrets and raw production data.

## Sensitive-Data Handling

Classification: none. The implementation uses repository Markdown and
synthetic fixture content only. The retrieval index or scan must exclude common
build, cache and dependency folders and must not persist sensitive data outside
the repository validation reports.

## Contract Validation Plan

Define a JSON-compatible report with:

- `task_id`
- `required_context`
- `optional_suggestions`
- `retrieval_mode`
- `findings`

The report is valid when required context and optional suggestions are separate,
suggestions include reason metadata, and missing tasks return structured
findings.

## Replay/Determinism Plan

Use deterministic keyword matching for this slice. Sort by descending score,
then by stable path. Tests must compare repeated output for the same fixture.

## Scope

Add a local optional retrieval capability that can be invoked for one task id
and returns bounded supporting document suggestions.

## Non-Goals

- No external API calls.
- No vector database.
- No embedding generation.
- No replacement of graph-required documents.
- No changes to immutable vision or constitution documents.

## Parallelization Plan

This validated plan is a single-agent execution plan in the parallel-agent
format. The implementation work changes one contract-bearing retrieval surface
and its focused tests, so concurrent implementation workstreams would create
avoidable ownership overlap. The validation/reporting work is dependency-gated
on the implementation result and runs after the implementation workstream.

### Ready-Now Parallel Goals

| Goal | Status | Owner role | Assigned files | Validation responsibility |
| --- | --- | --- | --- | --- |
| WS-011-A | ready now | context-engine implementation agent | `scripts/context_package_generator.py` or a new helper under `scripts/`; relevant tests under `tests/`; `graph/project_graph.example.yaml` only if new durable artifacts are introduced | Focused optional retrieval tests, full unit suite, repository validation command |

Separate-thread execution: WS-011-A is suitable for one dedicated Codex thread
when TASK-011 is not already implemented. No additional ready-now workstream is
available because the optional retrieval contract, implementation surface and
compatibility tests are shared.

### Dependency-Gated Goals

| Goal | Dependency | Owner role | Expected output |
| --- | --- | --- | --- |
| WS-011-V | WS-011-A implementation and command evidence | validation/documentation agent | TASK-011 validation evidence and final readiness confirmation |

### Blockers

No open blockers are recorded for the validated TASK-011 slice. External
embedding APIs, vector databases and protected intent documents remain out of
scope rather than blockers.

### Shared Files And Merge Order

| Shared file or contract | Owner | Merge/review order | Notes |
| --- | --- | --- | --- |
| Optional retrieval report contract exposed by the context package generator | WS-011-A | WS-011-A before WS-011-V | Contract fields are `task_id`, `required_context`, `optional_suggestions`, `retrieval_mode` and `findings`. |
| Tests under `tests/` that cover optional retrieval behavior | WS-011-A | WS-011-A before WS-011-V | Validation work reads the completed test evidence instead of editing tests concurrently. |
| `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md` | WS-011-V | WS-011-V after WS-011-A | Validation report records evidence after implementation. |

## Files to Inspect

- `scripts/context_package_generator.py`
- `scripts/graph_extractor.py`
- `tests/test_context_package_generator.py`
- `tests/test_graph_extractor.py`
- `06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `10_features/FEAT-003-optional-rag-retrieval.md`
- `17_governance/PROJECT_INVARIANTS.md`
- `23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Files to Create

- Focused tests for optional retrieval behavior if a new module is created.
- TASK-011 validation evidence after implementation.

## Files to Modify

- `scripts/context_package_generator.py` or a new retrieval helper under
  `scripts/`.
- Relevant tests under `tests/`.
- `graph/project_graph.example.yaml` only if implementation introduces new
  durable artifacts.

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`
- Existing validated TASK-004, TASK-009 and TASK-010 content unless a direct
  compatibility issue is found and reported.

## Implementation Steps

1. Define the optional retrieval report structure in code.
2. Reuse existing graph extraction or context-package metadata to identify
   required context for the target task.
3. Add deterministic keyword scoring over allowed repository Markdown files.
4. Exclude required graph documents from optional suggestions unless explicitly
   marked as already required.
5. Return bounded suggestions with path, reason, rank, score and retrieval mode.
6. Add tests for deterministic output, missing task findings and no-suggestion
   behavior.
7. Run validation gates and update the TASK-011 validation report.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-011-A | Implement deterministic optional retrieval contract and focused tests | yes, as the only ready implementation workstream | context-engine implementation agent in one dedicated session | `scripts/context_package_generator.py` or a new helper under `scripts/`; relevant tests under `tests/`; `graph/project_graph.example.yaml` only if new durable artifacts are introduced | Optional retrieval command/report behavior with deterministic suggestions and focused tests | none |
| WS-011-V | Validate TASK-011 and record evidence | no, dependency-gated | validation/documentation agent | `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md` | Validation report with command evidence and readiness recommendation | WS-011-A complete |

WS-011-A should be opened as its own Codex thread when the implementation is not
already complete. WS-011-V should start only after WS-011-A reports file changes
and command evidence.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-011-A | No open blocker recorded | context-engine implementation agent | Preserve graph-first retrieval, avoid external services, and keep output deterministic | resolved |
| WS-011-V | Requires implementation and test evidence from WS-011-A | validation/documentation agent | Run required gates and update TASK-011 validation evidence | resolved |

## Parallel Dispatch List

### Goal WS-011-A: Deterministic Optional Retrieval Contract

- Owner role: context-engine implementation agent.
- Objective: implement a local optional retrieval capability for one task id
  that separates required graph context from optional suggestions.
- Allowed files: `scripts/context_package_generator.py` or a new helper under
  `scripts/`; relevant tests under `tests/`; `graph/project_graph.example.yaml`
  only if implementation introduces new durable artifacts.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, unrelated validated TASK-004, TASK-009 and TASK-010
  content, and any fixture, prompt or report containing secrets or raw
  production data.
- Required inputs: TASK-011, this execution plan, GOAL-IMPACT-TASK-011,
  CP-task-011, FEAT-003, the context retrieval architecture, ADR-002,
  `scripts/context_package_generator.py`, `scripts/graph_extractor.py`, and the
  existing context-package and graph-extractor tests.
- Blockers: none open for the validated deterministic keyword slice.
- Validation evidence: focused optional retrieval tests,
  `python3 -m unittest discover -s tests`, and `npm run validate`.
- Handoff output: files changed, tests run, validation evidence, remaining
  blockers, compatibility notes and deviations.

### Goal WS-011-V: Validation Evidence And Readiness

- Owner role: validation/documentation agent.
- Objective: verify TASK-011 after WS-011-A and record evidence that the
  optional retrieval contract is deterministic, graph-first and safe.
- Allowed files:
  `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, implementation files already owned by WS-011-A unless
  a defect is found and reported as a deviation, and any artifact containing
  secrets or raw production data.
- Required inputs: WS-011-A handoff, TASK-011, this execution plan and the
  validation commands below.
- Blockers: WS-011-A must be complete.
- Validation evidence: `python3 -m unittest discover -s tests`,
  `npm run validate`, `python3 scripts/pre_coding_gate.py --root .`, and
  `python3 scripts/deployment_readiness_gate.py --root . --target TASK-011`.
- Handoff output: validation report update, command evidence, remaining
  blockers and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-011-A

You are the TASK-011 context-engine implementation agent for Intent
Preservation System. Implement deterministic optional retrieval suggestions for
one task id. Preserve graph-first retrieval, keep required graph context
separate from optional suggestions, avoid external APIs and vector databases,
and keep output stable for a fixed repository state. Modify only
`scripts/context_package_generator.py` or a new helper under `scripts/`,
relevant tests under `tests/`, and `graph/project_graph.example.yaml` only if a
new durable artifact is introduced. Do not modify
`00_constitution/CONSTITUTION.md`, `01_vision/VISION.md`, unrelated validated
TASK-004/TASK-009/TASK-010 content, or any artifact containing secrets or raw
production data. Validate with focused optional retrieval tests,
`python3 -m unittest discover -s tests`, and `npm run validate`. Return files
changed, validation evidence, blockers, compatibility notes and deviations for
the validation workstream.

### Workstream WS-011-V

You are the TASK-011 validation/documentation agent for Intent Preservation
System. Start only after WS-011-A reports implementation and test evidence.
Verify that optional retrieval separates required context from optional
suggestions, includes path/reason/rank or score/retrieval mode metadata, keeps
existing graph and context-package outputs backward compatible, and returns
structured missing-task/no-suggestion findings. Modify only
`../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md`. Do not
modify implementation files unless a defect requires a reported deviation.
Validate with `python3 -m unittest discover -s tests`, `npm run validate`,
`python3 scripts/pre_coding_gate.py --root .`, and
`python3 scripts/deployment_readiness_gate.py --root . --target TASK-011`.
Return command evidence, blockers, readiness recommendation and deviations.

## Test Plan

- Test successful optional suggestions for a synthetic task fixture.
- Test missing task id returns a structured finding.
- Test required graph context remains separate from optional suggestions.
- Test repeated runs return identical output.
- Run the full repository test suite.

## Validation Plan

Run focused tests, a repository sample command for TASK-011, full repository
validation, the pre-coding gate and the deployment-readiness gate targeting
TASK-011.

## Gate Commands

```bash
python3 -m unittest discover -s tests
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-011
```

| Gate | Required? | Command | Evidence path | Blocks next phase? |
|---|---|---|---|---|
| Unit tests | yes | `python3 -m unittest discover -s tests` | `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md` or terminal output | yes |
| Repository validation | yes | `npm run validate` | `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md` or terminal output | yes |
| Pre-coding | yes | `python3 scripts/pre_coding_gate.py --root .` | `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md` or terminal output | yes |
| Deployment-readiness | yes | `python3 scripts/deployment_readiness_gate.py --root . --target TASK-011` | `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md` or terminal output | yes |

## Documentation Updates

Update `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md` with
actual command evidence after implementation. Update context-package or prompt
guidance only if the implementation changes those contracts.

## Rollback Plan

Remove the optional retrieval code, tests and TASK-011 implementation evidence.
Leave reviewed planning documents only if Phase 5 remains planned.

## Agent Handoff Prompt

Implement TASK-011 by adding deterministic optional retrieval suggestions for a
task id. Preserve graph-first retrieval, separate required context from optional
suggestions, avoid external services, and keep output stable for a fixed
repository state.

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
