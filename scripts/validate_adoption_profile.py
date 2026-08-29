#!/usr/bin/env python3
"""Validate a project's lightweight IPS adoption profile."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CAPABILITIES = {
    "auth",
    "postgres",
    "redis",
    "logging",
    "notifications",
    "ai",
    "payments",
    "catalog",
    "orders",
    "warehouse",
    "invoices",
    "object-storage",
    "event-bus",
    "docs-rag",
    "monitoring",
    "backups",
}
REQUIRED_ARTIFACT_PATHS = {
    "readme": "README.md",
    "business": "BUSINESS.md",
    "system": "SYSTEM.md",
    "agents": "AGENTS.md",
    "operations": "AGENT_OPERATIONS.md",
    "claude": "CLAUDE.md",
    "tasks": "TASKS.md",
    "state": "STATE.json",
    "constitution": "docs/00_constitution/CONSTITUTION.md",
    "vision": "docs/01_vision/VISION.md",
    "integrationContract": "docs/06_architecture/INTEGRATION_CONTRACT.md",
    "projectInvariants": "docs/17_governance/PROJECT_INVARIANTS.md",
    "validationDebt": "docs/orchestrator/VALIDATION_DEBT.md",
    "bootstrapTask": "docs/11_tasks/TASK-001-bootstrap-service.md",
    "bootstrapGoalImpact": "docs/22_goal_impact/GOAL-IMPACT-TASK-001.md",
    "bootstrapExecutionPlan": "docs/21_execution_plans/EP-TASK-001-bootstrap-service.md",
    "bootstrapValidation": "docs/12_validation/VAL-TASK-001-bootstrap-service.md",
}
PLACEHOLDER = re.compile(r"REPLACE_ME|REPLACE_WITH_|REQUIRED_OR_NOT_APPLICABLE|\[(?:MISSING|UNKNOWN)(?::|\])", re.I)
DOCUMENT_PLACEHOLDER = re.compile(
    r"REPLACE_ME|REPLACE_WITH_|REQUIRED_OR_NOT_APPLICABLE|YYYY-MM-DD|\bTBD\b|(?:TASK|EP-TASK|GOAL-IMPACT|VAL)-XXX",
    re.I,
)
PROTECTED_ARTIFACTS = {"business", "constitution", "vision"}
TRACEABILITY_REFERENCES = {
    "bootstrapTask": {
        "../22_goal_impact/GOAL-IMPACT-TASK-001.md",
        "../21_execution_plans/EP-TASK-001-bootstrap-service.md",
        "../12_validation/VAL-TASK-001-bootstrap-service.md",
    },
    "bootstrapGoalImpact": {"../11_tasks/TASK-001-bootstrap-service.md", "../21_execution_plans/EP-TASK-001-bootstrap-service.md"},
    "bootstrapExecutionPlan": {
        "../11_tasks/TASK-001-bootstrap-service.md",
        "../22_goal_impact/GOAL-IMPACT-TASK-001.md",
        "../12_validation/VAL-TASK-001-bootstrap-service.md",
    },
    "bootstrapValidation": {"TASK-001-bootstrap-service", "../22_goal_impact/GOAL-IMPACT-TASK-001.md"},
}
REQUIRED_SECTIONS = {
    "readme": {
        "status",
        "documentation authority",
        "capabilities",
        "interfaces",
        "development",
        "configuration",
        "deployment",
        "health and observability",
    },
    "business": {
        "problem",
        "target users and stakeholders",
        "value proposition",
        "goals",
        "non-goals",
        "success metrics",
        "business constraints",
        "approval",
    },
    "system": {
        "purpose",
        "responsibilities",
        "non-responsibilities",
        "inputs",
        "outputs",
        "dependencies",
        "upstream traceability",
        "downstream artifacts",
        "validation criteria",
        "open questions",
    },
    "agents": {
        "required reading",
        "authority",
        "intent preservation system",
        "safety and operations",
        "project-specific rules",
        "required final report",
    },
    "operations": {
        "roles",
        "before work",
        "parallel work",
        "validation debt",
        "handoff",
        "project-specific operations",
    },
    "tasks": {"active", "ready next", "blocked", "completed", "handoff"},
    "constitution": {"purpose", "constitutional principles", "amendment process", "approval"},
    "vision": {
        "one-sentence vision",
        "problem statement",
        "target users",
        "core user need",
        "key outcomes",
        "non-goals",
        "success criteria",
        "approval",
    },
    "integrationContract": {
        "purpose",
        "capability decisions",
        "data ownership",
        "authentication and authorization",
        "synchronous dependencies",
        "asynchronous dependencies",
        "degraded operation",
        "validation",
    },
    "projectInvariants": {"purpose", "applicability", "invariants", "exceptions", "review cadence"},
    "validationDebt": {"purpose", "rules", "entries", "update format"},
    "bootstrapTask": {
        "objective",
        "upstream links",
        "goal impact",
        "project invariant impact",
        "sensitive-data classification",
        "contract and schema impact",
        "replay and determinism impact",
        "scope",
        "non-goals",
        "acceptance criteria",
        "required context",
        "validation task",
        "required gates",
        "parallel workstream context",
    },
    "bootstrapGoalImpact": {
        "goal",
        "contribution",
        "success metric",
        "invariant compatibility",
        "upstream and downstream links",
        "validation method",
    },
    "bootstrapExecutionPlan": {
        "upstream traceability",
        "scope",
        "non-goals",
        "project invariants",
        "sensitive-data handling",
        "contract validation plan",
        "replay and determinism plan",
        "files to inspect",
        "files to create",
        "files to modify",
        "files that must not be modified",
        "implementation steps",
        "parallel execution",
        "blockers",
        "test plan",
        "validation plan",
        "gate commands",
        "documentation updates",
        "rollback plan",
        "handoff",
        "completion checklist",
    },
    "bootstrapValidation": {
        "summary",
        "upstream goal",
        "acceptance criteria evidence",
        "gate evidence",
        "integration evidence",
        "invariant evidence",
        "sensitive-data evidence",
        "replay and determinism evidence",
        "issues and validation debt",
        "deviations",
        "recommendation",
        "traceability confirmation",
    },
}
COMPLETENESS_ARTIFACTS = {
    "business",
    "system",
    "constitution",
    "vision",
    "projectInvariants",
    "bootstrapTask",
    "bootstrapExecutionPlan",
}
REQUIRED_STATUSES = {
    "system": {"reviewed", "approved", "validated"},
    "projectInvariants": {"reviewed", "approved", "validated"},
    "bootstrapTask": {"approved", "completed", "validated"},
    "bootstrapGoalImpact": {"approved", "validated"},
    "bootstrapExecutionPlan": {"approved", "implemented", "validated", "closed"},
}
DEPLOYMENT_STATUSES = {
    "bootstrapTask": {"completed", "validated"},
    "bootstrapExecutionPlan": {"implemented", "validated", "closed"},
}
REQUIRED_STATE_KEYS = {
    "schemaVersion",
    "project",
    "lifecycle",
    "health",
    "activeTask",
    "lastUpdated",
    "deployment",
    "blockers",
    "followUps",
}
GENERIC_CONTENT = {"content", "content.", "approved project content", "approved project content.", "placeholder", "n/a"}
FORBIDDEN_APPROVER = re.compile(r"\b(ai|agent|automation|claude|codex|copilot)\b", re.I)
APPROVAL_EVIDENCE = re.compile(
    r"^(?:https://github\.com/[^/\s]+/[^/\s]+/(?:issues|pull|commit)/\S+|"
    r"(?:commit|issue|decision|owner-confirmation):\s*\S{3,})$",
    re.I,
)


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def unresolved_document_lines(text: str) -> list[int]:
    unresolved: list[int] = []
    in_fence = False
    scan_fence = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            if not in_fence:
                language = stripped[3:].strip().lower()
                in_fence = True
                scan_fence = language in {"yaml", "yml", "json"}
            else:
                in_fence = False
                scan_fence = False
            continue
        if in_fence and not scan_fence:
            continue
        visible = re.sub(r"`[^`]*`", "", line)
        marker = (
            bool(re.search(r"\[(?:MISSING|UNKNOWN)(?::|\])", visible))
            or bool(DOCUMENT_PLACEHOLDER.search(visible))
        )
        if marker:
            unresolved.append(line_number)
    return unresolved


def markdown_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            current = match.group(1).strip().lower()
            sections.setdefault(current, [])
        elif current is not None:
            sections[current].append(line)
    return {name: "\n".join(lines).strip() for name, lines in sections.items()}


def meaningful_content(content: str) -> bool:
    normalized = re.sub(r"\s+", " ", content).strip()
    return len(normalized) >= 12 and normalized.lower() not in GENERIC_CONTENT


def field_value(text: str, field: str) -> str | None:
    match = re.search(rf"(?mi)^{re.escape(field)}:\s*(.+?)\s*$", text)
    return match.group(1).strip() if match else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument(
        "--phase",
        choices=("planning", "deployment"),
        default="deployment",
        help="Planning allows a draft validation report; deployment requires completed evidence",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    profile_path = root / "ips-adoption.json"
    errors: list[str] = []

    if not profile_path.is_file():
        print("ERROR: missing ips-adoption.json")
        return 1
    try:
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERROR: invalid ips-adoption.json: {error}")
        return 1

    if profile.get("schemaVersion") != 1:
        errors.append("schemaVersion must be 1")
    if profile.get("profile") not in {"runtime-service", "application", "infrastructure", "tooling"}:
        errors.append("unsupported adoption profile")

    project = profile.get("project", {})
    standard = profile.get("standard", {})
    if not isinstance(project, dict):
        errors.append("project must be an object")
        project = {}
    if not isinstance(standard, dict):
        errors.append("standard must be an object")
        standard = {}
    for label, value in {
        "project.name": project.get("name"),
        "project.repository": project.get("repository"),
        "standard.repository": standard.get("repository"),
        "standard.revision": standard.get("revision"),
    }.items():
        if not nonempty_string(value) or PLACEHOLDER.search(str(value)):
            errors.append(f"{label} must be concrete")

    artifacts = profile.get("artifacts")
    if not isinstance(artifacts, dict):
        errors.append("artifacts must be an object")
        artifacts = {}
    missing_keys = sorted(set(REQUIRED_ARTIFACT_PATHS) - set(artifacts))
    if missing_keys:
        errors.append("missing artifact keys: " + ", ".join(missing_keys))
    for key, expected_relative in REQUIRED_ARTIFACT_PATHS.items():
        if key not in artifacts:
            continue
        relative = artifacts[key]
        if not nonempty_string(relative):
            errors.append(f"artifact {key} has no path")
            continue
        if relative != expected_relative:
            errors.append(
                f"artifact {key} must use canonical path {expected_relative}, got {relative}"
            )
            continue
        path = (root / str(relative)).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            errors.append(f"artifact {key} escapes project root: {relative}")
            continue
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"artifact {key} missing or empty: {relative}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            errors.append(f"artifact {key} cannot be read as UTF-8: {relative}: {error}")
            continue
        unresolved_lines = unresolved_document_lines(text)
        allow_draft_evidence = args.phase == "planning" and key == "bootstrapValidation"
        if unresolved_lines and not allow_draft_evidence:
            shown = ", ".join(str(line) for line in unresolved_lines[:5])
            suffix = "..." if len(unresolved_lines) > 5 else ""
            errors.append(f"artifact {key} has unresolved placeholders at lines {shown}{suffix}")
        sections = markdown_sections(text)
        for section in sorted(REQUIRED_SECTIONS.get(key, set())):
            if section not in sections:
                errors.append(f"artifact {key} missing required section: {section}")
            elif not allow_draft_evidence and not meaningful_content(sections[section]):
                errors.append(f"artifact {key} has incomplete section: {section}")
        if key not in REQUIRED_SECTIONS and key != "state" and len(text.strip()) < 80:
            errors.append(f"artifact {key} is too short to be meaningful")
        if key in COMPLETENESS_ARTIFACTS:
            completeness = field_value(text, "completeness_level")
            if completeness not in {"complete", "validated"}:
                errors.append(f"artifact {key} completeness_level must be complete or validated")
        if key in REQUIRED_STATUSES:
            statuses = re.findall(r"(?mi)^status:\s*([a-z-]+)\s*$", text)
            allowed_statuses = DEPLOYMENT_STATUSES.get(key, REQUIRED_STATUSES[key]) if args.phase == "deployment" else REQUIRED_STATUSES[key]
            if not statuses or any(status.lower() not in allowed_statuses for status in statuses):
                allowed = ", ".join(sorted(allowed_statuses))
                errors.append(f"artifact {key} status must be one of: {allowed}")
        if key == "bootstrapValidation" and args.phase == "deployment":
            statuses = re.findall(r"(?mi)^status:\s*([a-z-]+)\s*$", text)
            if not statuses or any(status.lower() != "validated" for status in statuses):
                errors.append("artifact bootstrapValidation status must be validated for deployment")
        for reference in sorted(TRACEABILITY_REFERENCES.get(key, set())):
            if reference not in text:
                errors.append(
                    f"artifact {key} is missing traceability reference {reference}"
                )
        if key == "state":
            try:
                state = json.loads(text)
            except json.JSONDecodeError as error:
                errors.append(f"artifact state must be valid JSON: {relative}: {error}")
            else:
                if not isinstance(state, dict):
                    errors.append("artifact state must contain a JSON object")
                    state = {}
                missing_state_keys = sorted(REQUIRED_STATE_KEYS - set(state))
                if missing_state_keys:
                    errors.append(
                        "artifact state missing keys: " + ", ".join(missing_state_keys)
                    )
                if state.get("project") != project.get("name"):
                    errors.append("artifact state project must match project.name")
                if state.get("schemaVersion") != 1:
                    errors.append("artifact state schemaVersion must be 1")
                for field in ("lifecycle", "health", "activeTask", "lastUpdated"):
                    if not nonempty_string(state.get(field)):
                        errors.append(f"artifact state {field} must be a concrete string")
                if nonempty_string(state.get("lastUpdated")) and not re.match(
                    r"^\d{4}-\d{2}-\d{2}(?:T[\d:.+-]+Z?)?$",
                    state["lastUpdated"],
                ):
                    errors.append("artifact state lastUpdated must be an ISO date or timestamp")
                deployment = state.get("deployment")
                if not isinstance(deployment, dict) or not nonempty_string(deployment.get("status")):
                    errors.append("artifact state deployment must contain a concrete status")
                if not isinstance(state.get("blockers"), list):
                    errors.append("artifact state blockers must be an array")
                if not isinstance(state.get("followUps"), list):
                    errors.append("artifact state followUps must be an array")
        if key in PROTECTED_ARTIFACTS:
            approved_by = field_value(text, "Approved by")
            approval_evidence = field_value(text, "Approval evidence")
            if not approved_by or FORBIDDEN_APPROVER.search(approved_by):
                errors.append(f"artifact {key} requires a concrete human approver")
            if not approval_evidence or not APPROVAL_EVIDENCE.match(approval_evidence):
                errors.append(f"artifact {key} requires durable approval evidence")
            statuses = re.findall(r"(?mi)^status:\s*([a-z-]+)\s*$", text)
            if not statuses or any(status.lower() != "approved" for status in statuses):
                errors.append(f"artifact {key} requires human-approved status")

    reviews = profile.get("integrationReview")
    if not isinstance(reviews, list):
        errors.append("integrationReview must be an array")
        reviews = []
    seen: set[str] = set()
    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            errors.append(f"integrationReview[{index}] must be an object")
            continue
        capability = review.get("capability")
        if capability not in CAPABILITIES:
            errors.append(f"integrationReview[{index}] has unknown capability: {capability}")
            continue
        if capability in seen:
            errors.append(f"duplicate integration capability: {capability}")
        seen.add(str(capability))
        decision = review.get("decision")
        if decision not in {"required", "not-applicable"}:
            errors.append(f"{capability}: decision must be required or not-applicable")
            continue
        reason = review.get("reason")
        if not nonempty_string(reason) or PLACEHOLDER.search(str(reason)):
            errors.append(f"{capability}: concrete reason required")
        if decision == "required":
            for field in ("contract", "configuration", "failureMode", "validation"):
                value = review.get(field)
                if not nonempty_string(value) or PLACEHOLDER.search(str(value)):
                    errors.append(f"{capability}: required integration needs {field}")

    missing_capabilities = sorted(CAPABILITIES - seen)
    if missing_capabilities:
        errors.append("unreviewed integration capabilities: " + ", ".join(missing_capabilities))

    for mandatory in ("logging", "docs-rag", "monitoring"):
        review = next((item for item in reviews if isinstance(item, dict) and item.get("capability") == mandatory), None)
        if profile.get("profile") in {"runtime-service", "application"} and review and review.get("decision") != "required":
            errors.append(f"{mandatory}: mandatory for runtime-service/application profiles")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"IPS adoption profile valid for {args.phase}: {project['name']} ({len(seen)} capabilities reviewed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
