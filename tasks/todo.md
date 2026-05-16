# TODO

## MVP

- [x] Add agent-agnostic root `AGENTS.md`.
- [x] Add `tasks/mvp-scope.md`.
- [x] Add missing templates for the core context pack.
- [x] Add Android MVP templates.
- [x] Update Android fixture.
- [x] Add `--profile generic` and `--profile android` validation modes.
- [x] Validate required files for each profile.
- [x] Validate `ai_summary`.
- [x] Validate source-of-truth paths.
- [x] Validate verification commands.
- [x] Reject placeholder and generic content.

## Cross-repo feedback

- [x] Validate `AGENTS.md` as an authority doc, not only as a required file.
- [x] Reject duplicate `ai_summary:` blocks so upgrade mode cannot keep old fenced metadata beside new frontmatter.
- [x] Document that legacy detail docs must not also be described as current authority docs until migrated.
- [x] Update the Android fixture and AGENTS template to use the authority doc contract.
- [x] Add regression tests for `AGENTS.md` contract validation and duplicate summaries.

## Review notes

The ForgeFlow upgrade review exposed two reusable rules: root `AGENTS.md` needs the same authority contract checks as docs, and upgrade mode must remove old metadata once frontmatter exists. These are now enforced by the canonical validator and covered by tests.

## Later

- [ ] Add optional `CLAUDE.md` adapter.
- [ ] Add optional Copilot instructions adapter.
- [ ] Add optional Cursor rules adapter.
- [ ] Add optional `GEMINI.md` adapter.
- [ ] Add optional `llms.txt` output.
- [ ] Add ADR templates.
- [ ] Add runbook templates.
- [ ] Add troubleshooting templates.
- [ ] Add Android navigation/deep-link docs.
- [ ] Add Android storage/migration docs.
- [ ] Add Android background-work docs.
- [ ] Add Android release docs.
- [ ] Add Android performance docs.
- [ ] Add behavioral evals.
