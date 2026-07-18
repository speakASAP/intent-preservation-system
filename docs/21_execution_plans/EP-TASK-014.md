# EP-TASK-014: Candidate Retrieval Comparison

```yaml
id: EP-TASK-014
status: validated
source_task: ../11_tasks/TASK-014-compare-candidate-retrieval-results.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-014.md
coding_prompt: ../14_prompts/PROMPT-TASK-014-candidate-retrieval-comparison.md
validation_report: ../12_validation/VAL-TASK-014-candidate-retrieval-comparison.md
```

## Metadata

This execution plan defined local comparison of candidate retrieval result files
against the deterministic baseline before semantic retrieval integration and
has been validated by
`../12_validation/VAL-TASK-014-candidate-retrieval-comparison.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-014.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan creates a measurement gate for candidate semantic retrieval results
without adding embeddings or making candidates authoritative.

## Project Invariants

- IPS-INV-001: comparison remains tied to baseline cases and task ids.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation stays bounded to local comparison.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: fixtures use synthetic data only.

## Sensitive-Data Handling

Classification: synthetic. Candidate fixtures use repository-local paths only.

## Contract Validation Plan

Add a JSON-compatible candidate comparison report with baseline path, candidate
path, retrieval mode, case results and findings.

## Replay/Determinism Plan

Sort case ids and paths deterministically. Tests compare repeated output.

## Scope

Add candidate comparison support to `scripts/context_package_generator.py`, a
synthetic candidate fixture and focused tests.

## Non-Goals

- No embeddings.
- No vector database.
- No external API calls.
- No graph-required context replacement.

## Files to Inspect

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `tests/fixtures/retrieval_baseline.json`
- `11_tasks/TASK-013-create-retrieval-evaluation-baseline.md`

## Files to Create

- `tests/fixtures/retrieval_candidate.json`
- TASK-014 documentation, context package, prompt and validation report.

## Files to Modify

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `graph/project_graph.example.yaml`
- TASK-014 documents after validation.

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Define candidate result parsing.
2. Match candidate cases to baseline cases by id.
3. Compare expected baseline paths to candidate returned paths.
4. Report missing expected paths, unexpected candidate paths and missing cases.
5. Add CLI support for candidate comparison.
6. Add focused tests and a synthetic fixture.
7. Run validation gates and update validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-014-A | Implement local candidate comparison behavior and tests | yes, as the only implementation workstream | context-engine implementation agent | `scripts/context_package_generator.py`; `tests/test_context_package_generator.py`; `tests/fixtures/retrieval_candidate.json` | Candidate comparison report and deterministic tests | none |
| WS-014-D | Update TASK-014 artifact chain and graph entries | no, dependency-gated | documentation/graph agent | TASK-014 documents and `graph/project_graph.example.yaml` | Traceable docs and validation artifacts | WS-014-A complete |
| WS-014-V | Final validation and readiness evidence | no, final integration | validation agent | `12_validation/VAL-TASK-014-candidate-retrieval-comparison.md` | Gate evidence and readiness recommendation | WS-014-A and WS-014-D complete |

WS-014-A may run in a separate Codex thread before implementation is complete.
WS-014-D and WS-014-V are dependency-gated because documentation and validation
depend on the final comparison contract.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-014-A | TASK-013 baseline contract must exist | context-engine implementation agent | Compare candidates against deterministic baseline expectations only | resolved |
| WS-014-D | Requires final candidate comparison behavior | documentation/graph agent | Update docs after WS-014-A handoff | dependency-gated |
| WS-014-V | Requires implementation and artifact evidence | validation agent | Run gates and update validation report | dependency-gated |

## Parallel Dispatch List

### Goal WS-014-A: Candidate Retrieval Comparison

- Owner role: context-engine implementation agent.
- Objective: compare candidate retrieval outputs against deterministic baseline
  expectations without making candidates authoritative.
- Allowed files: `scripts/context_package_generator.py`;
  `tests/test_context_package_generator.py`;
  `tests/fixtures/retrieval_candidate.json`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, graph-required context replacement logic and artifacts
  containing secrets or raw production data.
- Required inputs: TASK-014, this plan, TASK-013 baseline behavior and
  `tests/fixtures/retrieval_baseline.json`.
- Blockers: TASK-013 baseline contract must be available.
- Validation evidence: focused context-package tests and sample comparison CLI
  output.
- Handoff output: code/test/fixture changes, report fields, tests run, blockers
  and deviations.

### Goal WS-014-D: TASK-014 Artifact Chain

- Owner role: documentation/graph agent.
- Objective: update TASK-014 task, goal impact, execution plan, context package,
  prompt, validation report and graph entries after WS-014-A.
- Allowed files: TASK-014 documents and `graph/project_graph.example.yaml`.
- Forbidden files: protected vision/constitution files and implementation files
  unless reporting a deviation.
- Required inputs: WS-014-A handoff.
- Blockers: final comparison behavior from WS-014-A.
- Validation evidence: strict audit and artifact review.
- Handoff output: documentation/graph changes, blockers and deviations.

### Goal WS-014-V: Final Validation

- Owner role: validation agent.
- Objective: validate TASK-014 behavior and record readiness evidence.
- Allowed files:
  `12_validation/VAL-TASK-014-candidate-retrieval-comparison.md`.
- Forbidden files: protected files and implementation files unless a validation
  defect is reported.
- Required inputs: WS-014-A and WS-014-D handoffs.
- Blockers: implementation and artifact chain complete.
- Validation evidence: focused tests, sample candidate comparison CLI output,
  `npm run validate`, pre-coding gate and deployment-readiness gate for TASK-014.
- Handoff output: validation evidence and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-014-A

You are the TASK-014 context-engine implementation agent. Add deterministic
local comparison of candidate retrieval outputs against baseline expectations.
Do not add embeddings, vector search, external APIs or graph-required context
replacement. Return files changed, report fields, tests run, blockers and
deviations.

### Workstream WS-014-D

You are the TASK-014 documentation/graph agent. After WS-014-A, update only the
TASK-014 artifact chain and graph entries needed for traceability. Return files
changed, evidence, blockers and deviations.

### Workstream WS-014-V

You are the TASK-014 validation agent. After implementation and artifacts, run
focused tests, sample candidate comparison, repository validation, pre-coding
gate and deployment-readiness gate for TASK-014. Record evidence and readiness.

## Test Plan

- Test a passing candidate comparison.
- Test a failing candidate comparison.
- Test missing candidate case findings.
- Test deterministic output.

## Validation Plan

Run focused tests, sample candidate comparison CLI, `npm run validate`,
pre-coding gate and deployment-readiness gate for TASK-014.

## Gate Commands

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --compare-retrieval-candidate tests/fixtures/retrieval_baseline.json --candidate-results tests/fixtures/retrieval_candidate.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-014
```

## Documentation Updates

Update TASK-014 task, goal impact, execution plan and validation report after
implementation.

## Rollback Plan

Remove candidate comparison code, tests, fixture and TASK-014 validation status
updates.

## Agent Handoff Prompt

Implement TASK-014 by adding deterministic local comparison of candidate
retrieval outputs against baseline expectations. Preserve graph-first context
and avoid embeddings, vector search and external API calls.

## Completion Checklist

- [x] Implementation complete
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
