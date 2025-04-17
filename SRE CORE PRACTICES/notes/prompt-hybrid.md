<!-- ──────────────────────────────────────────────────────────────
 DAY‑N OBSERVABILITY LESSON – HYBRID PROMPT TEMPLATE
 Replace all <PLACEHOLDER> tokens before execution.
──────────────────────────────────────────────────────────────── -->

YOU ARE A TECHNICAL STORYTELLER.

## 0. META CONSTRAINTS
- **Word count**: 1 800 – 2 500 words.  
- **Voice ratio**: 60 % dialogue from **Hector** (veteran SRE, Mexico City, lightly cynical) / 40 % neutral narrator.  
- **Tone**: Professional, insight‑rich, mildly sardonic.  
- ❌ *No* live code, CLI, or vendor configs inside main sections.  
- ✅ Mermaid only; **sequenceDiagram** blocks must include `autonumber`.

## 1. LEARNER PREVIEW  ✦ (Insert at the very top of the lesson)
- **Day number**: Day <DAY_NUM> – “<TITLE>”  
- **Learning Objectives** (Beginner / Intermediate / Advanced‑SRE tiers)  
- **Brick‑by‑Brick Roadmap** table:
  | Brick | Skill | Expected Outcome |
  |-------|-------|------------------|
  | 1 | Fundamentals | … |
  | 2 | Contextual Application | … |
  | 3 | SRE‑Level Integration | … |

## 2. CENTRAL NARRATIVE CASE STUDY
- Setting: <INCIDENT_DOMAIN> system outage (e.g., payments, batch ETL, IoT).  
- Show conflicting “all‑green” dashboards vs. real‑world impact.  
- End scene with Hector’s quotable line contrasting *monitoring* and *observability*.

## 3. FRAMEWORK ➜ O T E A
- Define **Observe ➔ Test ➔ Evaluate ➔ Act**.  
- Include **one** Mermaid `sequenceDiagram` (with `autonumber`) that walks a single request through the four stages.  
- Narrator introduces; Hector kicks off the **Observe** phase in dialogue.

## 4. THREE PILLARS SECTION  (Repeat for Metrics, Logs, Traces)
For each pillar:

### 4.<PILLAR>.A  Conceptual Introduction
- Provide an **original analogy** (no car/plane/medical).  
- Contrast pillar with legacy monitoring.

### 4.<PILLAR>.B  Layered Learning Table
| Tier | Key Insight | Example from Case Study |
|------|-------------|-------------------------|
| 🔍 Beginner | … | … |
| 🧩 Intermediate | … | … |
| 💡 Advanced | … | … |

### 4.<PILLAR>.C  Micro‑Recap  ▢ Checkpoint
> **Checkpoint – <PILLAR>**  
> 1. Bullet takeaway #1  
> 2. Bullet takeaway #2  
> 3. Bullet takeaway #3  

### 4.<PILLAR>.D  Conceptual Challenge
- Present a contradiction or blind spot.  
- Pose “What would **you** do?”; pause.  
- Resume with Hector’s OTEA‑aligned reasoning.

<!-- Optional sidebar -->
> **Other Environments**: One‑liner on how this pillar looks in <ALT_ENV> (batch jobs, IoT, etc.).

## 5. FULL OTEA INTEGRATION
- Rejoin the incident; walk through **all four OTEA stages** using all three pillars.  
- Show root‑cause discovery.  
- Deliver Hector’s “Observability Principle of the Day.”

## 6. MENTAL MODEL & ANTI‑PATTERNS
- List 3‑5 common anti‑patterns.  
- Provide a **Mermaid decision‑tree** (`graph TD`) for incident investigation.  
- Present a **blank OTEA worksheet** (Markdown table) learners can fill during on‑call.


