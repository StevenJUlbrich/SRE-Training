# 🚀 Module 1: Git Fundamentals (Days 1-2)

## 🎯 Learning Objectives

By the end of this module, learners will be able to:

- Understand version control concepts and Git's distributed nature
- Execute essential Git commands confidently in real-world scenarios
- Create and manage repositories locally and on Bitbucket
- Track changes with effective commit practices
- Visualize commit history with a graph-based mental model
- Troubleshoot common Git issues effectively

---

## 📖 1. Theory – Core Git Concepts in Plain English

### What is Git?

Git is a distributed version control system that tracks changes in files, allowing multiple developers to collaborate efficiently. Unlike centralized systems, Git gives each user a complete copy of the repository history locally[^1]. Created by Linus Torvalds in 2005 during Linux kernel development, Git has become the most popular source code management tool, with services like Bitbucket, GitHub, and GitLab providing remote hosting.

[^1]: [Git - Wikipedia](https://en.wikipedia.org/wiki/Git)

### Key Concepts

| Concept         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
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

- You don't break shared code.
- You can trace, revert, or analyze code at any point in history.
- You can automate safely with confidence.

---

## 🔍 3. Essential Git Commands (Annotated)

```bash
# Initialize a new local repository
git init

# Clone a remote repository (from Bitbucket, GitHub, etc.)
git clone https://bitbucket.org/user/repo.git

# See what's changed
git status

# Add file to staging (queue for next commit)
git add README.md

# Add all changed files to staging
git add .

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

## 🧠 4. Git Commit Graph Visualization

Understanding Git's branch and commit structure is easier with a visual model:

```text
Time →
main
●──A──●──B──●──C ← main (HEAD)
         \
feature    \
           ●──D──● ← feature/login-page
```

- Each `●` = a commit
- `A, B, C` are commits on the main branch
- A new branch (`feature/login-page`) is created from `B`
- New commits `D` and `E` are made in the feature branch
- You can merge `feature` into `main` once tested

---

## 🛠️ 5. Hands-On Lab – Your First Git Workflow

### Setting Up Git (First Time Only)

```bash
# Configure your Git identity
git config --global user.name "Your Name"
git config --global user.email "your.email@company.com"
```

### Creating Your First Repository

```bash
# Create and navigate to a new project directory
mkdir my-first-repo
cd my-first-repo

# Initialize the Git repository
git init
```

### Create and Track Files

```bash
# Create a README file
echo "# My Project" > README.md

# Check status to see untracked file
git status

# Add file to staging area
git add README.md

# Commit the file with a descriptive message
git commit -m "Initial commit with README"
```

### Make Changes and Track Them

```bash
# Edit the README file to add more content
echo "This is my first Git project" >> README.md

# See what changed
git diff

# Add the updated file to staging
git add README.md

# Commit the changes
git commit -m "Update README with project description"
```

### Connect to Bitbucket

```bash
# Create a new repository on Bitbucket first, then:

# Add the remote connection
git remote add origin https://bitbucket.org/yourusername/my-first-repo.git

# Push your local repository to Bitbucket
git push -u origin main
```

💡 **Tip**: Always run `git status` before pushing to verify what you're sending upstream.

---

## ⚠️ 6. Common Pitfalls & Troubleshooting

| Pitfall | How to Avoid or Fix |
|---------|---------------------|
| **Forgetting to stage files** | Always use `git status` to verify what's staged before committing |
| **Committing directly to main** | Create a branch using `git checkout -b feature/my-change` |
| **Confusing pull and fetch** | `git pull` = fetch + merge. Use `fetch` if you want to inspect first |
| **Pushing to wrong branch** | Confirm your current branch with `git status` or `git branch` |
| **Accidentally committed wrong file** | Use `git reset HEAD <file>` to unstage it |
| **Need to undo last commit** | `git reset --soft HEAD~1` (keeps changes in working directory) |
| **Remote push rejected** | Run `git pull --rebase` or resolve conflicts locally first |
| **Remote repo doesn't exist** | Check `git remote -v` and confirm the correct URL |

---

## 🧯 7. A Typical Git Workflow

When working on a new feature, you might follow this pattern[^2]:

1. Create and switch to a new branch: `git checkout -b feature/login-page`
2. Work on code, periodically using `git status` to check changes
3. Stage the changes: `git add .` (or specific files)
4. Commit the changes: `git commit -m "Add login page UI and form"`
5. Repeat editing and committing as needed
6. Push the branch to Bitbucket: `git push -u origin feature/login-page`
7. Open a pull request on Bitbucket to merge your changes

[^2]: [Git Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows)

---

## 📈 8. Performance Tips and Advanced Features

- **Optimize cloning for large repositories**: Use `git clone --depth 1` for a shallow clone when you only need recent history
- **Create aliases** for frequently used commands:
  ```bash
  git config --global alias.st status
  git config --global alias.ci commit
  git config --global alias.co checkout
  ```
- **Use `.gitignore`** to exclude files (build artifacts, sensitive info)
- **Try `git log --oneline --graph`** to visualize commit tree structure
- **Experiment with `git tag`** to mark a specific commit as a release (e.g., `v1.0`)
- **Use `git diff`** to see what exactly has changed before staging

---

## ✅ 9. Knowledge Check (Mini Quiz)

**Q1:** What's the difference between the staging area and working directory?

**Q2:** What does `git init` do?

**Q3:** After making a change, what is the full sequence of Git commands to publish it?

**Q4:** How would you undo your last commit without losing changes?

### 💡 Open-Ended Task

Create a local repo, make two commits, push to Bitbucket, then clone the same repo in a second folder to simulate team collaboration. What do you observe?

---

## 📗 10. FAQ

**Q:** How often should I commit?  
**A:** "Commit early, commit often." Small, focused commits make it easier to manage your code and reduce merge conflicts.

**Q:** Can I recover lost commits?  
**A:** Yes, using `git reflog` you can find and recover commits that seem deleted.

**Q:** Should I commit directly to the main branch?  
**A:** Generally no. Best practice is to create a feature branch for your work and merge it via pull request.

**Q:** What makes a good commit message?  
**A:** A concise, descriptive message that explains what the commit does and why. Start with a verb.

---

## 📌 11. Best Practices

1. **Commit frequently** with meaningful, descriptive messages
2. **Pull before pushing** to integrate others' changes
3. **Use .gitignore** to exclude files that shouldn't be tracked (build artifacts, sensitive info)
4. **Never commit sensitive data** like passwords or API keys
5. **Create a new branch** for each new feature or bugfix
6. **Keep commits focused** on a single logical change
7. **Write clear commit messages** that explain the "what" and "why"

---

## 🧠 12. Advanced Learner Challenge

- Try resolving merge conflicts manually
- Experiment with `git rebase` to keep a clean project history
- Create and enforce Git hooks for commit message standards
- Set up a simple CI/CD pipeline with your Bitbucket repository

---

## 🎮 Bonus: Gamified Learning Resources

- [Learn Git Branching (Interactive Game)](https://learngitbranching.js.org/)
- [Oh My Git! – Visual Git Card Game (GitHub)](https://github.com/git-learning-game/oh-my-git)
- [Git Koans: Practice Git via puzzles](https://github.com/mbostock/git-koans)