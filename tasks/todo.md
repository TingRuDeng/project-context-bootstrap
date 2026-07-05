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
- [x] Add an `AGENTS.md` routing-file length budget to prevent knowledge-dump entrypoints.
- [x] Document nested git repository handling for coordination-directory projects.
- [x] Validate current completion-gate and checklist docs instead of skipping them by filename.
- [x] Add a coordination-root fixture and validator regression tests for nested repositories.
- [x] Validate multi-command verification sections require cost/side-effect tiers.
- [x] Parse inline `ai_summary` lists before checking source paths and commands.
- [x] Add a `network-read` verification tier for read-only registry, API, and web checks.
- [x] Document context input boundaries inspired by repository packing tools.
- [x] Document sensitive-data boundaries for generated context packs.

## Review notes

The ForgeFlow upgrade review exposed two reusable rules: root `AGENTS.md` needs the same authority contract checks as docs, and upgrade mode must remove old metadata once frontmatter exists. These are now enforced by the canonical validator and covered by tests.

The management-platform upgrade review exposed another reusable rule: coordination directories with nested `backend/.git` and `frontend/.git` need explicit repository-shape notes and `git -C <repo>` validation commands. It also showed that oversized `AGENTS.md` files should be blocked by the validator before they become knowledge dumps.

The follow-up management-platform review exposed that docs described as current completion gates or required checklists must not be excluded from the authority contract by hard-coded filename. The validator now only treats explicit `## Legacy detail docs`, archive docs, and prompt templates as non-authority docs.

The next hardening pass added a coordination-root fixture plus checks for nested `*/.git` repositories, `git -C <repo>` commands, multi-command verification tiers, and inline `ai_summary` lists. This turns recurring real-project failures into executable regressions instead of prose-only guidance.

The 2026-07-05 deep review compared AGENTS.md, llms.txt, Repomix, and Gitingest. The useful takeaways were a read-only external verification tier, clearer ignored-input boundaries, and explicit sensitive-data boundaries. The validator now accepts `network-read` and rejects `npm view` / `pnpm view` / `yarn info` under `release-side-effect`.

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
- [ ] Add more behavioral evals for legacy-doc-upgrade and full-stack Vue/Django repositories.
