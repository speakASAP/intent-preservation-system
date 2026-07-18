#!/usr/bin/env sh
set -eu

IMMUTABLE_PATTERN='^(docs/00_constitution/CONSTITUTION\.md|docs/01_vision/VISION\.md)$'
TARGET_BRANCH="${CI_MERGE_REQUEST_TARGET_BRANCH_NAME:-${CI_DEFAULT_BRANCH:-main}}"

if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  echo "No committed HEAD found; immutable document guard is intended for GitLab CI after the first commit."
  exit 0
fi

git fetch origin "$TARGET_BRANCH" --depth=100 >/dev/null 2>&1 || true

if git rev-parse "origin/$TARGET_BRANCH" >/dev/null 2>&1; then
  CHANGED_FILES="$(git diff --name-only "origin/$TARGET_BRANCH"...HEAD)"
else
  CHANGED_FILES="$(git diff-tree --no-commit-id --name-only -r HEAD)"
fi

PROTECTED_CHANGES="$(printf '%s\n' "$CHANGED_FILES" | grep -E "$IMMUTABLE_PATTERN" || true)"

if [ -z "$PROTECTED_CHANGES" ]; then
  echo "No immutable documents changed."
  exit 0
fi

echo "Immutable document changes detected:"
printf '%s\n' "$PROTECTED_CHANGES"

if [ "${CI_PIPELINE_SOURCE:-}" = "merge_request_event" ]; then
  cat <<'MSG'

This merge request changes immutable project intent documents.
GitLab must require Code Owner approval before merge.
Verify the protected branch rule has "Require approval from code owners" enabled.
MSG
  exit 0
fi

cat <<'MSG'

ERROR: Immutable documents changed outside a merge request.
Push changes through a merge request with human Code Owner approval.
MSG
exit 1
