---
name: project-context-bootstrap
description: Use when entering a new or poorly documented repository and you need to build a reliable human-and-agent-facing context and onboarding system.
---

# Project Context Bootstrap

## Overview

Use this skill to turn an unfamiliar codebase into a repository that both human developers and AI agents can enter and work in with less blind scanning and fewer architectural mistakes.

The goal is not to generate "more docs". The goal is to generate a small set of high-signal documents that define:
- how humans and agents should work in the repo
- what the system looks like
- where to start for common task types
- what historical traps and contract edges must not be broken

This skill should also reduce documentation entropy:
- one file should own workflow rules
- one file should own navigation
- old or superseded material should be archived instead of left in active circulation

This skill is a two-phase workflow:
- **Phase 1: Build** a usable first version of the human-and-agent-facing context system
- **Phase 2: Audit & Repair** that first version against the actual codebase before treating it as trustworthy

## When To Use

Use this skill when:
- a project has little or no agent-facing documentation
- human onboarding is slow because docs are hard to scan or too prompt-oriented
- agents repeatedly misread architecture or API contracts
- a team wants reusable project onboarding for AI-assisted development
- a repository needs a primary agent rule file plus a stable `docs/` context layer

Do not use this skill when:
- the user only wants a single bugfix or feature change
- the repository already has a complete, trusted, and actively maintained human-and-agent context system

## Target Outputs

Generate or update only the files that materially improve human and agent onboarding:

- the repository's primary agent rule file (for example `AGENTS.md`, `CLAUDE.md`, or an equivalent repo-level instruction file)
- `docs/README.md`
- `docs/ARCHITECTURE.md`
- `docs/API_ENDPOINTS.md`
- `docs/DATABASE_SCHEMA.md`
- `docs/KNOWN_PITFALLS.md`
- `docs/TECH_DEBT.md` when the repo has recurring mismatches, historical inconsistencies, or known architectural debt that agents must not mistake for global rules
- `docs/AGENT_STARTER_PROMPT.md` when a repository would benefit from a ready-to-send initialization prompt for future agents
- `docs/DOC_SYNC_CHECKLIST.md` when the team needs a concrete completion gate that forces documentation updates to ship with code changes
- `docs/ADR/0001-*.md`
- module-level `README.md` files for high-value code boundaries
- `docs/archive/README.md` when the repository has old, superseded, or generic documents that should be retained only as historical reference

If the repository already has equivalents, consolidate instead of duplicating.

Human-friendly quality baseline for generated docs:
- each authority doc should start with a short "Purpose" and "Who should read this"
- provide a quick summary section that a human can scan in under one minute
- avoid machine-only shorthand; explain local jargon or repo-specific terms on first use
- keep cross-links explicit so humans can navigate without relying on hidden agent memory

## Two-Phase Execution Model

Treat this skill as a deliberate two-step process:

1. **Build**
   - create the first coherent version of the context system
   - establish authority files, navigation, stable knowledge docs, tactical READMEs, and archive boundaries
   - accept that this first version may still contain fact drift or incomplete coverage

2. **Audit & Repair**
   - verify the first version against real code, route definitions, schemas, config, and active callers
   - identify false completeness, stale references, weakly evidenced pitfalls, dead client files, and multi-backend boundary confusion
   - repair high-risk findings before declaring the system reliable

Do not treat Phase 1 output as fully trustworthy until Phase 2 has been completed.

## Core Rules

1. **Code is the absolute source of truth.**
2. **Respect Local Reality over Universal Conventions.** If a project uses legacy naming conventions (e.g., plural instead of singular filenames) or mixes casing styles (e.g., `snake_case` in a TypeScript frontend) due to history, **document the reality**. Do not refactor the repo to match generic "best practices" unless explicitly asked.
3. **Beware of Framework "Magic".** Global behavior (like automatic `camelCase` to `snake_case` conversions) is often hidden deep in backend dependency configurations, package manifests, or middleware arrays, not just in frontend HTTP interceptors. Dig deep into the configuration layer before declaring "there is no conversion layer".
4. **Prefer a Single Authority Source per concern.** Do not let multiple files independently define the same workflow rules, startup order, or contract assumptions. Pick one authority file and make the others point to it.
5. **Archive, Don’t Leave Ghost Rules Behind.** Old onboarding docs, generic tutorials, or superseded numbered documents should be moved out of the active path if they are no longer authoritative.
6. **Do Not Claim Completeness Without Coverage.** If a doc is only partially verified, label it as a core overview or verified subset. Do not present it as a complete catalog unless route-by-route or model-by-model coverage has actually been checked.
7. **Pitfalls Need Evidence.** `KNOWN_PITFALLS.md` should be built from code, config, logs, or repeated verified failures. Unverified folklore should be marked as needing confirmation or removed.
8. **No Placeholder Governance Data.** `TECH_DEBT.md`, solved-debt sections, and maintenance timelines must not contain fake dates, placeholder markers, or template residue.
9. **Default to Dual-Audience Readability.** Every authoritative doc must remain useful to both humans and agents: concise summaries, explicit context, and traceable code anchors.

## Phase 1: Build

### 1. Detect the repository shape

Before writing anything, identify:
- languages and frameworks
- backend entrypoints & plugin manifests (check global middleware, configurations, and core framework settings for magic data converters)
- frontend entrypoints (check API interface contracts, Axios/Fetch interceptors)
- data model layer
- existing docs & existing repo rules

Start with:
- top-level directory structure
- package manifests and dependency files
- framework settings files
- routing files

If the repository contains more than one backend, service, or API surface:
- identify each backend separately
- record which routes, schemas, and auth flows belong to which backend
- do not merge multiple backends into a single implicit API description

### 2. Hunt for Implicit Contracts and Middleware

Before documenting API conventions:
- Check backend entry configurations for 3rd-party plugins or global middleware that implicitly manipulate variable names (e.g., automatic snake/camel case transformers).
- Do not assume frontend network interceptors handle all format translations. Look at both sides.
- Check actual request and response structures by locating the real contract points in the codebase, such as request builders, serializers, schema definitions, typed interfaces, or equivalent layers used by that stack.

### 3. Build a context map

Create a working mental map of:
- major modules & ownership boundaries
- common request/data flows
- authentication and permission path
- historical compatibility seams

Do not summarize every folder. Focus on the paths humans and agents will actually need during development.

### 4. Write the repository rule layer

Create or refine the repository's primary agent rule file (for example `AGENTS.md`, `CLAUDE.md`, or an equivalent repo-level instruction file) so it answers:
- what this repo contains and the mandatory startup checklist
- how to start reading it (what to read first for Frontend vs. Backend tasks)
- what checks are mandatory before changing API, permissions, database, or frontend pages
- what must never be changed casually
- what execution boundaries apply to agents working in the repo
- how and when docs must be kept in sync with the implementation
- that code tasks are not complete until the documentation sync checklist has been checked

The rule layer must define execution permissions, not just reading order. At minimum, document:
- whether agents may edit directly on the default branch
- when a task or feature branch is expected
- whether agents may commit or push code
- who may merge
- what verification or delivery evidence is required before claiming completion

If the repository uses multiple agent roles, describe these boundaries separately by role instead of assuming one universal policy. Generic role buckets may include:
- interactive/helper agents
- worker/executor agents
- reviewer/control agents

This file must define concrete workflow rules and guardrails, not just system design abstractions.
It should be the single authority source for execution rules unless the repo already has a clearly stronger equivalent.

### 5. Write the navigation layer

Create or refine `docs/README.md` so it tells humans and agents:
- what each document is for and its level of authority
- the exact step-by-step reading flow for specific tasks (e.g. CRUD vs API modifications), including where a human maintainer should start
- which sections are suitable for future script automation (e.g. endpoint lists, schema dumps) vs. which must remain human/agent-maintained (e.g. ADRs, pitfalls).
- where the repo-specific startup prompt and documentation sync checklist live, if the repository uses them

This file should function as a startup manual, not a project brochure.
It should route readers to the rule source, not silently duplicate that rule source.

### 6. Write the stable knowledge layer

Create or refine:

- `docs/ARCHITECTURE.md`: system shape, macro-level middleware behavior.
- `docs/API_ENDPOINTS.md`: contract patterns, pagination naming rules, and global wrapper structures (e.g., standard HTTP status codes vs custom business payload codes).
- `docs/DATABASE_SCHEMA.md`: core models, migration constraints, audit/status/soft-delete conventions.
- `docs/KNOWN_PITFALLS.md`: compatibility traps, dangerous localized exceptions to the rules, things agents repeatedly get wrong.
- `docs/TECH_DEBT.md`: confirmed inconsistencies or historical debt that should be documented instead of silently normalized away.

Keep these factual and implementation-aligned. Avoid idealized architecture prose.

Additional quality rules for this layer:
- If `docs/API_ENDPOINTS.md` is not fully verified, explicitly label it as a partial reference, verified subset, or core overview. Do not call it a complete API catalog unless you checked real route definitions across all active backends.
- If the repository has multiple backends, `docs/API_ENDPOINTS.md` and `docs/ARCHITECTURE.md` must distinguish them explicitly.
- `docs/KNOWN_PITFALLS.md` should prefer pitfalls with code or configuration anchors. Weakly supported entries should be downgraded or removed.
- `docs/TECH_DEBT.md` must not contain placeholder dates such as `2024-xx-xx` or unresolved template markers.
- each stable doc should include a short "How this was verified" note with concrete code-entry anchors.
- prefer scannable structures (short sections, concise tables, explicit headings) over dense narrative blocks.

### 7. Record the first ADR

If the repository lacks ADRs, create `docs/ADR/0001-*.md` for the first major decision that clearly affects development behavior.
Good ADR topics:
- API naming conversion mechanisms
- permission models
- routing architectures

ADR format should cover: background, decision, alternatives, rationale, impact, follow-up.

### 8. Add local module entry guides (Tactical READMEs)

For high-change or high-risk modules (e.g., core business logic folders, main frontend view directories), add short local `README.md` files.

Each tactical module guide should tell an agent:
- what this module owns
- actual mapped filenames (do not assume singular/plural or specific conventions without checking)
- where contract changes ripple
- local traps and non-negotiable constraints

Prefer short, operational guidance over narrative explanation.

When frontend API client folders exist, inspect them for dead or stale client files whose target endpoints no longer exist. These mismatches should influence both docs and cleanup recommendations.

### 9. Add a reusable startup prompt

When a repository will be worked on repeatedly by multiple agents, create a ready-to-send startup prompt such as `docs/AGENT_STARTER_PROMPT.md`.

That prompt should tell a future agent to:
- read the repository's primary agent rule file
- read `docs/README.md`
- read the target module `README.md`
- verify code before trusting a document
- update impacted docs in the same task when behavior changes
- respect the repository's branch / commit / push / merge boundaries

Keep this prompt short enough to paste into a new session without editing.
Do not copy the full workflow rules into this file if the primary rule file already owns them. This file should be an entry shim, not a second rulebook.
The startup prompt should briefly remind the agent that execution boundaries exist, while pointing back to the primary rule file for the full policy.

### 10. Add a documentation sync gate

When the repository has enough documentation to become a real workflow dependency, create or refine a concrete checklist such as `docs/DOC_SYNC_CHECKLIST.md`.

That checklist should answer:
- which code changes require which docs to be updated
- when a task is incomplete because code changed but docs did not
- when to update `docs/TECH_DEBT.md`
- when an agent may explicitly state "no doc impact" instead of editing docs
- that every code task must either update the impacted docs or explicitly record "no doc impact" with a reason
- how this check should appear in PR templates, task summaries, or completion notes when such workflow artifacts exist

The primary rule file should treat this checklist as a completion gate, not as optional reading.

### 11. Retire duplicated or stale documents

After the new system exists, inspect the repository for old onboarding or generic reference docs that are no longer part of the active workflow.

Common candidates:
- numbered legacy docs like `1.*.md`, `2.*.md`
- old quick-start guides replaced by `docs/README.md`
- generic framework primers that are not project-specific
- obsolete skill references or file links that no longer exist

For each candidate, decide one of:
- merge unique facts into current authority docs, then archive it
- archive it as historical reference
- delete it if it provides no unique value and the user wants cleanup

If archiving, place it under `docs/archive/` and add a short `docs/archive/README.md` stating:
- archive docs are historical only
- they are not the authority source for current development
- current authority starts from the primary rule file and `docs/README.md`

Do not leave superseded docs in the active root path without a clear label, because agents will keep reading them.

## Phase 2: Audit & Repair

After the first version exists, run a dedicated validation pass before considering the repository context system complete.

### 12. Audit the authority structure

Verify:
- there is one obvious rules entrypoint
- there is one obvious navigation entrypoint
- startup prompts point to authority docs instead of duplicating them
- module-level `README.md` files are tactical and local rather than shadow copies of top-level rules
- the primary rule file clearly makes the documentation sync checklist part of task completion rather than a suggestion

### 13. Audit factual accuracy against code

Check the first version of the docs against:
- real route definitions
- schema or serializer definitions
- actual request builders and frontend client code
- configuration files and middleware chains
- model definitions and migrations

This phase must explicitly look for:
- documents that imply full coverage without actually having it
- mixed-up boundaries in multi-backend or multi-service repositories
- frontend client files that target missing or outdated backend endpoints
- route names, auth flows, or response fields that drifted from code
- backend-specific endpoint ownership that was flattened into a single generic API story
- auth route mismatches where similar capabilities use different paths or names across backends/services

When the repository has multiple backends or services, explicitly audit:
- which endpoints exist only on one backend
- which endpoints are intentionally shared
- whether similarly named auth endpoints use different concrete paths across services
- whether frontend API client directories still contain demo, legacy, or test-only clients that no longer map to real endpoints

### 14. Repair high-risk findings

When the audit finds issues, prefer these corrections:
- downgrade a doc from "complete reference" to "verified subset" when coverage is partial
- split API and architecture docs by backend/service when boundaries were previously blurred
- explicitly mark endpoint ownership when a route exists only on one backend/service
- call out stale frontend API client files when they remain in the repo but should not be treated as active integration code
- remove or downgrade weakly evidenced pitfalls
- clean dead references, obsolete client files, and stale archive status labels
- remove placeholder governance data and fake dates from debt tracking docs

### 15. Re-check completion criteria

Only after repair should the system be considered stable enough for repeated human and agent use.

## Reading Protocol To Embed

Whenever you create this system for a repository, ensure the final docs teach humans and agents to work in this order:

1. Read the repository's primary agent rule file
2. Read `docs/README.md`
3. Read the micro-tactical `README.md` in the target module folder
4. Inspect the actual code path to verify the names and logic
5. If docs and code disagree, trust code and repair the docs in the same PR
6. Before closing the task, run the repo's documentation sync checklist if one exists
7. If no docs changed, explicitly state "no doc impact" and why

Also ensure the docs teach humans and agents this ownership split:
- the primary rule file owns workflow rules
- `docs/README.md` owns navigation
- module `README.md` files own tactical local entry guidance
- archive docs own historical context only

Also ensure the final system teaches agent execution boundaries:
- whether work on the default branch is allowed
- when a separate branch is expected
- which agent roles may commit or push
- who owns merge authority
- what evidence is required from code-producing agents
- what human-readable delivery evidence is required before task closeout

## Constraints

Always enforce these constraints:
- DO NOT blindly trust official documentation if the running code contradicts it.
- DO NOT correct "wrongly formatted" variable names in existing files just to satisfy best practices; document the exception instead.
- DO NOT flatten all knowledge into one file.
- DO NOT treat documentation as a replacement for code testing and `grep` searching.
- DO NOT let the primary rule file, `docs/README.md`, startup prompts, and local READMEs all restate the same workflow in parallel.
- DO NOT leave dead references to deleted docs, deleted skills, or nonexistent paths in the active document system.
- DO NOT let `docs/API_ENDPOINTS.md` imply full route coverage unless all relevant route sources were actually checked.
- DO NOT keep weakly evidenced pitfalls or placeholder debt metadata just to make docs look complete.
- DO NOT assume all agents in a repository share the same execution permissions; document role-specific boundaries when the repo uses distinct agent roles.
- DO NOT produce machine-first prose that a new human maintainer cannot understand without prompt context.

## Prompt Templates

When a user asks how to use this skill, provide the most relevant ready-to-send prompt from this section instead of only summarizing the workflow.
Adapt the template to the repository context, but keep the structure intact.

### Template 1: Build the system from scratch

```text
Please use the project-context-bootstrap skill for this repository.

Goal:
Build a reliable human-and-agent-facing project context system so future AI agents and human maintainers can enter this repo, understand how to start, and develop with less blind scanning and fewer incorrect assumptions.

Requirements:
1. Inspect the repository shape, frameworks, routing, configuration, data model layer, and existing documentation.
2. Create or refine a single rules entrypoint in the repository's primary agent rule file.
3. Create or refine a single navigation entrypoint in `docs/README.md`.
4. Create or refine the stable knowledge docs that are actually justified by the codebase, including:
   - `docs/ARCHITECTURE.md`
   - `docs/API_ENDPOINTS.md`
   - `docs/DATABASE_SCHEMA.md`
   - `docs/KNOWN_PITFALLS.md`
   - `docs/TECH_DEBT.md` when needed
5. Add module-level `README.md` files only for high-value or high-risk code boundaries.
6. Add `docs/AGENT_STARTER_PROMPT.md` if this repo will be used repeatedly by multiple agents.
7. Add `docs/DOC_SYNC_CHECKLIST.md` if the repo needs a concrete documentation sync gate.
8. If the repository has old, duplicate, generic, or superseded docs, move them into `docs/archive/` and add `docs/archive/README.md`.
9. Ensure each authoritative doc includes a human-readable quick summary and a clear "who should read this" section.

Constraints:
- Code is the source of truth.
- Do not invent architecture facts.
- Do not duplicate workflow rules across multiple files.
- The primary rule file should own workflow rules.
- `docs/README.md` should own navigation.
- The rule layer must describe execution boundaries such as default-branch policy, branch expectations, commit/push permissions, merge authority, and evidence requirements.
- If the repository uses multiple agent roles, describe those execution permissions separately by role.
- Archive docs must not remain in the active path as if they were authoritative.
- If docs conflict with code, fix the docs.
- The resulting system must make documentation sync a required completion check, not an optional reminder.
- Generated docs must be easy for humans to scan without relying on implicit agent memory.

Output:
- Make the documentation changes directly in the repository.
- Then report:
  1. which files were added
  2. which files were updated
  3. which docs were archived or removed
  4. which facts were verified against code
  5. how human readability was improved (summary structure, terminology clarity, navigation)
  6. which areas still require manual follow-up

Important:
- This completes Phase 1 only.
- After this pass, run a separate audit-and-repair pass before treating the documentation as fully trustworthy.
```

### Template 2: Audit and repair an existing system

```text
Please use the project-context-bootstrap skill to audit and repair this repository's existing human-and-agent-facing documentation system.

Goal:
Do not rebuild everything. Identify drift, duplication, stale guidance, dead references, and outdated docs, then bring the system back to a single-source-of-truth structure.

Audit focus:
1. Is there exactly one obvious rules entrypoint?
2. Is there exactly one obvious navigation entrypoint?
3. Are startup prompts duplicating workflow rules instead of pointing to the authority docs?
4. Are there stale or superseded docs still sitting in the active docs path?
5. Are there dead references to deleted docs, deleted skills, or nonexistent paths?
6. Do active docs contain absolute statements that are not fully supported by the current code?
7. Is the documentation sync checklist treated as mandatory in the primary rule file and completion flow?
8. Are the authority docs readable for a human maintainer without hidden prompt context?

Repair requirements:
- Keep the strongest authority files.
- Remove duplication between the primary rule file, `docs/README.md`, startup prompts, and module READMEs.
- Archive historical docs under `docs/archive/` instead of leaving them mixed with active docs.
- Preserve unique factual content by merging it into the current authority docs before archiving old files.
- Verify that execution boundaries are documented clearly enough that future agents can tell whether they may branch, commit, push, or merge.
- If the repository uses multiple agent roles, verify that those permissions are separated by role rather than flattened into one generic rule.
- If an API doc currently overclaims completeness, downgrade it to a verified overview or verified subset unless full route coverage is proven.
- In multi-backend repositories, verify endpoint ownership and route-name differences explicitly instead of assuming functional parity.
- Inspect frontend API client folders for stale or demo clients that no longer map to real backend endpoints.
- Remove, downgrade, or annotate pitfalls that cannot be tied to code, config, logs, or repeated verified failures.
- Remove placeholder dates, fake resolved timestamps, and template residue from debt-tracking docs.
- If a documentation sync checklist exists, make sure the primary rule file and completion flow treat it as mandatory before task closeout.
- Ensure each authority doc has a concise quick summary and an explicit intended audience.

Output:
- Apply the fixes directly in the repository.
- Then report:
  1. which active docs remain authoritative
  2. which docs were archived
  3. which dead references were removed
  4. which duplicated rule sources were collapsed
  5. whether execution boundaries are now explicit enough for future agents
  6. whether docs are now human-readable by default
  7. which risks still remain
```

### Template 3: Archive stale legacy docs

```text
Please use the project-context-bootstrap skill, but limit this task to retiring stale legacy documentation.

Goal:
Identify old onboarding docs, generic tutorials, numbered legacy docs, and superseded reference files that are no longer part of the active workflow. Move them out of the active docs path without losing useful history.

Requirements:
1. Check whether each candidate doc is still referenced by the active documentation system.
2. If a legacy doc contains unique facts that still matter, merge those facts into the current authority docs first.
3. Move stale docs into `docs/archive/`.
4. Add or update `docs/archive/README.md` so it clearly states archive docs are historical only and not authoritative for current development.
5. Remove dead references from active docs.

Constraints:
- Do not archive currently authoritative docs.
- Do not delete files unless they provide no unique value and cleanup is explicitly desired.
- Do not leave old docs in the active root path without a clear status.

Output:
- Apply the archival changes directly in the repository.
- Then report:
  1. which files were archived
  2. which references were updated
  3. which unique facts were preserved elsewhere
  4. whether the active docs path is now clean
```

## Completion Checks

Before considering the bootstrap complete, verify:

- the repository has one obvious rules entrypoint
- the repository has one obvious navigation entrypoint
- module-level entry guides exist only where they materially reduce blind scanning
- startup prompts point to authority docs instead of duplicating them
- the rule layer makes default-branch policy, branching expectations, commit/push permissions, merge authority, and evidence requirements explicit
- repositories with multiple agent roles document execution boundaries separately by role
- stale or superseded docs are either archived or clearly marked as non-authoritative
- no active doc still points to deleted files or obsolete skills
- multi-backend repositories are explicitly separated in architecture and API docs
- any API document that claims completeness has been checked against real route sources
- backend-specific endpoint ownership is explicit when similar capabilities differ across services
- stale frontend API client files are either cleaned up or clearly documented as non-authoritative
- pitfalls are backed by evidence or clearly marked as needing confirmation
- debt logs do not contain placeholder dates or template residue
- the documentation sync checklist is treated as a required completion gate, with an explicit "no doc impact" path when appropriate
- authoritative docs include clear human-readable summaries and audience markers

These checks should be satisfied after Phase 2, not merely after the initial build pass.
