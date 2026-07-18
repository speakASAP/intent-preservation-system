# Context Package: TASK-015

## Target task

TASK-015: `../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> TASK-015
```

## Included documents

- `../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`
- `../21_execution_plans/EP-TASK-015.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-015.md`
- `../12_validation/VAL-TASK-015-local-semantic-candidate-adapter.md`
- `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `../../tests/fixtures/retrieval_baseline.json`
- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Excluded documents

- Embedding providers, vector databases and external API documentation are
  excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Candidate output remains optional and non-authoritative.
- Do not add external services.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Parallel dispatch status

- Source execution plan: `../21_execution_plans/EP-TASK-015.md`
- Dispatch readiness: resolved in the execution plan through
  `Parallelization Plan`, `Parallel Execution Strategy`,
  `Goal Blockers And Dependencies`, `Parallel Dispatch List` and
  `Parallel Agent Handoff Prompts`.
- Workstream split: WS-015-A owns local adapter implementation in
  `../../scripts/context_package_generator.py`; WS-015-B owns focused tests and
  comparison compatibility in `../../tests/test_context_package_generator.py`;
  WS-015-C owns final documentation, gate execution and validation evidence.
- Derived prompt treatment: the existing coding prompt remains the original
  used single-agent prompt, with parallel workstream context now sourced from
  the refactored execution plan.
- Blockers: no current TASK-015 blockers remain because implementation and
  validation are complete. For replay, WS-015-C is dependency-gated on
  WS-015-A and WS-015-B handoff evidence.

## Agent prompt

Implement TASK-015 by adding deterministic local candidate generation compatible
with the candidate comparison harness.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-015
```
