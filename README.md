<div align="center">

# Learn Anything Skill

<p align="center">
  <img src="assets/hero.gif" alt="learn-anything-skill：从诊断起点到掌握度检查的教学闭环" width="100%"/>
</p>

> *让 AI 从「会回答问题」，变成「能带你真的学会」*

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-3fb950)](https://agentskills.io)
[![Runtime](https://img.shields.io/badge/Runtime-Codex%20%C2%B7%20Claude%20Code%20%C2%B7%20OpenCode%20%C2%B7%20Cursor-blueviolet)](#兼容性说明)
[![Method](https://img.shields.io/badge/Method-Project--Driven%20%2B%20Mastery%20Learning-blue)](#简介)
[![Stars](https://img.shields.io/github/stars/read2017/learn-anything-with-AI?style=social)](https://github.com/read2017/learn-anything-with-AI/stargazers)

<br>

**一个可移植的 `SKILL.md` 工作流包。默认扮演「导师 + 项目教练」：先诊断起点，再给学习路线、组织项目化练习、检查掌握度，并把学习产出落盘成 Markdown 文件。**

<sub>中文主讲 · 温柔鼓励 · 优先官方文档与权威材料 · 一个 SKILL.md 走遍 Codex / Claude Code / OpenCode</sub>

<sub>⭐ Star 收藏 · 👀 Watch 订阅更新（会持续迭代）</sub>

<br>

[图文 / 视频介绍](#图文和视频介绍) · [它会什么](#简介) · [学习目录工作流](#推荐学习目录工作流) · [快速开始](#快速开始) · [详细教程](#详细教程) · [适用主题](#适用主题) · [English README](./README.en.md)

<br>

</div>

---

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

## 简介

`learn-anything-skill` 是一个可移植的 `SKILL.md` 工作流包，核心目标不是“回答问题”，而是 **帮助用户真的学会**。

- 默认角色：`导师 + 项目教练`
- 默认方法：`项目驱动学习 + Mastery Learning`
- 默认产出：学习计划、学习笔记、课后复盘、项目任务书、掌握度检查、错题/卡点记录
- 默认行为：把关键学习产出写入当前工作目录下的 Markdown 文件，而不只停留在聊天记录里
- 默认来源策略：优先官方文档、原始资料、经典教材、权威机构材料，并区分事实依据与建议判断
- 默认项目化方式：
  - 编程主题：最小 demo、微项目、调试任务、小型任务书
  - 非编程主题：研究短报告、演讲提纲、案例分析、知识地图、读书笔记、复盘文档

适合：

- 想系统学习一个新主题的人
- 想把“知道”推进到“会用、会改、会迁移”的人
- 想把学习过程产品化、项目化、可复盘的人
- 想把 Skill 开源给 Codex / Claude Code / OpenCode 用户复用的人

## 推荐学习目录工作流

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

## 快速开始

### 1. 安装 Skill

推荐用 Agent Skills CLI：

```bash
npx skills add read2017/learn-anything-with-AI --skill learn-anything-skill
```

如果想全局安装：

```bash
npx skills add -g read2017/learn-anything-with-AI --skill learn-anything-skill
```

### 2. 创建学习目录

```bash
mkdir -p learn-ai
cd learn-ai
```

### 3. 开始学习

```text
用 $learn-anything-skill 帮我学习 SQL。
我会一点 Python，但没系统学过数据库。
请给我一个 4 周学习计划，并设计一个小项目任务书。
```

## 详细教程

首页只保留最短路径。更完整的安装、平台适配、调用方式、案例和提示词请看独立文档：

- 中文详细教程：[docs/tutorial.md](./docs/tutorial.md)
- English tutorial: [docs/tutorial.en.md](./docs/tutorial.en.md)

如果你是第一次用，建议顺序是：

1. 先看上面的图文介绍或视频教程
2. 按“快速开始”完成安装与目录准备
3. 再看详细教程，按自己的主题开始长期学习

## 目录结构

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

## 适用主题

这个 Skill 不是只给程序员用的。它适用于：

- 编程与软件工程
- 数学与统计
- 经济学与金融基础
- 英语和其他语言学习
- 历史、社会科学、人文阅读
- 写作、演讲、表达训练
- AI / LLM / 数据相关主题

## 开发与定制

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

## 兼容性说明

- **OpenAI / Codex / ChatGPT Skills**：这是最原生的目标形态
- **Claude Code**：可直接作为 Skill 使用；如果要发布给更多人，建议再包装成 plugin
- **OpenCode**：建议作为 command 适配，而不是假设它与本仓库的 Skill 目录完全同构
- **其他兼容 Agent Skills 的工具**：推荐优先使用 `npx skills add`

换句话说：这个仓库的核心资产是通用的 `SKILL.md + references + assets` 工作流；不同代理工具的安装入口不完全一样，但内容本身是可迁移的。

<details>
<summary><strong>展开查看参考资料</strong></summary>

以下官方资料对本仓库的安装说明和兼容性表述有帮助：

- OpenAI Skills 说明：<https://openai.com/academy/skills/>
- ChatGPT Skills 帮助中心：<https://help.openai.com/en/articles/20001066>
- Codex 与 Skills 介绍：<https://openai.com/index/introducing-the-codex-app/>
- Claude Code Commands / Skills：<https://support.claude.com/en/articles/14553413-claude-code-cheatsheet>
- Claude Code Plugins：<https://code.claude.com/docs/en/plugins>
- OpenCode Commands：<https://opencode.ai/docs/commands>

</details>

## 支持这个项目

如果这个 skill 帮你把一件事真的学会了：

- **⭐ Star** —— 让更多人看到它
- **👀 Watch** —— 订阅更新，我发新版本时你会收到通知
- **Fork** —— 改成你自己的版本（换语气、换项目风格、换资料策略都行，见[开发与定制](#开发与定制)）

有问题、想要新功能，或者想提名一个新的项目范式，欢迎开 [Issue](https://github.com/read2017/learn-anything-with-AI/issues)。

## License

本仓库使用 [MIT License](./LICENSE)。
