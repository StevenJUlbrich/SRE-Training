
# 🔀 Module 3: Conflict Resolution (Days 5–6)

## 🎯 Learning Outcomes

By the end of this module, learners will be able to:

- Identify why and how Git merge conflicts occur
- Resolve conflicts manually and with Git tools
- Understand the difference between merge and rebase strategies
- Practice clean integration using visual conflict resolution tools
- Reduce conflict frequency through best practices

---

## 📖 1. Theory – What Causes a Merge Conflict?

A **merge conflict** happens when:

- Two branches **change the same lines** in the same file
- One branch deletes a file that another branch modifies

Git cannot decide which version to keep, so it pauses and asks **you** to resolve it.

---

### Example Conflict Scenario

```text
main
●──A──B──C ← main
     \
      ●──D──E ← feature/login
```

If commit `B` and `E` both change the same line in `config.js`, a conflict will occur when merging `feature/login` into `main`.

---

## 🤔 2. Why This Matters in Real Projects

Merge conflicts:

- Disrupt CI/CD pipelines
- Delay deployments
- Cause regressions if resolved poorly

SRE teams must be able to:

- Respond to failed PRs quickly
- Resolve config and YAML file conflicts cleanly
- Choose merge vs rebase appropriately based on the context

---

## 🔍 3. How Git Shows Conflicts

Git inserts **conflict markers** in the file:

```diff
<<<<<<< HEAD
timeout = 30
=======
timeout = 45
>>>>>>> feature/update-timeout
```

You must edit the file to keep the correct content, and **remove the markers**.

---

## 🧠 4. ASCII Merge Conflict Flow

```text
          (Edit same file)
main:     ●──A──B──C
                   \
feature:            ●──D──E (conflicts with B)

Attempt: git merge feature → CONFLICT
```

---

## 🛠️ 5. Hands-On Lab – Simulate and Resolve a Conflict

### Step-by-Step Lab: Manual Conflict Resolution

```bash
# Step 1: Setup
mkdir merge-lab && cd merge-lab
git init
echo "timeout = 30" > config.txt
git add config.txt
git commit -m "Initial commit"

# Step 2: Create a branch and change the file
git checkout -b feature-branch
echo "timeout = 45" > config.txt
git commit -am "Feature changes timeout"

# Step 3: Switch back and edit on main
git checkout main
echo "timeout = 60" > config.txt
git commit -am "Main changes timeout"

# Step 4: Try to merge
git merge feature-branch
```

Git will report a **conflict**.

### Step 5: Resolve It

Open `config.txt`, resolve the conflict, then:

```bash
# Clean up the file (choose final value)
echo "timeout = 50" > config.txt

# Stage and commit
git add config.txt
git commit -m "Resolve merge conflict on timeout setting"
```

---

## 🧯 6. Troubleshooting & Tools

| Problem                          | Solution |
|----------------------------------|----------|
| Conflict markers left in code    | Manually remove them and re-commit |
| Cancel merge                     | `git merge --abort` |
| Prefer one version entirely      | `git checkout --ours <file>` or `--theirs` |
| Visualize conflicts              | Use VS Code, GitKraken, or `git mergetool` |

---

## 🔄 7. Merge vs Rebase (Comparison)

| Git Operation | Description | Pros | Caution |
|---------------|-------------|------|---------|
| `git merge`   | Combines histories with a merge commit | Easy, preserves history | May cause messy graphs |
| `git rebase`  | Replays commits on top of a base branch | Clean, linear history | Risky if used after pushing shared branches |

---

## ✅ 8. Knowledge Check (Mini Quiz)

**Q1:** What markers does Git use to identify conflicts in a file?  
**Q2:** Which command do you use to cancel a problematic merge?  
**Q3:** What does `git rebase` do differently from `git merge`?

### 💡 Open-Ended Task

Simulate a conflict with two branches editing the same YAML file. Practice resolving it using both manual editing and `git mergetool`.

---

## ⚠️ 9. Common Mistakes and How to Avoid Them

| Mistake | Fix |
|--------|-----|
| Leaving conflict markers in committed code | Always preview your file before committing |
| Trying to rebase a shared branch | Rebase only **before** pushing |
| Not testing code after conflict resolution | Always run tests after merging |
| Deleting the wrong version during conflict resolution | Use visual tools (VS Code, GitKraken) if unsure |

---

## 📌 10. Summary / Key Takeaways

- Merge conflicts are **normal**, not errors
- Conflict markers help you see both versions
- Use `git status` and `git log` to investigate
- Choose merge vs rebase based on your team’s policy
- Always **test** after resolving a conflict

---

## 🧠 11. Advanced Learner Challenge

- Use `git rebase` and handle a 3-way conflict
- Explore `git rerere` for automatic conflict resolution reuse
- Try `git cherry-pick` and resolve if it causes a conflict
- Create a `.gitattributes` file to set merge strategies per file type

---

## 🎮 Bonus: Gamified Learning Resources

- [Visual Merge Conflict Practice](https://learngitbranching.js.org/?demo=merge-conflict)
- [Git Merge Theirs / Ours Strategy](https://builtin.com/software-engineering-perspectives/git-merge-theirs)
- [Git Tower Conflict Resolution Guide](https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/merge-conflicts)
