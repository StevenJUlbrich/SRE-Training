# 🌿 Module 2: Branching Strategies (Days 3-4)

## 🎯 Learning Objectives

By the end of this module, participants will be able to:

- Understand how branches isolate work and enable parallel development
- Compare and contrast popular branching strategies and their use cases
- Implement effective branch management for different workflows
- Choose the appropriate strategy based on team size and release cadence
- Visualize branching and merging with commit graphs
- Identify, prevent, and resolve common branching issues

---

## 📖 1. Branch Fundamentals: What is a Git Branch?

A **branch** in Git is simply a movable pointer to a commit. It allows developers to isolate work, experiment freely, and merge changes when ready — without affecting the stable code.

### Key Branch Types

| Branch Type | Purpose |
|-------------|---------|
| `main` (or `master`) | Production-ready code (default branch) |
| `feature/*` | For working on individual features |
| `release/*` | For testing and stabilizing before deployment |
| `hotfix/*` | For urgent fixes directly off `main` |
| `develop` | Used in GitFlow to aggregate feature work |

---

## 🤔 2. Why Branching Matters for SRE and DevOps Teams

Branching strategies enable SRE and DevOps teams to:

- Work on bug fixes or configuration updates in isolation
- Deploy changes in phases (staging → production)
- Safely rollback or audit changes by preserving history
- Collaborate asynchronously while reducing merge conflicts
- Maintain production stability while developing new features

---

## 🧠 3. Git Branching Visualization

Understanding Git's branch and commit structure is easier with a visual model:

```text
main
●──A──●──B──●──E──●──G ← main (HEAD)
      \        \      /
feature1        ●──D
        \              \
         ●──C ← feature2
```

- Each `●` represents a commit
- Branches (`main`, `feature1`, `feature2`) are pointers to specific commits
- Working on different branches allows parallel development
- Merging brings changes from one branch into another

---

## 🔍 4. Popular Branching Strategies

### 🔹 Feature Branching

In feature branching, each new feature or bug fix is developed in its own dedicated branch. This isolates work until it's ready to be integrated[^1].

[^1]: [Git Feature Branch Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)

**Workflow**:

1. Create a branch from main for your feature: `git checkout -b feature/login-page`
2. Make changes, commit frequently
3. Push branch to remote: `git push -u origin feature/login-page`
4. Create a pull request to merge into main
5. After review and approval, merge and delete the feature branch

**Pros**: 
- Simple to understand and implement
- Isolates work effectively
- Good for teams of any size
- Flexible and minimizes disruption

**Cons**: 
- Frequent integration needed to avoid drift
- Potential for merge conflicts with long-lived branches

---

### 🔹 GitFlow

GitFlow is a more structured model with multiple branch types for different purposes, introduced by Vincent Driessen in 2010[^2].

[^2]: [Gitflow Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

**Branch Types**:

- `main`: Holds production-ready code
- `develop`: Integration branch for features
- `feature/*`: Individual feature development
- `release/*`: Preparing releases
- `hotfix/*`: Urgent fixes for production

```text
main      ----A---------E------------------G (releases)
               \       /           /
develop         B----C----D------F (features)
```

**Workflow**:

1. Feature development happens on branches from `develop`
2. Completed features merge back to `develop`
3. Release branches fork from `develop` when ready
4. Releases merge to both `main` (with version tag) and back to `develop`
5. Hotfixes branch from `main` and merge to both `main` and `develop`

**Pros**: 
- Well-structured for formal release cycles
- Clear roles for different branch types
- Supports parallel development
- Good for regulatory compliance and audit trails

**Cons**: 
- Complex for small teams or rapid deployment
- Can slow down continuous integration
- Overhead for simple projects

Many modern DevOps teams have moved away from GitFlow in favor of simpler, trunk-based approaches due to its complexity potentially hindering continuous integration and delivery[^3].

[^3]: [Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/)

---

### 🔹 Trunk-Based Development

Trunk-based development emphasizes frequent integration directly to the main branch[^4].

[^4]: [Trunk-based Development | Atlassian](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development)

**Workflow**:

1. Make small, frequent commits directly to main, or
2. Use very short-lived feature branches (hours or 1-2 days)
3. Use feature flags to disable incomplete features in production
4. Rely heavily on automated tests and CI/CD

**Pros**: 
- Promotes continuous integration
- Reduces merge conflicts
- Simpler history and workflow
- Excellent for CI/CD pipelines
- Faster feedback cycles

**Cons**: 
- Requires discipline and excellent test coverage
- May not suit all projects
- Higher risk without proper testing

Trunk-based development is particularly CI/CD friendly and recommended for achieving continuous integration and delivery.

---

## 📚 5. Real-World Case Study

### Enterprise Environment (Finance Sector)

A financial services firm experienced frequent downtime due to large, infrequent deployments. By implementing GitFlow, the firm:

- Established clear and predictable release cycles
- Reduced deployment failures by 40%
- Improved audit trails and regulatory compliance
- Created clear separation between development and production code

This case demonstrates how a more structured branching strategy can provide benefits in environments with strict compliance requirements. However, different organizations might benefit from different approaches based on their team size, release cadence, and regulatory environment.

---

## 🛠️ 6. Hands-On Lab – Exploring Branching Strategies

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

> Complete the workflow by creating a pull request to merge into `main`.

---

### Scenario B: GitFlow Simulation

```bash
# 1. Create develop branch from main
git checkout main
git checkout -b develop
git push -u origin develop

# 2. Start a feature
git checkout -b feature/user-login develop
# ... work ...
git commit -am "Create login feature"
git push -u origin feature/user-login

# 3. Merge into develop
git checkout develop
git merge --no-ff feature/user-login -m "Merge feature/user-login"

# 4. Start release
git checkout -b release/1.0 develop
# Test and stabilize...

# 5. Merge release to main + tag
git checkout main
git merge --no-ff release/1.0 -m "Release 1.0"
git tag -a v1.0 -m "Version 1.0"

# 6. Merge release back to develop
git checkout develop
git merge --no-ff release/1.0 -m "Merge release back to develop"
```

---

### Scenario C: Trunk-Based Development

```bash
# Work on a small, focused task
git checkout main
git pull origin main
git checkout -b fix/button-color

# Make change and commit
git commit -am "Fix button color"
git push -u origin fix/button-color

# Create PR, review, and merge ASAP
# The goal is to get this into main within hours, not days
```

---

## ⚠️ 7. Common Pitfalls & Troubleshooting

| Pitfall | How to Avoid or Fix |
|---------|---------------------|
| **Long-lived feature branches** | Merge or rebase with `main` frequently |
| **Direct commits to `main`** | Use branch protection rules and pull requests |
| **Poor branch naming** | Follow conventions: `feature/`, `bugfix/`, `hotfix/` |
| **Merging without testing** | Always test locally and via CI before merging |
| **"Non-fast-forward" error** | Pull latest changes before pushing |
| **Merge conflicts** | Resolve manually or use `git mergetool` |
| **Accidentally deleted branch** | Recover with `git reflog` if local |
| **Permission issues** | Check repository branch restrictions |

---

## 📋 8. Choosing the Right Strategy

Consider these factors when selecting a branching strategy:

- **Team size and experience**: Larger teams often need more structure
- **Release frequency**: Frequent releases favor simpler strategies
- **Project complexity**: Complex projects may need more formal branching
- **Deployment requirements**: Continuous deployment works well with trunk-based
- **Testing infrastructure**: Strong automated testing enables trunk-based
- **Regulatory requirements**: Regulated industries may benefit from GitFlow's structure

**Decision Matrix:**

| Factor | Feature Branching | GitFlow | Trunk-Based |
|--------|-------------------|---------|-------------|
| Team Size | Any size | Medium to large | Any size with good practices |
| Release Cadence | Flexible | Scheduled releases | Continuous |
| CI/CD Maturity | Basic | Intermediate | Advanced |
| Testing | Good | Good | Extensive |
| Regulation | Basic | Strong | Requires additional controls |

---

## ✅ 9. Knowledge Check (Mini Quiz)

**Q1:** What is the main difference between GitFlow and trunk-based development?

**Q2:** Which branching strategy is best for teams deploying several times per day?

**Q3:** In GitFlow, what branch is used for feature integration before release?

**Q4:** What command creates and switches to a new branch?

**Q5:** How can you avoid merge conflicts in long-running feature branches?

### 💡 Open-Ended Task

Create a feature branch. Make 2 commits. Simulate a pull request into `main`. Try to merge it. Then delete the branch locally and remotely. Document what you observe about the commit history.

---

## 📌 10. Best Practices

1. **Use descriptive branch names** with prefixes: `feature/`, `bugfix/`, `hotfix/`, etc.
2. **Delete branches after merging** to keep the repository clean
3. **Regularly update feature branches** with changes from main
4. **Keep branches focused** on a single task or feature
5. **Document your team's branching strategy** for consistency
6. **Use pull requests** for code review even in small teams
7. **Automate testing** on branches before merging
8. **Keep branches short-lived** whenever possible
9. **Regularly clean up old branches** with `git fetch --prune`
10. **Avoid rebasing public branches** that others may be using

---

## 🧠 11. Advanced Learner Challenge

- Rebase a feature branch onto `main` and resolve any conflicts
- Visualize the commit tree with: `git log --oneline --graph --all`
- Try `git cherry-pick` to apply a commit from one branch to another
- Implement Git hooks to enforce branch naming standards
- Create a CI/CD pipeline that automatically builds and tests new branches

---

## 📗 12. FAQ

**Q:** How often should I merge from main into my feature branch?  
**A:** At least daily, or whenever significant changes are made to main.

**Q:** When should I delete a branch?  
**A:** Delete branches after they're merged and no longer active.

**Q:** Can I recover a deleted branch?  
**A:** Yes, using `git reflog` if it was local. Remote branches can be recovered by administrators.

**Q:** Should I use merge or rebase to update my feature branch?  
**A:** It depends on your team's workflow. Rebase creates a cleaner history but should not be used on public branches.

**Q:** How do I enforce branch naming conventions?  
**A:** Use Git hooks or branch protection rules in your hosting service.

---

## 🎮 13. Bonus: Gamified Learning Resources

- [Learn Git Branching (Interactive Game)](https://learngitbranching.js.org/)
- [Oh My Git! – Visual Git Card Game](https://github.com/git-learning-game/oh-my-git)
- [Git Graph VS Code Extension](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- [Git Koans: Practice Git via puzzles](https://github.com/mbostock/git-koans)