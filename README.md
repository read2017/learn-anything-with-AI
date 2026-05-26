# Learn Anything Skill

![License](https://img.shields.io/badge/license-MIT-green.svg) ![Agent Skill](https://img.shields.io/badge/Agent%20Skill-learn--anything--skill-111827) ![Language](https://img.shields.io/badge/language-Chinese%20first-orange) ![Method](https://img.shields.io/badge/method-Project--Driven%20%2B%20Mastery%20Learning-blue) ![Open Source](https://img.shields.io/badge/open%20source-GitHub-black)

[English README](./README.en.md)

一个面向“学习任何知识”的通用 AI 学习 Skill，让AI成为你的《顶级私教》。  
它默认扮演 **导师 + 项目教练**：用中文主讲，温柔鼓励，专业幽默；不只解释概念，还会诊断你的起点、制定计划、组织项目化练习、检查掌握度，并在你没给资料时主动补官方文档与权威材料。

> 把 AI 从“会回答问题”推进成“能带你真的学会”的学习搭子。

## 图文和视频介绍

<table>
  <tr>
    <td align="center" width="50%">
      <strong><a href="http://xhslink.com/o/4DLignz1LpA">项目图文介绍</a></strong><br />
      <a href="http://xhslink.com/o/4DLignz1LpA">
        <img src="./docs/images/project-intro-cover.png" alt="learn-anything-skill 项目介绍" height="320" />
      </a>
    </td>
    <td align="center" width="50%">
      <strong><a href="http://xhslink.com/o/4DLignz1LpA">小白保姆级视频教程</a></strong><br />
      <a href="http://xhslink.com/o/4DLignz1LpA">
        <img src="./docs/images/video-tutorial-cover.png" alt="learn-anything-skill 视频教程封面" height="320" />
      </a>
    </td>
  </tr>
</table>

## 快速导航

[这是什么](#-这是什么) · [核心特性](#-核心特性) · [目录结构](#-目录结构) · [推荐学习目录工作流](#-推荐学习目录工作流) · [安装](#-安装) · [用法](#-用法) · [使用案例](#-使用案例) · [推荐提示词](#-推荐提示词) · [适用主题](#-适用主题) · [开发与定制](#-开发与定制) · [兼容性说明](#-兼容性说明)

## 一眼看懂

- `learn-anything-skill`：一个面向“学习任何知识”的导师型 Skill
- 默认角色：`导师 + 项目教练`
- 默认方法：`项目驱动学习 + Mastery Learning`
- 默认行为：自动补权威资料，并把学习计划、笔记、复盘沉淀到工作目录
- 适用平台：Codex / Claude Code / OpenCode / 其他兼容 Agent Skills 的工具

<details>
<summary>Expand English intro</summary>

A general-purpose AI learning skill for mastering almost any subject.  
It acts as a **mentor + project coach** by default: teaching primarily in Chinese, staying warm but rigorous, and focusing on plans, structured explanations, project-style practice, mastery checks, and authoritative sources when the user does not provide materials.

适合：

- 想系统学习一个新主题的人
- 想把“知道”推进到“会用、会改、会迁移”的人
- 想把学习过程产品化、项目化、可复盘的人
- 想把 Skill 开源给 Codex / Claude Code / OpenCode 用户复用的人

Good fit for:

- learners who want a structured path into a new topic
- people who want to move from "I know it" to "I can apply and transfer it"
- builders who prefer project-driven learning over passive explanation
- toolmakers who want a reusable open-source skill for Codex, Claude Code, and OpenCode users

</details>

## ✨ 这是什么

`learn-anything-skill` 是一个可移植的 `SKILL.md` 工作流包，核心目标不是“回答问题”，而是 **帮助用户真的学会**。

它默认结合两套方法：

- **项目驱动学习**：每轮学习尽量落到一个产出，而不只是停在概念解释
- **Mastery Learning**：不把“看懂”当完成，而把“能解释、能应用、能迁移”当掌握

这个 Skill 可以帮助用户生成：

- 学习计划
- 学习笔记
- 课后复盘
- 项目任务书
- 掌握度检查单
- 单次主题讲解与后续练习

## 🧠 核心特性

### 1. 默认是导师，而不是问答机器人

它会先判断当前任务属于哪类：

- 学新知识
- 制定学习路线
- 做项目陪练
- 精读资料
- 课后复盘
- 掌握度评估

如果目标不清晰，它会先补最关键的信息；如果目标已经清晰，它会直接进入教学。

### 2. 项目驱动，但不强迫所有主题都写代码

对于编程/工程主题，它会倾向于：

- 最小功能 demo
- 微项目
- 调试任务
- 小型系统任务书

对于非编程主题，它会自动转成产出型项目，比如：

- 研究短报告
- 讲解稿 / 演讲提纲
- 案例分析
- 知识地图
- 读书笔记
- 口语表达脚本

### 3. 用户没有给资料时，会主动补权威来源

默认资料优先级：

1. 官方文档、原始规范、第一手材料
2. 经典教材、标准著作、权威机构或课程
3. 高质量教程与最佳实践

回答时会尽量区分：

- **事实依据**：定义、原理、定理、规范、原文观点、史实
- **建议判断**：学习顺序、项目设计、练习安排、工程取舍

### 4. 内置“掌握度”视角

Skill 默认会把用户的掌握状态区分为：

- 知道
- 会用
- 会改
- 会设计
- 会迁移

它不会只问“懂了吗”，而是会通过复述、改错、变式、迁移和小产出判断你是不是真的掌握。

## 🗂️ 目录结构

```text
skills/
└── learn-anything-skill/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── mastery-rubric.md
    │   ├── project-patterns.md
    │   ├── source-strategy.md
    │   └── teaching-playbook.md
    └── assets/
        ├── learning-plan-template.md
        ├── mistakes-log-template.md
        ├── mastery-check-template.md
        ├── project-brief-template.md
        ├── session-review-template.md
        └── study-notes-template.md
```

## 📁 推荐学习目录工作流

推荐不要直接在杂乱的工作目录里学习，而是先单独新建一个学习目录，再在这个目录里调用 Skill。

例如你想系统学习 AI，可以先创建：

```bash
mkdir -p learn-ai
cd learn-ai
```

然后在这个目录里使用 `learn-anything-skill`。

这样做的好处是：

- 学习计划会自动保存为 Markdown 文件
- 学习笔记会持续追加和沉淀
- 课后复盘、掌握度检查、错题/卡点记录会留在同一个目录
- 一个主题的资料、练习、笔记和项目任务书不会和其他项目混在一起

默认情况下，Skill 会优先把学习产出写到当前工作目录下的 `study/` 子目录，例如：

```text
learn-ai/
└── study/
    ├── ai-learning-plan.md
    ├── ai-notes.md
    ├── ai-session-review.md
    ├── ai-mastery-check.md
    └── ai-mistakes-log.md
```

如果目录里已经有更合适的学习资料结构，Skill 也应优先复用已有目录，而不是重复新建散文件。

## 🚀 安装

### 推荐方式：用 Agent Skills CLI 安装

如果你使用的是支持 AgentSkill 的 agent（Claude Code / Codex / Cursor / OpenClaw / OpenCode 等），推荐直接用 `npx skills add` 安装：

```bash
npx skills add read2017/learn-anything-with-AI --skill learn-anything-skill
```

安装完成后，任何支持 AgentSkill 的 agent 都可以使用这套学习 Skill 来学习任何知识。它会作为 `learn-anything-skill` 被安装到对应 agent 可识别的 Skills 目录中。

如果你想全局安装，让多个项目都能复用，可以加 `-g`：

```bash
npx skills add -g read2017/learn-anything-with-AI --skill learn-anything-skill
```

<details open>
<summary><strong>展开查看 Codex / OpenAI Skills 手动安装方式</strong></summary>

### 手动安装到 Codex / OpenAI Skills

#### 方式 A：本地目录安装（适合 Codex 桌面端 / 本地工作流）

把本仓库里的 Skill 目录复制到本地 Skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/learn-anything-skill ~/.codex/skills/
```

复制完成后，重启 Codex 或刷新 Skills 列表。

如果你的环境支持自动发现，本 Skill 会以 `learn-anything-skill` 的名字出现在可用 Skills 中。

#### 方式 B：通过 Skills UI 上传 / 导入

OpenAI 的 Skills 采用可移植的开放标准，支持在不同产品间共享。  
如果你使用的 ChatGPT / Codex 版本带有 Skills 页面或导入入口，也可以直接通过 UI 上传此 Skill。

建议上传整个 `learn-anything-skill` 文件夹，保留 `references/` 与 `assets/`，不要只上传单个 `SKILL.md`。

</details>

<details>
<summary><strong>展开查看 Claude Code 安装方式</strong></summary>

## 安装到 Claude Code

Claude Code 当前最贴近的原生载体是 **Skills**。官方支持两种方式：

- 项目内独立配置：`.claude/skills/<name>/SKILL.md`
- 插件方式分发：插件根目录下的 `skills/<name>/SKILL.md`

### 方式 A：作为项目内 Skill 使用

把目录复制到你的项目中：

```bash
mkdir -p .claude/skills
cp -R ./skills/learn-anything-skill ./.claude/skills/
```

然后在 Claude Code 中：

- 直接输入 `/learn-anything-skill`
- 或在自然语言里显式说 `Use /learn-anything-skill ...`
- 或让 Claude 在相关任务里自动触发它

### 方式 B：作为 Claude Code Plugin 分发

如果你想把它发布成 Claude Code 插件，需要额外补一个插件清单：

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── learn-anything-skill/
        └── SKILL.md
```

开发阶段可本地测试：

```bash
claude --plugin-dir ./my-plugin
```

然后通过命名空间方式调用：

```text
/my-plugin:learn-anything-skill
```

如果你只是想快速使用，不想维护插件清单，优先用方式 A。

</details>

<details>
<summary><strong>展开查看 OpenCode 安装方式</strong></summary>

## 安装到 OpenCode

OpenCode 官方当前主打的是 **custom commands**，不是与 OpenAI / Claude 完全同构的 Skill 目录。  
因此最稳妥的做法是：**把本 Skill 的核心提示词适配成一个 OpenCode slash command**。

### 方式 A：项目级命令

创建目录：

```bash
mkdir -p .opencode/commands
```

创建文件 `.opencode/commands/learn-anything.md`：

```md
---
description: 中文导师式通用学习与项目陪练
---

请扮演“导师 + 项目教练”，用中文主讲、温柔鼓励、专业幽默的风格帮助我学习这个主题：$ARGUMENTS

要求：
- 先判断任务类型：学新知识、路线规划、项目陪练、资料精读、复盘纠偏、掌握度评估
- 如果目标不清晰，先补 1-3 个关键信息
- 按 Mastery Learning 推进，不把“看懂”视为掌握
- 尽量给出最小案例、项目化任务或产出型练习
- 如果我没有提供资料，主动查找官方文档、原始资料、经典教材、权威机构材料与最佳实践
- 在回答中区分“事实依据”和“建议判断”
- 结尾给出下一步学习动作
```

然后在 OpenCode 里输入：

```text
/learn-anything 微积分极限
```

### 方式 B：全局命令

如果你想在所有项目里复用，放到：

```text
~/.config/opencode/commands/learn-anything.md
```

### OpenCode 适配说明

OpenCode 的 command 文件是单文件 prompt 模板；它不会像原生 Skill 包那样自动附带 `references/` 和 `assets/` 目录。  
所以如果你要在 OpenCode 里完整复用本仓库的结构化资源，建议：

- 把 `references/` 里的规则手动合并到 command 模板
- 或把这个仓库一起放进工作区，让 agent 可以直接读取这些文件

</details>

## 🛠️ 用法

## 1. 显式调用

推荐先进入你为某个主题单独创建的学习目录里再调用，这样生成的学习计划、笔记和复盘会自动保存到该目录下。

适合你已经知道想让它做什么时：

```text
Use $learn-anything-skill to teach me calculus and create a 4-week study plan.
```

或直接中文：

```text
用 $learn-anything-skill 帮我学 SQL，并给我一个小项目任务书。
```

## 2. 自然语言触发

如果你的平台支持自动触发 Skill，可以直接说：

- 帮我学微积分，并给我四周计划
- 教我读《国富论》，顺手整理学习笔记
- 我要学英语口语，给我项目式练习和复盘
- 帮我学 SQL，并写一个小项目任务书
- 检查我对概率论的掌握度，指出薄弱点

## 3. 与你自己的资料一起用

这是最推荐的用法。你可以把这些材料直接交给它：

- 课程 PPT
- 老师讲义
- 教材章节
- 论文
- 博客文章
- 作业题
- 代码仓库
- 自己写的笔记

然后让它：

- 精读
- 提炼结构
- 转成讲义
- 补前置知识
- 出练习
- 做掌握度检查

## 📚 使用案例

## 案例 1：四周学习计划

```text
用 $learn-anything-skill 帮我学线性代数。
我现在只会高中数学，每周能学 6 小时。
请给我做一个 4 周学习计划，并且每周都要有小产出和验收标准。
```

你通常会得到：

- 当前起点评估
- 主线能力点拆解
- 4 周安排
- 每周练习与产出
- 风险提示

## 案例 2：读书陪练

```text
用 $learn-anything-skill 带我读《国富论》第一卷。
我不想只看总结，请帮我建立结构、做读书笔记，并安排每章后的复盘问题。
```

你通常会得到：

- 章节结构
- 关键概念和脉络
- 容易误解的地方
- 精读问题
- 复盘问题

## 案例 3：英语口语项目化练习

```text
用 $learn-anything-skill 帮我提升英语口语。
目标是 6 周后能做 3 分钟英文自我介绍和项目介绍。
请按项目驱动方式安排训练。
```

你通常会得到：

- 分阶段训练路线
- 每周脚本和练习主题
- 录音/表达产出任务
- 复盘和复测标准

## 案例 4：SQL + 小项目任务书

```text
用 $learn-anything-skill 教我 SQL。
我会一点 Python，但没系统学过数据库。
请给我一个学习路线，并设计一个学生成绩分析的小项目任务书。
```

你通常会得到：

- 最小前置知识诊断
- SQL 核心概念讲解
- 查询练习梯度
- 小项目任务书
- 掌握度检查点

## 案例 5：掌握度检查

```text
用 $learn-anything-skill 检查我对概率论里“条件概率”和“贝叶斯公式”的掌握度。
不要只问我懂不懂，请给我复述题、变式题和迁移题。
```

你通常会得到：

- 当前掌握等级判断
- 证据说明
- 薄弱点定位
- 补强任务
- 下一轮复测标准

## ✍️ 推荐提示词

如果你第一次用这个 Skill，可以直接复制这些提示：

### 生成学习计划

```text
用 $learn-anything-skill 帮我学习 [主题]。
我的基础是 [当前水平]，我每周能投入 [时间]。
请给我一个 [2/4/8] 周学习计划，每周都要有练习、产出和验收标准。
```

### 做单次讲解

```text
用 $learn-anything-skill 给我讲清楚 [主题]。
请按“核心概念 -> 最小示例/案例 -> 常见误区 -> 一个微产出任务 -> 掌握检查”的结构来讲。
```

### 做课后复盘

```text
用 $learn-anything-skill 帮我复盘今天学的 [主题]。
请帮我区分：我真正掌握了什么、我还模糊什么、下一步该补什么。
```

### 生成项目任务书

```text
用 $learn-anything-skill 帮我把 [主题] 变成一个项目任务书。
要求包括：背景、目标、交付物、约束、任务拆分、验收标准。
```

## 🎯 适用主题

这个 Skill 不是只给程序员用的。它适用于：

- 编程与软件工程
- 数学与统计
- 经济学与金融基础
- 英语和其他语言学习
- 历史、社会科学、人文阅读
- 写作、演讲、表达训练
- AI / LLM / 数据相关主题

## 🔧 开发与定制

如果你想改成自己的版本，最常见的修改点有：

- 改默认语气与输出语言
- 改项目风格：更偏考试、论文、实战或作品集
- 改资料策略：更强调官方文档或教材精读
- 改掌握度检查方式：更偏题目、口头复述、代码实现或论文解读

建议优先修改这些文件：

- `skills/learn-anything-skill/SKILL.md`
- `skills/learn-anything-skill/references/source-strategy.md`
- `skills/learn-anything-skill/references/project-patterns.md`
- `skills/learn-anything-skill/references/mastery-rubric.md`

## 🔌 兼容性说明

- **OpenAI / Codex / ChatGPT Skills**：这是最原生的目标形态
- **Claude Code**：可直接作为 Skill 使用；如果要发布给更多人，建议再包装成 plugin
- **OpenCode**：建议作为 command 适配，而不是假设它与本仓库的 Skill 目录完全同构

换句话说：这个仓库的核心资产是通用的 `SKILL.md + references + assets` 工作流；不同代理工具的安装入口不完全一样，但内容本身是可迁移的。

<details>
<summary><strong>展开查看参考资料</strong></summary>

## 参考资料

以下官方资料对本 README 的安装说明和兼容性表述有帮助：

- OpenAI Skills 说明：<https://openai.com/academy/skills/>
- ChatGPT Skills 帮助中心：<https://help.openai.com/en/articles/20001066>
- Codex 与 Skills 介绍：<https://openai.com/index/introducing-the-codex-app/>
- Claude Code Commands / Skills：<https://support.claude.com/en/articles/14553413-claude-code-cheatsheet>
- Claude Code Plugins：<https://code.claude.com/docs/en/plugins>
- OpenCode Commands：<https://opencode.ai/docs/commands>

</details>

## License

本仓库使用 [MIT License](./LICENSE)。
