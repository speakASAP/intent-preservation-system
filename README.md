# Intent Preservation System

A documentation-first framework for AI-assisted project delivery.

The system preserves original project intent, decomposes it into manageable implementation units, generates bounded context for AI agents, and validates work against upstream goals.

## Repository layers

```text
Constitution
  -> Vision
  -> Vision Evolution
  -> Business Case
  -> Systems
  -> Subsystems
  -> Architecture and ADRs
  -> Roadmap and Milestones
  -> Features
  -> Tasks
  -> Goal Impact Records
  -> Execution Plans
  -> Context Packages
  -> Coding Prompts
  -> Code
  -> Validation Reports
  -> Audit
```

## Directory structure

Documentation layers live under `docs/`. Runtime code, scripts, graph, and config stay at the repository root.

docs/00_constitution/       Project laws and immutable project rules
docs/01_vision/             Immutable product vision and original intent
docs/02_business_case/      Problem, users, value, success metrics
docs/03_domain_model/       Domain concepts, glossary, actors, workflows
docs/04_systems/            Top-level systems
docs/05_subsystems/         Detailed subsystem descriptions
docs/06_architecture/       Technical architecture and integration model
docs/07_decisions/          ADRs: architecture decision records
docs/08_roadmap/            Roadmap and sequencing strategy
docs/09_milestones/         Milestone definitions and completion criteria
docs/10_features/           Feature-level requirements
docs/11_tasks/              Atomic implementation tasks
docs/12_validation/         Validation plans and reports
docs/13_context_packages/   AI-agent input packages
docs/14_prompts/            Final coding prompts
docs/15_audits/             Project documentation and implementation audits
docs/16_operations/         Developer operations, release, deployment
docs/17_governance/         Change-control, permissions, review process
docs/18_templates/          Reusable templates
docs/19_examples/           Filled examples
docs/20_semantic_compression/ Summaries and ultra-summaries
docs/21_execution_plans/    Task-to-code execution plans
docs/22_goal_impact/        Goal impact mapping
docs/23_documentation_contracts/ strict completeness rules
docs/24_onboarding/         Onboarding generation model
graph/                 Project knowledge graph schema and examples
scripts/               Utility scripts
.github/workflows/     Optional CI checks

## Main principles

1. The original vision is immutable for AI agents.
2. Humans may change the vision only through a controlled amendment process.
3. Every task must trace back to a feature, subsystem, system and vision goal.
4. Every implementation task must have validation criteria.
5. Code generation happens only after documentation decomposition is complete.
6. Context packages are generated, not manually assembled.
7. RAG is optional; graph-based retrieval is primary.
8. Documentation completeness is continuously audited.
9. No code should be generated from vague intent.
10. Code should be generated from approved execution plans that trace back to business goals and original vision.
11. Project invariants, sensitive-data handling, contract impact and replay/determinism impact must be declared before coding.
12. Operational gates produce validation evidence before coding and deployment.

## Project adoption

Do not copy the complete IPS repository into every project. Central standards,
templates and validators stay here; project intent, decisions, tasks, plans
and evidence stay in the adopting repository.

Follow
[`docs/24_onboarding/PROJECT_ADOPTION_STANDARD.md`](docs/24_onboarding/PROJECT_ADOPTION_STANDARD.md):
and the complete
[`PROJECT_DOCUMENT_SET.md`](docs/24_onboarding/PROJECT_DOCUMENT_SET.md):

1. Create the project constitution and vision.
2. Create `ips-adoption.json` from the profile template.
3. Scaffold and complete every mandatory local project artifact.
4. Review every ecosystem integration capability.
5. Run `python3 scripts/validate_adoption_profile.py --root <project> --phase planning` before implementation.
6. Run the validator with `--phase deployment` before deployment.
6. Use the full strict audit/gates in repositories that adopt the complete IPS
   documentation tree.
7. Validate every completed task against original intent.

## Local self-audit

The first supported audit mode is local-only and assumes the repository uses this exact Intent Preservation System structure.

```bash
python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues
```

The strict audit checks required repository documents, required document groups, and required sections for task, execution-plan, goal-impact, and semantic-compression artifacts. When it finds gaps, it reports severity, recommendation, and the template that should be used to generate or update missing draft content.

## Operational gates

IPS includes local operational gates for delivery controls:

```bash
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root .
```

The pre-coding gate checks immutable documents, task and execution-plan traceability, validation-plan presence, project-invariant declaration, shared DOS principles when present, and sensitive-data policy violations.

The deployment-readiness gate runs the pre-coding gate, invokes the strict documentation audit, checks validation-report evidence, reports unresolved `[MISSING: ...]` markers and verifies protected vision/constitution files when a Git baseline exists.

## Reference project pattern

DOS is documented as an IPS reference project in `docs/19_examples/DOS_AS_IPS_REFERENCE_PROJECT.md`. The example shows how a concrete decision operating system maps protected intent to goal impact, systems, features, tasks, plans, gates and validation without making TDOS-specific rules part of the IPS core.

## Suggested Git rules

- Protect `main` branch.
- Require review for changes under `docs/00_constitution/` and `docs/01_vision/`.
- Forbid direct AI commits to immutable folders.
- Require ADR updates for major architecture changes.
- Require validation reports before merging implementation work.
