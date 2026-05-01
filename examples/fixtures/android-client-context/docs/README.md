# 文档导航

```yaml
ai_summary:
  authority: "Android 客户端示例的文档导航入口"
  scope: "示例仓库的阅读顺序、权威文件和验证入口"
  read_when:
    - "进入 Android 客户端仓库"
    - "为 AI 会话选择上下文"
  verify_with:
    - "settings.gradle.kts"
    - "app/build.gradle.kts"
  stale_when:
    - "模块结构或构建变体变化"
```

## 目的

说明 Android 客户端示例仓库的文档入口和阅读顺序。

## 适合读者

- Android 开发者
- AI 代理执行者
- 代码审查者

## 一分钟摘要

- 规则入口是根目录 `AGENTS.md`。
- AI 快速索引是 [AI_CONTEXT.md](AI_CONTEXT.md)。
- 架构入口是 [ARCHITECTURE.md](ARCHITECTURE.md)。

## 权威边界

本文件只负责导航，不复制架构、接口或数据库细节。

## 如何验证

- 检查 `settings.gradle.kts` 是否仍包含文档中提到的模块。
- 检查 `app/build.gradle.kts` 是否仍包含 Compose、Room、Retrofit 或 OkHttp 依赖。
