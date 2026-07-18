# Coding Prompt: TASK-014 Candidate Retrieval Comparison

```yaml
id: PROMPT-TASK-014-candidate-retrieval-comparison
source_task: ../11_tasks/TASK-014-compare-candidate-retrieval-results.md
execution_plan: ../21_execution_plans/EP-TASK-014.md
context_package: ../13_context_packages/CP-task-014.md
status: used
```

## Role

You are an implementation agent adding local candidate retrieval comparison for
IPS optional retrieval.

## Task

Implement TASK-014: compare candidate retrieval result files against the
deterministic retrieval baseline.

## Context

Use `../13_context_packages/CP-task-014.md` and preserve the TASK-013 baseline
contract.

## Constraints

- Do not add embeddings, vector search or external API calls.
- Use synthetic fixtures only.
- Candidate retrieval remains optional and non-authoritative.
- Keep output deterministic.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- `../../tests/fixtures/retrieval_candidate.json`
- TASK-014 validation documentation.

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any fixture, prompt or report containing secrets or raw production data.

## Implementation Instructions

1. Add candidate result parsing.
2. Match candidate cases to baseline cases by id.
3. Compare expected baseline paths to candidate paths.
4. Return case-level pass/fail, missing expected paths and unexpected candidate
   paths.
5. Add CLI support and focused tests.

## Parallel Workstream Context

- Prompt type: implementation prompt derived from a source execution plan that
  now exposes refactored parallel dispatch metadata.
- Source blocker: none; `../21_execution_plans/EP-TASK-014.md` includes
  Parallel Dispatch List, Goal Blockers And Dependencies and Parallel Agent
  Handoff Prompts.
- Dependencies: use the serial dependencies and files listed in the execution
  plan; `WS-014-A` depends on the TASK-013 baseline contract, and
  `WS-014-D`/`WS-014-V` depend on the implementation handoff.
- Owned files: `WS-014-A` owns implementation/test/fixture files; `WS-014-D`
  owns TASK-014 artifact and graph updates; `WS-014-V` owns final validation evidence.
- Expected handoff: return validation evidence, remaining blockers,
  dependencies on other agent workstreams and integration notes.

## Acceptance criteria

- A local command compares candidate retrieval results to a baseline file.
- Reports include case-level pass/fail, missing expected paths and unexpected
  candidate paths.
- Missing candidate cases produce structured findings.
- Comparison output is deterministic.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --compare-retrieval-candidate tests/fixtures/retrieval_baseline.json --candidate-results tests/fixtures/retrieval_candidate.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-014
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
