# Intent Preservation System agent instructions

## Project identity

Intent Preservation System is a documentation-first framework for AI-assisted project delivery. It preserves original project intent, decomposes it into bounded implementation units, generates context for AI agents, and validates work against upstream goals.

## Core governance

- The original vision is immutable for AI agents.
- Do not modify `docs/00_constitution/CONSTITUTION.md` or `docs/01_vision/VISION.md`.
- Human intent changes belong in `docs/01_vision/VISION_EVOLUTION.md`.
- Preserve the chain:

```text
Vision -> Goal Impact -> System -> Feature -> Task -> Execution Plan -> Coding Prompt -> Code -> Validation
```

## Before coding

Verify that the task has:

- Upstream traceability.
- Goal impact mapping.
- An execution plan that is approved or explicitly marked as draft work.
- A context package, or enough source material to generate one.
- Explicit validation criteria.
- Applicable project invariants.
- Sensitive-data classification.
- Contract/schema and replay/determinism impact.
- Required operational gates named.
- Parallelizable goals or workstreams, blockers, serial dependencies, and integration ownership when the work can be split across agents.

For DOS alignment work, read `docs/17_governance/SHARED_PRINCIPLES_WITH_DOS.md` and preserve the boundary that DOS is a reference project, not the IPS source of truth.

## Planning for parallel agents

When creating or refactoring plans, maximize safe parallel execution while preserving the project traceability chain:

- Split work into independent goal workstreams that can be started by separate agents.
- Mark each workstream as ready now, dependency-gated, blocked, or final integration.
- State blockers explicitly, including the exact dependency, decision, credential, environment, file, or validation evidence that unblocks the workstream.
- Give each parallel workstream its own allowed files, forbidden files, validation evidence, expected output, and handoff prompt.
- Add an integration workstream when parallel agents touch shared behavior, shared files, contracts, schemas, gates, generated artifacts, or documentation indexes.
- When thread-management tools are available, start each ready-now parallel workstream in a separate Codex thread so parallel plans are implemented in parallel instead of being serialized in one conversation.
- Mark unknown blockers or dependencies with `[MISSING: ...]` or `[UNKNOWN: ...]` instead of inventing details.

Do not serialize independent work without documenting the reason. Do not assign two agents to the same protected or contract-bearing artifact without a merge owner and conflict-resolution order.

## Documentation gap behavior

Follow:

- `docs/23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `docs/23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`

Agents may add missing sections to mutable documents. If content cannot be inferred from approved sources, add `[MISSING: ...]` or `[UNKNOWN: ...]` markers instead of inventing details.

## Derived artifact fidelity

Summaries, ultra-summaries, generated prompts, context packages, and audit reports are derived artifacts. Preserve the source artifact's meaning.

When editing semantic compression documents:

- Read the full source document first.
- Use only information present in the source document unless a separate section explicitly cites another linked source.
- Keep summaries within limits defined in `docs/20_semantic_compression/SEMANTIC_COMPRESSION_GUIDE.md`.
- Prefer fixing an incorrect audit rule over bloating compressed documents to satisfy an audit.
- Mark compressed documents as `ai-draft` unless a human has reviewed fidelity.

## Forbidden behavior

Do not:

- Invent business goals or approvals.
- Remove traceability.
- Change ADR decisions without creating a new ADR proposal.
- Convert vague tasks directly into code.
- Skip execution plans or validation.
- Put secrets, raw production data, confidential identifiers, or real customer data into prompts, tests, examples, logs, screenshots, plans, or reports.
- Modify files outside execution-plan scope without reporting the deviation.

## Cross-agent automation standard

Agents must also follow `docs/17_governance/CROSS_AGENT_AUTOMATION_STANDARD.md` when planning, automating, delegating, monitoring, or integrating work across repositories. Repositories adopting IPS should keep a repo-local `AGENT_OPERATIONS.md` or equivalent pointer so Codex, Claude Code, Copilot, Cursor, and other agents use the same operating model. Known out-of-scope validation failures must be tracked with the validation-debt ledger template in `docs/18_templates/VALIDATION_DEBT_LEDGER_TEMPLATE.md`.

## Essential commands

```bash
python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root .
```

Run the narrowest relevant checks for the change. For governance, traceability, or deployment-readiness changes, run all three commands if the scripts are present and executable.

## Required final report

After completing work, report:

- Files changed.
- Documents created.
- Missing sections filled.
- Remaining `[MISSING: ...]` markers.
- Validation evidence.
- Deviations from plan.
