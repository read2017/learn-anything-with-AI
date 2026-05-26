# Learn Anything Skill

![License](https://img.shields.io/badge/license-MIT-green.svg) ![Agent Skill](https://img.shields.io/badge/Agent%20Skill-learn--anything--skill-111827) ![Language](https://img.shields.io/badge/language-Chinese%20first-orange) ![Method](https://img.shields.io/badge/method-Project--Driven%20%2B%20Mastery%20Learning-blue) ![Open Source](https://img.shields.io/badge/open%20source-GitHub-black)

[中文说明](./README.md)

A general-purpose AI learning skill for mastering almost any subject.  
It acts as a **mentor + project coach** by default: teaching primarily in Chinese, staying warm but rigorous, and focusing on plans, structured explanations, project-style practice, mastery checks, and authoritative sources when the user does not provide materials.

> Turn AI from a question-answering tool into a study coach that actually helps you learn.

## Quick Navigation

[What This Is](#what-this-is) · [Core Features](#core-features) · [Repository Structure](#repository-structure) · [Recommended Learning Directory Workflow](#recommended-learning-directory-workflow) · [Installation](#installation) · [Usage](#usage) · [Use Cases](#use-cases) · [Recommended Prompts](#recommended-prompts) · [Suitable Topics](#suitable-topics) · [Customization](#customization) · [Compatibility Notes](#compatibility-notes)

## At a Glance

- `learn-anything-skill`: a mentor-style skill for learning almost any subject
- default role: `mentor + project coach`
- default method: `Project-Driven Learning + Mastery Learning`
- default behavior: fills in authoritative sources and saves learning outputs into the working directory
- target tools: Codex / Claude Code / OpenCode / other Agent Skills-compatible tools

## Preview

<table>
  <tr>
    <td align="center" width="50%">
      <strong><a href="http://xhslink.com/o/4DLignz1LpA">Project intro post</a></strong><br />
      <a href="http://xhslink.com/o/4DLignz1LpA">
        <img src="./docs/images/project-intro-cover.png" alt="learn-anything-skill project intro" height="320" />
      </a>
    </td>
    <td align="center" width="50%">
      <strong><a href="http://xhslink.com/o/4DLignz1LpA">Beginner video tutorial</a></strong><br />
      <a href="http://xhslink.com/o/4DLignz1LpA">
        <img src="./docs/images/video-tutorial-cover.png" alt="learn-anything-skill video tutorial cover" height="320" />
      </a>
    </td>
  </tr>
</table>

Good fit for:

- learners who want a structured path into a new topic
- people who want to move from "I know it" to "I can apply and transfer it"
- builders who prefer project-driven learning over passive explanation
- toolmakers who want a reusable open-source skill for Codex, Claude Code, and OpenCode users

<a id="what-this-is"></a>
## ✨ What This Is

`learn-anything-skill` is a portable `SKILL.md` workflow package whose goal is not just to answer questions, but to **help users actually learn**.

It combines two default methods:

- **Project-driven learning**: turn each study cycle into an output, not just a conceptual explanation
- **Mastery Learning**: do not stop at "I get it"; push toward "I can explain, apply, adapt, and transfer it"

This skill can help generate:

- study plans
- study notes
- session reviews
- project briefs
- mastery checklists
- one-off topic explanations with follow-up practice

<a id="core-features"></a>
## 🧠 Core Features

### 1. It behaves like a mentor, not a generic Q&A bot

It first identifies the task type:

- learning a new topic
- building a study roadmap
- project coaching
- close reading of source material
- post-study review
- mastery evaluation

If the goal is unclear, it asks for the minimum missing context. If the goal is already clear, it moves directly into teaching.

### 2. It is project-driven without forcing everything into code

For programming and engineering topics, it tends to assign:

- minimum viable demos
- micro-projects
- debugging exercises
- small system briefs

For non-programming topics, it converts learning into output-based projects such as:

- short research reports
- teaching scripts or presentation outlines
- case analyses
- knowledge maps
- reading notes
- speaking practice scripts

### 3. It fills in authoritative sources when the user does not provide material

Default source priority:

1. Official documentation, primary sources, original standards
2. Canonical textbooks, classic works, authoritative institutions or courses
3. High-quality tutorials and best practices

It tries to distinguish between:

- **Factual basis**: definitions, principles, theorems, standards, source claims, historical facts
- **Judgment and advice**: study order, project design, exercise sequencing, engineering tradeoffs

### 4. It uses a built-in mastery lens

The skill models user progress across levels such as:

- know it
- use it
- modify it
- design with it
- transfer it

It does not stop at "Do you understand?" It checks mastery through explanation, correction, variation, transfer, and concrete outputs.

<a id="repository-structure"></a>
## 🗂️ Repository Structure

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

<a id="recommended-learning-directory-workflow"></a>
## 📁 Recommended Learning Directory Workflow

Do not study inside a cluttered general workspace if you can avoid it.  
Create a dedicated learning directory first, then invoke the skill from inside that directory.

For example, if you want to study AI in a structured way:

```bash
mkdir -p learn-ai
cd learn-ai
```

Then use `learn-anything-skill` inside that directory.

Why this is recommended:

- study plans can be saved automatically as Markdown files
- study notes can accumulate over time instead of disappearing into chat history
- session reviews, mastery checks, and mistake logs stay in one place
- materials, exercises, notes, and project briefs for one topic do not get mixed into unrelated projects

By default, the skill prefers writing learning outputs into a `study/` subdirectory under the current working directory, for example:

```text
learn-ai/
└── study/
    ├── ai-learning-plan.md
    ├── ai-notes.md
    ├── ai-session-review.md
    ├── ai-mastery-check.md
    └── ai-mistakes-log.md
```

If the directory already has a better learning-material structure, the skill should reuse that existing structure instead of creating scattered duplicate files.

<a id="installation"></a>
## 🚀 Installation

### Recommended: install with the Agent Skills CLI

If you use an agent that supports AgentSkill (Claude Code / Codex / Cursor / OpenClaw / OpenCode, etc.), install it directly with `npx skills add`:

```bash
npx skills add read2017/learn-anything-with-AI --skill learn-anything-skill
```

After installation, any AgentSkill-compatible agent can use this learning skill to study almost any subject. It will be installed as `learn-anything-skill` into the skills directory recognized by the target agent.

To install it globally for reuse across projects, add `-g`:

```bash
npx skills add -g read2017/learn-anything-with-AI --skill learn-anything-skill
```

<details open>
<summary><strong>Expand Codex / OpenAI Skills manual installation</strong></summary>

### Manual install in Codex / OpenAI Skills

#### Option A: local directory install

Copy the skill folder into your local skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/learn-anything-skill ~/.codex/skills/
```

Then restart Codex or refresh the skills list.

If your environment supports automatic discovery, the skill should appear as `learn-anything-skill`.

#### Option B: upload or import through a Skills UI

OpenAI Skills use a portable format that can be shared across compatible products.  
If your ChatGPT or Codex build exposes a Skills page or an import flow, you can also upload the entire `learn-anything-skill` folder there.

Upload the whole folder, not just `SKILL.md`, so `references/` and `assets/` remain available.

</details>

<details>
<summary><strong>Expand Claude Code installation</strong></summary>

## Install in Claude Code

Claude Code currently maps most closely to **Skills**. Two practical options:

- project-local skill: `.claude/skills/<name>/SKILL.md`
- plugin distribution: `skills/<name>/SKILL.md` inside a plugin

### Option A: use it as a project skill

Copy it into your project:

```bash
mkdir -p .claude/skills
cp -R ./skills/learn-anything-skill ./.claude/skills/
```

Then in Claude Code you can:

- invoke `/learn-anything-skill`
- explicitly say `Use /learn-anything-skill ...`
- let Claude trigger it automatically on relevant tasks

### Option B: package it as a Claude Code plugin

If you want to publish it more formally, wrap it with plugin metadata:

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── learn-anything-skill/
        └── SKILL.md
```

For local testing:

```bash
claude --plugin-dir ./my-plugin
```

Then invoke it with:

```text
/my-plugin:learn-anything-skill
```

If you just want to use it quickly, prefer Option A.

</details>

<details>
<summary><strong>Expand OpenCode installation</strong></summary>

## Install in OpenCode

OpenCode currently emphasizes **custom commands**, not the same native skill folder format used by OpenAI or Claude.  
The safest approach is to adapt this skill into an OpenCode slash command.

### Option A: project-level command

Create the directory:

```bash
mkdir -p .opencode/commands
```

Create `.opencode/commands/learn-anything.md`:

```md
---
description: Chinese mentor-style learning and project coaching
---

Act as a mentor + project coach and help me learn this topic in Chinese: $ARGUMENTS

Requirements:
- identify the task type first: new topic, roadmap, project coaching, source reading, review, mastery evaluation
- if the goal is unclear, ask for 1-3 critical pieces of context
- use Mastery Learning rather than stopping at surface understanding
- provide the smallest useful example, exercise, or output-based project
- if I do not provide material, proactively look for official docs, primary sources, canonical texts, authoritative institutions, and best practices
- distinguish between factual basis and advisory judgment
- end with the next study action
```

Then run:

```text
/learn-anything calculus limits
```

### Option B: global command

If you want it available across projects, place it here:

```text
~/.config/opencode/commands/learn-anything.md
```

### OpenCode adaptation note

OpenCode command files are single-file prompt templates. They do not automatically carry the full `references/` and `assets/` folder structure.

If you want fuller reuse inside OpenCode:

- merge key rules from `references/` into the command template
- or keep this repository inside the workspace so the agent can read those files directly

</details>

<a id="usage"></a>
## 🛠️ Usage

## 1. Explicit invocation

It is recommended to enter a topic-specific learning directory first so generated plans, notes, and reviews can be saved into that workspace automatically.

Use this when you already know what you want it to do:

```text
Use $learn-anything-skill to teach me calculus and create a 4-week study plan.
```

Or in Chinese:

```text
用 $learn-anything-skill 帮我学 SQL，并给我一个小项目任务书。
```

## 2. Natural-language triggering

If your platform supports automatic skill triggering, prompts like these should work:

- Help me learn calculus and create a four-week plan
- Teach me how to read *The Wealth of Nations* and organize study notes
- I want to improve spoken English with project-style exercises and reviews
- Help me learn SQL and design a small project brief
- Check my understanding of probability and point out weak spots

## 3. Use it with your own materials

This is the recommended mode. You can hand it:

- course slides
- lecture notes
- textbook chapters
- papers
- blog posts
- homework sets
- code repositories
- your own notes

Then ask it to:

- read closely
- extract structure
- turn material into teaching notes
- fill prerequisite gaps
- create exercises
- run mastery checks

<a id="use-cases"></a>
## 📚 Use Cases

## Case 1: a four-week study plan

```text
Use $learn-anything-skill to help me learn linear algebra.
I only know high-school math and I can study 6 hours per week.
Please create a 4-week plan with weekly outputs and acceptance criteria.
```

Typical output:

- starting-level assessment
- capability breakdown
- four-week roadmap
- weekly exercises and deliverables
- risk reminders

## Case 2: guided reading

```text
Use $learn-anything-skill to guide me through Volume 1 of The Wealth of Nations.
I do not want a summary only. Help me build structure, make reading notes, and prepare review questions after each chapter.
```

Typical output:

- chapter structure
- key concepts and arguments
- common misunderstandings
- close-reading questions
- review questions

## Case 3: project-based spoken English training

```text
Use $learn-anything-skill to improve my spoken English.
My goal is to deliver a 3-minute self-introduction and project introduction in 6 weeks.
Please design the training in a project-driven way.
```

Typical output:

- staged training roadmap
- weekly speaking themes and scripts
- recording and output tasks
- review and retest criteria

## Case 4: SQL plus a small project brief

```text
Use $learn-anything-skill to teach me SQL.
I know some Python but have never studied databases systematically.
Please give me a roadmap and design a small student-score analysis project brief.
```

Typical output:

- minimum prerequisite diagnosis
- core SQL explanations
- graduated query practice
- small project brief
- mastery checkpoints

## Case 5: mastery checking

```text
Use $learn-anything-skill to assess my understanding of conditional probability and Bayes' rule.
Do not just ask whether I understand. Give me restatement tasks, variation tasks, and transfer tasks.
```

Typical output:

- current mastery-level judgment
- evidence for that judgment
- weak-point diagnosis
- reinforcement tasks
- retest criteria

<a id="recommended-prompts"></a>
## ✍️ Recommended Prompts

If this is your first time using the skill, start with one of these:

### Generate a study plan

```text
Use $learn-anything-skill to help me learn [topic].
My current level is [current level], and I can spend [time] each week.
Please create a [2/4/8]-week plan with exercises, outputs, and acceptance criteria for each week.
```

### Request a one-off explanation

```text
Use $learn-anything-skill to teach me [topic].
Please structure the answer as: core concept -> smallest useful example or case -> common mistakes -> one micro-output task -> mastery check.
```

### Run a post-study review

```text
Use $learn-anything-skill to review what I learned today about [topic].
Help me separate what I truly understand, what is still fuzzy, and what I should study next.
```

### Generate a project brief

```text
Use $learn-anything-skill to turn [topic] into a project brief.
Include background, goal, deliverables, constraints, task breakdown, and acceptance criteria.
```

<a id="suitable-topics"></a>
## 🎯 Suitable Topics

This skill is not only for programmers. It works well for:

- programming and software engineering
- mathematics and statistics
- economics and finance fundamentals
- English and other language learning
- history, social science, and humanities reading
- writing, speaking, and communication training
- AI, LLM, and data-related topics

<a id="customization"></a>
## 🔧 Customization

If you want your own version, the most common changes are:

- change the tone or default language
- shift project style toward exams, papers, real-world work, or portfolio building
- change source strategy to emphasize official docs or textbook reading
- change mastery checks to focus on problem solving, oral explanation, code implementation, or paper interpretation

The best files to edit first:

- `skills/learn-anything-skill/SKILL.md`
- `skills/learn-anything-skill/references/source-strategy.md`
- `skills/learn-anything-skill/references/project-patterns.md`
- `skills/learn-anything-skill/references/mastery-rubric.md`

<a id="compatibility-notes"></a>
## 🔌 Compatibility Notes

- **OpenAI / Codex / ChatGPT Skills**: this is the most native target format
- **Claude Code**: usable directly as a skill; for broader distribution, a plugin wrapper is recommended
- **OpenCode**: better treated as a command adaptation than as a fully identical skill system

In short: the core asset in this repository is the portable `SKILL.md + references + assets` workflow. Installation entry points differ across agents, but the teaching logic is reusable.

<details>
<summary><strong>Expand references</strong></summary>

## References

These official resources helped shape the installation and compatibility guidance in this repository:

- OpenAI Skills: <https://openai.com/academy/skills/>
- ChatGPT Skills help: <https://help.openai.com/en/articles/20001066>
- Codex app introduction: <https://openai.com/index/introducing-the-codex-app/>
- Claude Code cheatsheet: <https://support.claude.com/en/articles/14553413-claude-code-cheatsheet>
- Claude Code plugins: <https://code.claude.com/docs/en/plugins>
- OpenCode commands: <https://opencode.ai/docs/commands>

</details>

## License

This repository is released under the [MIT License](./LICENSE).
