# Coding Prompt: TASK-018 Embedding Provider Adapter Boundary

```yaml
id: PROMPT-TASK-018-embedding-provider-adapter-boundary
source_task: ../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md
execution_plan: ../21_execution_plans/EP-TASK-018.md
context_package: ../13_context_packages/CP-task-018.md
status: used
```

## Role

You are an implementation agent adding a provider adapter boundary for IPS
optional embedding retrieval.

## Task

Implement TASK-018: move the existing local embedding implementation behind an
explicit provider boundary and expose provider selection for candidate
generation.

## Context

Use `../13_context_packages/CP-task-018.md` and preserve graph-first retrieval.

## Constraints

- Do not add external providers in this slice.
- Do not call external services.
- Do not add provider credentials.
- Do not replace graph-required context.
- Keep output deterministic for `local-hash`.

## Allowed Changes

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- TASK-018 validation documentation.
- `../../graph/project_graph.example.yaml`

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any fixture, prompt or report containing secrets or raw production data.

## Implementation Instructions

1. Add provider boundary types.
2. Implement the current hash vector logic as `local-hash`.
3. Add provider selection to embedding candidate generation.
4. Record provider metadata in candidate output.
5. Add focused tests and validate through existing gates.

## Parallel Workstream Context

This prompt maps to the only source-backed TASK-018 workstream in
`../21_execution_plans/EP-TASK-018.md`.

- Source parallel dispatch list: `WS-TASK-018-IMPL`.
- Workstream model: standalone single-agent implementation/integration session;
  separate-thread dispatch is not applicable because the implementation, tests
  and graph traceability share the same files and merge owner.
- Objective: add the provider adapter boundary behind local embedding-index
  retrieval, keep `local-hash` deterministic, reject unknown providers and
  record selected provider metadata in candidate output.
- Dependencies: TASK-017 local embedding index and TASK-014 comparison harness
  context; both are resolved inputs for this validated workstream.
- Blockers: none open for TASK-018. External provider credentials, real
  provider decisions and provider safety gates remain outside this task.
- Owned files from source EP: `../../scripts/context_package_generator.py`,
  `../../tests/test_context_package_generator.py` and
  `../../graph/project_graph.example.yaml`.
- Merge order: generator, focused tests, graph traceability, then TASK-018
  governance and validation documents.
- Handoff output: files changed, tests run, validation evidence, blockers
  encountered or cleared, integration notes, deviations and remaining
  documentation gaps.

## Acceptance criteria

- Embedding provider selection is explicit.
- The local hash provider implements the adapter boundary.
- Unknown providers fail with a clear error.
- Candidate output records the selected provider.
- Existing embedding candidate comparison still passes.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode local-embedding-index --embedding-provider local-hash --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-018
```

## Expected Output

The implementation agent must return files changed, tests run, validation
evidence, blockers encountered or cleared, dependencies on other workstreams,
integration notes, deviations and remaining documentation gaps.
