# AGENTS.md

## Project purpose

This repository maintains `project-context-bootstrap`, a tool and documentation system for generating agent-friendly context packs for software projects.

The project is agent-agnostic. Do not make core behavior specific to Codex, Claude Code, GitHub Copilot, Cursor, Gemini CLI, OpenHands, Aider, or any single AI coding agent.

## Before making changes

Read:

- `README.md`
- `SKILL.md`
- `tasks/mvp-scope.md`
- `templates/AI_CONTEXT.md`
- `scripts/validate_docs.py`
- `tests/test_validate_docs.py`

For Android context examples, read:

- `examples/fixtures/android-client-context/docs/AI_CONTEXT.md`

## Source of truth

- `SKILL.md` defines the context-generation workflow.
- `templates/` defines generated document shapes.
- `scripts/validate_docs.py` defines validation behavior.
- `tests/test_validate_docs.py` defines expected validator behavior.
- `examples/fixtures/android-client-context/` defines the Android MVP fixture.

## Validation commands

Run these before finishing changes:

```bash
python3 -m unittest tests/test_validate_docs.py
python3 scripts/validate_docs.py examples/fixtures/android-client-context --profile android
```

## Documentation Rules

- Keep core docs agent-agnostic.
- Prefer concrete paths, commands, and module names over generic advice.
- Do not duplicate long content across files.
- Keep `AGENTS.md` as a routing file, not a knowledge dump.
- Keep `docs/AI_CONTEXT.md` as a concise context map.

## Android Context Rules

Android MVP support focuses on:

- Gradle modules and build variants.
- Module responsibilities and dependencies.
- Test types and Gradle test commands.
- Manifests, exported components, and permissions.

Do not add advanced Android docs in MVP unless explicitly requested.

## Do not

- Do not make this project specific to one AI coding agent.
- Do not make templates depend on one AI tool.
- Do not add adapter files in MVP.
- Do not accept placeholder or generic context as valid documentation.
