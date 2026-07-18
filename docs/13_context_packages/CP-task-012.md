# Context Package: TASK-012

## Target task

TASK-012: `../11_tasks/TASK-012-harden-optional-local-retrieval.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> TASK-012
```

## Included documents

- `../11_tasks/TASK-012-harden-optional-local-retrieval.md`
- `../21_execution_plans/EP-TASK-012.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-012.md`
- `../12_validation/VAL-TASK-012-harden-optional-local-retrieval.md`
- `../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md`
- `../21_execution_plans/EP-TASK-011.md`
- `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md`
- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../17_governance/PROJECT_INVARIANTS.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Excluded documents

- Embedding providers, vector databases and external API documentation are
  excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Preserve TASK-011 report fields.
- Keep required graph context separate from optional suggestions.
- Keep all scoring deterministic and local.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Parallel dispatch status

- Source execution plan: `../21_execution_plans/EP-TASK-012.md`
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

Implement TASK-012 by adding score components, query terms, scan summary and
minimum-score filtering to local optional retrieval.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-012
```
