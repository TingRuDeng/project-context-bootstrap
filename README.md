# project-context-bootstrap

A reusable agent skill for building and repairing AI-facing project context systems in code repositories.

This skill helps transform a repository into something future AI agents can enter and work in with less blind scanning, fewer architectural mistakes, and fewer duplicated or stale documentation paths.

## What This Skill Is For

Use this skill when a repository needs a reliable agent-facing context layer, especially if:

- the project has little or no agent-facing documentation
- agents repeatedly misread architecture, API contracts, or naming conventions
- the docs are fragmented, duplicated, or stale
- the team wants a repeatable repository bootstrap for AI-assisted development

This skill is designed to create or repair a system centered around:

- `AGENTS.md` for workflow rules
- `docs/README.md` for navigation
- stable factual docs such as architecture, API, schema, and pitfalls
- module-level `README.md` files for tactical entry points
- `docs/archive/` for historical or superseded material

## What It Produces

Depending on the repository, this skill may generate or refine:

- `AGENTS.md`
- `docs/README.md`
- `docs/ARCHITECTURE.md`
- `docs/API_ENDPOINTS.md`
- `docs/DATABASE_SCHEMA.md`
- `docs/KNOWN_PITFALLS.md`
- `docs/TECH_DEBT.md`
- `docs/AGENT_STARTER_PROMPT.md`
- `docs/DOC_SYNC_CHECKLIST.md`
- `docs/ADR/0001-*.md`
- module-level `README.md` files
- `docs/archive/README.md`

## Core Principles

- Code is the source of truth.
- Document repository reality, not idealized architecture.
- Keep one authority source for rules and one authority source for navigation.
- Do not let startup prompts, navigation docs, and local READMEs all restate the same workflow in parallel.
- Archive stale or superseded docs instead of leaving them in the active path.
- Treat documentation as a navigation and coordination layer, not a replacement for reading code.

## Install

Install this standalone skill repo with:

```bash
npx skills add TingRuDeng/project-context-bootstrap
```

Or use the full GitHub URL:

```bash
npx skills add https://github.com/TingRuDeng/project-context-bootstrap
```

If your environment supports direct skill folder installation, place `SKILL.md` in a `project-context-bootstrap/` directory under your global skills path.

## Usage

When invoking this skill, give the agent a concrete repository-level task such as:

### 1. Build a context system from scratch

```text
Please use the project-context-bootstrap skill for this repository.

Goal:
Build a reliable agent-facing project context system so future AI agents can enter this repo, understand how to start, and develop with less blind scanning and fewer incorrect assumptions.

Requirements:
1. Inspect the repository shape, frameworks, routing, configuration, data model layer, and existing documentation.
2. Create or refine a single rules entrypoint in `AGENTS.md`.
3. Create or refine a single navigation entrypoint in `docs/README.md`.
4. Create or refine the stable knowledge docs that are actually justified by the codebase.
5. Add module-level `README.md` files only for high-value or high-risk code boundaries.
6. Archive stale, duplicate, generic, or superseded docs under `docs/archive/`.

Constraints:
- Code is the source of truth.
- Do not invent architecture facts.
- Do not duplicate workflow rules across multiple files.
- If docs conflict with code, fix the docs.
```

### 2. Audit and repair an existing system

```text
Please use the project-context-bootstrap skill to audit and repair this repository's existing agent-facing documentation system.

Goal:
Do not rebuild everything. Identify drift, duplication, stale guidance, dead references, and outdated docs, then bring the system back to a single-source-of-truth structure.
```

### 3. Retire stale legacy docs

```text
Please use the project-context-bootstrap skill, but limit this task to retiring stale legacy documentation.

Goal:
Identify old onboarding docs, generic tutorials, numbered legacy docs, and superseded reference files that are no longer part of the active workflow. Move them out of the active docs path without losing useful history.
```

## Typical Outcome

After using this skill well, a repository should have:

- one obvious rules entrypoint
- one obvious navigation entrypoint
- tactical local module guides only where they reduce blind scanning
- startup prompts that point to authority docs instead of duplicating them
- stale docs archived or clearly marked as non-authoritative
- no dead references to deleted docs, deleted skills, or nonexistent paths

## When Not To Use It

Do not use this skill when:

- the user only wants a single bugfix or feature change
- the repository already has a complete and trusted agent context system
- the task is local implementation work rather than repository context design

## License

MIT
