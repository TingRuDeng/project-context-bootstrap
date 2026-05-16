---
ai_summary:
  purpose: "Concise context map for AI coding agents."
  read_when:
    - "Before making code changes."
    - "When deciding which authority docs to inspect."
  source_of_truth:
    - "AGENTS.md"
    - "docs/README.md"
  verify_with:
    - "python3 scripts/validate_docs.py . --profile generic"
  stale_when:
    - "Project structure, build commands, or authority docs change."
---

# AI Context

## Project Snapshot

Describe the repository purpose, primary language, framework, and runtime in three to five bullets.

## Core Directories

List the source, test, configuration, and documentation directories that an AI coding agent should inspect first.

## Documentation Map

Map authority docs to the questions they answer.

## Common Task Reading Paths

Route common task types to the minimum docs and source files needed.

## High-Risk Areas

List boundaries where unsupported edits are likely to break the project.

## Validation Commands

List exact commands that prove the context pack and common code changes are valid.

## Stale when

List the repository changes that require regenerating or updating this context map.
