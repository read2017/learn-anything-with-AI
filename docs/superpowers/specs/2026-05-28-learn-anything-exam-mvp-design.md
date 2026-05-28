# Learn Anything Exam MVP Design

## Product Thesis

The first product should use a narrow market entry and a general learning engine.

The market entry is college STEM final exam prep. The learning engine remains the general `learn-anything-skill` loop: diagnose the goal and starting point, gather or search sources, teach the smallest useful concept, assign practice, give feedback, test mastery, write learning memory, and decide whether to advance.

The product is not a course platform, a check-in app, or a traditional question bank. It is a Codex-style AI tutor workspace where the student mainly learns through conversation, while the system quietly preserves structure, progress, files, sources, weak points, and mastery evidence.

## Target User And First Scenario

Primary first users are college students preparing for STEM final exams, especially subjects such as calculus, linear algebra, probability, physics, circuits, data structures, and other engineering courses.

The first high-value scenario is not "answer one question." It is:

> I have a final exam soon, I do not know how to review, and I need an AI tutor to break the course into learning loops I can complete.

The product should still support all knowledge-learning topics over time, because the underlying learning abstraction is general. The exam scenario is the first validation wedge.

## Core Concept: Learnspace

A `learnspace` is one long-running learning subject or learning task.

Examples:

- Calculus final exam sprint
- Probability final exam sprint
- Data structures final exam sprint
- CET-6 reading improvement
- AI full-stack learning

The left sidebar manages learnspaces. Users can create, switch, and rename them. Each learnspace has its own conversation, uploaded materials, learning loop history, and durable learning files.

The product should expose friendly product names, but the underlying files should map to the `learn-anything-skill` outputs:

- `learning-plan.md`: learning plan and loop queue
- `notes.md`: accumulated study notes
- `session-review.md`: learning loop review records
- `mastery-check.md`: mastery checks and evidence
- `mistakes-log.md`: mistakes, weak points, and root causes
- `project-brief.md`: optional task or stage brief
- `sources/`: uploaded files and indexed source metadata

## Information Architecture

The first version should use a clean three-area layout:

```text
App
  Left sidebar: Learnspaces
    - Calculus final exam sprint
    - Probability final exam sprint
    - Data structures final exam sprint
    - New learnspace

  Main area: AI tutor conversation
    - AI diagnoses the user goal and starting point
    - AI guides material upload when useful
    - AI teaches and tests through learning loops

  Right panel: Current loop state, collapsible
    - Current loop goal
    - Loop phase
    - Acceptance criteria
    - Uploaded/source status
    - Weak points
    - Next suggested action
```

The main interaction should stay conversational. The side panels support memory and orientation but should not become the main experience.

## Learning Loop State Machine

The smallest unit of progress is a `Learning Loop`, not a day.

A student may complete zero, one, or five loops in a day. The product should advance based on mastery evidence, not calendar check-ins.

A loop contains:

1. Goal definition: one clear ability point for this round.
2. Starting-point diagnosis: check prerequisite knowledge and current level.
3. Shortest useful explanation: concept, use case, conditions, and common traps.
4. Minimal examples: one or two representative problems or cases.
5. Active practice: the student solves, derives, explains, writes, or applies.
6. Immediate feedback: the AI corrects, explains root cause, and repairs missing prerequisites.
7. Mastery test: three to five validation tasks, including basic and variant tasks.
8. Review persistence: update notes, mistakes, mastery level, and next action.
9. Advancement decision: pass and move to the next loop, or create a repair loop.

The UI should not show all nine steps as a heavy wizard. The AI should guide them naturally in conversation. The right panel only displays the compact current state:

```text
Current loop
Conditional probability definition and usage

Status
Diagnosing / Explaining / Practicing / Testing / Passed / Needs repair

Acceptance
- Explain what P(A|B) means
- Distinguish P(A|B) from P(B|A)
- Solve two variant problems
```

By default, the product recommends moving forward only after the student passes the mastery test. The user may manually skip when necessary, but the system should record that as a skipped or unverified loop.

## Sources And Search Strategy

The AI should not cite sources on every message. That would make the learning experience feel heavy and unnatural.

The system should keep source awareness in the background and surface it only when it matters:

- Planning a sprint path
- Judging likely exam emphasis
- Explaining a disputed or high-risk concept
- Filling gaps when user materials are missing
- Making recommendations that depend on source quality

Source priority:

1. Current learnspace materials: uploaded slides, assignments, past papers, exam scope, teacher notes.
2. Internal Baoyandao resources: school papers, similar course materials, question distributions, common exam patterns.
3. Active AI search: official websites, official docs where applicable, authoritative courses, standard textbooks, and best practices.
4. General model knowledge: useful for explanation, analogy, and practice generation, with important claims kept verifiable when needed.

The AI should naturally teach by default. When materials are missing or uncertainty matters, it should say so and suggest what to upload or search next.

## First-Run User Journey

The first-run flow should be conversation-first:

1. User opens the website and sees a clean AI tutor workspace.
2. The AI says it will use learning loops to help with exam prep.
3. The AI asks for course, exam date, current foundation, and optional materials.
4. The user says, for example, "I want to review probability, the exam is in 10 days, my foundation is average."
5. The system creates a learnspace named "Probability final exam sprint."
6. The AI diagnoses the starting point with a few questions or a short diagnostic problem set.
7. The AI generates an exam sprint frame: topic map, prioritized loop queue, first loop, and recommended materials to upload.
8. The AI starts the first learning loop in chat.
9. The student practices and completes the mastery test.
10. The system updates learning files and recommends the next loop or a repair loop.

The desired first-session benchmark is:

- Within 3 minutes: create a learnspace.
- Within 10 minutes: enter the first learning loop and complete diagnosis plus explanation.
- Within 20 minutes: complete the first mastery test or produce a clear repair plan.

## MVP Scope

The MVP must include:

- Learnspace management: create, switch, rename.
- Conversation-first AI tutor.
- Learning loop engine with diagnosis, explanation, practice, feedback, testing, review, and advancement decision.
- Exam sprint planning from course, exam date, foundation, and target.
- Material upload into the active learnspace.
- Durable learning files for plan, notes, reviews, mastery checks, mistakes, and sources.
- Collapsible current-loop state panel.
- Basic source search for official materials, authoritative materials, and best practices.
- Integration path for Baoyandao internal exam-paper resources.

The MVP should not include:

- Complex level maps or gamified progression.
- Leaderboards, communities, or social check-ins.
- A full traditional question-bank system.
- Teacher or institution admin dashboards.
- Payment and subscription flows.
- Multi-user collaboration.
- Native mobile apps.
- Complex knowledge graph visualization.

## Acceptance Scenario

The MVP is successful when a user can complete this path:

```text
Create "Probability final exam sprint"
  -> Tell the AI the exam is in 10 days and their foundation is average
  -> Receive a prioritized learning-loop queue
  -> Upload materials or continue without upload
  -> Start the first loop
  -> Complete practice and mastery testing
  -> See mistakes, mastery evidence, notes, and next-loop recommendation saved
  -> Return later and continue from the same learnspace
```

## Product Voice

The product should sound like a calm, capable AI tutor. It should encourage with specific feedback, not empty praise.

Useful positioning lines:

- "Let an AI tutor break final exam prep into learning loops you can pass one by one."
- "Do not just plan your review. Close the feedback loop."
- "Learn through conversation, test mastery, and keep your learning memory."

The product should avoid overclaiming that it can predict exams perfectly. It can use uploaded materials, internal papers, and source search to make better plans, while being honest about uncertainty.

## Open Product Decisions

These decisions remain for later specs:

- Exact data schema for learnspaces, loops, source metadata, and learning files.
- Whether the learning files are first-class editable documents or mostly hidden system memory.
- The first supported file types for upload.
- The search provider and source retrieval architecture.
- How Baoyandao internal resources are indexed, permissioned, and ranked.
- How to handle model cost, rate limits, and long-context material ingestion.
