
# 🤝 Module 4: Bitbucket Collaboration & Code Reviews (Days 7–8)

## 🎯 Learning Outcomes
By the end of this module, learners will be able to:
- Use Bitbucket for pull requests, approvals, and code discussions
- Set branch permissions to protect production code
- Understand the collaborative review lifecycle
- Link commits and branches to Jira for traceability
- Avoid common review process issues

---

## 📖 1. Theory – What Are Pull Requests?

A **pull request (PR)** is a way to propose changes, get feedback, and merge code safely.

It provides:
- A **visual diff** of code changes
- A **discussion thread** for review comments
- **Approval gates** before merging
- Integration with **CI pipelines** and **Jira issues**

---

## 🤔 2. Why This Matters for SRE & DevOps Teams

- **Code changes tied to incident fixes** can be reviewed and rolled back easily
- PRs help maintain **production hygiene** and reduce risky merges
- Enforces **peer accountability** and consistent standards
- **Jira-Bitbucket integration** ensures traceability from issue to deployment

---

## 🔍 3. PR Workflow Overview

```text
Feature branch pushed → PR created → Review & approve → Merge to main
```

### Typical Flow:
1. Dev pushes code to `feature/abc`
2. Opens a PR to `main`
3. Team reviews using **inline comments**
4. CI pipeline runs (status shown on PR)
5. After approval & successful build, PR is merged

---

## 🧠 4. ASCII: Pull Request Lifecycle

```text
feature/abc
     ●──A──B──C ← PR opened
                 \
main               ●──D ← review, approval, merge
```

---

## 🛠️ 5. Hands-On Lab – Create & Review a PR

### A. Setup a Repo and Feature Branch

```bash
git clone https://bitbucket.org/yourname/project.git
cd project
git checkout -b feature/add-logging
# Make changes
git add .
git commit -m "Add structured logging to core module"
git push -u origin feature/add-logging
```

---

### B. Create a PR on Bitbucket
1. Go to the repo in Bitbucket
2. Click **Create Pull Request**
3. Choose:
   - Source: `feature/add-logging`
   - Destination: `main`
4. Add a descriptive title and link a Jira ticket (e.g., `PROJ-123`)
5. Assign 1+ reviewers

---

### C. Review Workflow
- Use the **Diff view** to examine changes
- Comment on lines with suggestions
- Once approved, click **Merge**
- Bitbucket can **delete the branch automatically**

---

## 🔐 6. Branch Permissions & Merge Rules

### Bitbucket Branch Restrictions:

| Rule                          | Benefit                       |
|-------------------------------|-------------------------------|
| Prevent direct push to `main` | Enforces PR-only workflow     |
| Require 1+ approvals          | Code must be peer-reviewed    |
| Require successful builds     | CI/CD integration safety net  |

Configure in **Repo → Settings → Branch Permissions**.

---

## 🔄 7. Jira Integration Tips

### A. Naming & Linking Standards

| Action | Example |
|--------|---------|
| Branch name | `feature/PROJ-123-add-login-ui` |
| Commit message | `PROJ-123: Add login UI and form validation` |
| PR title | `PROJ-123: Implement Login Flow` |

Jira will automatically show:
- Related branches
- Commits
- Pull requests

---

### B. Smart Commits
Use in commit messages to **transition Jira issues**:
```text
PROJ-123 #comment Added error handling #time 1h #done
```

---

## ⚠️ 8. Common Mistakes & How to Avoid Them

| Mistake | Fix |
|--------|-----|
| Merging without review | Set branch permissions to require approval |
| Missing issue traceability | Always use Jira issue key in branch/commit/PR |
| Giant PRs hard to review | Make small, focused branches |
| Ignoring failed pipelines | Block merges unless CI passes |

---

## 🧯 9. Troubleshooting Tips

| Problem | Solution |
|--------|----------|
| Can't push to `main` | Likely blocked by branch permissions |
| No Jira links showing | Confirm correct issue key and linked account |
| Reviewer can’t approve | Check Bitbucket permissions: needs “Write” access |
| PR blocked by failed pipeline | Fix tests or use re-run button after correction |

---

## ✅ 10. Knowledge Check (Mini Quiz)

**Q1:** What’s the primary benefit of a pull request in Bitbucket?  
**Q2:** How can you ensure a PR is linked to a Jira issue?  
**Q3:** Where do you set rules like “no direct push to `main`”?  

💡 **Open Task:**  
Create a feature branch, push code, open a PR, and link it to a Jira issue. Merge it after approval and CI success. Then view the Jira issue for linked activity.

---

## 📌 11. Summary / Key Takeaways

- Pull requests are the **backbone of collaborative review**
- Bitbucket integrates CI and Jira for traceable, reviewable, and testable code
- Set **permissions** to protect `main` and enforce team rules
- Always review small, focused PRs and reference **Jira tickets** clearly

---

## 🧠 12. Advanced Learner Challenges

- Create a **PR template** using Bitbucket's default PR description feature
- Setup **merge checks** (approval + passing CI + task list completion)
- Automate Jira transitions via **Smart Commits**
- Use **Draft PRs** for work-in-progress code

---

## 🎮 Bonus: Practice Tools & Integration Simulators

- [Bitbucket Pull Request Guide (Atlassian)](https://support.atlassian.com/bitbucket-cloud/docs/pull-requests/)
- [Jira + Bitbucket Dev Panel Setup](https://support.atlassian.com/jira-software-cloud/docs/integrate-with-bitbucket/)
- [Oh My Git – Pull Request Tutorial (Game)](https://ohmygit.org/)
- [GitHub vs Bitbucket PR Comparison](https://www.toolsqa.com/git/git-bitbucket/)
