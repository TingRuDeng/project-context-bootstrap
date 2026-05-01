# AI Context

> Android 客户端示例仓库的 AI 上下文索引，用于快速选择权威文档和验证入口。

## 权威文档地图

- [文档导航](README.md): 示例仓库的阅读顺序、权威边界和验证入口。
- [架构概览](ARCHITECTURE.md): Android 模块边界、数据流和高风险变更点。

## 任务读取路径

- 修改 Compose 页面：先读 `AGENTS.md`，再读 `docs/ARCHITECTURE.md`，最后核对目标页面和 ViewModel。
- 修改网络接口：先读 `docs/ARCHITECTURE.md`，再核对 Retrofit 或 OkHttp 调用点。
- 修改本地数据：先读 `docs/ARCHITECTURE.md`，再核对 Room migration 或 DataStore key。

## 关键证据入口

- `settings.gradle.kts`
- `app/build.gradle.kts`
- `app/src/main/AndroidManifest.xml`
- `./gradlew testDebugUnitTest`

## 高风险误读点

- 不要把 debug 构建变体行为当成 release 行为。
- 不要绕过 ViewModel 在 Compose UI 中直接发起网络请求。
- 修改权限后必须核对 Manifest 和运行时权限处理。

## Optional

- `docs/archive/README.md`
