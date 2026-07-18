# Coding Prompt: TASK-020 External Provider Dry-Run Contract

```yaml
id: PROMPT-TASK-020-external-provider-dry-run-contract
source_task: ../11_tasks/TASK-020-add-external-provider-dry-run-contract.md
execution_plan: ../21_execution_plans/EP-TASK-020.md
context_package: ../13_context_packages/CP-task-020.md
status: used
```

## Role

You are an implementation agent adding a dry-run external provider contract for
IPS optional retrieval.

## Task

Implement TASK-020: add an external-provider dry-run pathway that validates
provider configuration, candidate output shape and comparison compatibility
without network calls or repository text transmission.

## Context

Use `../13_context_packages/CP-task-020.md` and preserve graph-first retrieval.

## Constraints

- Do not add a real external provider.
- Do not add credentials.
- Do not call external services.
- Do not read repository document body text for dry-run candidates.
- Keep dry-run output marked as non-production evidence.

## Allowed Changes

- `../../config/embedding_provider_gates.json`
- `../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- `../../scripts/embedding_provider_gate.py`
- `../../scripts/context_package_generator.py`
- `../../tests/test_embedding_provider_gate.py`
- `../../tests/test_context_package_generator.py`
- TASK-020 validation documentation.
- `../../graph/project_graph.example.yaml`

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any credential values or sensitive data.

## Implementation Instructions

1. Add an offline dry-run provider registry entry.
2. Add dry-run safety gate rules.
3. Add dry-run candidate mode.
4. Mark dry-run output and network call count.
5. Add focused tests and validate through existing gates.

## Parallel Workstream Context

This prompt is for WS-020-IMPLEMENTATION-INTEGRATION, the only source-backed
TASK-020 workstream in `../21_execution_plans/EP-TASK-020.md`.

- Source parallel dispatch list: WS-020-IMPLEMENTATION-INTEGRATION adds and
  validates the offline external-provider dry-run contract.
- Dependencies: TASK-019 provider safety gates.
- Owned files from source EP: `../../config/embedding_provider_gates.json`,
  `../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`,
  `../../scripts/embedding_provider_gate.py`,
  `../../scripts/context_package_generator.py`,
  `../../tests/test_embedding_provider_gate.py`,
  `../../tests/test_context_package_generator.py` and
  `../../graph/project_graph.example.yaml`.
- Blockers: none remain for validated TASK-020. Future real-provider work
  requires a separate approved execution plan, provider credentials,
  provider-specific contracts and data-movement review.
- Handoff output: files changed, tests run, validation evidence, blockers or
  dependencies, integration notes, deviations and remaining documentation gaps.
- Integration guidance: do not split this prompt across agents because the EP
  identifies one source-backed workstream that owns the shared contract surface.

## Acceptance criteria

- Dry-run provider registry entry passes provider safety gate.
- Dry-run candidate generation emits expected output shape.
- Dry-run candidate output reports zero network calls.
- Dry-run candidate output compares through the existing harness.
- Tests prove dry-run does not require repository document text.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_context_package_generator tests.test_embedding_provider_gate
python3 scripts/embedding_provider_gate.py --root .
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode external-provider-dry-run --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-020
```

## Expected Output

The implementation agent must return files changed, tests run, validation
evidence, blockers encountered or cleared, dependencies on other workstreams,
integration notes, deviations and remaining documentation gaps.
