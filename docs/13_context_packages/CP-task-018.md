# Context Package: TASK-018

## Target task

TASK-018: `../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> TASK-018
```

## Included documents

- `../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md`
- `../21_execution_plans/EP-TASK-018.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-018.md`
- `../12_validation/VAL-TASK-018-embedding-provider-adapter-boundary.md`
- `../11_tasks/TASK-017-implement-local-embedding-index.md`
- `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Excluded documents

- External embedding provider documentation is excluded.
- Provider credentials, secrets and real customer data are excluded.

## Constraints

- Keep provider-backed retrieval optional.
- Do not add external services in this slice.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Agent prompt

Implement TASK-018 by adding an embedding provider adapter boundary behind the
existing local embedding-index retrieval mode.

## Parallel dispatch and blockers

- Parallelization source: `../21_execution_plans/EP-TASK-018.md`.
- Execution model in source EP: standalone single-agent
  implementation/integration workstream.
- Parallel dispatch list: `WS-TASK-018-IMPL` is the only source-backed
  workstream. It owns provider boundary implementation, focused tests, graph
  traceability, TASK-018 documentation updates and validation evidence.
- Ready-now parallel goals: none beyond `WS-TASK-018-IMPL`; separate-thread
  dispatch is not applicable because the workstream touches the shared
  generator, tests and graph traceability files together.
- Dependency-gated goals: none for TASK-018. The workstream depends on already
  validated TASK-017 local embedding index behavior and TASK-014 comparison
  harness context.
- Blockers: none open for the validated local-provider adapter boundary.
- Shared-file ownership: `../../scripts/context_package_generator.py`,
  `../../tests/test_context_package_generator.py` and
  `../../graph/project_graph.example.yaml` are owned by `WS-TASK-018-IMPL`.
- Merge order: generator, focused tests, graph traceability, then TASK-018
  governance and validation documents.
- Handoff output: files changed, tests run, validation evidence, blockers
  encountered or cleared, integration notes, deviations and remaining
  documentation gaps.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode local-embedding-index --embedding-provider local-hash --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-018
```
