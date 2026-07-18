# Context Package: TASK-014

## Target task

TASK-014: `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> TASK-014
```

## Included documents

- `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `../21_execution_plans/EP-TASK-014.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-014.md`
- `../12_validation/VAL-TASK-014-candidate-retrieval-comparison.md`
- `../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`
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

- Candidate fixtures must be synthetic.
- Candidate retrieval remains optional and non-authoritative.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Parallel dispatch status

- Source execution plan: `../21_execution_plans/EP-TASK-014.md`
- Dispatch readiness: [MISSING: source execution plan does not include a
  `Parallel Dispatch List` or `Parallel Agent Handoff Prompts` section after the
  parallel-agent execution-plan refactor.]
- Derived prompt treatment: use the coding prompt as a single-agent
  implementation prompt until the execution plan is refactored with explicit
  workstream ownership.
- Blockers: [MISSING: workstream owners, per-workstream allowed files,
  per-workstream forbidden files, blockers, validation evidence and handoff
  outputs.]

## Agent prompt

Implement TASK-014 by adding deterministic candidate retrieval comparison.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --compare-retrieval-candidate tests/fixtures/retrieval_baseline.json --candidate-results tests/fixtures/retrieval_candidate.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-014
```
