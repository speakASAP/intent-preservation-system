# FEAT-001 Documentation Audit

Parent system: SYS-003 Audit Engine

## Goal

Allow users to scan an existing project and identify missing or weak documentation.

## User story

As a project owner, I want to audit my project documentation so that I know whether the project is ready for AI-assisted implementation.

## Acceptance criteria

- The system checks required folders and files.
- The system detects missing vision, business case, systems, subsystems, ADRs, roadmap, milestones, features, tasks and validation plans.
- The system reports missing traceability.
- The system produces recommendations.
- The system proposes template-based draft generation for missing or incomplete documents.
- The system asks for human approval before creating or updating documents.

## Traceability

Vision goal: Audit existing projects and reveal weak points.

## Validation

Run the audit on a project with intentionally missing documents and verify that the report identifies them.
