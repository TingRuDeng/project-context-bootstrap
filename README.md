# project-context-bootstrap

## What this project does

`project-context-bootstrap` generates an agent-friendly context pack for software repositories.

It is designed for human maintainers and AI coding agents. It is agent-agnostic: Codex, Claude Code, GitHub Copilot, Cursor, Gemini CLI, OpenHands, Aider, and future AI coding agents are consumers, not the center of the design.

The generated context pack helps AI coding agents understand project structure, build commands, test commands, source-of-truth files, high-risk areas, validation evidence, and stale conditions.

Generated prose should match the target repository and user context. The workflow uses the user's requested language first, then the dominant language of existing docs, then the user's local conversation language, and falls back to English when there is no clear signal.

## What this project generates

For every software repository, the core output is:

- `AGENTS.md`
- `docs/README.md`
- `docs/AI_CONTEXT.md`
- `scripts/validate_docs.py`

For Android projects, the Android MVP profile adds:

- `docs/BUILD_MATRIX.md`
- `docs/MODULE_MAP.md`
- `docs/TESTING_MATRIX.md`
- `docs/MANIFEST_AND_PERMISSIONS.md`

## Core context pack

`AGENTS.md` is the portable agent instruction entrypoint.

`docs/README.md` is the generated docs index.

`docs/AI_CONTEXT.md` is the concise context map for AI coding agents.

`scripts/validate_docs.py` is the canonical validator. The workflow should copy or upgrade this validator in target repositories instead of generating a simplified local variant.

All authority docs must include:

- `ai_summary.purpose`
- `ai_summary.read_when`
- `ai_summary.source_of_truth`
- `ai_summary.verify_with`
- `ai_summary.stale_when`
- `## Purpose`
- `## Source of truth`
- `## Key facts`
- `## How to verify`
- `## Stale when`

## Android MVP profile

The Android MVP profile covers:

- Gradle modules and build variants
- module responsibilities and dependencies
- local and instrumented test commands
- manifest paths, exported components, permissions, and intent filters

The Android MVP profile does not cover navigation, Room migrations, WorkManager, release operations, or performance docs.

## Validation

Run validation commands against generated context packs:

```bash
python3 scripts/validate_docs.py <context-root> --profile generic
python3 scripts/validate_docs.py <context-root> --profile android
python3 -m unittest tests/test_validate_docs.py
```

Validate the Android fixture with:

```bash
python3 scripts/validate_docs.py examples/fixtures/android-client-context --profile android
```

The validator checks required files, required headings, complete `ai_summary`, existing `source_of_truth` paths, concrete `verify_with` commands, placeholders, and generic sections.

Generic-content detection covers common English and Chinese placeholders such as `Run tests`, `Check manually`, `Follow best practices`, `运行测试`, `手动确认`, and `遵循最佳实践`.

The validator also rejects machine-local filesystem paths such as `/Users/...`, `/Volumes/...`, `/home/...`, and `C:\...`; generated context packs should use repository-relative paths.

## Recommended workflow

1. Run the context bootstrap workflow against a target repository.
2. Let the workflow inspect existing docs and choose create mode or upgrade mode.
3. Choose the documentation language from the user request, existing docs, or local conversation context.
4. In create mode, generate the core context pack from the repository evidence.
5. In upgrade mode, preserve accurate existing facts and migrate old docs to the current contract.
6. If the target is Android, generate or upgrade the Android profile docs.
7. Install or upgrade the canonical `scripts/validate_docs.py`.
8. Split verification commands into quick, full, device-required, and release-side-effect groups when cost or side effects differ.
9. For multi-implementation repositories, include validation commands for each active implementation or state why one is out of scope.
10. Run `validate_docs.py`.
11. Fix missing paths, weak commands, placeholders, and generic sections.
12. Commit the context pack.
13. Ask future AI coding agents to start from `AGENTS.md` and `docs/AI_CONTEXT.md`.

## Existing documentation

The workflow supports repositories with or without an existing documentation system.

When no context pack exists, it creates `AGENTS.md`, `docs/README.md`, and `docs/AI_CONTEXT.md`, plus profile docs when a supported technology profile is detected.

When older context docs already exist, it upgrades them in place: it keeps accurate project-specific content, adds missing `ai_summary` metadata, fills concrete `source_of_truth` and `verify_with` evidence, aligns required sections, and removes obsolete generated docs only after useful content has been preserved elsewhere.

When non-generated legacy docs are indexed as detail docs, the workflow either adds lightweight freshness metadata to those docs or clearly labels them under `## Legacy detail docs` in `docs/README.md` with freshness limits. The canonical validator treats that section as an explicit legacy boundary instead of forcing those detail docs into the authority-doc contract.

## Tool adapters

Tool-specific files such as `CLAUDE.md`, Copilot instructions, Cursor rules, `GEMINI.md`, and `llms.txt` are future optional adapters.

They should point to the canonical core context pack instead of duplicating it.

MVP does not generate tool adapters.

## MVP limitations

- No tool-specific adapters.
- No real Gradle introspection.
- No real manifest merge parsing.
- No Room migration parsing.
- No behavioral evals.

## Install

Install with:

```bash
npx skills add https://github.com/TingRuDeng/project-context-bootstrap
```

Update a global installation with:

```bash
npx skills update project-context-bootstrap -g -y
```

## Reference practices

| Project | Adopted | Not adopted in MVP |
| --- | --- | --- |
| [AGENTS.md](https://github.com/agentsmd/agents.md) | Stable agent instruction entrypoint | Tool-specific behavior |
| [llms.txt](https://llmstxt.org/) | Concise Markdown context map ideas | `llms.txt` adapter |
| [Repomix](https://github.com/yamadashy/repomix) | Context budget and evidence mindset | Repository packing |
| [Gitingest](https://github.com/coderamp-labs/gitingest) | Prompt-friendly context shape | Full source digest |

## License

MIT
