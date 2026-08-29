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
REQUIRED_ARTIFACT_KEYS = {
    "business",
    "system",
    "agents",
    "operations",
    "tasks",
    "state",
    "constitution",
    "vision",
    "integrationContract",
    "projectInvariants",
    "validationDebt",
    "bootstrapTask",
    "bootstrapGoalImpact",
    "bootstrapExecutionPlan",
    "bootstrapValidation",
}
PLACEHOLDER = re.compile(r"REPLACE_ME|REQUIRED_OR_NOT_APPLICABLE|\[MISSING:", re.I)


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
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
    missing_keys = sorted(REQUIRED_ARTIFACT_KEYS - set(artifacts))
    if missing_keys:
        errors.append("missing artifact keys: " + ", ".join(missing_keys))
    for key in sorted(REQUIRED_ARTIFACT_KEYS & set(artifacts)):
        relative = artifacts[key]
        if not nonempty_string(relative):
            errors.append(f"artifact {key} has no path")
            continue
        path = root / str(relative)
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"artifact {key} missing or empty: {relative}")

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
    print(f"IPS adoption profile valid: {project['name']} ({len(seen)} capabilities reviewed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
