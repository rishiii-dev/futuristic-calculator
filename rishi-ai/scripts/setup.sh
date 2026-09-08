#!/usr/bin/env bash
set -euo pipefail

command -v docker >/dev/null 2>&1 || { echo "Docker is required."; exit 1; }
docker compose up -d --build

echo "Rishi AI is running."
