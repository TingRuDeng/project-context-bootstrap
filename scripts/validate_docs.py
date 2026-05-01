#!/usr/bin/env python3
import re
import sys
from pathlib import Path

AI_CONTEXT_PATH = Path("docs/AI_CONTEXT.md")
MAX_FILE_BYTES = 1_000_000
MAX_AI_CONTEXT_LINES = 120
PLACEHOLDER_PATTERN = re.compile(r"\b(TBD|TODO|placeholder|fill in|later)\b|待补")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

REQUIRED_AUTHORITY_HEADINGS = (
    "## 目的",
    "## 适合读者",
    "## 一分钟摘要",
    "## 权威边界",
    "## 如何验证",
)

REQUIRED_AI_KEYS = (
    "authority:",
    "scope:",
    "read_when:",
    "verify_with:",
    "stale_when:",
)

AI_CONTEXT_SECTIONS = (
    "## 权威文档地图",
    "## 任务读取路径",
    "## 关键证据入口",
    "## 高风险误读点",
    "## Optional",
)

SKIPPED_DOC_PARTS = (
    "docs/archive/",
    "docs/AGENT_STARTER_PROMPT.md",
    "docs/DOC_SYNC_CHECKLIST.md",
)


def validate_root(root):
    base = Path(root).resolve()
    issues = validate_base(base)
    if issues:
        return issues

    issues.extend(validate_authority_docs(base))
    issues.extend(validate_ai_context(base))
    issues.extend(validate_links(base))
    return issues


def validate_base(base):
    if not base.exists():
        return [f"{base}: 路径不存在"]
    if not base.is_dir():
        return [f"{base}: 必须是目录"]
    return []


def validate_authority_docs(base):
    issues = []
    for path in sorted((base / "docs").glob("*.md")):
        rel = relative_path(path, base)
        if should_skip_authority_doc(rel):
            continue
        text = read_text(path)
        issues.extend(validate_file_text(path, base, text))
        if rel != AI_CONTEXT_PATH.as_posix():
            issues.extend(validate_authority_contract(path, base, text))
    return issues


def validate_file_text(path, base, text):
    rel = relative_path(path, base)
    issues = []
    if PLACEHOLDER_PATTERN.search(text):
        issues.append(f"{rel}: 存在占位词或未完成标记")
    if path.stat().st_size > MAX_FILE_BYTES:
        issues.append(f"{rel}: 文件超过 {MAX_FILE_BYTES} 字节")
    return issues


def validate_authority_contract(path, base, text):
    rel = relative_path(path, base)
    issues = []
    for heading in REQUIRED_AUTHORITY_HEADINGS:
        if heading not in text:
            issues.append(f"{rel}: 缺少必备标题 {heading}")
    issues.extend(validate_ai_summary(rel, text))
    return issues


def validate_ai_summary(rel, text):
    block = find_ai_summary_block(text)
    if not block:
        return [f"{rel}: 缺少 ai_summary 摘要块"]

    issues = []
    for key in REQUIRED_AI_KEYS:
        if key not in block:
            issues.append(f"{rel}: ai_summary 缺少字段 {key}")
    return issues


def find_ai_summary_block(text):
    pattern = re.compile(r"```ya?ml\s+(ai_summary:.*?)```", re.DOTALL)
    match = pattern.search(text)
    return match.group(1) if match else ""


def validate_ai_context(base):
    path = base / AI_CONTEXT_PATH
    if not path.exists():
        return []

    text = read_text(path)
    rel = AI_CONTEXT_PATH.as_posix()
    issues = validate_file_text(path, base, text)
    issues.extend(validate_ai_context_sections(rel, text))
    if count_lines(text) > MAX_AI_CONTEXT_LINES:
        issues.append(f"{rel}: 超过 {MAX_AI_CONTEXT_LINES} 行上下文预算")
    return issues


def validate_ai_context_sections(rel, text):
    positions = []
    issues = []
    for section in AI_CONTEXT_SECTIONS:
        index = text.find(section)
        if index == -1:
            issues.append(f"{rel}: AI_CONTEXT 缺少章节 {section}")
        positions.append(index)

    known_positions = [position for position in positions if position >= 0]
    if known_positions != sorted(known_positions):
        issues.append(f"{rel}: AI_CONTEXT 章节顺序错误")
    return issues


def validate_links(base):
    issues = []
    for path in sorted(base.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = read_text(path)
        issues.extend(validate_links_in_file(path, base, text))
    return issues


def validate_links_in_file(path, base, text):
    issues = []
    for target in LINK_PATTERN.findall(text):
        if is_external_or_anchor(target):
            continue
        target_path = (path.parent / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            rel = relative_path(path, base)
            issues.append(f"{rel}: 本地链接不存在 {target}")
    return issues


def should_skip_authority_doc(rel):
    return rel in SKIPPED_DOC_PARTS or rel.startswith("docs/archive/")


def is_external_or_anchor(target):
    return (
        target.startswith("#")
        or "://" in target
        or target.startswith("mailto:")
    )


def read_text(path):
    return path.read_text(encoding="utf-8")


def relative_path(path, base):
    return path.resolve().relative_to(base).as_posix()


def count_lines(text):
    return len(text.splitlines())


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    root = Path(args[0]) if args else Path.cwd()
    issues = validate_root(root)
    for issue in issues:
        print(issue)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
