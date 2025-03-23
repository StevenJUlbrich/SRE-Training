# Module 1: Git Fundamentals (Days 1-2)

## Learning Objectives

- Understand version control concepts and Git's distributed nature
- Master essential Git commands for daily workflows
- Create and manage repositories locally and on Bitbucket
- Track changes with effective commit practices

### Key Concepts

#### What is Git?

Git is a distributed version control system that tracks changes in files, allowing multiple developers to collaborate efficiently. Unlike centralized systems, Git gives each user a complete copy of the repository history locally[^1]. Created by Linus Torvalds in 2005 during Linux kernel development, Git has become the most popular source code management tool, with services like Bitbucket, GitHub, and GitLab providing remote hosting.

[^1]: [Git - Wikipedia](https://en.wikipedia.org/wiki/Git#:~:text=As%20with%20most%20other%20distributed,A)

---

## 📖 Theory – Core Git Concepts in Plain English

| Concept         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Repository**  | A Git repo is a database of snapshots. It's where everything is stored – code, history, branches. |
| **Working Directory** | Your actual project folder where changes are made.                      |
| **Staging Area**     | A temporary area where you queue up changes for the next commit. Think of it like a shopping cart. |
| **Commit**           | A saved snapshot of your changes. Each commit is like a checkpoint in time. |
| **Branch**           | A pointer to a commit. Lets you work on different versions of your project. |
| **Remote**           | A copy of the repository hosted on a service like Bitbucket. Shared with your team. |

---

## 🤔 Why This Matters for SREs & Production Teams

As an SRE or production support engineer, you often:

- Respond to incidents that require quick, traceable config/code rollbacks.
- Work across **multiple Git branches** for hotfixes and feature toggles.
- Collaborate through **Pull Requests** and **CI/CD pipelines**.

Understanding Git ensures:

- You don’t break shared code.
- You can trace, revert, or analyze code at any point in history.
- You can automate safely with confidence.

---

## Core Components

- **Repository (repo)**: The collection of tracked files and change history
- **Working Directory**: Your current files where you make changes
- **Staging Area (Index)**: The intermediate area where changes are prepared for committing
- **Commit**: A snapshot of your changes with a descriptive message
- **Branch**: A parallel line of development (we'll explore this deeply in Module 2)
- **Remote**: A copy of the repository hosted on a server (like Bitbucket)

### Essential Commands

```cmd
# Start a new repository
git init

# Copy an existing repository
git clone <repository-url>

# Check status of changes
git status

# Stage changes for commit
git add <file>     # Add specific file
git add .          # Add all changes

# Commit staged changes
git commit -m "Descriptive message"

# View commit history
git log

# Push changes to remote repository
git push origin main

# Get latest changes
git pull origin main
```

### Hands-On Exercise: Creating Your First Repository

1. **Setup**: Install Git if needed and configure with:

   ```cmd
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

2. **Create a repository**:

   ```cmd
   mkdir my-first-repo
   cd my-first-repo
   git init
   ```

3. **Create and track files**:

   ```cmd
   echo "# My Project" > README.md
   git status                    # See untracked file
   git add README.md             # Stage file
   git commit -m "Initial commit with README"  # Commit file
   ```

4. **Make changes**:

   ```bash
   # Edit README.md to add more content
   git diff                      # See what changed
   git add README.md
   git commit -m "Update README with project description"
   ```

5. **Connect to Bitbucket**:
   - Create a new repository on Bitbucket
   - Follow Bitbucket's instructions to add a remote
   - Push your local repository:
  
   ```bash
     git remote add origin https://bitbucket.org/username/repo-name.git
     git push -u origin main
   ```

### A Typical Git Workflow

When working on a new feature, you might follow this pattern[^2]:

1. Create and switch to a new branch: `git checkout -b feature/login-page`
2. Work on code, periodically using `git status` to check changes
3. Stage the changes: `git add .` (or specific files)
4. Commit the changes: `git commit -m "Add login page UI and form"`
5. Repeat editing and committing as needed
6. Push the branch to Bitbucket: `git push -u origin feature/login-page`
7. Open a pull request on Bitbucket to merge your changes

[^2]: [Git Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows#:~:text=Once%20John%20finishes%20his%20feature%2C,git%20push%20command%2C%20like%20so)

### Best Practices

1. **Commit frequently** with meaningful, descriptive messages
2. **Pull before pushing** to integrate others' changes
3. **Use .gitignore** to exclude files that shouldn't be tracked (build artifacts, sensitive info)
4. **Never commit sensitive data** like passwords or API keys

---

## 🎮 Bonus: Gamified Learning Resources

- [Learn Git Branching (Interactive Game)](https://learngitbranching.js.org/)
- [Oh My Git! – Visual Git Card Game (GitHub)](https://github.com/git-learning-game/oh-my-git)
- [Git Koans: Practice Git via puzzles](https://github.com/mbostock/git-koans)
