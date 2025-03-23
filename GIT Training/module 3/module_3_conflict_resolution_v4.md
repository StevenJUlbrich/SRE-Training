# 🔀 Module 3: Conflict Resolution (Days 5-6)

## 🎯 Learning Objectives

By the end of this module, participants will be able to:

- Understand why and how merge conflicts occur
- Develop strategies to minimize conflicts
- Master techniques for resolving conflicts when they arise
- Compare merging and rebasing approaches
- Use practical tools to visualize and manage conflicts effectively
- Apply best practices to reduce conflict frequency

---

## 📖 1. Understanding Merge Conflicts

### What Causes a Merge Conflict?

A merge conflict occurs when Git cannot automatically reconcile differences between branches. This typically happens when[^1]:

[^1]: [Resolving a merge conflict using the command line - GitHub Docs](https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line)

1. **Same line conflicts**: Two branches modify the same lines differently
2. **Delete vs. modify**: One branch deletes a file another branch modified
3. **Complex structural changes**: Overlapping changes that can't be automatically merged

Git cannot decide which version to keep, so it pauses and asks **you** to resolve it.

---

### Visualizing Conflicts

```text
          (Edit same file)
main:     ●──A──B──C
                   \
feature:            ●──D──E (conflicts with B)

Attempt: git merge feature → CONFLICT
```

When two branches make different changes to the same lines in a file, Git cannot automatically determine which changes should be kept.

---

## 🔍 2. Conflict Markers Explained

When Git encounters a conflict, it inserts markers in the affected files[^2]:

[^2]: [How to resolve merge conflicts in Git](https://graphite.dev/guides/how-to-resolve-merge-conflicts-in-git)

```diff
<<<<<<< HEAD
Your changes (current branch)
=======
Their changes (branch being merged)
>>>>>>> branch-name
```

Your task is to edit these files, decide on the final content, and remove the markers.

---

## 🤔 3. Why This Matters in Real Projects

As an SRE or DevOps engineer, conflicts can:

- Disrupt CI/CD pipelines
- Delay critical deployments
- Cause regressions if resolved incorrectly
- Block important security patches

Understanding conflict resolution helps you:
- Respond to failed PRs quickly
- Resolve config and YAML file conflicts cleanly
- Choose merge vs rebase appropriately based on context
- Keep production infrastructure changes flowing smoothly

---

## 📚 4. Real-World Case Study

### Software Development Team Scenario

A development team faced frequent delays due to merge conflicts in shared configuration files. After adopting structured conflict resolution strategies, the team:

- Reduced integration issues by 60%
- Improved collaboration and development velocity
- Enhanced the stability of their software releases
- Decreased time spent resolving conflicts by 75%

The key improvements included:
- Better communication about who was editing which files
- More frequent integration of changes
- Using tools to visualize conflicts
- Establishing clear resolution procedures

---

## 🛠️ 5. Resolution Process: Step by Step

1. **Identify conflicted files**: Use `git status` to see which files are in conflict
2. **Understand both changes**: Review the conflict markers to understand both versions
3. **Decide on resolution**: Choose one version, combine them, or rewrite as needed
4. **Remove conflict markers**: Edit the file to contain only the final content
5. **Mark as resolved**: Use `git add <file>` to stage the resolved file
6. **Complete the merge**: Run `git commit` to finalize (or `git rebase --continue` if rebasing)
7. **Test the result**: Ensure your code still works after resolution

---

## 🧠 6. Hands-On Lab – Simulate and Resolve a Conflict

### Setting Up a Conflict Scenario

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

### Resolving the Conflict

1. Open `config.txt` in your editor. You'll see:

```
<<<<<<< HEAD
timeout = 60
=======
timeout = 45
>>>>>>> feature-branch
```

2. Decide on the final value and edit the file:

```bash
# Clean up the file (choose final value)
echo "timeout = 50" > config.txt

# Stage and commit
git add config.txt
git commit -m "Resolve merge conflict on timeout setting"
```

---

## 🔄 7. Merge vs. Rebase: Understanding the Difference

Both `git merge` and `git rebase` can cause conflicts, but they approach integration differently:

| Git Operation | Description | Pros | Caution |
|---------------|-------------|------|---------|
| `git merge` | Creates a new commit combining changes from both branches | - Preserves complete history<br>- Branch structure remains visible<br>- Non-destructive operation | - Creates "merge bubbles" in history<br>- Can make history harder to follow |
| `git rebase` | Replays your commits on top of the target branch | - Creates linear, clean history<br>- Easier to follow chronology<br>- Cleaner project history | - Rewrites commit history<br>- Dangerous on shared branches<br>- More complex conflict resolution |

### When to Use Each Approach

**Choose Merge When:**
- Working on a shared branch 
- The branch structure is important to preserve
- You want to maintain the exact chronology of work

**Choose Rebase When:**
- Working on a personal feature branch
- You want a clean, linear history before sharing
- You want to incorporate the latest changes from the main branch

---

## ⚠️ 8. Common Pitfalls & Troubleshooting

| Pitfall | How to Avoid or Fix |
|---------|---------------------|
| **Committing unresolved markers** | Always review files before committing (`git diff --cached`) |
| **Rebasing shared branches** | Only rebase branches that haven't been pushed yet |
| **Not testing after resolution** | Always run tests after resolving conflicts |
| **Choosing wrong version** | Use visual diff tools when unsure |
| **Leaving conflict markers in code** | Use `git diff` to check for markers before committing |
| **Cancel merge in progress** | Use `git merge --abort` to start over |
| **Dealing with binary files** | Use `git checkout --ours <file>` or `--theirs` |

---

## 🧯 9. Tools to Make Conflict Resolution Easier

### Command Line Tools

- **`git diff`**: Show differences between conflicting versions
- **`git checkout --ours <file>`**: Use version from current branch
- **`git checkout --theirs <file>`**: Use version from merging branch
- **`git mergetool`**: Launch configured visual merge tool

### Visual Tools

1. **Visual editors**: VS Code, IntelliJ, etc. have built-in conflict resolution
2. **Git GUI clients**: GitKraken, Sourcetree show visual diffs
3. **Merge strategies**: For specific cases, try `git merge -X ours <branch>` to favor current branch changes[^3]

[^3]: [Git Merge Theirs Explained - Built In](https://builtin.com/articles/git-merge-theirs)

---

## 📌 10. Minimizing Conflicts: Best Practices

Prevention is better than cure:

1. **Communicate with your team** about who works on what
2. **Pull changes frequently** to stay in sync[^4]
3. **Keep branches short-lived** to reduce divergence
4. **Make smaller, focused commits** to reduce conflict surface area
5. **Structure code to minimize overlap** between team members
6. **Agree on code formatting** to avoid style-based conflicts
7. **Use feature flags** instead of long-running branches
8. **Set up Git hooks** to enforce formatting rules

[^4]: [Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/)

---

## ✅ 11. Knowledge Check (Mini Quiz)

**Q1:** What markers does Git use to identify conflicts in a file?

**Q2:** Which command do you use to cancel a problematic merge?

**Q3:** What does `git rebase` do differently from `git merge`?

**Q4:** How do you tell Git that you've resolved a conflict in a file?

**Q5:** When should you NOT use rebasing as a conflict resolution strategy?

### 💡 Open-Ended Task

Simulate a conflict with two branches editing the same YAML file. Practice resolving it using both manual editing and `git mergetool`.

---

## 📗 12. FAQ

**Q:** Can merge conflicts be completely avoided?  
**A:** Not entirely, but regular integration greatly reduces their frequency.

**Q:** What's the difference between `git merge --abort` and `git reset --hard`?  
**A:** `merge --abort` cleanly cancels an in-progress merge, while `reset --hard` can discard changes beyond the merge.

**Q:** How to recover from a wrongly resolved conflict?  
**A:** Use `git reflog` to find the commit before the merge, then reset to it.

**Q:** Should I always use a visual tool for conflicts?  
**A:** For simple conflicts, manual editing can be faster. For complex ones, visual tools help prevent mistakes.

**Q:** What if I can't resolve a conflict myself?  
**A:** Involve the team members who made the conflicting changes to ensure the correct solution.

---

## 🧠 13. Advanced Learner Challenge

- Use `git rebase -i` to squash commits before merging to reduce conflicts
- Explore `git rerere` for automatic conflict resolution reuse
- Try `git cherry-pick` and resolve if it causes a conflict
- Create a `.gitattributes` file to set merge strategies per file type
- Experiment with `git merge --strategy=recursive -X patience` for improved merges

---

## 🎮 14. Bonus: Gamified Learning Resources

- [Visual Merge Conflict Practice](https://learngitbranching.js.org/?demo=merge-conflict)
- [Git Merge Theirs / Ours Strategy](https://builtin.com/software-engineering-perspectives/git-merge-theirs)
- [Git Tower Conflict Resolution Guide](https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/merge-conflicts)
- [Oh My Git! Conflict Scenarios](https://github.com/git-learning-game/oh-my-git)