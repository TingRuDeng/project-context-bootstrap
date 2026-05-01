# AGENTS.md

## 启动检查

- 先读 `docs/README.md`。
- 处理 Android UI、网络、数据库或权限任务前，读对应模块文档并核对真实 Gradle 配置。

## 验证要求

- 修改 Kotlin 或 Compose 代码后运行 `./gradlew testDebugUnitTest`。
- 修改 Manifest、权限或构建变体后运行 `./gradlew assembleDebug`。

## 执行边界

- 不直接改默认分支，功能任务使用独立分支。
- 未运行验证命令前，不声明任务完成。
