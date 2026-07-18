# Context Package: TASK-013

## Target task

TASK-013: `../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> TASK-013
```

## Included documents

- `../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`
- `../21_execution_plans/EP-TASK-013.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-013.md`
- `../12_validation/VAL-TASK-013-retrieval-evaluation-baseline.md`
- `../11_tasks/TASK-012-harden-optional-local-retrieval.md`
- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Excluded documents

- Embedding providers, vector databases and external API documentation are
  excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Evaluation fixtures must be synthetic.
- Required graph context remains separate from optional suggestions.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Parallel dispatch status

- Source execution plan: `../21_execution_plans/EP-TASK-013.md`
- Dispatch readiness: the execution plan defines a parallel dispatch list and
  parallel agent handoff prompts.
- Ready-now workstreams: WS-013A retrieval evaluator and CLI, WS-013C
  documentation scaffolding.
- Dependency-gated workstreams: WS-013B tests and synthetic fixture after the
  WS-013A baseline JSON shape and report fields are available.
- Final integration: WS-013D integrates workstreams, runs validation gates and
  records evidence.
- Shared-file ownership and merge order are defined in the execution plan.
- Remaining blockers: none recorded for the validated TASK-013 implementation.

## Agent prompt

Implement TASK-013 by adding deterministic retrieval baseline evaluation.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --evaluate-retrieval tests/fixtures/retrieval_baseline.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-013
```
