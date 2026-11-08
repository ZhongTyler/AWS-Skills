# Skills 协作与独立接入

本仓的基础入口和领域规则由本仓提供。运行环境按 module.json 与业务说明核对。当前用户授权、宿主权威及事实所有权适用于所有接线。

## 接口合同

module-entry@1 由 module.json、README 和本说明组成，提供模块身份、版本、能力、任务入口、必要环境和可选关系。它支持 Agent 或工具发现和组织交接。具体业务数据仍采用目标模块已有协议和 schema，接入前读取相关入口。

| 相关模块 | 可补充的职责 | 入口 |
|---|---|---|
| Meta | Optional workspace governance and recoverable collaboration. | [README](https://github.com/ZhongTyler/AWS-Meta) |
| Research | Collect sources and compile traceable studies and reader navigation. | [README](https://github.com/ZhongTyler/AWS-Research) |
| Knowledge | Query source-grounded material and maintain an owned knowledge library. | [README](https://github.com/ZhongTyler/AWS-Knowledge) |
| Tools | Configure optional source, processing and local-model tools. | [README](https://github.com/ZhongTyler/AWS-Tools) |
| GameAnalysisDecision | Analyze game evidence and conditional design decisions. | [README](https://github.com/ZhongTyler/AWS-GameAnalysisDecision) |
| GamePresentation | Prepare, review and integrate game presentation resources. | [README](https://github.com/ZhongTyler/AWS-GamePresentation) |
| GameProject | Create an owned Godot project with maintenance and resource atlases. | [README](https://github.com/ZhongTyler/AWS-GameProject) |
| Travel | Research, plan and render an owned trip as an offline website. | [README](https://github.com/ZhongTyler/AWS-Travel) |

## 交接与验收

1. 先明确当前目标、现有工作流、拟借用能力和授权。读取相关模块声明，审阅职责重叠、输入输出和调用入口、数据与事实归属、恢复边界。
2. 交接材料包含问题、约束、资料或产物位置、版本与来源、预期结果和接收 owner。目标模块拥有自己的工作产物和验证记录，调用方保留原任务决定。
3. 相似名称和已下载目录仅提供发现线索。通过库存的同一模块可复用，已有替代能力按当前任务审阅，采用适配或并存方案后再接线。
4. 模块间使用明确路径或宿主登记的位置。缺少可选模块时按本仓基础方法继续，并保留实际缺口。依赖某项工具或服务的具体功能先验证其接口版本与配置。
5. 获取入口在 .module/module_manager.py，相关模块安装到工作区平级 modules 目录。它只获取代码，业务接线和服务启用沿实际任务授权执行。单个模块目录也可以独立克隆或下载后使用。

## 发布与恢复

本仓是唯一公开发布内容权威，AWS 通过 Git submodule 固定已发布提交。后续版本在本仓维护，更新 module.json、文件库存和相关说明，验证后创建不可变 tag 与正式附件。AWS 更新引用并验证组合。

已有安装从 1.30.0 升级时使用 AWS 2.0.0 的迁移入口，保留原受管文件、事务与客户端 Skill 记录。独立 Git 获取保留版本和工作区 owner，可先使用新目录审阅差异，再按实际范围升级。用户修改、项目与私人数据由用户保全。获取失败的 staging 与事务记录留在 .module-manager 中供检查，不能据此宣称安装完成。

图示表示可选交接方向。真实业务适配、研究结论、艺术质量与人类接受沿实际任务验证。

## 维护本仓

修改前读取当前文件、Git 与 owner。新文件经公开边界审阅后显式 git add，用户资料留包外。修改关系声明后运行 `python .module/module_docs.py --root .`，再用 `--check` 核对全景。预览库存使用 `python .module/module_manager.py seal`，确认范围后加 `--apply`，随后运行 verify 与受影响业务测试。提交、tag 与正式附件沿本仓版本进行，AWS 更新对应 gitlink 并验证组合。

共享模块管理器和全景生成器由 AWS scripts 中的通用源构建，本仓随版本附带确定字节副本。接收方运行本仓副本即可，运行时读取本仓 module.json。业务接线按实际能力合同进行。
