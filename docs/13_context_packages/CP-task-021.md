# Context Package: TASK-021

## Target task

TASK-021: `../11_tasks/TASK-021-add-provider-promotion-thresholds.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> TASK-021
```

## Included documents

- `../11_tasks/TASK-021-add-provider-promotion-thresholds.md`
- `../21_execution_plans/EP-TASK-021.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-021.md`
- `../12_validation/VAL-TASK-021-provider-promotion-thresholds.md`
- `../11_tasks/TASK-020-add-external-provider-dry-run-contract.md`
- `../../config/provider_promotion_rules.json`
- `../../scripts/provider_promotion_gate.py`
- `../../tests/test_provider_promotion_gate.py`
- `../../tests/fixtures/retrieval_candidate_dry_run.json`
- `../../scripts/embedding_provider_gate.py`

## Excluded documents

- Provider credentials are excluded.
- Real external provider outputs are excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Do not add real provider calls.
- Do not add credentials.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Agent prompt

Implement TASK-021 by adding provider promotion thresholds and comparison rules
for dry-run and future provider candidates.

## Parallel dispatch and blockers

- Parallelization source: `../21_execution_plans/EP-TASK-021.md`.
- Execution model in source EP: single implementation/integration workstream.
- Ready-now dispatch goal: `TASK-021-IMPL`, owned by a context-engine
  implementation and validation agent.
- Objective: add provider promotion thresholds and comparison rules so dry-run
  and future provider candidates can be promoted only after passing configured
  safety, comparison, dry-run and zero-network gates.
- Allowed files: `../../config/provider_promotion_rules.json`,
  `../../scripts/provider_promotion_gate.py`,
  `../../tests/test_provider_promotion_gate.py`,
  `../../tests/fixtures/retrieval_candidate_dry_run.json`, `../../package.json`,
  `../../graph/project_graph.example.yaml`, TASK-021 task, goal impact, execution
  plan, context package, prompt and validation report.
- Forbidden files: `../00_constitution/CONSTITUTION.md`,
  `../01_vision/VISION.md`, credential files, real provider outputs, unrelated
  task ranges and unrelated architecture or ADR documents.
- Dependencies: TASK-020 external provider dry-run contract, TASK-021 task,
  GOAL-IMPACT-TASK-021, static retrieval baseline fixture and provider safety
  gate behavior.
- Blockers: none open; the TASK-020 dry-run contract dependency is resolved.
- Integration guidance: do not split this workstream across agents unless a
  future plan creates independent ownership boundaries. The EP states that the
  rule config, gate script, fixture and tests form one cohesive promotion-gate
  slice.
- Merge order if replayed: promotion rules and dry-run fixture, promotion gate
  and focused tests, `../../package.json` validation coverage,
  `../../graph/project_graph.example.yaml` and TASK-021 documentation, then
  validation report evidence.
- Expected handoff output: files changed, tests run, validation evidence,
  blockers encountered or cleared, integration notes, deviations and remaining
  documentation gaps.

## Validation instructions

Run:

```bash
python3 -m unittest tests.test_provider_promotion_gate
python3 scripts/provider_promotion_gate.py --root . --baseline tests/fixtures/retrieval_baseline.json --candidate tests/fixtures/retrieval_candidate_dry_run.json --provider external-provider-dry-run
python3 scripts/embedding_provider_gate.py --root .
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-021
```
