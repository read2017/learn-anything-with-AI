# 安装 learn-anything-skill

## 给人类看的

把下面这句话复制粘贴给你的 AI Agent（OpenCode、Claude Code、Codex 均可）：

```
安装 learn-anything-skill，按这里的指南操作：https://raw.githubusercontent.com/read2017/learn-anything-with-AI/main/docs/guide/installation.md
```

或者手动操作：把 `skills/learn-anything-skill/` 整个文件夹复制到你项目里的 `.opencode/skills/learn-anything-skill/`（或对应平台路径），重启 Agent。

---

## 给 LLM Agent 看的

如果你是一个帮助用户安装 `learn-anything-skill` 的 AI Agent，按以下步骤操作。

**重要：请用 `curl` 拉取文件内容，不要用 WebFetch。WebFetch 会摘要化内容、丢失文件结构。**

```bash
curl -fsSL https://raw.githubusercontent.com/read2017/learn-anything-with-AI/main/docs/guide/installation.md
```

### Step 1: 检测当前平台

确定用户在使用哪个 Agent 平台：

```bash
# 检测 OpenCode
if command -v opencode &> /dev/null; then
    echo "OpenCode $(opencode --version) 已安装"
    PLATFORM="opencode"
# 检测 Claude Code
elif command -v claude &> /dev/null; then
    echo "Claude Code 已安装"
    PLATFORM="claude"
else
    echo "未检测到 OpenCode 或 Claude Code"
    PLATFORM="unknown"
fi
```

### Step 2: 下载 skill 文件

根据平台选择目标路径：

| 平台 | Skill 目标路径 |
|------|---------------|
| OpenCode | `.opencode/skills/learn-anything-skill/` |
| Claude Code | `.claude/skills/learn-anything-skill/` |
| Codex | `~/.codex/skills/learn-anything-skill/` |

以 OpenCode 为例（当前推荐平台），按以下步骤操作：

```bash
# 1. 创建目标目录
mkdir -p .opencode/skills/learn-anything-skill
mkdir -p .opencode/skills/learn-anything-skill/references
mkdir -p .opencode/skills/learn-anything-skill/assets

# 2. 下载核心文件
BASE="https://raw.githubusercontent.com/read2017/learn-anything-with-AI/main/skills/learn-anything-skill"

curl -fsSL "$BASE/SKILL.md" -o .opencode/skills/learn-anything-skill/SKILL.md

# 3. 下载 reference 文件
curl -fsSL "$BASE/references/mastery-rubric.md" -o .opencode/skills/learn-anything-skill/references/mastery-rubric.md
curl -fsSL "$BASE/references/project-patterns.md" -o .opencode/skills/learn-anything-skill/references/project-patterns.md
curl -fsSL "$BASE/references/source-strategy.md" -o .opencode/skills/learn-anything-skill/references/source-strategy.md
curl -fsSL "$BASE/references/teaching-playbook.md" -o .opencode/skills/learn-anything-skill/references/teaching-playbook.md

# 4. 下载模板文件
curl -fsSL "$BASE/assets/learning-plan-template.md" -o .opencode/skills/learn-anything-skill/assets/learning-plan-template.md
curl -fsSL "$BASE/assets/mastery-check-template.md" -o .opencode/skills/learn-anything-skill/assets/mastery-check-template.md
curl -fsSL "$BASE/assets/mistakes-log-template.md" -o .opencode/skills/learn-anything-skill/assets/mistakes-log-template.md
curl -fsSL "$BASE/assets/project-brief-template.md" -o .opencode/skills/learn-anything-skill/assets/project-brief-template.md
curl -fsSL "$BASE/assets/session-review-template.md" -o .opencode/skills/learn-anything-skill/assets/session-review-template.md
curl -fsSL "$BASE/assets/study-notes-template.md" -o .opencode/skills/learn-anything-skill/assets/study-notes-template.md
```

### Step 3: 验证安装

```bash
# 确认文件存在
ls .opencode/skills/learn-anything-skill/SKILL.md && echo "✅ SKILL.md 已就位"
ls .opencode/skills/learn-anything-skill/references/ && echo "✅ references/ 已就位"
ls .opencode/skills/learn-anything-skill/assets/ && echo "✅ assets/ 已就位"
```

### Step 4: 告知用户

告诉用户：

🎉 **learn-anything-skill 已安装成功！**

下一步需要：
1. **重启 Agent**（skill 只在启动时加载，不热重载）
2. 重启后，试着输入：`帮我学微积分，给我做一个4周学习计划`
3. Skill 会自动触发，以中文导师 + 项目教练模式开始教学
4. 学习产出（计划、笔记、复盘等）会自动保存到当前工作目录的 `study/` 子文件夹

### 可选：全局安装（所有项目可用）

如果用户想在所有项目里都能用这个 skill：

```bash
mkdir -p ~/.config/opencode/skills/learn-anything-skill
# 重复 Step 2 的下载步骤，目标路径改为 ~/.config/opencode/skills/learn-anything-skill/
```

### 可选：通过 Git 安装

```bash
git clone https://github.com/read2017/learn-anything-with-AI.git /tmp/learn-anything-skill-install
cp -R /tmp/learn-anything-skill-install/skills/learn-anything-skill .opencode/skills/learn-anything-skill
rm -rf /tmp/learn-anything-skill-install
```
