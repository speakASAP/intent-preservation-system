# Context Package: TASK-016

## Target task

TASK-016: `../11_tasks/TASK-016-create-manager-visibility-interface.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-004-manager-visibility.md -> TASK-016
```

## Included documents

- `../10_features/FEAT-004-manager-visibility.md`
- `../11_tasks/TASK-016-create-manager-visibility-interface.md`
- `../21_execution_plans/EP-TASK-016.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-016.md`
- `../12_validation/VAL-TASK-016-manager-visibility-interface.md`
- `../12_validation/VALIDATION_PYRAMID.md`
- `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Excluded documents

- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.
- External dashboard, analytics and deployment services are excluded.

## Constraints

- The interface must remain static and local.
- The interface must explain traceability, comparison and validation in manager
  language.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Parallel dispatch status

- Source execution plan: `../21_execution_plans/EP-TASK-016.md`
- Dispatch readiness: ready. The execution plan includes `Parallelization Plan`,
  `Parallel Execution Strategy`, `Goal Blockers And Dependencies`, `Parallel
  Dispatch List` and `Parallel Agent Handoff Prompts`.
- Ready-now workstreams: WS-016-A governance chain documents, WS-016-B static
  manager interface and WS-016-C graph traceability entry.
- Dependency-gated workstream: WS-016-D final validation and evidence after
  WS-016-A, WS-016-B and WS-016-C complete.
- Derived prompt treatment: use the coding prompt as the validated historical
  implementation prompt, with parallel workstream context resolved from the
  execution plan.
- Blockers: no approval, credential, production data or external environment
  blocker is identified in the source artifacts; WS-016-D depends on completed
  ready-now workstreams.

## Agent prompt

Implement TASK-016 by adding a static manager-facing interface under
`../../manager_interface/`.

## Validation instructions

Run:

```bash
python3 -m unittest discover -s tests
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-016
```
