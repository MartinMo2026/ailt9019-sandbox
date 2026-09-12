#!/usr/bin/env bash
# Save helper for the ailt9019-sandbox repo.
# Usage (from inside the repo folder):
#     ./save.sh "Short message about what now works"
#
# What it does:
#   1. `git add .`   — stage all changed files
#   2. `git commit`  — record the change with your message
#   3. `git push`    — send it to GitHub

set -e

if [ -z "$1" ]; then
  echo "Usage: ./save.sh \"message describing the change\""
  exit 1
fi

git add .
git commit -m "$1"
git push