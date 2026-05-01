# AI Context

> 用一句话说明本仓库是什么，以及 AI 读取本文件能解决什么问题。

## 权威文档地图

- `README.md`: 说明每份文档的职责、读者和阅读顺序。
- `ARCHITECTURE.md`: 说明系统边界、模块关系和关键数据流。

## 任务读取路径

- 修改 API：先读 `README.md`，再读 `API_ENDPOINTS.md`，最后核对真实路由和客户端调用。
- 修改数据模型：先读 `DATABASE_SCHEMA.md`，再核对模型、迁移和测试。
- 修改模块逻辑：先读目标模块 `README.md`，再核对实现文件。

## 关键证据入口

- `path/to/router.py:function_name`
- `path/to/schema.py:ClassName`
- `path/to/test_file.py::test_name`

## 高风险误读点

- 不要把未验证的接口列表当成完整 API 目录。
- 不要把局部模块例外推广成全局规则。

## Optional

- `archive/README.md`: 只在追溯旧决策时读取。
