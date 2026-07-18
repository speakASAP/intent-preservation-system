# AI Agent Rules

## Purpose

These rules define what AI agents may and may not do inside this documentation-first project system.

## Immutable documents

Agents must not modify:

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

Changes to project intent must be proposed in:

- `01_vision/VISION_EVOLUTION.md`

## Required work chain

Agents must preserve this chain:

```text
Vision -> Goal Impact -> System -> Feature -> Task -> Execution Plan -> Coding Prompt -> Code -> Validation
```

## Before coding

An agent must verify:

- Task exists.
- Task has upstream traceability.
- Task has goal impact mapping.
- Execution plan exists and is approved or explicitly marked as draft work.
- Context package is available or can be generated.
- Validation criteria are explicit.
- Parallelizable goals or workstreams are listed, or the plan explains why no parallel work is available.
- Blockers and serial dependencies are explicit.
- Applicable project invariants are declared or explicitly marked not applicable.
- Sensitive-data classification is declared.
- Contract/schema and replay/determinism impact are declared.
- Required operational gates are named.
- Shared-file, shared-schema or shared-contract ownership is assigned when multiple agents may work in parallel.

If cross-repository alignment is in scope, agents must also verify the applicable shared-principles document. For DOS alignment, use `17_governance/SHARED_PRINCIPLES_WITH_DOS.md` and preserve the boundary that DOS is a reference project, not the source of truth for IPS.

## Documentation gap behavior

If documentation is incomplete, the agent must follow:

- `23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`

The agent may add missing sections to mutable documents. If it cannot infer content from approved sources, it must add `[MISSING: ...]` or `[UNKNOWN: ...]` markers.

## Parallel planning behavior

Planning agents must maximize safe use of parallel coding agents. Before producing coding prompts, the planner must:

- decompose work by independent goals or workstreams;
- label each workstream as ready now, dependency-gated, blocked, or final integration;
- list blockers and the exact resolution needed for blocked workstreams;
- create separate handoff prompts for workstreams that can start in parallel;
- when thread-management tools are available, start each ready-now parallel workstream in a separate Codex thread instead of running those workstreams sequentially in one conversation;
- identify a merge or integration owner when workstreams touch shared files, contracts, schemas, gates, generated artifacts or user-facing workflows.

Agents must not assign parallel workstreams that require uncoordinated edits to the same protected files, immutable intent documents, contract schemas or validation gates.

## Derived artifact fidelity

Summaries, ultra-summaries, generated prompts, context packages and audit reports are derived artifacts. Agents must preserve the source artifact's meaning instead of optimizing for checklist compliance.

When editing semantic compression documents, agents must:

- Read the full source document first.
- Use only information present in the source document unless a separate section explicitly says the information comes from another linked source.
- Keep summaries within the compression limits defined in `20_semantic_compression/SEMANTIC_COMPRESSION_GUIDE.md`.
- Prefer changing an incorrect audit rule over bloating a compressed document to satisfy the audit.
- Mark compressed documents as `ai-draft` unless a human has reviewed fidelity.

## Forbidden behavior

Agents must not:

- Invent business goals.
- Invent approvals.
- Remove traceability.
- Change ADR decisions without creating a new ADR proposal.
- Convert vague tasks directly into code.
- Skip execution plans.
- Collapse independent goals into a serial plan when they can be safely assigned to separate agents.
- Start parallel workstreams that touch the same file, shared schema or public contract unless the plan defines an integration owner and conflict-resolution order.
- Skip validation.
- Put secrets, raw production data, confidential identifiers or real customer data into prompts, tests, examples, logs, screenshots, plans or reports.
- Use production samples for local tests or contract examples unless a human-approved secure workflow outside AI prompts explicitly allows it.
- Modify files outside execution-plan scope without reporting deviation.
- Add architecture, ADR, roadmap or implementation decisions to a compressed vision document unless those decisions are present in the source vision.

## Cross-agent automation and validation debt

Agents that coordinate work across repositories or multiple worker sessions must follow `17_governance/CROSS_AGENT_AUTOMATION_STANDARD.md`. The standard separates readiness scanning, bounded worker execution, worker monitoring, and integration validation so agents do not race shared files or repeatedly rediscover known blockers.

Known repo-wide or out-of-scope validation failures must be recorded in a validation-debt ledger based on `18_templates/VALIDATION_DEBT_LEDGER_TEMPLATE.md`. Validation debt never excuses failures introduced by the current task.

## Required final report

After completing work, the agent must report:

- Files changed
- Documents created
- Missing sections filled
- Remaining `[MISSING: ...]` markers
- Validation evidence
- Deviations from plan
