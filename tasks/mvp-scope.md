# MVP Scope

## Goal

Generate a minimal, portable, evidence-backed context pack for software repositories, with first-class MVP support for Android apps.

The project must remain agent-agnostic. Codex, Claude Code, GitHub Copilot, Cursor, Gemini CLI, OpenHands, and Aider are consumers, not the center of the design.

## In scope

- Root `AGENTS.md` as the canonical agent instruction entrypoint.
- `docs/README.md` as the generated docs index.
- `docs/AI_CONTEXT.md` as the concise context map.
- Android authority docs:
  - `docs/BUILD_MATRIX.md`
  - `docs/MODULE_MAP.md`
  - `docs/TESTING_MATRIX.md`
  - `docs/MANIFEST_AND_PERMISSIONS.md`
- Validator improvements:
  - required file checks
  - required heading checks
  - `ai_summary` checks
  - local path checks
  - verification command checks
  - placeholder and generic-content detection

## Out of scope for MVP

- `CLAUDE.md`
- `.github/copilot-instructions.md`
- `.cursor/rules/`
- `GEMINI.md`
- `llms.txt`
- Codex-specific configuration
- Claude-specific configuration
- Copilot-specific configuration
- ADR generation
- runbook generation
- troubleshooting docs
- Android navigation docs
- Room migration docs
- WorkManager docs
- release operation docs
- performance docs
- behavioral evals

## MVP exit criteria

A generated context pack includes:

- one portable root instruction file
- one docs index
- one concise AI context map
- four Android authority docs when using the Android profile
- real file paths, module names, and verification commands
- validator failure for placeholder, generic, or unverifiable content
