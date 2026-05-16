---
name: project-context-bootstrap
description: Generate an agent-agnostic, evidence-backed context pack for software repositories, with Android MVP profile support.
---

# Project Context Bootstrap

## Purpose

Use this workflow to generate an agent-agnostic context pack for a software repository.

The generated context pack must be useful to human maintainers and any AI coding agent. It must not make core behavior specific to Codex, Claude Code, GitHub Copilot, Cursor, Gemini CLI, OpenHands, Aider, or any single AI coding agent.

## Core Output

Every target repository should receive the core context pack:

- `AGENTS.md`
- `docs/README.md`
- `docs/AI_CONTEXT.md`

`AGENTS.md` is the portable agent instruction entrypoint. `docs/AI_CONTEXT.md` is the concise context map.

## Android MVP Output

If the target repository is an Android project, also generate:

- `docs/BUILD_MATRIX.md`
- `docs/MODULE_MAP.md`
- `docs/TESTING_MATRIX.md`
- `docs/MANIFEST_AND_PERMISSIONS.md`

The Android MVP profile covers Gradle modules, build variants, module boundaries, test commands, manifest entries, exported components, and permissions.

## Android Detection

Treat a repository as Android when one or more of these signals are present:

- `settings.gradle` or `settings.gradle.kts`
- `build.gradle` or `build.gradle.kts`
- `AndroidManifest.xml`
- `com.android.application` or `com.android.library` in Gradle files

Use the signals as a starting point, then verify the real file tree before writing docs.

## Authority Doc Contract

Every generated authority doc must include frontmatter:

```yaml
---
ai_summary:
  purpose: "Concrete purpose of this document."
  read_when:
    - "Specific task that should read this document."
  source_of_truth:
    - "Real path that exists in the target repository."
  verify_with:
    - "Concrete command that can be run."
  stale_when:
    - "Concrete change that makes the document stale."
---
```

Every authority doc body must include:

- `## Purpose`
- `## Source Of Truth`
- `## Key Facts`
- `## How To Verify`
- `## Stale When`

Do not accept placeholder, generic, or unverifiable content.

## Workflow

Follow this sequence:

1. Scan the target repository structure.
2. Identify technology stack and profile.
3. Locate source-of-truth files and directories.
4. Generate `AGENTS.md`.
5. Generate `docs/README.md`.
6. Generate `docs/AI_CONTEXT.md`.
7. If the target is Android, generate the four Android authority docs.
8. Fill every authority doc with real `source_of_truth` paths and concrete `verify_with` commands.
9. Run `scripts/validate_docs.py` with the matching profile.
10. Fix validation errors before reporting completion.
11. Report changed files, validation commands, validation results, and remaining risks.

## Core Context Rules

- Keep core docs agent-agnostic.
- Keep `AGENTS.md` as a routing file, not a knowledge dump.
- Keep `docs/AI_CONTEXT.md` concise.
- Prefer concrete paths, commands, module names, and stale conditions.
- Do not duplicate long content across files.
- If docs and code disagree, trust the code and repair the docs.

## Android MVP Rules

Android MVP support is limited to:

- Gradle modules and build variants.
- Module responsibilities and dependency boundaries.
- Test source sets and Gradle test commands.
- Manifest paths, exported components, permissions, and intent filters.

Do not add Android navigation, Room migrations, WorkManager, release operations, performance docs, or other non-MVP Android docs unless explicitly requested.

## Tool Adapters

Tool-specific adapters are future optional work:

- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `.cursor/rules/`
- `GEMINI.md`
- `llms.txt`

MVP must not generate these files. Future adapters should point to the core context pack instead of duplicating it.

## Validation

Run:

```bash
python3 scripts/validate_docs.py <context-root> --profile generic
python3 scripts/validate_docs.py <context-root> --profile android
```

For this repository, run:

```bash
python3 -m unittest tests/test_validate_docs.py
python3 scripts/validate_docs.py examples/fixtures/android-client-context --profile android
```

## Do Not

- Do not make this project specific to one AI coding agent.
- Do not make templates depend on one AI tool.
- Do not add tool adapters in MVP.
- Do not invent source paths.
- Do not write `Run tests`, `Check manually`, `Follow best practices`, `TBD`, or similar generic content as validation evidence.
