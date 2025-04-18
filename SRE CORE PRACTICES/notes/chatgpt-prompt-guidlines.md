# 🚀 TEMPLATE PROMPT — Narrative‑Driven SRE Training Module

editors to understand the logic. Delete any comment lines you don’t need.
\-->

```
YOU ARE A TECHNICAL STORYTELLER.  
CREATE A DAY {{DAY_NUMBER}} LESSON TITLED "{{DAY_TITLE}}" FOR AN SRE COHORT.
USE A NARRATIVE CASE STUDY GUIDED BY {{PROTAGONIST}}, A VETERAN SRE FROM {{CITY}}.

# 0. WORD‑COUNT & VOICE CONSTRAINTS
- Aim for 1,800 – 2,500 words.  
- 60 % protagonist dialogue / 40 % neutral narrator.  
- Tone: professional, lightly cynical, insight‑rich.

# 1. CENTRAL CASE STUDY (OPENING SCENE)
<!-- Establish stakes & hook. Describe system, user complaints, “green dashboard” paradox. -->
- Detail the environment (e.g., payment mesh, micro‑services).  
- Show initial confusion & business impact.  
- Close scene with protagonist’s quotable line.

# 2. FRAMEWORK INTRODUCTION — OTEA
<!-- OTEA is the organising spine. Embed first call‑out here. -->
- Define Observe → Test → Evaluate → Act conceptually.  
- Visualise with **one** Mermaid `sequenceDiagram` (autonumber).  
- Demonstrate protagonist beginning *Observe*.

# 3. OBSERVABILITY PILLARS
REPEAT the following sub‑template for **Metrics, Logs, Traces**:

## A. CONCEPTUAL INTRODUCTION
- Provide an **original** analogy (not car dashboards).  
- Define pillar; contrast with traditional monitoring.  
- End with a protagonist comment.

## B. LAYERED LEARNING
- 🔍 **Beginner Insight** — direct tie‑in to case study.  
- 🧩 **Intermediate Insight** — nuanced dimension.  
- 💡 **Advanced Insight** — expert perspective.

## C. CONCEPTUAL CHALLENGE
- Present pillar seeming to contradict others.  
- Pose “What would you do?” to learner.  
- Show protagonist’s reasoning using OTEA step (Test or Evaluate).  
- State key “conceptual pivot.”

# 4. INTEGRATION SECTION (FULL OTEA CYCLE)
<!-- Correlate all three pillars to reveal true root cause. -->
- Walk through Observe → Test → Evaluate → Act explicitly.  
- Highlight correlation moments.  
- Finish with protagonist’s “lesson learned” quote.

# 5. MENTAL MODEL REINFORCEMENT
- List **3‑5 observability anti‑patterns** & why they fail.  
- Provide a concise decision tree (Mermaid `graph TD`) for investigations.  
- State three protagonist “Observability Principles.”

# 6. ASSESSMENT
- 3‑5 scenario‑based questions tied to previous insights.  
- Include answer key **only after** a scrolling marker `--- ANSWER KEY BELOW ---`.

# IMPORTANT GUIDELINES
- ❌  NO code, CLI, or vendor‑specific configs.  
- ✅  Use Mermaid diagrams only for conceptual visuals; all `sequenceDiagram` blocks must have `autonumber`.  
- ✅  Ensure narrative tension; protagonist should challenge the learner.
- ✅  All facts must be technically accurate & practical.
- ✅  Analogies must be fresh (no car/plane references).

# OUTPUT FORMAT
Return **one** well‑formatted Markdown document. Start with an H1 title. Use
sub‑headings exactly as numbered above (# 1, # 2, … # 6). Include tables for
sidebars when beneficial.
```

---

## 📋 How to Use This Template

1. **Copy the entire code block** into ChatGPT.
2. Replace placeholders (`{{DAY_NUMBER}}`, etc.).
3. Add any day‑specific constraints (e.g., highlight canary releases).
4. Submit. Review for tone/depth.
5. Iterate by tweaking word‑count or voice ratios.

---

### Revision Log

- **v0.1** (2025‑04‑16) — Initial template derived from user prompt + checklist.

