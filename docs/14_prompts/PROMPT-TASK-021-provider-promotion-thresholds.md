# Coding Prompt: TASK-021 Provider Promotion Thresholds

```yaml
id: PROMPT-TASK-021-provider-promotion-thresholds
source_task: ../11_tasks/TASK-021-add-provider-promotion-thresholds.md
execution_plan: ../21_execution_plans/EP-TASK-021.md
context_package: ../13_context_packages/CP-task-021.md
status: used
```

## Role

You are an implementation agent adding provider promotion rules for IPS optional
retrieval providers.

## Task

Implement TASK-021: add provider comparison thresholds and promotion rules so a
candidate can graduate from experimental to approved candidate only after
passing configured gates.

## Context

Use `../13_context_packages/CP-task-021.md` and preserve graph-first retrieval.

## Constraints

- Do not add real provider calls.
- Do not add credentials.
- Do not change retrieval ranking.
- Keep promotion fixtures synthetic and path-only.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../config/provider_promotion_rules.json`
- `../../scripts/provider_promotion_gate.py`
- `../../tests/test_provider_promotion_gate.py`
- `../../tests/fixtures/retrieval_candidate_dry_run.json`
- `../../package.json`
- TASK-021 validation documentation.
- `../../graph/project_graph.example.yaml`

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any credential values or sensitive data.

## Implementation Instructions

1. Add provider promotion rule config.
2. Add promotion gate that combines comparison and provider safety status.
3. Enforce pass rate, failed case, unexpected path, dry-run and network limits.
4. Add focused pass and fail tests.
5. Validate with repository gates.

## Parallel Workstream Context

This prompt is for the source-backed `TASK-021-IMPL` single
implementation/integration workstream in `../21_execution_plans/EP-TASK-021.md`.
No additional parallel workstreams are source-supported because the rule config,
promotion gate, fixture and tests form one cohesive promotion-gate slice.

- Owner role: context-engine implementation and validation agent.
- Dependencies: TASK-020 external provider dry-run contract, TASK-021 task,
  GOAL-IMPACT-TASK-021, static retrieval baseline fixture and provider safety
  gate behavior.
- Blockers: none open; the TASK-020 dry-run contract dependency is resolved.
- Owned files from source EP: `../../config/provider_promotion_rules.json`,
  `../../scripts/provider_promotion_gate.py`,
  `../../tests/test_provider_promotion_gate.py`,
  `../../tests/fixtures/retrieval_candidate_dry_run.json`, `../../package.json`,
  `../../graph/project_graph.example.yaml`, TASK-021 task, goal impact, execution
  plan, context package, prompt and validation report.
- Forbidden files: `../00_constitution/CONSTITUTION.md`,
  `../01_vision/VISION.md`, credential files, real provider outputs, unrelated
  task ranges and unrelated architecture or ADR documents.
- Integration guidance: if replayed, merge promotion rules and dry-run fixture
  first, then promotion gate and focused tests, `../../package.json` validation
  coverage, `../../graph/project_graph.example.yaml` and TASK-021 documentation,
  then validation report evidence.
- Expected handoff output: files changed, tests run, validation evidence,
  blockers encountered or cleared, dependencies, integration notes, deviations
  and remaining documentation gaps.

## Acceptance criteria

- Promotion rules define required mode, pass rate and failure thresholds.
- Promotion gate checks provider safety gate status.
- Promotion gate checks dry-run and zero-network requirements.
- Promotion gate rejects failed comparisons and wrong candidate modes.
- Promotion gate passes the dry-run candidate fixture.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_provider_promotion_gate
python3 scripts/provider_promotion_gate.py --root . --baseline tests/fixtures/retrieval_baseline.json --candidate tests/fixtures/retrieval_candidate_dry_run.json --provider external-provider-dry-run
python3 scripts/embedding_provider_gate.py --root .
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-021
```

## Expected Output

The implementation agent must return files changed, tests run, validation
evidence, blockers encountered or cleared, dependencies on other workstreams,
integration notes, deviations and remaining documentation gaps.
