import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_docs


VALID_DOC = """# 示例文档

```yaml
ai_summary:
  authority: "示例权威职责"
  scope: "示例覆盖范围"
  read_when:
    - "修改示例模块"
  verify_with:
    - "src/example.py:Example"
  stale_when:
    - "示例模块结构变化"
```

## 目的

说明示例文档的用途。

## 适合读者

- 维护者

## 一分钟摘要

- 示例系统具备稳定入口。

## 权威边界

本文件只描述示例上下文。

## 如何验证

- 检查 `src/example.py:Example`。
"""


VALID_AI_CONTEXT = """# AI Context

> 示例仓库的 AI 上下文索引。

## 权威文档地图

- [文档导航](README.md): 示例导航入口。

## 任务读取路径

- 修改示例模块：先读 `README.md`。

## 关键证据入口

- `src/example.py:Example`

## 高风险误读点

- 不要把示例规则当成生产规则。

## Optional

- [归档说明](archive/README.md): 可跳过的历史材料。
"""


class ValidateDocsTest(unittest.TestCase):
    def test_valid_context_system_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_file(root / "docs" / "README.md", VALID_DOC)
            write_file(root / "docs" / "AI_CONTEXT.md", VALID_AI_CONTEXT)
            write_file(root / "docs" / "archive" / "README.md", "# 归档\n")

            issues = validate_docs.validate_root(root)

            self.assertEqual([], issues)

    def test_missing_ai_summary_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_file(root / "docs" / "README.md", "# 文档\n\n## 目的\n\n缺少摘要块。\n")

            issues = validate_docs.validate_root(root)

            self.assertTrue(has_issue(issues, "缺少 ai_summary 摘要块"))

    def test_ai_context_section_order_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_file(root / "docs" / "AI_CONTEXT.md", "# AI Context\n\n## 任务读取路径\n")

            issues = validate_docs.validate_root(root)

            self.assertTrue(has_issue(issues, "AI_CONTEXT 缺少章节"))


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def has_issue(issues, text):
    return any(text in issue for issue in issues)


if __name__ == "__main__":
    unittest.main()
