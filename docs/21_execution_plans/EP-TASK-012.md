# EP-TASK-012: Harden Optional Local Retrieval

```yaml
id: EP-TASK-012
status: validated
source_task: ../11_tasks/TASK-012-harden-optional-local-retrieval.md
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
context_package: ../13_context_packages/CP-task-012.md
coding_prompt: ../14_prompts/PROMPT-TASK-012-harden-optional-local-retrieval.md
validation_report: ../12_validation/VAL-TASK-012-harden-optional-local-retrieval.md
```

## Metadata

This execution plan defined a bounded hardening slice for TASK-012 before any
embedding or vector-search implementation and has been validated by
`../12_validation/VAL-TASK-012-harden-optional-local-retrieval.md`.

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../10_features/FEAT-003-optional-rag-retrieval.md
milestone: ../09_milestones/MS-005-rag-integration.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-012.md
system: ../04_systems/SYS-002-context-engine.md
architecture: ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
adr: ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
```

## Goal Impact

The plan improves optional retrieval transparency while preserving graph-first
context. It gives future semantic retrieval a deterministic baseline.

## Project Invariants

- IPS-INV-001: retrieval output remains traceable to the target task.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation is bounded to local retrieval hardening.
- IPS-INV-004: validation evidence is captured before closure.
- IPS-INV-005: fixtures and reports avoid secrets and raw production data.

## Sensitive-Data Handling

Classification: none. Tests use synthetic fixture documents and repository-local
Markdown only.

## Contract Validation Plan

Preserve TASK-011 report fields and add backward-compatible fields for query
terms, scan summary and score components.

## Replay/Determinism Plan

Use deterministic token scoring and stable path tie-breaking. Tests must compare
repeated output.

## Scope

Harden `scripts/context_package_generator.py` optional retrieval report and
focused tests.

## Non-Goals

- No embeddings.
- No vector database.
- No external API calls.
- No graph-required context replacement.

## Files to Inspect

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- `11_tasks/TASK-011-define-optional-rag-retrieval-contract.md`
- `21_execution_plans/EP-TASK-011.md`

## Files to Create

- TASK-012 documentation, context package, prompt and validation report.

## Files to Modify

- `scripts/context_package_generator.py`
- `tests/test_context_package_generator.py`
- TASK-012 documentation after validation.
- `graph/project_graph.example.yaml`

## Files That Must Not Be Modified

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Implementation Steps

1. Add score component details to optional suggestions.
2. Add query terms and scan summary to the report.
3. Add minimum-score filtering to function and CLI.
4. Preserve TASK-011 report fields.
5. Add focused tests.
6. Run validation gates and update validation evidence.

## Parallel Execution Strategy

| Workstream | Goal | Can start in parallel? | Recommended agent/session | Allowed files | Expected output | Integration dependency |
| --- | --- | --- | --- | --- | --- | --- |
| WS-012-A | Harden optional retrieval report behavior and tests | yes, as the only implementation workstream | context-engine implementation agent | `scripts/context_package_generator.py`; `tests/test_context_package_generator.py` | Backward-compatible report fields, score details and filters | none |
| WS-012-D | Update TASK-012 artifact chain and graph entries | no, dependency-gated | documentation/graph agent | TASK-012 documents and `graph/project_graph.example.yaml` | Traceable docs and validation artifacts | WS-012-A complete |
| WS-012-V | Final validation and readiness evidence | no, final integration | validation agent | `12_validation/VAL-TASK-012-harden-optional-local-retrieval.md` | Gate evidence and readiness recommendation | WS-012-A and WS-012-D complete |

WS-012-A may run in a separate Codex thread before implementation is complete.
WS-012-D and WS-012-V are dependency-gated because they depend on the final
retrieval report contract.

## Goal Blockers And Dependencies

| Workstream | Blocker or dependency | Owner | Required resolution | Status |
| --- | --- | --- | --- | --- |
| WS-012-A | TASK-011 optional retrieval contract must remain compatible | context-engine implementation agent | Preserve TASK-011 fields and graph-required context separation | resolved |
| WS-012-D | Requires final report fields and CLI behavior | documentation/graph agent | Update docs after WS-012-A handoff | dependency-gated |
| WS-012-V | Requires implementation and artifact evidence | validation agent | Run gates and update validation report | dependency-gated |

## Parallel Dispatch List

### Goal WS-012-A: Optional Retrieval Hardening

- Owner role: context-engine implementation agent.
- Objective: add score components, query terms, scan summary and minimum-score
  filtering while preserving TASK-011 compatibility.
- Allowed files: `scripts/context_package_generator.py`;
  `tests/test_context_package_generator.py`.
- Forbidden files: `00_constitution/CONSTITUTION.md`,
  `01_vision/VISION.md`, graph-required context contracts and artifacts
  containing secrets or raw production data.
- Required inputs: TASK-012, this plan, TASK-011 contract and ADR-002.
- Blockers: TASK-011 compatibility must be preserved.
- Validation evidence: focused context-package tests and sample CLI output.
- Handoff output: code/test changes, report fields, tests run, blockers and
  deviations.

### Goal WS-012-D: TASK-012 Artifact Chain

- Owner role: documentation/graph agent.
- Objective: update TASK-012 task, goal impact, execution plan, context package,
  prompt, validation report and graph entries after WS-012-A.
- Allowed files: TASK-012 documents and `graph/project_graph.example.yaml`.
- Forbidden files: protected vision/constitution files and implementation files
  unless reporting a deviation.
- Required inputs: WS-012-A handoff.
- Blockers: final report fields from WS-012-A.
- Validation evidence: strict audit and artifact review.
- Handoff output: documentation/graph changes, blockers and deviations.

### Goal WS-012-V: Final Validation

- Owner role: validation agent.
- Objective: validate TASK-012 behavior and record readiness evidence.
- Allowed files: `12_validation/VAL-TASK-012-harden-optional-local-retrieval.md`.
- Forbidden files: protected files and implementation files unless a validation
  defect is reported.
- Required inputs: WS-012-A and WS-012-D handoffs.
- Blockers: implementation and artifact chain complete.
- Validation evidence: focused tests, `npm run validate`, pre-coding gate and
  deployment-readiness gate for TASK-012.
- Handoff output: validation evidence and readiness recommendation.

## Parallel Agent Handoff Prompts

### Workstream WS-012-A

You are the TASK-012 context-engine implementation agent. Harden optional local
retrieval reporting with score components, query terms, scan summary and
minimum-score filtering. Preserve TASK-011 fields and graph-required context
separation. Return files changed, report fields, tests run, blockers and
deviations.

### Workstream WS-012-D

You are the TASK-012 documentation/graph agent. After WS-012-A, update only the
TASK-012 artifact chain and graph entries needed for traceability. Return files
changed, evidence, blockers and deviations.

### Workstream WS-012-V

You are the TASK-012 validation agent. After implementation and artifacts, run
focused tests, repository validation, pre-coding gate and deployment-readiness
gate for TASK-012. Record evidence and readiness.

## Test Plan

- Test score component metadata.
- Test minimum-score filtering.
- Test report scan summary.
- Test deterministic output remains stable.
- Run full repository validation.

## Validation Plan

Run focused context-package tests, sample CLI output, `npm run validate`,
pre-coding gate and deployment-readiness gate for TASK-012.

## Gate Commands

```bash
python3 -m unittest tests.test_context_package_generator
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-012
```

## Documentation Updates

Update TASK-012 task, goal impact, execution plan and validation report after
implementation.

## Rollback Plan

Revert TASK-012 code, tests and validation status updates. Leave TASK-011
retrieval behavior intact.

## Agent Handoff Prompt

Implement TASK-012 by hardening local optional retrieval reporting with score
components, query terms, scan summary and minimum-score filtering. Preserve
TASK-011 fields and keep graph-required context separate.

## Completion Checklist

- [x] Implementation complete
- [x] Tests complete
- [x] Validation evidence collected
- [x] Documentation updated
- [x] Deviations documented
