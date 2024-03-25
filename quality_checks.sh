#!/bin/bash
# This script is for running quality checks in GitHub Actions.
# It runs tests, security analysis with Bandit, and type checks with mypy.

set -e # Exit immediately if a command exits with a non-zero status.

echo "Running pytest for unit tests..."
poetry run pytest

echo "Running Bandit for security analysis..."
poetry run bandit -r pyshiny_template

echo "Running mypy for type checking..."
poetry run mypy pyshiny_template
