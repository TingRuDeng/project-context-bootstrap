import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "project-context-bootstrap"
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

import validate_docs

from tests.fixtures import VALID_AGENTS_DOC, VALID_AI_CONTEXT, VALID_DOC, VALID_FRONTMATTER_DOC

class ValidateDocsTest(unittest.TestCase):
    def test_valid_context_system_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_file(root / "AGENTS.md", VALID_AGENTS_DOC)
            write_file(root / "docs" / "README.md", VALID_DOC)
            write_file(root / "docs" / "AI_CONTEXT.md", VALID_AI_CONTEXT)
            write_file(root / "docs" / "archive" / "README.md", "# 归档\n")
            write_file(root / "src" / "example.py", "# example\n")

            issues = validate_docs.validate_root(root)

            self.assertEqual([], issues)

    def test_frontmatter_authority_doc_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_file(root / "AGENTS.md", VALID_AGENTS_DOC)
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

    def test_coordination_fixture_passes(self):
        root = SKILL_ROOT / "examples" / "fixtures" / "coordination-root"

        issues = validate_docs.validate_root(root, profile="generic")

        self.assertEqual([], issues)

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

    def test_machine_absolute_path_is_reported(self):
        content = VALID_FRONTMATTER_DOC.replace(
            "`src/example.py`",
            "`/Users/example/project/src/example.py`",
        )

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "包含不可移植的本机绝对路径"))

    def test_api_home_route_is_not_reported_as_machine_path(self):
        content = VALID_FRONTMATTER_DOC.replace(
            "The example has a concrete source file.",
            "The API route `/oauth/home/` is a valid project route.",
        )

        issues = validate_single_doc(content)

        self.assertFalse(has_issue(issues, "包含不可移植的本机绝对路径"))

    def test_legacy_detail_docs_are_skipped_when_indexed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)
            append_file(
                root / "docs" / "README.md",
                "\n## Legacy detail docs\n\n- [Architecture](ARCHITECTURE.md)\n",
            )
            write_file(root / "docs" / "ARCHITECTURE.md", "# Architecture\n")

            issues = validate_docs.validate_root(root)

            self.assertEqual([], issues)

    def test_unindexed_legacy_doc_is_still_validated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)
            write_file(root / "docs" / "ARCHITECTURE.md", "# Architecture\n")
            write_file(root / "docs" / "DOC_SYNC_CHECKLIST.md", "# Completion Gate\n")

            issues = validate_docs.validate_root(root)

            self.assertTrue(has_issue(issues, "ARCHITECTURE.md: 缺少必备标题"))
            self.assertTrue(has_issue(issues, "DOC_SYNC_CHECKLIST.md: 缺少必备标题"))

    def test_agents_contract_is_validated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)
            write_file(root / "AGENTS.md", "# AGENTS.md\n")

            issues = validate_docs.validate_root(root)

            self.assertTrue(has_issue(issues, "AGENTS.md: 缺少必备标题"))

    def test_agents_file_budget_is_reported(self):
        long_agents = VALID_AGENTS_DOC + "\n".join("- 具体规则\n" for _ in range(360))

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)
            write_file(root / "AGENTS.md", long_agents)

            issues = validate_docs.validate_root(root)

            self.assertTrue(has_issue(issues, "AGENTS.md: 超过 350 行路由文件预算"))

    def test_duplicate_ai_summary_is_reported(self):
        content = VALID_FRONTMATTER_DOC + "\n```yaml\nai_summary:\n  purpose: duplicate\n```\n"

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "包含多个 ai_summary 摘要块"))

    def test_inline_ai_summary_lists_are_checked(self):
        content = VALID_FRONTMATTER_DOC.replace(
            '  source_of_truth:\n    - "src/example.py"',
            '  source_of_truth: ["src/missing.py"]',
        )

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "source_of_truth 路径不存在 src/missing.py"))

    def test_multi_command_verify_section_requires_tiers(self):
        content = VALID_FRONTMATTER_DOC.replace(
            "```bash\npython3 -m unittest tests/test_validate_docs.py\n```",
            "```bash\npython3 -m unittest tests/test_validate_docs.py\npython3 scripts/validate_docs.py . --profile generic\n```",
        )

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "缺少验证命令分层"))

    def test_network_read_verify_tier_is_accepted(self):
        content = VALID_FRONTMATTER_DOC.replace(
            "```bash\npython3 -m unittest tests/test_validate_docs.py\n```",
            "Quick:\n\n```bash\npython3 -m unittest tests/test_validate_docs.py\n```\n\n"
            "Network-read:\n\n```bash\nnpm view example-package version --json\n```",
        )

        issues = validate_single_doc(content)

        self.assertEqual([], issues)

    def test_read_only_external_command_under_release_side_effect_is_reported(self):
        content = VALID_FRONTMATTER_DOC.replace(
            "```bash\npython3 -m unittest tests/test_validate_docs.py\n```",
            "Release-side-effect:\n\n```bash\nnpm view example-package version --json\n```",
        )

        issues = validate_single_doc(content)

        self.assertTrue(has_issue(issues, "只读外部命令应放入 network-read 分层"))

    def test_nested_git_repositories_require_git_c_commands(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)
            write_file(root / "backend" / ".git" / "HEAD", "ref: refs/heads/main\n")
            write_file(root / "frontend" / ".git" / "HEAD", "ref: refs/heads/main\n")

            issues = validate_docs.validate_root(root)

            self.assertTrue(has_issue(issues, "coordination directory"))
            self.assertTrue(has_issue(issues, "git -C backend"))
            self.assertTrue(has_issue(issues, "git -C frontend"))

    def test_dependency_markdown_links_are_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)
            write_file(root / "node_modules" / "pkg" / "README.md", "[bad](missing.md)\n")

            issues = validate_docs.validate_root(root)

            self.assertEqual([], issues)

    def test_local_agent_tool_markdown_links_are_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_core_context(root)
            write_file(root / ".agents" / "skills" / "demo" / "SKILL.md", "[bad](missing.md)\n")
            write_file(root / ".codex" / "skills" / "demo" / "SKILL.md", "[bad](missing.md)\n")

            issues = validate_docs.validate_root(root)

            self.assertEqual([], issues)

def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def append_file(path, content):
    with path.open("a", encoding="utf-8") as handle:
        handle.write(content)

def write_core_context(root):
    write_file(root / "AGENTS.md", VALID_AGENTS_DOC)
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
        write_file(root / "AGENTS.md", VALID_AGENTS_DOC)
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
