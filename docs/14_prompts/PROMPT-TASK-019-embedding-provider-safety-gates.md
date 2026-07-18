# Coding Prompt: TASK-019 Embedding Provider Safety Gates

```yaml
id: PROMPT-TASK-019-embedding-provider-safety-gates
source_task: ../11_tasks/TASK-019-add-embedding-provider-safety-gates.md
execution_plan: ../21_execution_plans/EP-TASK-019.md
context_package: ../13_context_packages/CP-task-019.md
status: used
```

## Role

You are an implementation agent adding provider safety gates for IPS optional
embedding retrieval.

## Task

Implement TASK-019: add credential, environment and sensitive-data gates before
future embedding providers can be enabled.

## Context

Use `../13_context_packages/CP-task-019.md` and preserve graph-first retrieval.

## Constraints

- Do not implement an external provider.
- Do not add real credentials.
- Do not include secrets, raw production data or customer data.
- Keep the gate dependency-free and deterministic.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`
- `../../config/embedding_provider_gates.json`
- `../../scripts/embedding_provider_gate.py`
- `../../tests/test_embedding_provider_gate.py`
- `../../package.json`
- TASK-019 validation documentation.
- `../../graph/project_graph.example.yaml`

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any credential values or sensitive data.

## Implementation Instructions

1. Add provider safety policy.
2. Add provider registry for the current local provider.
3. Add a gate that validates credentials, environment, external-network and
   data classification rules.
4. Add focused pass and fail tests.
5. Add the gate to validation coverage.

## Parallel Workstream Context

This prompt is derived from `../21_execution_plans/EP-TASK-019.md` and targets
the source-backed standalone implementation/integration workstream
`WS-019: Embedding Provider Safety Gates`.

- Source parallel dispatch list: one validated single-agent workstream,
  `WS-019`; no independent ready-now parallel workstreams are supported because
  the policy, registry, gate script, tests, package validation hook and graph
  traceability form one shared validation surface.
- Dependencies: TASK-018 provider adapter boundary and sensitive-data policy
  context are resolved upstream inputs.
- Blockers: none open.
- Owner and validation responsibility: context engine implementation and
  validation agent owns the full TASK-019 safety gate slice.
- Owned files from source EP:
  `../23_documentation_contracts/EMBEDDING_PROVIDER_SAFETY_GATES.md`,
  `../../config/embedding_provider_gates.json`,
  `../../scripts/embedding_provider_gate.py`,
  `../../tests/test_embedding_provider_gate.py`, `../../package.json` and
  `../../graph/project_graph.example.yaml`.
- Integration guidance: do not split this prompt across agents. `WS-019` is the
  sole integration workstream if the plan is re-run.
- Handoff output: changed files, tests run, validation evidence, blockers,
  integration notes, deviations and remaining documentation gaps.

## Acceptance criteria

- Provider registry exists without secrets.
- Credential mode rules are machine-checkable.
- Environment and external-network rules are machine-checkable.
- Sensitive classification is rejected for embedding providers.
- Gate tests cover passing and failing provider configurations.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_embedding_provider_gate
python3 scripts/embedding_provider_gate.py --root .
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-019
```

## Expected Output

The implementation agent must return files changed, tests run, validation
evidence, blockers encountered or cleared, dependencies on other workstreams,
integration notes, deviations and remaining documentation gaps.
