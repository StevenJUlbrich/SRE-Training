# 🔧 Module 6: Advanced Git Techniques – Comprehensive SRE Workshop

---

## 🎯 Learning Objectives

By the end of this module, participants will:

- Master advanced Git concepts including rebasing, cherry-picking, and stashing.
- Understand and manipulate Git internals for troubleshooting and optimization.
- Implement Git hooks and automation to streamline workflows.
- Manage large repositories effectively using Git LFS.

---

## 📖 Core Concept Breakdown: Advanced Git Techniques

### Key Advanced Concepts:

| Technique       | Description                                                  |
|-----------------|--------------------------------------------------------------|
| **Git Rebase**  | Rewriting commit history for cleaner, linear project history |
| **Cherry-pick** | Applying specific commits from one branch to another         |
| **Git Stash**   | Temporarily saving changes without committing                |
| **Git LFS**     | Managing large files efficiently in repositories             |

---

## 📚 Real-World Context: Case Study

### Scenario: Large-scale Development Team

A large development team struggled with complex and disorganized commit histories, leading to confusion and mistakes. By adopting advanced Git practices:

- Commit histories became clear and manageable.
- The team streamlined patch deployments via cherry-picking.
- Improved handling of large files significantly increased repo performance.

---

## 📋 Practical Code Examples: Advanced Git Operations

### Hands-On Exercise: Git Rebase

```bash
# Start interactive rebase

git checkout feature-branch
git rebase -i main

# Follow prompts to reorder, squash, or edit commits
```

### Hands-On Exercise: Cherry-picking

```bash
# Cherry-pick a commit from another branch

git checkout target-branch
git cherry-pick <commit-hash>
```

### Hands-On Exercise: Git Stash

```bash
# Temporarily stash changes
git stash save "Work in progress on login feature"

# Restore stashed changes
git stash pop
```

---

## 🎨 Visualization Support: Git Rebase vs Merge

```ascii
Before Rebase:
main:      A---B---C
feature:         \---D---E

After Rebase (linear history):
main:      A---B---C---D---E
```

---

## 🎯 Implementation Reasoning

- **Clean History:** Simplifies code reviews, debugging, and tracking changes.
- **Selective Integration:** Cherry-picking enables selective deployment of changes.
- **Productivity:** Git stash improves developer productivity and workflow flexibility.

---

## 🚧 Common Pitfalls

| Pitfall                          | Mitigation Strategy                                 |
|----------------------------------|-----------------------------------------------------|
| Misusing rebase on shared branch | Restrict rebasing to local branches only            |
| Forgetting stashed changes       | Regularly check stash list (`git stash list`)       |
| Poor handling of large files     | Implement Git LFS for efficient management          |

---

## 🎓 Interactive Elements

**Mini-Quiz:**
- What's the main difference between rebasing and merging?
- How would you retrieve a specific stashed change?

**Scenario:**
- Simulate a complex rebase scenario requiring conflict resolution.

---

## 📈 Performance Optimization

- Regularly clean up repository history with rebase and squash commits.
- Use Git LFS for efficient storage and management of large binaries.

---

## 🔧 Troubleshooting Guide

| Issue                                   | Resolution                                         |
|-----------------------------------------|----------------------------------------------------|
| Rebase conflicts                        | Resolve conflicts manually, stage and continue rebase |
| Incorrect cherry-picked commit          | Use `git revert` or reset to remove unwanted commit|
| Lost changes after stash operations     | Check `git stash list` and recover from there      |

---

## ✅ Module Summary: Key Takeaways

- Advanced Git operations enhance clarity, manageability, and workflow efficiency.
- Rebasing keeps commit history clean and linear.
- Cherry-picking enables targeted, precise changes.

---

## 🚀 Advanced Challenges

- Write a custom pre-commit Git hook that runs automated tests.
- Create and manage large binary files using Git LFS.
- Implement complex cherry-pick scenarios involving multiple branches.

---

## 📗 FAQ

**Q:** When should I avoid rebasing?
**A:** Avoid rebasing on shared branches that other developers rely on.

**Q:** How can I efficiently manage large files in Git?
**A:** Implement Git LFS to store large binary files efficiently.

---

## 📚 Recommended Additional Resources

- [Git Rebase Documentation](https://git-scm.com/docs/git-rebase)
- [Git LFS Tutorial](https://git-lfs.com/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)

