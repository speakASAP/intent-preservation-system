#!/usr/bin/env bash
# Idempotent installer for the ecosystem IPS validator/healer systemd user timer.
# Safe to re-run any time (e.g. if the units are ever lost from ~/.config/systemd/user).
set -euo pipefail
UNIT_DIR="$HOME/.config/systemd/user"
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$UNIT_DIR"
cp "$SRC_DIR/ips-ecosystem-validator.service" "$UNIT_DIR/"
cp "$SRC_DIR/ips-ecosystem-validator.timer" "$UNIT_DIR/"
systemctl --user daemon-reload
systemctl --user enable --now ips-ecosystem-validator.timer
systemctl --user status ips-ecosystem-validator.timer --no-pager
