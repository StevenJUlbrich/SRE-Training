**What’s still open after reading `authoring_contract_hector.yaml`**

| Theme | Covered in the contract | Remaining gap |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **File-level output structure** | Each chapter must be its own Markdown file beginning with `# Chapter <N> – <Title>`, and image definitions live in a *separate* JSON that follows `external_image_data_schema`. | ✅ No action needed. |
| **Beat-map ↔ panel schema linkage** | `scene_sync` + full JSON schema specify every required field and ID mapping. | ✅ No action needed. |
| **Panel / image budget** | Global rule of **6–15 panels per chapter** with checklist enforcement. | ✅ No action needed. |
| **Learner reflection hooks** | Each Teaching Narrative must include a *Learner Prompt* line; `Learner Reflection` widget is whitelisted but **frequency/placement not mandated** (only Aphorism & Anecdote have explicit placement rules). | *Decide*: Do you want a minimum count or specific placement rule for reflection widgets similar to Aphorisms? |
| **Assessment / quizzes** | **No heading, widget, or schema** for quizzes, rubrics, or checkpoint questions appears anywhere in the contract (the word “quiz” is absent). | *Outstanding*: If chapter-end or tier-end quizzes are required, we need spec fields (item count, difficulty tags, output format, etc.). |
| **Regulatory / risk voice earlier in the arc** | Contract enforces a general “banking context anchor” per section, but it never calls out compliance or risk narratives until the characters supply them ad-hoc. | *Clarify*: Are explicit risk/compliance call-outs needed in Foundations and Intermediate tiers, or is it OK that Lucía (Risk Lens) doesn’t surface until later? |
| **Production-cost guardrails (pages, art budget)** | Panel count is set, but there’s **no upper-bound on physical pages** or guidance on image resolution/size budgeting. | *Optional*: Add pagination or pixel-dimension advice if budgeting matters. |
| **Widget catalogue completeness** | A healthy list is whitelisted, but if you plan to add future widgets (e.g., `:::quiz`), they’re not yet in `allowed_inline_widgets` . | *Plan*: Extend the whitelist or note that new widgets need contract updates. |

______________________________________________________________________

### TL;DR

The contract locks down narrative cadence, image schema, and prose rules very well. What it **still doesn’t specify** are:

1. **How formal assessments (quizzes/rubrics) should be generated and delivered.**
2. **Whether—and where—regulatory-risk commentary must appear in early chapters.**
3. **Exact rules for frequency/placement of `Learner Reflection` widgets.**
4. **Any physical-page or image-resolution limits if you need to manage production costs.**

Everything else from my earlier checklist is now answered. Let me know which of those four areas (or others) you’d like to nail down in the next contract revision.

You're right — the questions in `round-1-questions.md` are smart and well-aimed. They surface **strategic pressure points** in your authoring framework. Here's my opinion on each, given your responses:

______________________________________________________________________

### ✅ 1. **Formal Assessments**

> **Your answer:** Not now — will be generated later.

______________________________________________________________________

### ✅ 2. **Regulatory/Risk Commentary**

> **Your answer:** Not necessary early in the material.

______________________________________________________________________

### 🟡 3. **Learner Reflection Frequency**

> Updated the authoring_contract_hector.yaml review it

______________________________________________________________________

### ✅ 4. **Physical Page or Image Resolution**

> **Your answer:** Not a factor.
