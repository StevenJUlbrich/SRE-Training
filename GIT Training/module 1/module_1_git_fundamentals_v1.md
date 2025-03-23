# 🚀 Module 1: Git Fundamentals (Days 1–2)

## 🎯 Learning Outcomes

By the end of this module, learners will be able to:

- Understand how Git works under the hood (repository, staging, commit, branches)
- Execute essential Git commands confidently
- Set up and sync local and remote repositories (Bitbucket)
- Track, stage, and commit changes using best practices
- Visualize commit history with a graph-based mental model

---

## 📖 1. Theory – Core Git Concepts in Plain English

| Concept         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| **Repository**  | A Git repo is a database of snapshots. It's where everything is stored – code, history, branches. |
| **Working Directory** | Your actual project folder where changes are made.                      |
| **Staging Area**     | A temporary area where you queue up changes for the next commit. Think of it like a shopping cart. |
| **Commit**           | A saved snapshot of your changes. Each commit is like a checkpoint in time. |
| **Branch**           | A pointer to a commit. Lets you work on different versions of your project. |
| **Remote**           | A copy of the repository hosted on a service like Bitbucket. Shared with your team. |

---

## 🤔 2. Why This Matters for SREs & Production Teams

As an SRE or production support engineer, you often:

- Respond to incidents that require quick, traceable config/code rollbacks.
- Work across **multiple Git branches** for hotfixes and feature toggles.
- Collaborate through **Pull Requests** and **CI/CD pipelines**.

Understanding Git ensures:

- You don’t break shared code.
- You can trace, revert, or analyze code at any point in history.
- You can automate safely with confidence.

---

## 🔍 3. Annotated Examples of Common Commands

```bash
# Initialize a new local repository
git init

# Clone a remote repository (from Bitbucket, GitHub, etc.)
git clone https://bitbucket.org/user/repo.git

# See what’s changed
git status

# Add file to staging (queue for next commit)
git add README.md

# Commit changes with a message
git commit -m "Add initial README"

# See commit history (long form)
git log

# Push changes to Bitbucket (remote main branch)
git push origin main

# Pull changes from Bitbucket into your local branch
git pull origin main
```

---

## 🧠 4. Git Commit Graph Diagram (ASCII Visual)

```text
Time →
main
●──A──●──B──●──C ← main (HEAD)
         \
feature    \
           ●──D──● ← feature/login-page
```

- Each `●` = a commit.
- `A, B, C` are commits on the main branch.
- A new branch (`feature/login-page`) is created from `B`.
- New commits `D` and `E` are made in the feature branch.
- You can merge `feature` into `main` once tested.

---

## 🛠️ 5. Hands-On Lab – Your First Git Workflow

### 🔧 Step-by-Step

```bash
# Step 1: Configure your Git identity (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@company.com"

# Step 2: Create a new local project folder and initialize Git
mkdir my-first-repo
cd my-first-repo
git init

# Step 3: Create a file and commit it
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit with README"

# Step 4: Create a remote Bitbucket repo, then link it here
git remote add origin https://bitbucket.org/yourusername/my-first-repo.git
git push -u origin main

# Step 5: Make a change and push again
echo "New line" >> README.md
git add README.md
git commit -m "Add new line to README"
git push
```

💡 *Tip: Always run `git status` before pushing to verify what you’re sending upstream.*

---

## ⚠️ 6. Common Pitfalls & Mistakes

| Pitfall                           | How to Avoid                                           |
|----------------------------------|--------------------------------------------------------|
| Forgetting to stage files        | Use `git status` to verify what's staged before committing |
| Committing directly to `main`    | Create a branch using `git checkout -b feature/my-change` |
| Confusing `pull` and `fetch`     | `git pull` = fetch + merge. Use `fetch` if you want to inspect first |
| Pushing to the wrong branch      | Always confirm your current branch with `git status` or `git branch` |

---

## 🧯 7. Troubleshooting Tips & FAQ

| Problem                          | Fix                                                       |
|----------------------------------|------------------------------------------------------------|
| Accidentally committed wrong file | Use `git reset HEAD <file>` to unstage it                |
| Need to undo last commit          | `git reset --soft HEAD~1`                                |
| Remote repo doesn’t exist         | Check `git remote -v` and confirm the correct URL         |
| Push rejected (non-fast-forward) | Run `git pull --rebase` or resolve conflicts locally first |

---

## ✅ 8. Knowledge Check (Mini Quiz)

**Q1:** What’s the difference between the staging area and working directory?  
**Q2:** What does `git init` do?  
**Q3:** After making a change, what is the full sequence of Git commands to publish it?

### 💡 Open-Ended Task

Create a local repo, make two commits, push to Bitbucket, then clone the same repo in a second folder to simulate team collaboration. What do you observe?

---

## 📌 9. Summary & Key Takeaways

- Git helps you **track**, **stage**, and **commit** your changes safely.
- The **staging area** is a powerful feature to control exactly what goes into each commit.
- Git integrates easily with Bitbucket, which acts as your remote team repo.
- A clean commit history and proper push/pull workflow helps keep teams aligned.

---

## 🧠 10. Advanced Learner Challenge

- Try `git log --oneline --graph` to visualize commit tree structure.
- Use `.gitignore` to exclude files (e.g., `.env`, `node_modules`).
- Experiment with `git tag` to mark a specific commit as a release (e.g., `v1.0`).
- Explore `git diff` to see what exactly has changed before staging.

---

## 🎮 Bonus: Gamified Learning Resources

- [Learn Git Branching (Interactive Game)](https://learngitbranching.js.org/)
- [Oh My Git! – Visual Git Card Game (GitHub)](https://github.com/git-learning-game/oh-my-git)
- [Git Koans: Practice Git via puzzles](https://github.com/mbostock/git-koans)
