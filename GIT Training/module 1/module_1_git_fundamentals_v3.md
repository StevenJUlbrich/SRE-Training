# 🚀 Module 1: Git Fundamentals (Version 3)

---

## 🎯 Learning Objectives

By the end of this module, learners will be able to:

- Clearly explain version control concepts and Git’s distributed nature.
- Confidently execute essential Git commands in real-world scenarios.
- Create and synchronize repositories locally and remotely (Bitbucket).
- Use effective commit practices to track changes.

---

## 📖 Theory: Core Git Concepts

**What is Git?**

Git is a distributed version control system, created by Linus Torvalds in 2005. Unlike centralized systems, Git allows each user to keep a full history of their repository locally, facilitating collaboration, branching, and merging.

### Key Concepts Explained

- **Repository**: Stores your project history, including code, commits, and branches.
- **Working Directory**: Your active workspace, where you edit files.
- **Staging Area**: A place to prepare and review changes before committing.
- **Commit**: Saves a snapshot of your project at a point in time.
- **Branch**: Allows parallel versions of your project for feature development.
- **Remote**: A shared repository hosted online (e.g., Bitbucket, GitHub).

### Why Does Git Matter for SREs?

Git provides:

- Quick rollback capabilities during incidents.
- Branching strategies for stable and experimental code paths.
- Collaborative workflows through Pull Requests and CI/CD pipelines.

---

## 🎬 Practical Exercises: Hands-On Demonstrations

### Setting Up Git

**Step-by-step setup:**

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Creating Your First Repository

1. **Initialize the repository**:

```bash
mkdir my-first-repo
cd my-first-repo
git init
```

2. **Create and commit a file**:

```bash
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit with README"
```

3. **Connect to Bitbucket**:

- Create a new repository in Bitbucket.
- Link your local repo:
  
```bash
git remote add origin https://bitbucket.org/username/my-first-repo.git
git push -u origin main
```

---

## 🧯 Troubleshooting Common Issues

| Issue                              | Solution                                                      |
|------------------------------------|---------------------------------------------------------------|
| Forgot to stage files              | Always run `git status` before committing                     |
| Committed directly to `main` branch| Use branches (`git checkout -b feature/new-feature`)           |
| Remote push rejected               | Pull changes first (`git pull origin main`) or use rebase     |

---

## 📌 Knowledge Check

**Quiz:**

1. Describe the difference between staging area and working directory.
2. How would you undo your last commit without losing changes?

**Open-ended Task:**

- Create a local repository with two commits, push it to Bitbucket, then clone it into a separate folder. Document your observations.

---

## 🎯 Lesson Summary: Key Takeaways

- Git helps you safely track and manage your project history.
- Effective commit messages and frequent commits simplify troubleshooting.
- Understanding branching and remote workflows enhances collaboration and productivity.

---

## 🛠️ Advanced Tasks

- Experiment with advanced git log formats (`git log --oneline --graph`).
- Create a `.gitignore` file to exclude sensitive and unnecessary files.
- Tag a commit (`git tag v1.0`) to mark release milestones.

---

## 🚩 Common Pitfalls

- **Overwriting changes**: Always verify with `git status` and `git diff`.
- **Losing commits**: Understand commands clearly (`git reset` vs. `git revert`).

---

## 📈 Performance Tips and Advanced Features

- Optimize cloning and fetching for large repositories (`git clone --depth`).
- Use aliases for frequent commands (`git config --global alias.st status`).

---

## 📗 FAQ

**Q:** How often should I commit?
**A:** "Commit early, commit often." Small, focused commits simplify code management and reduce merge conflicts.

**Q:** Can I recover lost commits?
**A:** Yes, using `git reflog` to retrieve deleted commits.

---

## 🔖 Recommended Additional Resources

- [Interactive Git Branching Game](https://learngitbranching.js.org/)
- [Oh My Git! - Visual Card Game](https://github.com/git-learning-game/oh-my-git)
- [Git Koans: Practice Git via puzzles](https://github.com/mbostock/git-koans)
