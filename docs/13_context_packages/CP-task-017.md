# Context Package: TASK-017

## Target task

TASK-017: `../11_tasks/TASK-017-implement-local-embedding-index.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> TASK-017
```

## Included documents

- `../11_tasks/TASK-017-implement-local-embedding-index.md`
- `../21_execution_plans/EP-TASK-017.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-017.md`
- `../12_validation/VAL-TASK-017-local-embedding-index.md`
- `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Excluded documents

- External embedding provider documentation is excluded.
- Vector database documentation is excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Keep retrieval candidates optional and non-authoritative.
- Do not add external services.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Agent prompt

Implement TASK-017 by adding deterministic local embedding-index candidate
generation compatible with the candidate comparison harness.

## Parallel dispatch and blockers

- Parallelization source: `../21_execution_plans/EP-TASK-017.md`.
- Execution model in source EP: one validated
  `WS-017-implementation-integration` workstream.
- Ready-now parallel goals: none. The source EP states no independent
  ready-now parallel goals are source-supported because the validated task
  centers on shared generator, test and candidate-contract files.
- Dependency-gated goals: none. TASK-014 comparison harness and TASK-015 local
  semantic adapter context are already available.
- Blockers: none remaining.
- Shared-file ownership: `../../scripts/context_package_generator.py`,
  `../../tests/test_context_package_generator.py` and
  `../../graph/project_graph.example.yaml` belong to the single TASK-017
  implementation/integration workstream.
- Merge order if follow-up work later splits this area:
  `../../scripts/context_package_generator.py`, then
  `../../tests/test_context_package_generator.py`, then
  `../../graph/project_graph.example.yaml`, then validation documentation.
- Handoff output expected from the workstream: files changed, tests run,
  validation evidence, blockers encountered or cleared, dependency notes,
  integration notes, deviations and remaining documentation gaps.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode local-embedding-index --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-017
```
