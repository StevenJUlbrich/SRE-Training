# 🔀 Module 3: Conflict Resolution – Comprehensive SRE Workshop

---

## 🎯 Learning Objectives

By the end of this module, participants will:

- Clearly understand the causes of Git merge conflicts and their implications.
- Master manual and automated conflict resolution techniques.
- Distinguish between merging and rebasing, choosing appropriate scenarios for each.
- Use practical tools to visualize and manage conflicts effectively.
- Implement best practices to proactively minimize conflicts.

---

## 📖 Core Concept Breakdown: Understanding Merge Conflicts

### What Causes a Merge Conflict?

Merge conflicts occur when:
- Two branches modify the same lines in the same file.
- One branch modifies a file while another branch deletes it.

Git cannot automatically resolve these changes and requires manual intervention.

### Example Conflict Scenario:

```ascii
main
●──A──B──C ← main
     \
      ●──D──E ← feature/login
```

Conflicts occur when merging branches with changes to identical lines or files.

---

## 📚 Real-World Context: Case Study

### Scenario: Software Development Team

A development team faced frequent delays due to merge conflicts in shared configuration files. After adopting structured conflict resolution strategies, the team:
- Reduced integration issues significantly.
- Improved collaboration and development velocity.
- Enhanced the stability of their software releases.

---

## 📋 Practical Code Examples: Conflict Resolution Workflow

### Hands-On Exercise: Resolving Conflicts Manually

```bash
# Repository Initialization
mkdir merge-example && cd merge-example
git init
echo "max_connections = 10" > settings.conf
git add settings.conf
git commit -m "Initial configuration"

# Feature Branch

# Create and modify on feature branch
git checkout -b feature-update
echo "max_connections = 20" > settings.conf
git commit -am "Update max connections"

# Main Branch

# Switch back to main and modify differently
git checkout main
echo "max_connections = 15" > settings.conf
git commit -am "Adjust max connections on main"

# Attempt Merge
git merge feature-update
```

Resolve the conflict manually, then:

```bash
# Resolve and commit
echo "max_connections = 18" > settings.conf
git add settings.conf
git commit -m "Resolve max connections conflict"
```

---

## 🎨 Visualization Support: Merge Conflict Flow

```ascii
main:    ●──A──B──C
                  \
feature:           ●──D──E

Merge attempt → Conflict detected!
```

---

## 🎯 Implementation Reasoning

Resolving conflicts effectively:
- Maintains a clear, accurate commit history.
- Reduces disruptions during code integration.
- Enhances collaboration and productivity.

---

## 🚧 Common Pitfalls

| Pitfall                                   | Mitigation Strategy                              |
|-------------------------------------------|--------------------------------------------------|
| Committing unresolved conflict markers    | Review all files carefully before committing     |
| Rebasing shared branches                  | Use rebasing primarily for local branches        |
| Skipping post-resolution tests            | Always run tests after resolving conflicts       |

---

## 🎓 Interactive Elements

**Mini-Quiz:**
- What are Git’s conflict markers?
- When would you choose rebasing over merging?

**Scenario:**
- Create a merge conflict using simple text files and practice both manual and tool-based resolutions.

---

## 📈 Performance Optimization

- Integrate frequently to minimize conflicts.
- Utilize automated checks and visual tools to detect conflicts early.

---

## 🔧 Troubleshooting Guide

| Issue                                  | Resolution                                      |
|----------------------------------------|-------------------------------------------------|
| Leftover conflict markers after merge  | Remove markers manually and commit changes      |
| Aborting a problematic merge           | Use `git merge --abort`                         |
| Difficulty with complex merges         | Utilize visual tools (`git mergetool`, IDEs)    |

---

## ✅ Module Summary: Key Takeaways

- Merge conflicts are a natural part of version control.
- Clear strategies and tools facilitate quick resolution.
- Decide between merge or rebase based on your workflow and requirements.

---

## 🚀 Advanced Challenges

- Perform rebases involving multiple conflicting commits and resolve them.
- Implement `git rerere` to automate repetitive conflict resolutions.
- Experiment with `git cherry-pick` on conflicting commits.

---

## 📗 FAQ

**Q:** Can merge conflicts be completely avoided?  
**A:** Not entirely, but regular integration greatly reduces their frequency.

**Q:** How to recover from a wrongly resolved conflict?  
**A:** Utilize `git reflog` to revert or reset to a previous stable commit.

---

## 📚 Recommended Additional Resources

- [Interactive Conflict Resolution Practice](https://learngitbranching.js.org/?demo=merge-conflict)
- [Git Merge Conflict Resolution Guide](https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/merge-conflicts)
- [Visual Git Conflict Management Tools](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)

