
# 🌿 Module 2: Branching Strategies (Days 3–4)

## 🎯 Learning Outcomes

By the end of this module, learners will be able to:

- Understand how Git branches support parallel development
- Choose and implement the right branching strategy (GitFlow, Trunk-Based, Feature Branch)
- Use real-world workflows to manage branches efficiently
- Visualize branching and merging with commit graphs
- Avoid and resolve common branching issues

---

## 📖 1. Theory – What Is a Git Branch?

A **branch** in Git is simply a pointer to a commit. It lets you isolate work, experiment freely, and merge changes when ready — without affecting the stable code on `main`.

| Branch Type     | Purpose                                      |
|-----------------|----------------------------------------------|
| `main` (or `master`) | Production-ready code (default branch)     |
| `feature/*`     | For working on individual features            |
| `release/*`     | For testing and stabilizing before deployment |
| `hotfix/*`      | For urgent fixes directly off `main`          |
| `develop`       | Used in GitFlow to aggregate feature work     |

---

## 🤔 2. Why This Matters in SRE and DevOps Context

Branching lets SRE teams:

- Work on bug fixes or config updates in isolation
- Deploy changes in phases (staging → production)
- Safely rollback or audit changes by preserving history
- Collaborate asynchronously while reducing merge conflicts

---

## 🔍 3. Git Branching Strategies – Pros and Cons

### 🔹 Feature Branching

Each new task (feature or bug) gets its own branch.

```bash
git checkout -b feature/add-login-form
```

✅ Simple and flexible  
❗ Can cause conflicts if branches are long-lived

---

### 🔹 GitFlow

A structured strategy using:

- `develop` for integration
- `main` for production
- Feature, release, and hotfix branches for coordination

```text
main      ----A---------E------------------G (releases)
               \       /           /
develop         B----C----D------F (features)
```

✅ Clear release and hotfix coordination  
❗ Heavy for fast-moving teams

---

### 🔹 Trunk-Based Development

Minimal branching. Developers push small changes directly (or via short-lived PRs) into `main`.

```bash
git checkout -b bugfix/timeout-handling
# Small commit
git commit -am "Fix timeout bug"
git push origin bugfix/timeout-handling
# Merge immediately via PR
```

✅ Great for CI/CD & automation  
❗ Requires discipline and test coverage

---

## 🧠 4. ASCII Diagram – Git Branching Visual

```text
main
●──A──●──B──●──E──●──G ← main (HEAD)
      \        \      /
feature1        ●──D
        \              \
         ●──C ← feature2
```

---

## 🛠️ 5. Hands-On Lab – Exploring Branching Strategies

### Scenario A: Feature Branch Workflow

```bash
# 1. Checkout main
git checkout main

# 2. Pull latest changes
git pull origin main

# 3. Create feature branch
git checkout -b feature/add-logging

# 4. Make changes, stage, and commit
git add .
git commit -m "Add logging module"

# 5. Push and create PR
git push -u origin feature/add-logging
```

> Merge via PR into `main`. Clean and safe!

---

### Scenario B: Simulate GitFlow

```bash
# 1. Create develop branch from main
git checkout -b develop main
git push -u origin develop

# 2. Start a feature
git checkout -b feature/user-login develop
# ... work ...
git commit -am "Create login feature"
git push -u origin feature/user-login

# 3. Merge into develop
git checkout develop
git merge feature/user-login

# 4. Start release
git checkout -b release/1.0 develop

# 5. Merge release to main + tag
git checkout main
git merge release/1.0
git tag -a v1.0 -m "Release v1.0"

# 6. Merge release back to develop
git checkout develop
git merge release/1.0
```

---

### Scenario C: Trunk-Based CI Workflow

```bash
# Fix quickly, then push & merge
git checkout -b fix/button-color
# Edit & commit
git commit -am "Fix button color"
git push -u origin fix/button-color
# Create PR, review, and merge ASAP
```

---

## ⚠️ 6. Common Pitfalls & Mistakes

| Mistake                         | Solution |
|--------------------------------|----------|
| Long-lived feature branches    | Merge often or rebase with `main` |
| Direct commits to `main`       | Use PRs and branch protection |
| Poor branch naming conventions | Use prefixes like `feature/`, `bugfix/`, `hotfix/` |
| Merging without testing        | Always test locally and via CI before merging |

---

## 🧯 7. Troubleshooting Tips

| Problem                           | Solution |
|----------------------------------|----------|
| “Non-fast-forward” error         | Pull latest `main` before pushing |
| Merge conflict when merging PR   | Resolve manually in editor or use `git mergetool` |
| Accidentally deleted branch      | Recover with `git reflog` if local |
| Cannot push due to permissions   | Check Bitbucket branch restrictions |

---

## ✅ 8. Knowledge Check (Mini Quiz)

**Q1:** What is the main difference between GitFlow and trunk-based development?  
**Q2:** Which branching strategy is best for teams deploying several times per day?  
**Q3:** What command creates and switches to a new branch?  

### 💡 Open-Ended Task

Create a feature branch. Make 2 commits. Simulate a pull request into `main`. Try to merge it. Then delete the branch locally and remotely. Observe the history.

---

## 📌 9. Summary / Key Takeaways

- Git branches isolate work safely and cleanly.
- Choose the right strategy based on **release cadence** and **team structure**.
- Use clear naming, short-lived branches, and pull requests.
- Branching strategy affects how you **merge, test, and release**.

---

## 🧠 10. Advanced Learner Challenge

- Rebase a feature branch onto `main` and resolve any conflicts.
- Visualize the commit tree with:  

  ```bash
  git log --oneline --graph --all
  ```
  
- Try `git cherry-pick` to apply a commit from one branch to another.
- Explore Bitbucket’s “branching model” settings for automation.

---

## 🎮 Bonus: Gamified Learning Tools

- [Learn Git Branching (Advanced Tree Scenarios)](https://learngitbranching.js.org/)
- [Oh My Git! GitFlow Simulation](https://ohmygit.org/)
- [Git Graph VS Code Extension](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
