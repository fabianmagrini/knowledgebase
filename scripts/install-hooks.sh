#!/bin/sh
# Point git at the version-controlled hooks in scripts/hooks/.
# Run once after cloning: sh scripts/install-hooks.sh
set -e
repo_root=$(git rev-parse --show-toplevel)
git -C "$repo_root" config core.hooksPath scripts/hooks
chmod +x "$repo_root"/scripts/hooks/* 2>/dev/null || true
echo "Hooks enabled: core.hooksPath -> scripts/hooks"
