# Context Package: TASK-019

## Target task

TASK-019: `../11_tasks/TASK-019-add-embedding-provider-safety-gates.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> TASK-019
```

## Included documents

- `../11_tasks/TASK-019-add-embedding-provider-safety-gates.md`
- `../21_execution_plans/EP-TASK-019.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-019.md`
- `../12_validation/VAL-TASK-019-embedding-provider-safety-gates.md`
- `../11_tasks/TASK-018-add-embedding-provider-adapter-boundary.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`
- `../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- `../../config/embedding_provider_gates.json`
- `../../scripts/embedding_provider_gate.py`
- `../../tests/test_embedding_provider_gate.py`

## Excluded documents

- Real provider credentials are excluded.
- External provider implementation documentation is excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Do not add a real embedding provider.
- Do not add credentials or credential values.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Agent prompt

Implement TASK-019 by adding credential, environment and sensitive-data gates
for future embedding providers.

## Parallel dispatch and blockers

- Parallelization source: `../21_execution_plans/EP-TASK-019.md`.
- Execution model in source EP: validated single-agent implementation and
  integration workstream, `WS-019`.
- Parallel dispatch list: one source-backed workstream, `WS-019: Embedding
  Provider Safety Gates`; no independent ready-now parallel workstreams are
  supported because the policy, registry, gate script, tests, package
  validation hook and graph traceability form one shared validation surface.
- Dependencies: TASK-018 provider adapter boundary and sensitive-data policy
  context are resolved upstream inputs.
- Blockers: none open.
- Owner and validation responsibility: context engine implementation and
  validation agent owns the full TASK-019 safety gate slice.
- Owned files:
  `../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`,
  `../../config/embedding_provider_gates.json`,
  `../../scripts/embedding_provider_gate.py`,
  `../../tests/test_embedding_provider_gate.py`, `../../package.json` and
  `../../graph/project_graph.example.yaml`.
- Merge order: no multi-agent merge order is required; `WS-019` is the sole
  integration workstream if the plan is re-run.
- Handoff output: changed files, tests run, validation evidence, blockers,
  integration notes, deviations and remaining documentation gaps.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_embedding_provider_gate
python3 scripts/embedding_provider_gate.py --root .
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-019
```
