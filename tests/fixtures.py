VALID_DOC = """---
ai_summary:
  purpose: "示例文档"
  read_when:
    - "修改示例模块"
  source_of_truth:
    - "src/example.py"
  verify_with:
    - "python3 -m unittest tests/test_validate_docs.py"
  stale_when:
    - "示例模块结构变化"
---

# Example Doc

## Purpose

说明示例文档的用途。

## Source of truth

- `src/example.py`

## Key facts

- 示例系统具备稳定入口。

## How to verify

```bash
python3 -m unittest tests/test_validate_docs.py
```

## Stale when

- 示例模块变化。
"""

VALID_FRONTMATTER_DOC = """---
ai_summary:
  purpose: "示例文档"
  read_when:
    - "修改示例模块"
  source_of_truth:
    - "src/example.py"
  verify_with:
    - "python3 -m unittest tests/test_validate_docs.py"
  stale_when:
    - "示例模块变化"
---

# Example Doc

## Purpose

Explain the example document.

## Source of truth

- `src/example.py`

## Key facts

- The example has a concrete source file.

## How to verify

```bash
python3 -m unittest tests/test_validate_docs.py
```

## Stale when

- The example source file changes.
"""

VALID_AI_CONTEXT = """---
ai_summary:
  purpose: "示例上下文地图"
  read_when:
    - "修改示例模块"
  source_of_truth:
    - "AGENTS.md"
    - "docs/README.md"
  verify_with:
    - "python3 -m unittest tests/test_validate_docs.py"
  stale_when:
    - "示例模块结构变化"
---

# AI Context

> 示例仓库的 AI 上下文索引。

## Project Snapshot

- 示例仓库用于验证 context pack。

## Core Directories

- `src/`

## Documentation Map

- `docs/README.md`

## Common Task Reading Paths

- 修改示例模块：先读 `docs/README.md`。

## High-Risk Areas

- 不要把示例规则当成生产规则。

## Validation Commands

```bash
python3 -m unittest tests/test_validate_docs.py
```

## Stale when

- 示例结构变化。
"""
