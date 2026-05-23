<div align="center">

<img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License">
<img src="https://img.shields.io/badge/Skill%20Format-SKILL.md-10B981?style=flat-square" alt="SKILL.md">
<img src="https://img.shields.io/badge/Language-中文主讲-orange?style=flat-square" alt="Language">
<img src="https://img.shields.io/badge/Platform-Codex%20%7C%20Claude%20%7C%20OpenCode-7C3AED?style=flat-square" alt="Platforms">

</div>

<br>

---

# 🎓 Learn Anything Skill

> A general-purpose AI learning skill. **Mentor + Project Coach** mode.
> Doesn't just answer questions — **helps you truly learn.**

[中文说明](./README.md)

---

## ⚡ One-Line Install

Copy this sentence to your AI Agent (OpenCode, Claude Code, Codex):

```
Install learn-anything-skill by following the instructions at: https://raw.githubusercontent.com/read2017/learn-anything-with-AI/main/docs/guide/installation.md
```

The agent reads the guide, downloads files, configures everything. You just **restart**.

> 📖 Full guide: [docs/guide/installation.md](docs/guide/installation.md)

---

## 📖 What This Is

A portable `SKILL.md` workflow package built on two methods:

| Method | Description |
|--------|-------------|
| **Project-Driven Learning** | Every session produces a tangible output (demo, report, notes, script) |
| **Mastery Learning** | Mastery ≠ reading. Must explain, apply, transfer to pass |

**It can generate:**
- 📋 Study Plans  ·  📝 Notes  ·  🔄 Session Reviews
- 📦 Project Briefs  ·  ✅ Mastery Checklists  ·  🎯 Topic Explanations

---

## ✨ Key Features

### 🤖 Mentor Mode, Not a Q&A Bot

Auto-identifies task type:
```
New Topic → Roadmap → Project Coaching → Source Reading → Review → Mastery Check
```

### 🏗 Project-Driven (Not Just Code)

| Coding/Engineering | Non-Coding |
|-------------------|-----------|
| Minimal demo | Research report |
| Micro-project | Case analysis |
| Debugging task | Knowledge map |
| System brief | Teaching script |

### 📚 Auto-Sources Authority

```
Official Docs > Canonical Textbooks > Best Practices
```

Always distinguishes **factual basis** from **advisory judgment**.

### 🎯 Built-in Mastery Levels

```
Know → Use → Modify → Design → Transfer
```

Stops asking "Do you understand?" Starts checking "Can you do it?"

---

## 📂 Repository Structure

```
skills/learn-anything-skill/
├── SKILL.md              ← 🧠 Main skill file
├── agents/openai.yaml     ← OpenAI agent config
├── references/            ← 📖 Deep reference rules
│   ├── mastery-rubric.md
│   ├── project-patterns.md
│   ├── source-strategy.md
│   └── teaching-playbook.md
└── assets/                ← 📄 Output templates
    ├── learning-plan-template.md
    ├── study-notes-template.md
    ├── session-review-template.md
    ├── project-brief-template.md
    ├── mastery-check-template.md
    └── mistakes-log-template.md
```

---

## 🚀 Recommended Workflow

Create a dedicated directory per topic:

```bash
mkdir learn-ai && cd learn-ai
```

The skill auto-saves output to `study/` in your current directory. Reuses existing structures when found.

---

## 📦 Installation

### ⚡ One-Line Install (Recommended)

```
Install learn-anything-skill by following the instructions at: https://raw.githubusercontent.com/read2017/learn-anything-with-AI/main/docs/guide/installation.md
```

See the [installation guide](docs/guide/installation.md) for details.

---

### Install in Codex / OpenAI Skills

**Option A: local directory install**

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/learn-anything-skill ~/.codex/skills/
```

Restart Codex or refresh the skills list.

**Option B: upload via Skills UI**

Upload the entire `learn-anything-skill` folder, keeping `references/` and `assets/`.

---

### Install in Claude Code

**Option A: project skill**

```bash
mkdir -p .claude/skills
cp -R ./skills/learn-anything-skill ./.claude/skills/
```

Invoke with `/learn-anything-skill` or natural language.

**Option B: Claude Code plugin**

```text
my-plugin/
├── .claude-plugin/plugin.json
└── skills/learn-anything-skill/SKILL.md
```

```bash
claude --plugin-dir ./my-plugin
```

---

### Install in OpenCode

OpenCode now natively supports **skills** (`SKILL.md` format), compatible with Codex and Claude Code.

**Use the one-line install** above — your agent handles everything.

**Manual install:**

```bash
mkdir -p .opencode/skills
cp -R ./skills/learn-anything-skill .opencode/skills/
```

Restart OpenCode.

**Global install (all projects):**

```bash
mkdir -p ~/.config/opencode/skills
cp -R ./skills/learn-anything-skill ~/.config/opencode/skills/
```

---

## 📚 Usage

### 1. Explicit Invocation

```text
Use learn-anything-skill to teach me calculus and create a 4-week study plan
```

### 2. Natural-Language Triggering

- Help me learn calculus and create a four-week plan
- Guide me through The Wealth of Nations with study notes
- Improve my spoken English with project-style exercises
- Check my understanding of probability

### 3. With Your Own Materials

Hand it course slides, lecture notes, textbook chapters, papers, code repos — it reads closely, extracts structure, fills prerequisite gaps, creates exercises, and runs mastery checks.

---

## 💡 Use Cases

<details>
<summary><b>📋 Study Plan</b></summary>

```text
Use learn-anything-skill to help me learn linear algebra.
I only know high-school math, 6h/week.
Create a 4-week plan with outputs and acceptance criteria.
```

→ Gets: level assessment · capability breakdown · weekly plan · deliverables · risk notes

</details>

<details>
<summary><b>📖 Guided Reading</b></summary>

```text
Use learn-anything-skill to guide me through The Wealth of Nations Vol 1.
Help me build structure, take notes, prepare chapter review questions.
```

→ Gets: chapter structure · key concepts · common misunderstandings · review questions

</details>

<details>
<summary><b>🗣 Spoken English</b></summary>

```text
Use learn-anything-skill to improve my spoken English.
Goal: 3-minute self-introduction in 6 weeks. Project-driven training.
```

→ Gets: staged roadmap · weekly scripts · recording tasks · retest criteria

</details>

<details>
<summary><b>💻 SQL + Project</b></summary>

```text
Use learn-anything-skill to teach me SQL.
I know Python but not databases.
Give me a roadmap and a student-score analysis project brief.
```

→ Gets: prerequisite check · core concepts · graded exercises · project brief · checkpoints

</details>

<details>
<summary><b>✅ Mastery Check</b></summary>

```text
Use learn-anything-skill to assess my understanding of conditional probability.
Don't ask if I understand — give me restatement, variation, and transfer tasks.
```

→ Gets: level judgment · evidence · weak points · reinforcement · retest standard

</details>

---

## 🎨 Suitable Topics

This skill isn't just for programmers:

`Coding` · `Math` · `Stats` · `Economics` · `Finance` · `English` · `Japanese` · `History` · `Social Science` · `Writing` · `Speaking` · `AI/LLM`

---

## 🛠 Customization

Want your own version? Start here:

| File | Controls |
|------|----------|
| `SKILL.md` | Overall behavior, task tree, teaching flow |
| `references/source-strategy.md` | Source lookup priority |
| `references/project-patterns.md` | Project-driven formats |
| `references/mastery-rubric.md` | Mastery criteria |

---

## 🔗 Compatibility

| Platform | Skill Format | Install |
|----------|-------------|---------|
| **OpenAI / Codex / ChatGPT Skills** | ✅ Native | `~/.codex/skills/` or Skills UI |
| **Claude Code** | ✅ Supported | `.claude/skills/` or Plugin |
| **OpenCode** | ✅ Native | `.opencode/skills/` or one-line install |

> The core asset is the portable `SKILL.md + references + assets` workflow. Install entry points differ by platform, but the content itself is cross-platform.

---

## 📄 License

MIT · See [LICENSE](./LICENSE)
