# Context Package: TASK-020

## Target task

TASK-020: `../11_tasks/TASK-020-add-external-provider-dry-run-contract.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> TASK-020
```

## Included documents

- `../11_tasks/TASK-020-add-external-provider-dry-run-contract.md`
- `../21_execution_plans/EP-TASK-020.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-020.md`
- `../12_validation/VAL-TASK-020-external-provider-dry-run-contract.md`
- `../11_tasks/TASK-019-add-embedding-provider-safety-gates.md`
- `../../config/embedding_provider_gates.json`
- `../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- `../../scripts/embedding_provider_gate.py`
- `../../scripts/context_package_generator.py`
- `../../tests/test_embedding_provider_gate.py`
- `../../tests/test_context_package_generator.py`

## Excluded documents

- External provider credentials are excluded.
- Real provider API documentation is excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Do not add a real external provider.
- Do not call external services.
- Do not read repository document body text for dry-run output.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Agent prompt

Implement TASK-020 by adding a dry-run external provider contract that validates
provider configuration and candidate output shape without network calls.

## Parallel dispatch and blockers

- Parallelization source: `../21_execution_plans/EP-TASK-020.md`.
- Execution model in source EP: single source-backed implementation,
  integration and validation workstream.
- Parallel dispatch list: WS-020-IMPLEMENTATION-INTEGRATION is the only
  source-backed ready-now goal. It owns the dry-run provider registry, safety
  policy, provider gate, candidate generator, focused tests, graph traceability
  and TASK-020 validation handoff.
- Dependency-gated goals: real external provider integration is outside
  TASK-020 and requires future approved work, provider credentials,
  provider-specific contracts and data-movement review.
- Blockers: none remain for validated TASK-020. Future real-provider work is
  blocked until a separate approved execution plan and data-protection review
  exist.
- Shared-file ownership: no parallel merge order is needed for TASK-020 because
  one workstream owns the shared contract surface. If future maintenance splits
  the work, merge registry and policy before gate behavior, candidate generator,
  tests, graph traceability and documentation.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_context_package_generator tests.test_embedding_provider_gate
python3 scripts/embedding_provider_gate.py --root .
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode external-provider-dry-run --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-020
```
