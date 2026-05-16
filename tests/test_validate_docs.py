import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_docs

from tests.fixtures import VALID_AI_CONTEXT, VALID_DOC, VALID_FRONTMATTER_DOC

class ValidateDocsTest(unittest.TestCase):
    def test_valid_context_system_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_file(root / "AGENTS.md", "# AGENTS.md\n")
            write_file(root / "docs" / "README.md", VALID_DOC)
            write_file(root / "docs" / "AI_CONTEXT.md", VALID_AI_CONTEXT)
            write_file(root / "docs" / "archive" / "README.md", "# 归档\n")
            write_file(root / "src" / "example.py", "# example\n")

            issues = validate_docs.validate_root(root)

            self.assertEqual([], issues)

    def test_frontmatter_authority_doc_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_file(root / "AGENTS.md", "# AGENTS.md\n")
            write_file(root / "docs" / "README.md", VALID_FRONTMATTER_DOC)
            write_file(root / "docs" / "AI_CONTEXT.md", VALID_AI_CONTEXT)
            write_file(root / "docs" / "archive" / "README.md", "# 归档\n")
            write_file(root / "src" / "example.py", "# example\n")

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

    def test_generic_profile_requires_agents(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)
            (root / "AGENTS.md").unlink()

            issues = validate_docs.validate_root(root, profile="generic")

            self.assertTrue(has_issue(issues, "缺少必需文件 AGENTS.md"))

    def test_generic_profile_requires_ai_context(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)
            (root / "docs" / "AI_CONTEXT.md").unlink()

            issues = validate_docs.validate_root(root, profile="generic")

            self.assertTrue(has_issue(issues, "缺少必需文件 docs/AI_CONTEXT.md"))

    def test_generic_profile_does_not_require_android_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)

            issues = validate_docs.validate_root(root, profile="generic")

            self.assertEqual([], issues)

    def test_android_profile_requires_build_matrix(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_android_context(root)
            (root / "docs" / "BUILD_MATRIX.md").unlink()

            issues = validate_docs.validate_root(root, profile="android")

            self.assertTrue(has_issue(issues, "缺少必需文件 docs/BUILD_MATRIX.md"))

    def test_android_profile_requires_module_map(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_android_context(root)
            (root / "docs" / "MODULE_MAP.md").unlink()

            issues = validate_docs.validate_root(root, profile="android")

            self.assertTrue(has_issue(issues, "缺少必需文件 docs/MODULE_MAP.md"))

    def test_android_profile_requires_testing_matrix(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_android_context(root)
            (root / "docs" / "TESTING_MATRIX.md").unlink()

            issues = validate_docs.validate_root(root, profile="android")

            self.assertTrue(has_issue(issues, "缺少必需文件 docs/TESTING_MATRIX.md"))

    def test_android_profile_requires_manifest_doc(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_android_context(root)
            (root / "docs" / "MANIFEST_AND_PERMISSIONS.md").unlink()

            issues = validate_docs.validate_root(root, profile="android")

            self.assertTrue(has_issue(issues, "缺少必需文件 docs/MANIFEST_AND_PERMISSIONS.md"))

    def test_ai_summary_purpose_empty_is_reported(self):
        content = VALID_FRONTMATTER_DOC.replace('purpose: "示例文档"', 'purpose: ""')

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "ai_summary.purpose 不能为空"))

    def test_ai_summary_verify_with_empty_is_reported(self):
        content = VALID_FRONTMATTER_DOC.replace(
            'verify_with:\n    - "python3 -m unittest tests/test_validate_docs.py"',
            "verify_with: []",
        )

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "ai_summary.verify_with 必须至少包含一项"))

    def test_verify_with_natural_language_is_reported(self):
        content = VALID_FRONTMATTER_DOC.replace(
            "python3 -m unittest tests/test_validate_docs.py",
            "Run tests",
        )

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "verify_with 不是具体命令"))

    def test_source_of_truth_missing_path_is_reported(self):
        content = VALID_FRONTMATTER_DOC.replace("src/example.py", "src/missing.py")

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "source_of_truth 路径不存在 src/missing.py"))

    def test_key_section_tbd_is_reported(self):
        content = replace_section(VALID_FRONTMATTER_DOC, "## Key facts", "TBD")

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "章节 ## Key facts 内容过于空泛"))

    def test_key_section_best_practices_is_reported(self):
        content = replace_section(
            VALID_FRONTMATTER_DOC,
            "## Key facts",
            "Follow best practices",
        )

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "章节 ## Key facts 内容过于空泛"))

    def test_verify_with_chinese_natural_language_is_reported(self):
        content = VALID_FRONTMATTER_DOC.replace(
            "python3 -m unittest tests/test_validate_docs.py",
            "手动确认",
        )

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "verify_with 不是具体命令"))

    def test_chinese_generic_section_is_reported(self):
        content = replace_section(
            VALID_FRONTMATTER_DOC,
            "## How to verify",
            "运行测试",
        )

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "章节 ## How to verify 内容过于空泛"))

def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def write_core_context(root):
    write_file(root / "AGENTS.md", "# AGENTS.md\n")
    write_file(root / "docs" / "README.md", VALID_FRONTMATTER_DOC)
    write_file(root / "docs" / "AI_CONTEXT.md", VALID_AI_CONTEXT)
    write_file(root / "docs" / "archive" / "README.md", "# 归档\n")
    write_file(root / "src" / "example.py", "# example\n")

def write_android_context(root):
    write_core_context(root)
    for name in (
        "BUILD_MATRIX.md",
        "MODULE_MAP.md",
        "TESTING_MATRIX.md",
        "MANIFEST_AND_PERMISSIONS.md",
    ):
        write_file(root / "docs" / name, VALID_FRONTMATTER_DOC)

def validate_single_doc(content):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        write_file(root / "AGENTS.md", "# AGENTS.md\n")
        write_file(root / "docs" / "README.md", content)
        write_file(root / "docs" / "AI_CONTEXT.md", VALID_AI_CONTEXT)
        write_file(root / "docs" / "archive" / "README.md", "# 归档\n")
        write_file(root / "src" / "example.py", "# example\n")
        return validate_docs.validate_root(root, profile="generic")

def replace_section(content, heading, replacement):
    start = content.index(heading) + len(heading)
    next_heading = content.index("\n## ", start)
    return content[:start] + "\n\n" + replacement + "\n" + content[next_heading:]

def has_issue(issues, text):
    return any(text in issue for issue in issues)

if __name__ == "__main__":
    unittest.main()
