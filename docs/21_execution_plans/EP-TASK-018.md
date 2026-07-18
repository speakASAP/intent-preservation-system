# EP-TASK-018: Embedding Provider Adapter Boundary

```yaml
id: EP-TASK-018
status: validated
source_task: ../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
parallelization_strategy: single_agent
project_invariant_impact: preserves
sensitive_data_classification: synthetic
contract_schema_impact: changes
replay_determinism_impact: required
required_gates:
  - focused-tests
  - candidate-generation
  - repository-validate
  - pre-coding
  - deployment-readiness
context_package: ../13_context_packages/CP-task-018.md
coding_prompt: ../14_prompts/PROMPT-TASK-018-embedding-provider-adapter-boundary.md
validation_report: ../12_validation/VAL-TASK-018-embedding-provider-adapter-boundary.md
```

## Metadata

This execution plan adds an adapter boundary around embedding generation for
optional retrieval candidates.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-018.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan makes future embedding providers a bounded implementation choice while
preserving the comparison contract and graph-first retrieval behavior.

## Project Invariants

- IPS-INV-001: embedding providers remain optional retrieval support.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation is bounded to provider boundary code, tests and
  TASK-018 documentation.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: test data remains synthetic and repository-local.

## Sensitive-Data Handling

Classification: synthetic. The only implemented provider remains local and
does not transmit repository content.

## Contract Validation Plan

Preserve candidate path comparison behavior. Add provider metadata to candidate
output for embedding-index mode.

## Replay/Determinism Plan

Keep `local-hash` deterministic and reject unsupported providers before
candidate generation.

## Scope

Modify `scripts/context_package_generator.py` and
`tests/test_context_package_generator.py`, then update TASK-018 governance and
graph traceability.

## Non-Goals

- No external embedding providers.
- No provider credentials.
- No vector database.
- No graph-required context replacement.

## Parallelization Plan

This validated task is a standalone single-agent implementation/integration
workstream. The source task, goal impact and completed validation describe one
cohesive change to the provider boundary inside the existing embedding-index
candidate path. No independent implementation workstream is source-supported
without splitting edits to the same generator, tests and graph traceability
files.

### Ready-Now Parallel Goals

None. The only source-backed ready workstream is `WS-TASK-018-IMPL`, which owns
implementation, tests, graph traceability, documentation updates and validation
evidence as one integration session.

### Dependency-Gated Goals

None. TASK-018 depends on the already validated TASK-017 local embedding index
and TASK-014 comparison harness context; no additional dependency-gated
TASK-018 workstream is defined by the source task.

### Blockers

No open blockers remain for the validated task. Future provider-backed work is
outside TASK-018 scope and remains blocked by later provider safety gates and
human-approved provider decisions.

### Shared Files And Merge Order

Because this plan has one implementation/integration workstream, there are no
parallel shared-file conflicts. The merge order for the completed single
workstream is:

1. `scripts/context_package_generator.py`
2. `tests/test_context_package_generator.py`
3. `graph/project_graph.example.yaml`
4. TASK-018 governance and validation documents

## Files to Inspect

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `11_tasks/TASK-017-implement-local-embedding-index.md`
- `11_tasks/TASK-014-compare-candidate-retrieval-results.md`

## Files to Create

- TASK-018 task, goal impact, execution plan, context package, prompt and
  validation report.

## Files to Modify

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Define embedding input, result and provider boundary types.
2. Implement the existing hash vector logic as the `local-hash` provider.
3. Make local embedding retrieval receive a provider selection.
4. Add CLI provider selection for embedding candidate generation.
5. Record selected provider metadata in candidate output.
6. Add focused tests.
7. Run repository gates and update validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-TASK-018-IMPL | Add the embedding provider adapter boundary behind local embedding-index retrieval and validate it end to end. | No; this is the sole source-backed implementation/integration workstream. | Context-engine implementation agent | `scripts/context_package_generator.py`; `tests/test_context_package_generator.py`; `graph/project_graph.example.yaml`; TASK-018 governance and validation documents | Provider boundary code, explicit `local-hash` selection, provider metadata in candidate output, focused tests and validation evidence | TASK-017 local embedding index and TASK-014 comparison harness context |

Separate Codex thread dispatch is not applicable for this already implemented
and validated plan because only one source-backed workstream exists and it
touches the shared implementation, test and graph files together.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-TASK-018-IMPL | TASK-017 local embedding index must exist before adding the provider boundary. | context-engine-agent | Use `../11_tasks/TASK-017-implement-local-embedding-index.md` and existing local embedding-index behavior as input. | resolved |
| WS-TASK-018-IMPL | TASK-014 comparison harness context must remain compatible. | context-engine-agent | Preserve candidate path comparison behavior and validate embedding candidate output. | resolved |
| WS-TASK-018-IMPL | External provider credentials or real provider decisions. | human/future provider workstream | Not required for TASK-018; keep external providers out of scope. | not applicable |

## Parallel Dispatch List

### Goal WS-TASK-018-IMPL: Provider Adapter Boundary Implementation

- Owner role: context-engine implementation agent.
- Objective: add an explicit embedding input/result/provider boundary behind
  the existing local embedding-index retrieval mode, keep `local-hash`
  deterministic, reject unknown providers and record selected provider metadata
  in candidate output.
- Allowed files: `scripts/context_package_generator.py`,
  `tests/test_context_package_generator.py`, `graph/project_graph.example.yaml`
  and TASK-018 governance and validation documents.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, external provider documentation, credential stores,
  production data, unrelated task ranges and unrelated retrieval contracts.
- Required inputs: `../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md`,
  `../22_goal_impact/GOAL-IMPACT-TASK-018.md`,
  `../11_tasks/TASK-017-implement-local-embedding-index.md`,
  `../11_tasks/TASK-014-compare-candidate-retrieval-results.md` and
  `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`.
- Blockers: none open for the validated local-provider adapter boundary.
- Validation evidence: focused context-package tests, provider-selected
  candidate generation, repository validation, pre-coding gate and
  deployment-readiness gate for TASK-018.
- Handoff output: files changed, tests run, validation evidence, blockers
  encountered or cleared, integration notes, deviations and remaining
  documentation gaps.

## Parallel Agent Handoff Prompts

### Workstream WS-TASK-018-IMPL

You are the context-engine implementation agent for TASK-018. Implement the
embedding provider adapter boundary behind the existing local embedding-index
retrieval mode. Modify only `scripts/context_package_generator.py`,
`tests/test_context_package_generator.py`, `graph/project_graph.example.yaml`
and TASK-018 governance/validation documents. Do not add external providers,
credentials, vector databases or changes to required graph context. Preserve
compatibility with TASK-014 candidate comparison and use TASK-017 local
embedding-index behavior as the implementation base. Validate with focused
context-package tests, provider-selected candidate generation, repository
validation, the pre-coding gate and deployment-readiness gate for TASK-018.
Return files changed, tests run, validation evidence, blockers, integration
notes, deviations and remaining documentation gaps.

## Test Plan

- Test provider boundary deterministic output.
- Test unknown provider rejection.
- Test index metadata records the selected provider.
- Test embedding candidate comparison still passes.

## Validation Plan

Run focused tests, sample provider-selected candidate generation, `npm run
validate`, pre-coding gate and deployment-readiness gate for TASK-018.

## Gate Commands

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode local-embedding-index --embedding-provider local-hash --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-018
```

## Documentation Updates

Update TASK-018 task, goal impact, execution plan and validation report after
implementation.

## Rollback Plan

Remove the provider boundary code, tests and TASK-018 graph and governance
documents.

## Agent Handoff Prompt

Implement TASK-018 by adding an embedding provider adapter boundary behind the
existing local embedding-index retrieval mode.

## Completion Checklist

- [x] Implementation complete
- [x] Parallelizable workstreams identified
- [x] Blockers and serial dependencies documented
- [x] Agent handoff prompts created for source-backed workstreams
- [x] Integration order documented
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
