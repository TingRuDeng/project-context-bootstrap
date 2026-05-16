# project-context-bootstrap

## What this project does

`project-context-bootstrap` generates an agent-friendly context pack for software repositories.

It is designed for human maintainers and AI coding agents. It is agent-agnostic: Codex, Claude Code, GitHub Copilot, Cursor, Gemini CLI, OpenHands, Aider, and future AI coding agents are consumers, not the center of the design.

The generated context pack helps AI coding agents understand project structure, build commands, test commands, source-of-truth files, high-risk areas, validation evidence, and stale conditions.

## What this project generates

For every software repository, the core output is:

- `AGENTS.md`
- `docs/README.md`
- `docs/AI_CONTEXT.md`

For Android projects, the Android MVP profile adds:

- `docs/BUILD_MATRIX.md`
- `docs/MODULE_MAP.md`
- `docs/TESTING_MATRIX.md`
- `docs/MANIFEST_AND_PERMISSIONS.md`

## Core context pack

`AGENTS.md` is the portable agent instruction entrypoint.

`docs/README.md` is the generated docs index.

`docs/AI_CONTEXT.md` is the concise context map for AI coding agents.

All authority docs must include:

- `ai_summary.purpose`
- `ai_summary.read_when`
- `ai_summary.source_of_truth`
- `ai_summary.verify_with`
- `ai_summary.stale_when`
- `## Purpose`
- `## Source Of Truth`
- `## Key Facts`
- `## How To Verify`
- `## Stale When`

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

## Recommended workflow

1. Run the context bootstrap workflow against a target repository.
2. Generate the core context pack.
3. If the target is Android, generate the Android profile docs.
4. Run `validate_docs.py`.
5. Fix missing paths, weak commands, placeholders, and generic sections.
6. Commit the context pack.
7. Ask future AI coding agents to start from `AGENTS.md` and `docs/AI_CONTEXT.md`.

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
