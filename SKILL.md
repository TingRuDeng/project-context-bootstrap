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
- `scripts/validate_docs.py`

`AGENTS.md` is the portable agent instruction entrypoint. `docs/AI_CONTEXT.md` is the concise context map.
`scripts/validate_docs.py` is the canonical validation script for the generated context pack.

## Execution Mode

Before writing files, inspect the target repository and choose one mode:

- Create mode: use this when no recognizable context pack exists. Generate the core context pack from the current repository structure, source files, build files, and test commands.
- Upgrade mode: use this when the target already has `AGENTS.md`, `docs/README.md`, `docs/AI_CONTEXT.md`, older project-context-bootstrap output, or another local documentation system that serves the same purpose.

In upgrade mode:

1. Read the existing documentation before editing it.
2. Preserve accurate project-specific facts, paths, commands, constraints, and task-routing guidance.
3. Convert existing docs to the current authority doc contract.
4. Add missing `ai_summary` fields, source-of-truth paths, verification commands, stale conditions, and required sections.
5. Replace placeholder, generic, or unverifiable claims with evidence from the repository.
6. Remove or consolidate obsolete generated docs only when their useful content has been moved into the current context pack.
7. Keep manual product, design, architecture, and operations docs intact unless they directly conflict with the context pack.
8. If legacy detail docs are indexed from `docs/README.md`, either add lightweight `ai_summary` frontmatter to those docs or label them as legacy detail docs with freshness limits in the index.
9. Report whether the run created a new context pack or upgraded an existing one.

Do not overwrite useful existing documentation just because a template exists. Templates define the target shape; the target repository defines the facts.

## Validator Output

When writing or upgrading a target repository, install or update `scripts/validate_docs.py` from this project as the canonical validator.

Do not rewrite a simplified validator in the target project. The target validator must preserve these checks:

- required files for `generic` and `android` profiles
- required authority doc headings
- complete and non-empty `ai_summary`
- existing local `source_of_truth` paths
- concrete `verify_with` commands
- placeholder and generic-content rejection, including English and Chinese generic phrases
- local Markdown link checks

If the target repository already has a validator, compare it against the canonical behavior and upgrade it in place. After writing it, run:

```bash
python3 -m py_compile scripts/validate_docs.py
```

## Documentation Language

Choose the generated documentation language from the target repository and user context:

1. If the user explicitly requests a language, use that language.
2. Otherwise, match the dominant language of existing project docs, especially `README.md`, `docs/`, and existing context-pack files.
3. If there is no existing documentation signal, match the user's local conversation language when it is clear.
4. If the language is still unclear, use English for maximum portability.

Keep file names, code identifiers, commands, package names, Gradle task names, and source paths exactly as they appear in the repository. Translate explanatory prose only.

For upgrade mode, preserve the existing documentation language unless the user asks to change it. If a repository already mixes languages, keep each document internally consistent and prefer the language used by its nearest existing source document.

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
- `## Source of truth`
- `## Key facts`
- `## How to verify`
- `## Stale when`

Do not accept placeholder, generic, or unverifiable content.

## Verification Command Tiers

Separate verification commands by cost and side effect whenever a document lists more than one command:

- `quick`: local, low-cost checks suitable after small edits.
- `full`: broader local regression checks.
- `device-required`: commands that require an emulator, physical device, external service, or credentials.
- `release-side-effect`: commands that create, sign, publish, upload, or synchronize artifacts.

Do not present `device-required` or `release-side-effect` commands as ordinary quick validation. Keep command strings exact and add prerequisite notes when needed.

## Workflow

Follow this sequence:

1. Scan the target repository structure.
2. Detect whether this is a create run or an upgrade run.
3. Choose the documentation language.
4. Identify technology stack and profile.
5. Locate source-of-truth files and directories.
6. Generate or upgrade `AGENTS.md`.
7. Generate or upgrade `docs/README.md`.
8. Generate or upgrade `docs/AI_CONTEXT.md`.
9. If the target is Android, generate or upgrade the four Android authority docs.
10. Install or upgrade the canonical `scripts/validate_docs.py`.
11. Fill every authority doc with real `source_of_truth` paths and concrete tiered `verify_with` commands.
12. Run `scripts/validate_docs.py` with the matching profile.
13. Fix validation errors before reporting completion.
14. Report changed files, execution mode, documentation language, validation commands, validation results, and remaining risks.

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
