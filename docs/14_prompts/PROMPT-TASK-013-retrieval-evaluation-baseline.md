# Coding Prompt: TASK-013 Retrieval Evaluation Baseline

```yaml
id: PROMPT-TASK-013-retrieval-evaluation-baseline
source_task: ../11_tasks/TASK-013-create-retrieval-evaluation-baseline.md
execution_plan: ../21_execution_plans/EP-TASK-013.md
context_package: ../13_context_packages/CP-task-013.md
status: used
```

## Role

You are an implementation agent adding deterministic retrieval evaluation for
IPS optional retrieval.

## Task

Implement TASK-013: evaluate optional retrieval against local synthetic baseline
cases.

## Context

Use `../13_context_packages/CP-task-013.md` and preserve the TASK-012 retrieval
contract.

## Constraints

- Do not add embeddings, vector search or external API calls.
- Use synthetic fixtures only.
- Preserve graph-required context separation.
- Keep output deterministic.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../../tests/fixtures/retrieval_baseline.json`
- TASK-013 validation documentation.

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any fixture, prompt or report containing secrets or raw production data.

## Implementation Instructions

1. Add baseline case parsing.
2. Evaluate optional retrieval for each case.
3. Compare expected and returned optional suggestion paths.
4. Return case-level pass/fail, missing and unexpected paths.
5. Add CLI support and focused tests.

## Parallel Workstream Context

- Prompt type: historical single-agent implementation prompt for the validated
  TASK-013 implementation.
- Source execution plan: `../21_execution_plans/EP-TASK-013.md` now defines
  parallel dispatch metadata, including ready-now, dependency-gated and final
  integration workstreams.
- Ready-now workstreams: WS-013A retrieval evaluator and CLI, WS-013C
  documentation scaffolding.
- Dependency-gated workstream: WS-013B tests and synthetic fixture after WS-013A
  confirms the baseline JSON shape and report fields.
- Final integration workstream: WS-013D runs focused tests, sample CLI output,
  repository validation, pre-coding gate and deployment-readiness gate, then
  records evidence.
- Owned files, forbidden files, blockers, validation evidence, expected handoff
  outputs and merge order are defined in the execution plan's parallel dispatch
  sections.
- Remaining blockers: none recorded for the validated TASK-013 implementation.

## Acceptance criteria

- A local command evaluates retrieval cases from a JSON baseline file.
- Reports include case-level pass/fail, expected, returned, missing and
  unexpected documents.
- Missing task cases produce structured findings.
- Evaluation output is deterministic.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --evaluate-retrieval tests/fixtures/retrieval_baseline.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-013
```

## Expected Output

The implementation agent must return:

- Files changed.
- Documents created.
- Missing sections filled.
- Remaining missing-information markers.
- Validation evidence.
- Blockers encountered or cleared.
- Dependencies on other agent workstreams.
- Integration or merge notes.
- Deviations from plan.
