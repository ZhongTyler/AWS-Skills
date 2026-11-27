# 中文方法目录

显示名和简介来自 [统一中文映射](../locales/zh-CN.json)。英文 ID 用于调用、选装与升级；中文名用于阅读。

外部方法按包内来源记录列出原仓库。工作区维护表示当前维护归属，不据此宣称原创。上游正文、原始快照、代码和既有许可保持原样。

| 中文名称 | 调用 ID | 简介 | 来源 |
|---|---|---|---|
| [匿名对照评测](../library/agent-blind-eval/SKILL.md) | agent-blind-eval | 当需要实际评测候选提示词、流程或回答策略，或交付可执行评测协议时，组织预注册匿名对照与独立评分，按需自主判断是否重复生成观察稳定性；不用于普通方案选型、参数比较、单份回答审查或仅审计既有评测结论。 | 工作区维护 |
| [去防御式写作](../library/anti-defensive-writing/SKILL.md) | anti-defensive-writing | 改写论文、技术报告、审稿回复和技术操作说明中的重复免责、层叠试探或薄弱主线，保留证据、必要限定与操作含义；支持直接点名，也可由现有写作技能按需调用，普通润色无需额外加载。 | [原仓库](https://github.com/Kiterlin/anti-defensive-writing) |
| [双向最强论证](../library/bidirectional-steelman/SKILL.md) | bidirectional-steelman | 当目标已清楚、两种立场各有实质理由且关键前提会改变选择时，构造双方最强论证与条件化建议；不用于普通参数对比、事实查询、已拍板执行或尚需定义问题的困惑。 | 工作区维护 |
| [学术引文管理](../library/citation-management/SKILL.md) | citation-management | 检索并核对学术文献元数据，解析 DOI、PMID、arXiv 标识，整理或去重 BibTeX。用于有明确学术引文需求的任务；普通网页问答、剪藏、知识入库和证据推理本身不触发。 | [原仓库](https://github.com/K-Dense-AI/scientific-agent-skills) |
| [代码模块设计](../library/codebase-design/SKILL.md) | codebase-design | 用深模块的设计方法审视代码接口、职责边界和实现细节，寻找简化接口、提高可测试性及便于智能体理解代码的机会；也供其他方法引用这套设计术语。 | [原仓库](https://github.com/mattpocock/skills) |
| [设计评审](../library/design-critique/SKILL.md) | design-critique | 从可用性、信息层级和一致性出发提供结构化设计反馈。适用于评审界面、设计稿、Figma 链接或截图，可用于探索阶段到最终完善阶段。 | [原仓库](https://github.com/anthropics/knowledge-work-plugins) |
| [设计开发交接](../library/design-handoff/SKILL.md) | design-handoff | 将已准备进入开发的设计整理成交接规格，覆盖布局、设计变量、组件参数、交互状态、响应式断点、边界情况和动效细节。 | [原仓库](https://github.com/anthropics/knowledge-work-plugins) |
| [持续文档组织](../library/document-organization/SKILL.md) | document-organization | 组织或重构面向人读的清单、规划、资料索引、README与工作入口，保留查找、比较、续接和持续更新所需的信息功能。纯语句润色、代理执行合同和业务流程改造沿已有入口。 | 工作区维护 |
| [领域建模](../library/domain-modeling/SKILL.md) | domain-modeling | 建立并梳理项目的领域模型。用于讨论代码中的业务术语、编写或调整术语表，以及记录或修改架构决策。 | [原仓库](https://github.com/mattpocock/skills) |
| [直观与专业双层解释](../library/dual-layer-explainer/SKILL.md) | dual-layer-explainer | 当用户需要理解机制为何成立、如何运作及类比边界时，用直观模型对应准确术语；算法、协议、检索、推断或资源过程可按需做成可操作解释。普通定义、翻译、代码注释和明确实施不自动触发。 | 工作区维护 |
| [评测结果分析](../library/eval-result-analysis/SKILL.md) | eval-result-analysis | 分析已有 AI 对照或重复试验，拆解题型准确度、部分符合、生成稳定性、置信度、错误来源与全流程消耗，并复查分析缺漏；不用于启动新盲评、普通参数选型或只核对一个总分。 | 工作区维护 |
| [证据审查](../library/evidence-audit/SKILL.md) | evidence-audit | 审查既有实质论断或研究报告的来源可靠性、证据覆盖与推理，按原目标查重要遗漏，并按需复核返修；不用于普通查事实、核对数量、运行测试、代码审查或从零广泛研究。 | 工作区维护 |
| [反馈闭环](../library/feedback-loop/SKILL.md) | feedback-loop | 当开发或实验任务因状态难观察、参数反复调整、问题难复现或结果难比较而受阻时，按共用方法复用或补齐最小反馈入口，并验证实际生效、比较与恢复；不限表现层，不用于普通解释、一次明确修改或无实际瓶颈时预建平台。 | 工作区维护 |
| [界面专项审查](../library/finesse-ui/SKILL.md) | finesse-ui | 按实际缺口审查组件状态、配置流程或产品操作界面，选用固定版本 Finesse 专项参考；不用于普通文字润色、已定方案的小修或强制换风格。 | [原仓库](https://github.com/mouse-lin/finesse-skill) |
| [游戏改动审查](../library/game-change-audit/SKILL.md) | game-change-audit | 审计游戏规则改动、玩法实现或界面与美术资源交付，结合批准规格、实际产物和可复现状态定位退化、漏项及合理取舍；适用于改动评审、资源自审和验收前查漏，不用于泛泛游戏评论或只检查文件能否加载。 | 工作区维护 |
| [游戏设计决策支持](../library/game-decision-support/SKILL.md) | game-decision-support | 游戏设计或开发的下一关键判断缺少经验、案例、专业分析或发行产物证据时，按缺口选择可用的 Knowledge、GameAnalysisDecision、Research 或 REA，并写回宿主；不用于既定规格的机械实现、普通源码调试或纯状态查询。 | 工作区维护 |
| [游戏介绍写作](../library/game-description-writing/SKILL.md) | game-description-writing | 撰写或重组面向玩家的游戏介绍，包括 Steam 商店页、短描述、关于这款游戏、游戏详情和试玩描述。个人作品集借用玩法段结构，作者口吻由作品集 Skill 负责。设计规格、技术交接和纯润色沿原入口。 | 工作区维护 |
| [游戏开发作品介绍](../library/game-development-portfolio/SKILL.md) | game-development-portfolio | 组织在研游戏的作品介绍、完整详情和开发案例。按读者问题与版位选材，讲清游戏怎样运转、关键规则为何这样设计，以及成品长处是怎样做出来的。已发布游戏仅在需要讲开发过程时使用。Steam 短描述、纯玩法介绍、普通作品卡片和纯润色沿各自入口。 | 工作区维护 |
| [游戏证据搜集](../library/game-evidence-collection/SKILL.md) | game-evidence-collection | 为单款游戏研究搜集并核对具体规则、版本、发行包、截图与操作过程，选择源码、发行物或多模态取证路径；由通用研究搜集按需调用，不用于一般游戏新闻或直接生成整作研究结论。 | 工作区维护 |
| [游戏操作反馈](../library/game-feel/SKILL.md) | game-feel | 为机制已正确的命中、落地、拾取等事件选择震屏、顿帧、缓动与音画反馈配方，按重要性分档并保持恢复；不替代控制器、镜头跟随或玩法规则设计。 | [原仓库](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) |
| [游戏流程与资源图](../library/game-flow-diagrams/SKILL.md) | game-flow-diagrams | 当需要绘制或审查游戏流程图、玩法循环图或资源流转图时，沿真实构建标出玩家动作、状态转折与资源去向，核对反馈循环和移动端可读性。 | 工作区维护 |
| [游戏美术与表现](../library/game-presentation/SKILL.md) | game-presentation | 按用途推进游戏美术、UI、动画和音效资源准备、真实引擎接入与可恢复验证；适用于表现升级，不用于纯玩法数值修改。 | 工作区维护 |
| [游戏运行时模式](../library/game-runtime-patterns/SKILL.md) | game-runtime-patterns | 当游戏资源或场景生命周期、时间输入、坐标碰撞、规则视图、联机会话或性能复用存在具体缺口，或浏览器游戏缺少可核验操作回放时，选择宿主适配配方并验证；不用于引擎选型、纯美术或无缺口全量架构重建。 | 工作区维护 |
| [游戏界面与操作体验](../library/game-ui-ux/SKILL.md) | game-ui-ux | 实现或修复游戏 HUD 与菜单的布局缩放、安全区、键鼠或手柄焦点、返回路径和状态更新；按当前引擎与宿主结构采用，不用于普通网页视觉风格或纯玩法规则。 | [原仓库](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) |
| [Godot 脚本开发模式](../library/godot-gdscript-patterns/SKILL.md) | godot-gdscript-patterns | 提供 Godot 4 的 GDScript 开发模式，涵盖信号、场景、状态机与性能优化。用于开发 Godot 游戏、实现游戏系统或学习脚本开发方法。 | [原仓库](https://github.com/wshobson/agents) |
| [纵向追踪与横向研究](../library/horizontal-vertical-research/SKILL.md) | horizontal-vertical-research | 当研究问题需要连接历史演化与同类差异时，做有来源的纵向追踪和横向比较；不用于快速概览、查当前事实、按已给规格列表或核查单项既有论断，不因“比较”一词触发。 | 工作区维护 |
| [研究的人读表达](../library/human-research-expression/SKILL.md) | human-research-expression | 为已有研究案例或复杂报告判断哪些内容需要图解、动态或交互，并按理解任务组织人读表达；适用于规划、制作和审查报告表达，不替代原研究取证，也不用于仅修页面样式。 | 工作区维护 |
| [中文自然表达](../library/humanizer-zh/SKILL.md) | humanizer-zh | 编辑中文文章、评论和文档中的空话、重复及模板化表达，让文字更自然，同时保留事实、确定程度和作者声音。适用于润色已有文本，不用于判断作者身份或保证通过 AI 检测器。 | [原仓库](https://github.com/op7418/Humanizer-zh) |
| [交互设计](../library/interaction-design/SKILL.md) | interaction-design | 设计或修复网页、App 与游戏 UI 的控件选型、选择与输入、导航弹层、状态反馈、界面文案取舍、拖拽和交互动效；按需保持连续操作、取消恢复、输入替代与减少运动，不用于纯视觉风格、角色素材制作或玩法规则设计。 | 工作区维护 |
| [经历与能力的机会探索](../library/opportunity-flow/SKILL.md) | opportunity-flow | 当用户希望从已有经历或能力系统探索副业、服务产品或职业转型机会，并形成优先级与行动计划，或要运行经历到机会的七步提示词时使用；普通简历润色、单项薪酬查询和仅研究提示词本身不自动启动本流程。 | 工作区维护 |
| [像素素材制作](../library/pixel-asset-production/SKILL.md) | pixel-asset-production | 制作或扩展游戏像素角色、动作或物件时，按文字、参考图、分层素材或已有骨骼选路线并验证交付；不用于普通网页设计或单次图片缩放。 | 工作区维护 |
| [中文通俗表达](../library/plain-language-zh/SKILL.md) | plain-language-zh | 将专业或抽象内容改写为目标读者能理解的日常表达。用于明确要求少术语、接地气，或非专业读者难以理解文案时；保留必要术语及准确含义，普通润色沿humanizer-zh。 | 工作区维护 |
| [问题澄清](../library/problem-clarifier/SKILL.md) | problem-clarifier | 当目标冲突或问题含义不清、不同理解会改变下一必要动作时，将困惑澄清为可行动问题；不用于目标明确的修复、事实查询、普通缺参数或已知选项的取舍，也不因“帮我”措辞触发。 | 工作区维护 |
| [基于性质的测试](../library/property-based-testing/SKILL.md) | property-based-testing | 编写、审查和调试基于性质的测试：围绕整个输入范围验证规律，而不只列举手选样例。适用于编解码、解析器、规范化、校验、数值、排序、数据结构和智能合约不变量，以及检查测试性质、生成器和缩减反例。支持 Hypothesis、fast-check、proptest、jqwik、rapid、Echidna 和 Medusa；不替代二进制模糊测试、变异测试、静态分析、性能基准或界面端到端测试。 | [原仓库](https://github.com/trailofbits/skills) |
| [设计问题原型验证](../library/prototype/SKILL.md) | prototype | 用可丢弃的原型回答一个具体设计问题。适用于验证状态模型、操作逻辑是否合理，或探索界面应呈现怎样的形式。 | [原仓库](https://github.com/mattpocock/skills) |
| [范例反向拆解](../library/reference-deconstruction/SKILL.md) | reference-deconstruction | 当用户要从具体范例学会可迁移做法时，反向拆解成果、机制及适用条件；不用于单纯摘要、翻译、照图实施、事实验真或游戏体验问题诊断，材料是截图不构成触发理由。 | 工作区维护 |
| [研究材料搜集](../library/research-collection/SKILL.md) | research-collection | 为研究问题规划并执行多来源材料搜集，或围绕已有研究的关键缺口补证，控制重复、版本、读取范围和阶段投入；不用于普通单条事实查询、仅改写已给文本或自动订阅采集。 | 工作区维护 |
| [可撤回实验设计](../library/reversible-experiment-design/SKILL.md) | reversible-experiment-design | 当尚未决定的方向可通过有界现实反馈区分时，设计低成本、可撤回且有停止条件的最小实验；不用于已批准实施的常规测试、匿名候选评测或已有 GameAnalysisDecision 证据化问题的 ExperimentPlan 编译。 | 工作区维护 |
| [会话交接与续接](../library/session-handoff/SKILL.md) | session-handoff | 在换会话、上下文重置或长任务暂停时准备可恢复交接，或从指定交接入口续接已授权工作；复用项目记录，核对当前产物和负责人。普通进度询问不创建交接文件。 | [原仓库](https://github.com/wanshuiyin/HERO-Anti-OverDefense) |
| [来源保真](../library/source-fidelity/SKILL.md) | source-fidelity | 将原材料消化、改写为知识正文，或对照来源检查派生正文的保真度时，识别无源新增、数字条件失真、前提反例丢失和空壳案例；不用于普通润色、外部事实验真或只检查格式。 | 工作区维护 |
| [系统化调试](../library/systematic-debugging/SKILL.md) | systematic-debugging | 在原因不明、修复多次失败、问题间歇出现或跨组件时，区分假设、定位故障并验证修复。明显笔误等简单修正无需另开调试流程。 | [原仓库](https://github.com/obra/superpowers) |
| [任务工具化](../library/task-tooling/SKILL.md) | task-tooling | 当任务因反复人工转译、批量校对、领域编辑或重复操作而低效，且缺少合适入口时，判断是否值得选用、适配或制作小工具；按需完成可供人和智能体使用的操作与实际使用验证。一次明确修改或现有命令已足够时直接完成。 | 工作区维护 |
| [任务收尾](../library/workflow-closure/SKILL.md) | workflow-closure | 当用户要求收尾、提交、完成并提交或暂停交接，或已授权任务进入最终闭合阶段时，按工作区合同完成验证、交互学习归属判断、主干集成、父仓指针闭合、推送与按需清理，并判断 AgentWorkSpace 与个人网站影响；不用于普通进度询问、只读解释或中间实现，不替代项目验收或授予产品发布权限。 | 工作区维护 |
| [工作流审查与重设计](../library/workflow-redesign/SKILL.md) | workflow-redesign | 审查、复盘或重设计工作流，核对以往优化是否起效、当前产出与成本是否合理，并按证据保留或改进内容、职责和工具接线；也用于执行中重复、低增量或收尾迟滞，不用于普通进度汇报、文档润色或原因明确的局部修复。 | 工作区维护 |
| [面向智能体的文档写作](../library/writing-for-agents/SKILL.md) | writing-for-agents | 为智能体编写易于执行和按需读取的文档。用于创建或修改技能，以及维护 AGENTS.md、CLAUDE.md 等执行说明。 | [原仓库](https://github.com/mattpocock/skills) |
