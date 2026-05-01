# 架构概览

```yaml
ai_summary:
  authority: "Android 客户端示例的架构入口"
  scope: "模块边界、数据流、构建变体和验证入口"
  read_when:
    - "修改 Compose 页面"
    - "修改网络层或本地缓存"
  verify_with:
    - "app/src/main/AndroidManifest.xml"
    - "app/build.gradle.kts"
  stale_when:
    - "新增 Gradle 模块"
    - "替换网络或数据库框架"
```

## 目的

说明 Android 客户端示例的主要边界，避免把 UI、网络和本地缓存规则混在一起。

## 适合读者

- Android 开发者
- 测试维护者
- AI 代理执行者

## 一分钟摘要

- `app` 模块承载 Compose UI、导航、ViewModel 和依赖注入入口。
- 网络层通过 Retrofit 或 OkHttp 暴露接口，不能在 UI 中直接拼接 URL。
- Room 或 DataStore 属于本地状态边界，迁移需要单独验证。

## 权威边界

本文件是示例架构概览，不替代真实代码中的 Gradle、Manifest、路由和测试。

## 如何验证

- 检查 `app/build.gradle.kts` 的插件、依赖和构建变体。
- 检查 `app/src/main/AndroidManifest.xml` 的权限和入口 Activity。
- 运行 `./gradlew testDebugUnitTest` 验证核心逻辑。
