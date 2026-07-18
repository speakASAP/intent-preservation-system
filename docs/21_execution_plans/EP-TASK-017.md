# EP-TASK-017: Local Embedding Index

```yaml
id: EP-TASK-017
status: validated
source_task: ../11_tasks/TASK-017-implement-local-embedding-index.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
parallelization_strategy: single_agent
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: creates
replay_determinism_impact: required
context_package: ../13_context_packages/CP-task-017.md
coding_prompt: ../14_prompts/PROMPT-TASK-017-local-embedding-index.md
validation_report: ../12_validation/VAL-TASK-017-local-embedding-index.md
required_gates:
  - focused-context-package-tests
  - candidate-generation
  - candidate-comparison
  - repository-validation
  - pre-coding
  - deployment-readiness
```

## Metadata

This execution plan adds a deterministic local embedding-style index for
optional retrieval candidates.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-017.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan advances Phase 5 by adding a vector-index candidate mode while keeping
required graph context authoritative.

## Project Invariants

- IPS-INV-001: local embedding candidates remain optional.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation is bounded to retrieval code, tests, fixtures and
  TASK-017 documentation.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: fixture data is synthetic and repository-local.

## Sensitive-Data Handling

Classification: synthetic. The local index scans repository Markdown and
synthetic fixtures only.

## Contract Validation Plan

Keep existing keyword retrieval and `local-semantic-token-overlap` candidate
output unchanged. Add `local-embedding-index` as an explicit candidate mode.

| Contract or schema | Impact | Validator/command | Evidence path | Owner |
|---|---|---|---|---|
| Candidate mode `local-embedding-index` | creates | `python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode local-embedding-index --pretty` | Terminal output and `../12_validation/VAL-TASK-017-local-embedding-index.md` | context-engine-agent |
| Candidate comparison output | validates | `python3 scripts/context_package_generator.py --root . --compare-retrieval-candidate tests/fixtures/retrieval_baseline.json --candidate-results tests/fixtures/retrieval_candidate.json --pretty` | Terminal output and `../12_validation/VAL-TASK-017-local-embedding-index.md` | context-engine-agent |

## Replay/Determinism Plan

Use deterministic hashing for token vector buckets, cosine scoring and stable
path tie-breaking.

| Behavior | Required? | Validation method | Evidence path |
|---|---|---|---|
| Replay | yes | Re-run focused context package tests and candidate generation for a fixed repository state. | `../12_validation/VAL-TASK-017-local-embedding-index.md` |
| Idempotency | yes | Candidate generation must not mutate source documents. | Terminal output from candidate generation command |
| Deterministic output | yes | `test_generate_embedding_candidate_results_compare_against_baseline` and deterministic output checks in `tests/test_context_package_generator.py`. | `../12_validation/VAL-TASK-017-local-embedding-index.md` |

## Scope

Modify `scripts/context_package_generator.py` and
`tests/test_context_package_generator.py`, then update TASK-017 governance and
graph traceability.

## Non-Goals

- No external embedding API.
- No vector database.
- No graph-required context replacement.
- No sensitive data indexing.

## Parallelization Plan

TASK-017 is an already implemented and validated single-task slice. The
source-backed scope centers on one shared implementation file,
`scripts/context_package_generator.py`, with matching tests and graph
traceability. Because the implementation steps all converge on the same
candidate-generation contract and shared test surface, the plan uses one
implementation/integration workstream instead of inventing independent parallel
goals.

### Ready-Now Parallel Goals

None. No independent ready-now parallel goals are source-supported for this
validated task because splitting the work would create uncoordinated edits to
the same generator, tests and candidate contract.

### Dependency-Gated Goals

None. TASK-017 depends on the already available TASK-014 comparison harness and
TASK-015 local semantic adapter context; no additional dependency-gated
workstream remains for this validated plan.

### Blockers

No blockers remain. The TASK-014 comparison harness, TASK-015 local semantic
adapter context, synthetic fixtures and repository gate commands are available.

### Shared Files And Merge Order

No parallel merge order applies because the plan has one
implementation/integration workstream. If future follow-up work splits this
area, merge order must be: implementation in
`scripts/context_package_generator.py`, focused tests in
`tests/test_context_package_generator.py`, graph traceability in
`graph/project_graph.example.yaml`, then validation documentation.

## Files to Inspect

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `tests/fixtures/retrieval_baseline.json`
- `11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`

## Files to Create

- TASK-017 task, goal impact, execution plan, context package, prompt and
  validation report.

## Files to Modify

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Add deterministic hashed token vector helpers.
2. Build a local embedding index over optional Markdown candidates.
3. Exclude required graph context from optional vector ranking.
4. Add `local-embedding-index` retrieval report output.
5. Add candidate generation mode for embedding-index output.
6. Add focused tests and validate through candidate comparison.
7. Run repository gates and update validation evidence.

Because these steps all touch the same retrieval generator and tests, they are
kept in one implementation/integration wave.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-017-implementation-integration | Implement and validate deterministic local embedding-index candidate generation. | no | context-engine implementation agent | `scripts/context_package_generator.py`, `tests/test_context_package_generator.py`, `graph/project_graph.example.yaml`, TASK-017 governance and validation documents | Deterministic `local-embedding-index` mode, focused tests, graph traceability and validation evidence | TASK-014 comparison harness and TASK-015 adapter context already available |

Separate Codex-thread execution is not applicable to the validated source plan:
there is only one source-supported workstream and it owns shared implementation,
test and validation responsibilities.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-017-implementation-integration | TASK-014 comparison harness | context-engine-agent | Use existing comparison harness for candidate validation. | resolved |
| WS-017-implementation-integration | TASK-015 local semantic adapter context | context-engine-agent | Preserve local/offline deterministic retrieval shape. | resolved |
| WS-017-implementation-integration | External embedding providers | context-engine-agent | Exclude from scope; use deterministic local hashed vectors only. | not applicable |

## Parallel Dispatch List

### Goal WS-017-implementation-integration: Local embedding-index implementation and validation

- Owner role: context-engine implementation agent.
- Objective: add deterministic local embedding-index candidate generation that
  remains optional, excludes required graph context from optional ranking and
  compares through the TASK-014 harness.
- Allowed files: `scripts/context_package_generator.py`,
  `tests/test_context_package_generator.py`, `graph/project_graph.example.yaml`
  and TASK-017 governance/validation artifacts.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, external provider integrations, vector database
  configuration and files outside TASK-017 scope.
- Required inputs: `../11_tasks/TASK-017-implement-local-embedding-index.md`,
  `../22_goal_impact/GOAL-IMPACT-TASK-017.md`, TASK-014 comparison harness,
  TASK-015 local semantic adapter context and
  `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`.
- Blockers: none remaining; dependencies are resolved.
- Validation evidence: focused context-package tests, `local-embedding-index`
  candidate generation, candidate comparison, `npm run validate`,
  pre-coding gate and deployment-readiness gate evidence in
  `../12_validation/VAL-TASK-017-local-embedding-index.md`.
- Handoff output: files changed, tests run, validation evidence, blockers
  encountered or cleared, dependency notes, integration notes, deviations and
  remaining documentation gaps.

## Parallel Agent Handoff Prompts

### Workstream WS-017-implementation-integration

You are the context-engine implementation agent for TASK-017. Work only within
the TASK-017 execution-plan scope. Implement deterministic local
embedding-index candidate generation in `scripts/context_package_generator.py`,
add focused tests in `tests/test_context_package_generator.py`, preserve
graph-first required context and update TASK-017 graph/governance evidence.
Do not call external embedding APIs, add a vector database, replace required
graph context or modify `00_constitution/CONSTITUTION.md` or
`01_vision/VISION.md`. Validate with focused context-package tests, sample
`local-embedding-index` candidate generation, candidate comparison,
`npm run validate`, pre-coding gate and deployment-readiness gate for TASK-017.
Return files changed, validation evidence, blockers, dependencies, integration
notes, deviations and remaining documentation gaps.

## Test Plan

- Test index metadata and required document exclusion.
- Test local embedding retrieval report shape.
- Test embedding candidate output compares against baseline.
- Test deterministic output.

## Validation Plan

Run focused tests, sample CLI candidate generation, sample candidate comparison,
`npm run validate`, pre-coding gate and deployment-readiness gate for TASK-017.

## Gate Commands

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode local-embedding-index --pretty
python3 scripts/context_package_generator.py --root . --compare-retrieval-candidate tests/fixtures/retrieval_baseline.json --candidate-results tests/fixtures/retrieval_candidate.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-017
```

| Gate | Required? | Command | Evidence path | Blocks next phase? |
|---|---|---|---|---|
| Focused tests | yes | `python3 -m unittest tests.test_context_package_generator` | `../12_validation/VAL-TASK-017-local-embedding-index.md` | yes |
| Candidate generation | yes | `python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode local-embedding-index --pretty` | Terminal output and `../12_validation/VAL-TASK-017-local-embedding-index.md` | yes |
| Contract/schema | yes | `python3 scripts/context_package_generator.py --root . --compare-retrieval-candidate tests/fixtures/retrieval_baseline.json --candidate-results tests/fixtures/retrieval_candidate.json --pretty` | Terminal output and `../12_validation/VAL-TASK-017-local-embedding-index.md` | yes |
| Repository validation | yes | `npm run validate` | `../12_validation/VAL-TASK-017-local-embedding-index.md` | yes |
| Pre-coding | yes | `python3 scripts/pre_coding_gate.py --root .` | `../12_validation/VAL-TASK-017-local-embedding-index.md` | yes |
| Deployment-readiness | yes | `python3 scripts/deployment_readiness_gate.py --root . --target TASK-017` | `../12_validation/VAL-TASK-017-local-embedding-index.md` | yes |

## Documentation Updates

Update TASK-017 task, goal impact, execution plan and validation report after
implementation.

## Rollback Plan

Remove the local embedding-index code, tests and TASK-017 graph and governance
documents.

## Agent Handoff Prompt

Final integration prompt is listed under `Parallel Agent Handoff Prompts` as
`WS-017-implementation-integration`.

## Completion Checklist

- [x] Implementation complete
- [x] Parallelizable workstreams identified
- [x] Blockers and serial dependencies documented
- [x] Agent handoff prompts created for independent workstreams or single
  implementation/integration workstream
- [x] Integration order documented
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
