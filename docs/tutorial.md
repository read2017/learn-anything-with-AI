# 使用教程

这个文档保留 `learn-anything-skill` 的完整使用说明。首页 README 只保留最短路径，这里放详细内容。

## 安装

### 推荐方式：用 Agent Skills CLI 安装

如果你使用的是支持 AgentSkill 的 agent（Claude Code / Codex / Cursor / OpenClaw / OpenCode 等），推荐直接用 `npx skills add` 安装：

```bash
npx skills add read2017/learn-anything-with-AI --skill learn-anything-skill
```

如果你想全局安装，让多个项目都能复用，可以加 `-g`：

```bash
npx skills add -g read2017/learn-anything-with-AI --skill learn-anything-skill
```

### 手动安装到 Codex / OpenAI Skills

#### 方式 A：本地目录安装

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/learn-anything-skill ~/.codex/skills/
```

#### 方式 B：通过 Skills UI 上传 / 导入

建议上传整个 `learn-anything-skill` 文件夹，保留 `references/` 与 `assets/`，不要只上传单个 `SKILL.md`。

### 安装到 Claude Code

#### 方式 A：作为项目内 Skill 使用

```bash
mkdir -p .claude/skills
cp -R ./skills/learn-anything-skill ./.claude/skills/
```

然后可以：

- 直接输入 `/learn-anything-skill`
- 或在自然语言里显式说 `Use /learn-anything-skill ...`

#### 方式 B：作为 Claude Code Plugin 分发

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── learn-anything-skill/
        └── SKILL.md
```

### 安装到 OpenCode

#### 方式 A：项目级命令

```bash
mkdir -p .opencode/commands
```

创建 `.opencode/commands/learn-anything.md`：

```md
---
description: 中文导师式通用学习与项目陪练
---

请扮演“导师 + 项目教练”，用中文主讲、温柔鼓励、专业幽默的风格帮助我学习这个主题：$ARGUMENTS
```

#### 方式 B：全局命令

放到：

```text
~/.config/opencode/commands/learn-anything.md
```

## 调用方式

### 1. 显式调用

```text
Use $learn-anything-skill to teach me calculus and create a 4-week study plan.
```

或直接中文：

```text
用 $learn-anything-skill 帮我学 SQL，并给我一个小项目任务书。
```

### 2. 自然语言触发

- 帮我学微积分，并给我四周计划
- 教我读《国富论》，顺手整理学习笔记
- 我要学英语口语，给我项目式练习和复盘
- 帮我学 SQL，并写一个小项目任务书
- 检查我对概率论的掌握度，指出薄弱点

### 3. 与你自己的资料一起用

你可以直接把这些材料交给它：

- 课程 PPT
- 老师讲义
- 教材章节
- 论文
- 博客文章
- 作业题
- 代码仓库
- 自己写的笔记

## 使用案例

### 案例 1：四周学习计划

```text
用 $learn-anything-skill 帮我学线性代数。
我现在只会高中数学，每周能学 6 小时。
请给我做一个 4 周学习计划，并且每周都要有小产出和验收标准。
```

### 案例 2：读书陪练

```text
用 $learn-anything-skill 带我读《国富论》第一卷。
我不想只看总结，请帮我建立结构、做读书笔记，并安排每章后的复盘问题。
```

### 案例 3：英语口语项目化练习

```text
用 $learn-anything-skill 帮我提升英语口语。
目标是 6 周后能做 3 分钟英文自我介绍和项目介绍。
请按项目驱动方式安排训练。
```

### 案例 4：SQL + 小项目任务书

```text
用 $learn-anything-skill 教我 SQL。
我会一点 Python，但没系统学过数据库。
请给我一个学习路线，并设计一个学生成绩分析的小项目任务书。
```

### 案例 5：掌握度检查

```text
用 $learn-anything-skill 检查我对概率论里“条件概率”和“贝叶斯公式”的掌握度。
不要只问我懂不懂，请给我复述题、变式题和迁移题。
```

## 推荐提示词

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
