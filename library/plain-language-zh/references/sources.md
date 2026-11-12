# 来源与边界

2026年11月10日按公开源核对以下三个技能，随后以中文重新组织本技能。它们是方法参考，运行时无需联网，也没有安装这些仓库的脚本。下文保留固定来源提交和正文 SHA256，供接收方按需核对。

## shuorenhua

- 来源为[MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua/blob/9b91ed9464b944258c5031993c5e7d5d4e9637a8/skills/shuorenhua/SKILL.md)。固定提交为`9b91ed9464b944258c5031993c5e7d5d4e9637a8`，正文SHA256为`0cbdd6011e0b1db1aa4172c996a44d5e36f8de012d663de2302a9ba426b9b5cb`。
- 已读主文件，以及同仓editing-guide、examples两份参考。重点是去套话时保信息、限定改写范围、未知主体不补写、目标与结果分开。主旨与现有humanizer-zh重合度高。
- 本地采用其对“重复”的细分，将数据结果、意义评价和能力判断分别核对，补入humanizer主编辑步骤。其余已被现有保真规则覆盖的要求不再重复维护。

## plain-language的两种实现

- [arjunprabhulal/agent-skills](https://github.com/arjunprabhulal/agent-skills/blob/42dd24080fce6d731d00e2a1134f398c3da4171b/skills/docs/plain-language/SKILL.md)，提交`42dd24080fce6d731d00e2a1134f398c3da4171b`，正文SHA256为`5e146a79331ef0bab7a5d41e3735327d77e41fad51ba1cd2cb9eb0db578ee9e8`。采用读者用途、术语分别处理、名词展开成动作、保留精确条件等思路；不采用每条抽象论断都必须追加例子的固定要求。
- [davidamitchell/Skills](https://github.com/davidamitchell/Skills/blob/17196c19a89eacdf5c9f41d445ca4cf8379a2c6a/plain-language/SKILL.md)，提交`17196c19a89eacdf5c9f41d445ca4cf8379a2c6a`，正文SHA256为`a2da54619ac9a1b42d716e5e281fe3633ad9ea77bff4fea066df706e1fc85f8b`。采用术语首次解释及完整性回读；不采用固定句长、默认提问或无法简化时的固定标签。

公开技能所述效果与评测保持原作者归属，本轮没有复现其评测。此处是来源和本地采用说明，未将源文件整份复制成第二个编辑主入口。

## 本地增量

用户反馈指出，少套话之后仍可能满是专业名词、抽象判断和工作汇报式表达。本技能补入生活场景与已知动作、通用建议和具体判断分开、场景不得扩写为真实经历，以及一份连贯成稿等要求。方法适用于一般文案，案例身份、预测题材和私人资料不进入技能正文。

humanizer-zh负责自然表达，plain-language-zh负责减少理解门槛，dual-layer-explainer负责深入机制解释，anti-defensive-writing处理重复防御及薄弱主线。几种方法可在同一轮编辑中组合，按实际缺口选择。
