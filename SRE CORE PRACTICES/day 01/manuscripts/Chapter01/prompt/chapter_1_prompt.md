## 📜 Authoring Contract (Full YAML Specification)
authoring_contract_hector_v2.yaml

Use this contract as the authoritative style, structure, and validation source.
All generated markdown **must** comply with these rules.

---

### 🏈 Initial Prompt to Start Fresh Markdown Generation (Chapter 1)

You are a technical authoring assistant trained to produce high-quality instructional markdown chapters based on a structured narrative curriculum.

Your task is to write **Chapter 1** of a training novella on **Observability for Banking SREs**, using a panel-by-panel narrative structure and integrated teaching moments.

---

## 🌟 PURPOSE
Create a markdown training chapter titled:
**# Chapter 1 – “The Site Is Down” Isn’t a Root Cause**

This chapter teaches that dashboards showing green don’t mean a system is healthy. It focuses on logs, traces, and metrics that reveal actual failures hidden behind uptime metrics.

The tone is narrative, dramatic, dryly humorous, and always banking-relevant. Use fictional SRE Hector Alvarez as the main teacher. Include a junior engineer (Wanjiru), a VP (Manu), and a DB engineer (Juana).

---

## 📊 STRUCTURE REQUIREMENTS

Follow this general sequence:
1. `# Chapter 1 – ...`
2. Chapter Overview (2–5 paragraphs)
3. 🎯 Learning Objective
4. ✅ Takeaway
5. 🚦 Applied Example (with `mermaid` diagram)
6. Teaching Narrative (panel by panel, with dialogue, CLI output, and widgets)
7. Panel Image Embed (must use correct filenames)
8. Must include:
   - `:::hector quote`
   - `:::reflection`
   - `:::try this`
   - `:::debug pattern`

---

## 📸 IMAGE PATH FORMAT
All image embeds must use this format:

```markdown
![Alt text](images/<filename>.png){width=800}
```

Refer to the following filename mapping when embedding panels:
- Panel 1: `ch01_p01_pager_screams.png`
- Panel 2: `ch01_p02_dashboard_dissonance.png`
- Panel 3: `ch01_p03_log_discovery.png`
- Panel 4: `ch01_p04_dashboard_lying.png`
- Panel 5: `ch01_p05_trace_id_missing.png`
- Panel 6: `ch01_p06_three_pillars.png`
- Panel 7: `ch01_p07_lesson_locked_in.png`

---

## 🧠 WIDGETS TO USE
- `:::debug pattern` for reusable diagnostics (e.g., “Green Wall Fallacy”)
- `:::hector quote` for aphorisms
- `:::try this` and `:::reflection` for learner engagement
- `:::incident flashback` for real-world context
- `mermaid` diagrams for flows and traces

---

## 📋 CONTENT GOALS
- Total word count: **12,000–18,000**
- Each Teaching Narrative section: **1,500–2,100 words**
- At least **7 scenes/panels**
- At least **6 image embeds**
- One **Teaching Interlude** between Panel 5 and 6 explaining trace injection and retro-instrumentation
- Include **at least one** of each required widget

---

## 🗺️ PANEL BEAT MAP FOR CHAPTER 1
1. **The Pager Screams** – Dashboard all green; pager alert hits.
2. **Wanjiru Panics** – She can’t find the issue; logs are vague.
3. **What’s Actually Broken?** – Terminal reveals 500s; no helpful metrics.
4. **The Dashboard Is Lying** – Hector enters, points out replica issue.
5. **Context is Missing** – Logs lack trace ID; team blind.
6. **Three Pillars, One Story** – Logs, metrics, traces come together (Teaching Interlude here).
7. **Lesson Locked In** – Incident resolved; new observability culture defined.

---

## 🔄 SELF-CHECK REMINDER
At the end of generation, validate:
- ✅ All required widgets appear
- ✅ Images use `images/<filename>.png` with `{width=800}`
- ✅ Word count within target range
- ✅ Teaching Interlude appears between Panel 5 and 6
- ✅ Panel beats align with narrative goals
If any rule fails, pause generation and output an error summary.

---

## ✨ BEGIN GENERATION
Start output from:
```markdown
# Chapter 1 – “The Site Is Down” Isn’t a Root Cause
```

