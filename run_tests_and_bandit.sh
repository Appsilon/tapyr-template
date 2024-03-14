#!/bin/bash
# This script is for Github Action purposes.
# You cannot run multiple commands with runCmd in devcontainers/ci@v0.3 action
# Hence, this script is created to run the tests and bandit.

set -e # Exit immediately if a command exits with a non-zero status.

echo "Running pytest..."
poetry run pytest

echo "Running Bandit..."
poetry run bandit -r pyshiny_template
