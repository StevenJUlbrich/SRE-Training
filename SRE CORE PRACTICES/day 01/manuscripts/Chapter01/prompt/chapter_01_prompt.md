## ✅ MASTER CHAPTER GENERATION PROMPT – CHAPTER 1

You are generating Chapter 1 of an illustrated, instructional novella about observability in banking systems. Your goal is to produce teaching-rich markdown content that blends narrative, CLI/code examples, widgets, and graphic panel descriptions.

______________________________________________________________________

### 📁 Required References

Use ONLY the following files:

- `authoring_contract_hector_v2.yaml` – structure, prose style, widgets, pacing【304†source】
- `chapter_1_outline.md` – primary concepts, panel beats, teaching sequences, artifact expectations【305†source】
- `hector_alvarez_persona.md` + `hector_alvaz_quotes_catch-phrases.md` – tone, delivery, emotional rhythm【309†source】【311†source】
- `junior_characters.md`, `sre_other_characters.md` – learner arc and cast constraints【307†source】【306†source】
- `house_palette_line_style_hector.md` – visual clarity and diagrammatic tone【308†source】

______________________________________________________________________

### ❌ DO NOT:

- Add panels beyond the 7 defined in the outline
- Add quizzes, labs, or bonus scenes
- Include characters not in the provided cast
- Break the structure or pacing rules in the contract
- Invent new tools or technologies

______________________________________________________________________

### 🧱 STRUCTURE:

Start with:

```markdown
# Chapter 1 – “The Site Is Down” Isn’t a Root Cause
```

Then follow the exact section structure from `authoring_contract_hector_v2.yaml`. Each panel must:

- Align to the concept map in `chapter_1_outline.md`
- Include a 1–2 paragraph scene and dialogue (minimum)
- Integrate technical artifacts (CLI/code/logs/diagram) as defined
- Include at least one properly styled widget per panel or per teaching sequence

Target **12,000–18,000 narrative words**, excluding CLI/code blocks.

______________________________________________________________________

### ✍️ STYLE & VOICE:

- Use Hector’s dry, practical tone from his persona file
- Keep panels cinematic but always educational
- Ensure all visuals and prose reinforce the stated teaching outcome

______________________________________________________________________

### 🧠 VALIDATION CHECKLIST (POST-GENERATION)

After generation, validate the chapter by comparing output against the following contract points:

- [ ] Word count between 12,000–18,000 narrative words (exclude code/CLI blocks)
- [ ] Panel count = 7, matching titles in the outline
- [ ] Every panel includes:
  - [ ] A clear teaching moment
  - [ ] A specific character POV or dialogue line
  - [ ] One CLI, diagram, log line, or metric as artifact
  - [ ] One `widget` (debug pattern, quote, reflection, try this)
- [ ] No non-canon characters, tools, or invented frameworks
- [ ] Hector speaks in-character and reinforces the theme: “Green ≠ good”
- [ ] Teaching arc builds from scene to scene to support learner insight

______________________________________________________________________

### 🧪 BEGIN GENERATION:

Do not invent structure or characters. Generate using the teaching arc in the outline.
Start from:

```markdown
# Chapter 1 – “The Site Is Down” Isn’t a Root Cause
```

Continue through all 7 teaching sequences. End with the final assessment prompt and reflection.
