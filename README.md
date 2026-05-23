<div align="center">

<img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License">
<img src="https://img.shields.io/badge/Skill%20Format-SKILL.md-10B981?style=flat-square" alt="SKILL.md">
<img src="https://img.shields.io/badge/Language-中文主讲-orange?style=flat-square" alt="Language">
<img src="https://img.shields.io/badge/Platform-Codex%20%7C%20Claude%20%7C%20OpenCode-7C3AED?style=flat-square" alt="Platforms">

</div>

<br>

---

# 🎓 Learn Anything Skill

> 一个 **中文导师 + 项目教练** 式的通用 AI 学习 Skill。  
> 不只回答问题，**帮你真的学会。**

> A general-purpose AI learning skill. **Mentor + Project Coach** mode.  
> Doesn't just answer questions — **helps you truly learn.**

[English README](./README.en.md)

---

## ⚡ 一句话安装

把下面这句话复制给你的 AI Agent（OpenCode / Claude Code / Codex 均可）：

```
安装 learn-anything-skill，按这里的指南操作：https://raw.githubusercontent.com/read2017/learn-anything-with-AI/main/docs/guide/installation.md
```

Agent 会自动读安装指南、下载 skill 文件、完成配置。你只需要**重启 Agent**。

> 📖 详细安装说明：[docs/guide/installation.md](docs/guide/installation.md)

---

## 📖 这是什么

`learn-anything-skill` 是一个可移植的 `SKILL.md` 工作流包，核心目标不是「回答问题」，而是 **帮助用户真的学会**。

它默认结合两套方法：

| 方法 | 说明 |
|------|------|
| **项目驱动学习** | 每轮学习落到一个产出（代码 demo、报告、笔记、演讲稿等），不空谈概念 |
| **Mastery Learning** | 掌握 ≠ 看懂。必须能解释、能应用、能迁移才算过 |

**它能帮你生成：**
- 📋 学习计划  ·  📝 学习笔记  ·  🔄 课后复盘
- 📦 项目任务书  ·  ✅ 掌握度检查单  ·  🎯 单次主题讲解

---

## ✨ 核心特性

### 🤖 导师模式，不是问答机器人

自动判断任务类型：
```
学新知识 → 路线规划 → 项目陪练 → 资料精读 → 课后复盘 → 掌握度评估
```

目标不清晰？先补关键信息。目标清晰？直接开讲。

### 🏗 项目驱动（不限编程）

| 编程/工程主题 | 非编程主题 |
|-------------|-----------|
| 最小功能 demo | 研究短报告 |
| 微项目 | 案例分析 |
| 调试任务 | 知识地图 |
| 系统任务书 | 教学讲义 |

### 📚 自动补权威来源

```
官方文档 > 经典教材 > 最佳实践
```

回答严格区分 **事实依据** 与 **建议判断**。

### 🎯 内置掌握度分级

```
知道 → 会用 → 会改 → 会设计 → 会迁移
```

不问「懂了没」，只验证「能不能做」。

---

## 📂 目录结构

```
skills/learn-anything-skill/
├── SKILL.md              ← 🧠 Skill 主文件
├── agents/openai.yaml     ← OpenAI 代理配置
├── references/            ← 📖 深度参考规则
│   ├── mastery-rubric.md      掌握度分级细则
│   ├── project-patterns.md    项目化模式
│   ├── source-strategy.md     资料策略
│   └── teaching-playbook.md   教学操作手册
└── assets/                ← 📄 输出模板
    ├── learning-plan-template.md
    ├── study-notes-template.md
    ├── session-review-template.md
    ├── project-brief-template.md
    ├── mastery-check-template.md
    └── mistakes-log-template.md
```

---

## 🚀 推荐学习目录工作流

建议为每个学习主题单独建目录，再在这个目录里调用 Skill：

```bash
mkdir learn-ai && cd learn-ai
```

Skill 会自动把学习产出写入当前目录的 `study/` 子文件夹，持续积累。已有学习资料目录时，优先复用现有结构。

---

## 📦 安装

### ⚡ 一句话安装（推荐）

```
安装 learn-anything-skill，按这里的指南操作：https://raw.githubusercontent.com/read2017/learn-anything-with-AI/main/docs/guide/installation.md
```

详见 [安装指南](docs/guide/installation.md)。

---

### 安装到 Codex / OpenAI Skills

**方式 A：本地目录安装**

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/learn-anything-skill ~/.codex/skills/
```

重启 Codex 或刷新 Skills 列表。

**方式 B：通过 Skills UI 上传 / 导入**

上传整个 `learn-anything-skill` 文件夹，保留 `references/` 与 `assets/`。

---

### 安装到 Claude Code

**方式 A：作为项目内 Skill 使用**

```bash
mkdir -p .claude/skills
cp -R ./skills/learn-anything-skill ./.claude/skills/
```

然后输入 `/learn-anything-skill` 或自然语言触发。

**方式 B：作为 Claude Code Plugin 分发**

```text
my-plugin/
├── .claude-plugin/plugin.json
└── skills/learn-anything-skill/SKILL.md
```

```bash
claude --plugin-dir ./my-plugin
```

---

### 安装到 OpenCode

OpenCode 现已原生支持 **skills**（`SKILL.md` 格式），与 Codex / Claude Code 兼容。

**使用一句话安装**：发送安装提示词给 Agent，自动下载配置。

**手动安装：**

```bash
mkdir -p .opencode/skills
cp -R ./skills/learn-anything-skill .opencode/skills/
```

重启 OpenCode 后生效。

**全局安装（所有项目可用）：**

```bash
mkdir -p ~/.config/opencode/skills
cp -R ./skills/learn-anything-skill ~/.config/opencode/skills/
```

---

## 📚 使用方式

### 1. 显式调用

```text
用 learn-anything-skill 帮我学 SQL，并给我一个小项目任务书
```

```text
Use learn-anything-skill to teach me calculus and create a 4-week study plan
```

### 2. 自然语言触发

- 帮我学微积分，并给我四周计划
- 教我读《国富论》，顺手整理学习笔记
- 我要学英语口语，给我项目式练习和复盘
- 检查我对概率论的掌握度，指出薄弱点

### 3. 与你自己的资料一起用

把课程 PPT、讲义、教材、论文、代码仓库交给它，让它精读、提炼结构、出练习、做掌握度检查。

---

## 💡 使用案例

<details>
<summary><b>📋 四周学习计划</b></summary>

```text
用 learn-anything-skill 帮我学线性代数。
我现在只会高中数学，每周能学 6 小时。
给我做一个 4 周学习计划，每周都要有产出和验收标准。
```

→ 得到：起点评估 · 能力拆解 · 周计划 · 验收标准 · 风险提示

</details>

<details>
<summary><b>📖 读书陪练</b></summary>

```text
用 learn-anything-skill 带我读《国富论》第一卷。
帮我建立结构、做读书笔记，安排每章后的复盘问题。
```

→ 得到：章节结构 · 关键概念 · 易误解点 · 精读问题 · 复盘问题

</details>

<details>
<summary><b>🗣 英语口语训练</b></summary>

```text
用 learn-anything-skill 帮我提升英语口语。
目标是 6 周后能做 3 分钟英文自我介绍。
请按项目驱动方式安排训练。
```

→ 得到：分阶段路线 · 每周脚本 · 录音任务 · 复测标准

</details>

<details>
<summary><b>💻 SQL + 小项目任务书</b></summary>

```text
用 learn-anything-skill 教我 SQL。
我会一点 Python，但没系统学过数据库。
给我一个学习路线，设计一个学生成绩分析的小项目任务书。
```

→ 得到：前置诊断 · 核心概念 · 梯度练习 · 项目任务书 · 掌握检查点

</details>

<details>
<summary><b>✅ 掌握度检查</b></summary>

```text
用 learn-anything-skill 检查我对条件概率和贝叶斯公式的掌握度。
不要只问我懂不懂，给我复述题、变式题和迁移题。
```

→ 得到：等级判定 · 证据 · 薄弱点 · 补强任务 · 复测标准

</details>

---

## 🎨 适用主题

这个 Skill 不只是给程序员用的：

`编程` · `数学` · `统计` · `经济学` · `金融` · `英语` · `日语` · `历史` · `社会科学` · `写作` · `演讲` · `AI/LLM`

---

## 🛠 开发与定制

想改成自己的版本？优先修改这些文件：

| 文件 | 控制什么 |
|------|---------|
| `SKILL.md` | 整体行为、任务决策树、教学流程 |
| `references/source-strategy.md` | 资料查找优先级 |
| `references/project-patterns.md` | 项目化方式 |
| `references/mastery-rubric.md` | 掌握度判定标准 |

---

## 🔗 兼容性说明

| 平台 | Skill 格式 | 安装方式 |
|------|-----------|---------|
| **OpenAI / Codex / ChatGPT Skills** | ✅ 原生 | `~/.codex/skills/` 或 Skills UI |
| **Claude Code** | ✅ 支持 | `.claude/skills/` 或 Plugin |
| **OpenCode** | ✅ 原生 | `.opencode/skills/` 或一句话安装 |

> 核心资产是通用的 `SKILL.md + references + assets` 工作流。不同平台的安装入口略有不同，但内容本身可跨平台迁移。

---

## 📄 License

MIT · 详见 [LICENSE](./LICENSE)
