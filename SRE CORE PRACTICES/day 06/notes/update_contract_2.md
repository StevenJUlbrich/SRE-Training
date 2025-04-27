I see why the new draft still feels “text-booky.”  
While the contract now forces **banking anchors** and **hands-on snippets**, it doesn’t *require* the warm mentoring beats the original chapter delivered (e.g., Ava’s mini-stories, learner questions, short dialogues). We can tighten the contract so future units **must** contain those teaching-heart elements.

---

## Gaps that still allow a sterile tone

| Missing flavour | Why it slipped through |
|-----------------|------------------------|
| **Conversational dialogue** between Ava and learners | No clause demands actual quoted back-and-forth. |
| **Emotional hooks / relatable micro-stories** (e.g., nervous CFO, relieved teller) | Storytelling ratio allows 20–40 % scene, but doesn’t insist on *character interaction*. |
| **Mentor prompts to reader** (“Pause and check your own dashboards…”) | Widgets like *Try This* are optional; not enforced per unit. |
| **Narrative pacing questions** (“What would happen if…?”) | No requirement for rhetorical or reflective questions. |

---

## Contract clauses to bake those in

Add these under `prose_requirements`:

```yaml
dialogue_quota:
  description: "Ensure real conversational tone."
  min_lines: 2        # At least two distinct quoted lines
  scope: "per Teaching Narrative"

learner_prompt:
  description: "Direct question or reflective challenge to the reader."
  required: true
  scope: "per Teaching Narrative"
```

Add these to `voice_guideline`:

```yaml
must_include_per_unit:
  - "Swahili proverb"
  - "Wrist-Slap Moment"
  - "Dialogue Line"   # e.g., Ava: “...”, Learner: “...?”
  - "Learner Prompt"  # a second-person question to the reader
```

Add a new **Widget** to enforce interactive tasks:

```yaml
allowed_inline_widgets:
  - "Try This"        # already present, but make it mandatory
try_this_frequency:
  per_unit: true
```

Update **consistency_checklist**:

```yaml
- "At least 2 lines of character dialogue per Teaching Narrative"
- "Direct learner prompt present per unit"
- "Try This widget present per unit"
```

With these rules:

1. **Dialogue Quote Example**

   > **Ava:** “Why does a green server lie?”  
   > **You:** “Because the user isn’t on the server!”

2. **Learner Prompt**

   > “Look at your last five outages—how many were invisible to host dashboards?”

3. **Try This** widget appears every unit.

---

## Result

Validators will now reject any unit lacking:

* Ava ↔ learner conversation (adds warmth).  
* A reflective question (engages reader).  
* An interactive “Try This” box (applies learning).  

This guarantees the chapter can’t devolve into pure formulae—even if we keep the 70 % technical quota.

If you approve these additions, I’ll patch the contract and retrofit Part A again with dialogue, prompts, and per-unit *Try This* tasks.