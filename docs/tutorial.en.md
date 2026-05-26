# Tutorial

This document keeps the full usage guide for `learn-anything-skill`. The homepage README keeps only the shortest path.

## Installation

### Recommended: install with the Agent Skills CLI

```bash
npx skills add read2017/learn-anything-with-AI --skill learn-anything-skill
```

Global install:

```bash
npx skills add -g read2017/learn-anything-with-AI --skill learn-anything-skill
```

### Manual install in Codex / OpenAI Skills

#### Option A: local directory install

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/learn-anything-skill ~/.codex/skills/
```

#### Option B: upload or import through a Skills UI

Upload the whole `learn-anything-skill` folder, not just `SKILL.md`, so `references/` and `assets/` remain available.

### Install in Claude Code

#### Option A: use it as a project skill

```bash
mkdir -p .claude/skills
cp -R ./skills/learn-anything-skill ./.claude/skills/
```

#### Option B: package it as a Claude Code plugin

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── learn-anything-skill/
        └── SKILL.md
```

### Install in OpenCode

#### Option A: project-level command

```bash
mkdir -p .opencode/commands
```

Create `.opencode/commands/learn-anything.md`:

```md
---
description: Chinese mentor-style learning and project coaching
---

Act as a mentor + project coach and help me learn this topic in Chinese: $ARGUMENTS
```

#### Option B: global command

```text
~/.config/opencode/commands/learn-anything.md
```

## Usage

### 1. Explicit invocation

```text
Use $learn-anything-skill to teach me calculus and create a 4-week study plan.
```

### 2. Natural-language triggering

- Help me learn calculus and create a four-week plan
- Teach me how to read *The Wealth of Nations* and organize study notes
- I want to improve spoken English with project-style exercises and reviews
- Help me learn SQL and design a small project brief
- Check my understanding of probability and point out weak spots

### 3. Use it with your own materials

You can hand it:

- course slides
- lecture notes
- textbook chapters
- papers
- blog posts
- homework sets
- code repositories
- your own notes

## Use Cases

### Case 1: a four-week study plan

```text
Use $learn-anything-skill to help me learn linear algebra.
I only know high-school math and I can study 6 hours per week.
Please create a 4-week plan with weekly outputs and acceptance criteria.
```

### Case 2: guided reading

```text
Use $learn-anything-skill to guide me through Volume 1 of The Wealth of Nations.
I do not want a summary only. Help me build structure, make reading notes, and prepare review questions after each chapter.
```

### Case 3: project-based spoken English training

```text
Use $learn-anything-skill to improve my spoken English.
My goal is to deliver a 3-minute self-introduction and project introduction in 6 weeks.
Please design the training in a project-driven way.
```

### Case 4: SQL plus a small project brief

```text
Use $learn-anything-skill to teach me SQL.
I know some Python but have never studied databases systematically.
Please give me a roadmap and design a small student-score analysis project brief.
```

### Case 5: mastery checking

```text
Use $learn-anything-skill to assess my understanding of conditional probability and Bayes' rule.
Do not just ask whether I understand. Give me restatement tasks, variation tasks, and transfer tasks.
```

## Recommended Prompts

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
