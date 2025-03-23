# 🤝 Module 4: Bitbucket Collaboration & Code Reviews (Days 7-8)

## 🎯 Learning Objectives

By the end of this module, participants will be able to:

- Master pull request workflows for code review and collaboration
- Configure repository permissions and branch protection
- Integrate Bitbucket with Jira for ticket management
- Implement effective code review practices
- Avoid common pitfalls in the collaboration process
- Use Bitbucket's features to enhance team productivity

---

## 📖 1. Pull Request Fundamentals

### What Are Pull Requests?

Pull requests (PRs) are Bitbucket's core mechanism for code review and collaboration. They provide a dedicated place to discuss changes before integrating them into the main codebase[^1].

[^1]: [Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request)

A pull request offers:
- A **visual diff** of all code changes
- A **discussion thread** for review comments
- **Approval gates** before merging
- Integration with **CI pipelines** and **Jira issues**
- **History tracking** of the review process

---

## 🤔 2. Why PRs Matter for SRE & DevOps Teams

As an SRE or production support engineer, pull requests help you:

- Ensure **code changes tied to incident fixes** can be reviewed and rolled back easily
- Maintain **production stability** and reduce risky merges
- Enforce **peer accountability** and consistent standards
- Provide **audit trails** for compliance and production changes
- Keep **infrastructure changes** safe through review

---

## 📚 3. Real-World Case Study

### Software Development Team Scenario

A software engineering team consistently faced issues due to uncontrolled merges into the main branch. After implementing structured pull request workflows and branch protections in Bitbucket, the team:

- Reduced production incidents by 60%
- Cut time-to-recovery during incidents
- Improved deployment reliability and reduced downtime
- Enhanced collaboration and accountability through peer reviews
- Streamlined issue tracking and project management via Jira integration

The key improvements included requiring reviews, automating testing, and enforcing branch protection rules.

---

## 🧠 4. Pull Request Workflow Visualization

```text
Feature branch pushed → PR created → Review & approve → Merge to main

feature/JIRA-456
   ●──A──B──C ← PR opened
               \
main            ●──D ← review, approval, merge
```

---

## 🔍 5. Creating a Pull Request

### Step-by-Step Process

1. Push your branch to Bitbucket: `git push -u origin feature/new-feature`
2. In Bitbucket, navigate to your repository
3. Click "Create pull request" and select your source branch and target branch
4. Add a descriptive title and details about your changes
5. Assign reviewers and submit

The general process is: branch → push → pull request → review/discuss → refine → merge and close[^2].

[^2]: [Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request)

### Writing Effective PR Descriptions

A good pull request description should include:

- **What** changes were made
- **Why** the changes were needed
- **How** the changes accomplish the goal
- Any **testing** performed
- **Related issues** or tickets
- Potential **side effects** or areas needing special attention

---

## 🛠️ 6. Hands-On Lab – Create & Review a PR

### A. Setup a Repo and Feature Branch

```bash
# Clone the repository
git clone https://bitbucket.org/yourname/project.git
cd project

# Create a feature branch
git checkout -b feature/JIRA-123-add-logging

# Make changes to files
# ...

# Commit the changes with a Jira reference
git add .
git commit -m "JIRA-123: Add structured logging to core module"

# Push the branch to Bitbucket
git push -u origin feature/JIRA-123-add-logging
```

### B. Create a PR on Bitbucket

1. Go to the repo in Bitbucket
2. Click **Create Pull Request**
3. Choose:
   - Source: `feature/JIRA-123-add-logging`
   - Destination: `main`
4. Add a descriptive title and link a Jira ticket
5. Assign reviewers
6. Add labels if applicable

### C. Review Workflow

As a reviewer:
1. Review the diff to understand changes
2. Comment on specific lines with questions or suggestions
3. Approve, request changes, or decline the PR
4. Look for issues like:
   - Code correctness and logic
   - Test coverage
   - Security concerns
   - Performance implications
   - Adherence to standards

---

## 🔐 7. Repository & Branch Permissions

Bitbucket lets you control access at repository and branch levels to protect your code.

### Repository Permissions

- **Admin**: Full control, can change settings
- **Write**: Can push branches and create PRs
- **Read**: Can clone and view code only

### Branch Permissions

Configure under Repository settings > Branch permissions[^3]:

[^3]: [Use branch permissions | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/)

| Rule | Benefit |
|------|---------|
| **Require pull requests** | Prevent direct pushes to protected branches |
| **Require approvals** | Set minimum number of reviewers |
| **Require successful builds** | Ensure CI passes before merging |
| **Restrict who can merge** | Limit merging to specific users/groups |

Example protection for main branch:
- No direct pushes (require PR)
- 1+ approvals required
- CI must pass
- Only project leads can execute merges

Branch permissions help enforce workflows and prevent mistakes, like a new developer accidentally deleting or force-pushing to the main branch.

---

## 🔄 8. Jira Integration

Bitbucket integrates with Jira to connect code and tickets, providing full traceability between issues and code changes.

### Setting Up Integration

1. Go to Jira > Project Settings > DVCS accounts
2. Link your Bitbucket repository
3. Grant appropriate permissions

### Naming & Linking Standards

| Action | Example | Purpose |
|--------|---------|---------|
| Branch name | `feature/JIRA-123-add-login-ui` | Automatic linking |
| Commit message | `JIRA-123: Add login UI and form validation` | Shows in issue activity |
| PR title | `JIRA-123: Implement Login Flow` | Links PR to issue |

### Smart Commits

Use special syntax in commit messages to update Jira directly[^4]:

[^4]: [Use Smart Commits | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-smart-commits/)

```
JIRA-123 #comment Implemented login UI #time 2h #resolve
```

This would:
- Add a comment to the issue
- Log 2 hours of work
- Resolve the issue

### Benefits

- See all related code activity directly in Jira
- Track which issues are in development, ready for review, or deployed
- Automatically transition issues based on code activity
- Create development reports and metrics

---

## ⚠️ 9. Common Mistakes & How to Avoid Them

| Mistake | Fix |
|---------|-----|
| **Merging without review** | Set branch permissions to require approval |
| **Missing issue traceability** | Always use Jira issue key in branch/commit/PR |
| **Giant PRs hard to review** | Make small, focused branches (<400 lines changed) |
| **Ignoring failed pipelines** | Block merges unless CI passes |
| **Leaving PR comments unaddressed** | Enforce addressing all comments before merge |
| **Direct commits to main** | Configure branch protection to require PRs |

---

## 🧯 10. Troubleshooting Tips

| Problem | Solution |
|---------|----------|
| **Can't push to `main`** | Likely blocked by branch permissions |
| **No Jira links showing** | Confirm correct issue key and linked account |
| **Reviewer can't approve** | Check Bitbucket permissions: needs "Write" access |
| **PR blocked by failed pipeline** | Fix tests or use re-run button after correction |
| **Merge conflicts** | Pull latest main and resolve conflicts locally |
| **PR comments not notifying** | Check notification settings in Bitbucket |

---

## 📌 11. PR Best Practices

1. **Keep PRs focused and small** (easier to review)
2. **Write meaningful descriptions** explaining the "why" not just the "what"
3. **Link to relevant Jira issues** for context
4. **Respond to feedback** constructively and promptly
5. **Run tests before creating the PR** to avoid obvious issues
6. **Use draft PRs** for work in progress[^5]
7. **Request specific reviewers** who know the code area
8. **Check your own diff** before submitting for review
9. **Break large changes** into a series of smaller PRs
10. **Include screenshots** for UI changes

[^5]: [Draft pull requests | Bitbucket Data Center | Atlassian Documentation](https://confluence.atlassian.com/display/BitbucketServer/Draft+pull+requests)

---

## ✅ 12. Knowledge Check (Mini Quiz)

**Q1:** What's the primary benefit of a pull request in Bitbucket?

**Q2:** How can you ensure a PR is linked to a Jira issue?

**Q3:** Where do you set rules like "no direct push to `main`"?

**Q4:** What does a Smart Commit with `#time 3h #comment Fixed bug #resolve` do?

**Q5:** What branch permission setting prevents direct pushes to main?

### 💡 Open-Ended Task

Create a feature branch with a Jira issue key in the name, make changes, push code, open a PR, and link it to a Jira issue. Ask a colleague to review it, respond to their feedback, and merge it after approval.

---

## 📗 13. FAQ

**Q:** How many reviewers should I assign to a PR?  
**A:** Typically 1-2 reviewers is optimal. More can slow down the process without adding proportional value.

**Q:** How do I ensure all PRs meet code quality standards?  
**A:** Use Bitbucket merge checks to enforce approvals, CI passing, and code coverage thresholds.

**Q:** Can I automatically transition Jira issues when PRs are merged?  
**A:** Yes, use smart commits in your PR and commit messages with keywords like `#resolve`.

**Q:** When should I use a Draft PR?  
**A:** Use draft PRs for work-in-progress that needs early feedback but isn't ready for final review.

**Q:** Is there a way to enforce PR templates?  
**A:** Yes, Bitbucket supports default description templates for PRs.

---

## 🧠 14. Advanced Learner Challenges

- Create a **PR template** using Bitbucket's default PR description feature
- Setup **merge checks** (approval + passing CI + task list completion)
- Configure **auto-merge** for PRs that meet all requirements
- Create **custom workflows** in Jira that integrate with Bitbucket
- Set up **code owners** for automatic reviewer assignment
- Create branch-specific **CI/CD pipelines**

---

## 🎮 15. Bonus: Resources & Additional Learning

- [Atlassian's Bitbucket Pull Request Guide](https://support.atlassian.com/bitbucket-cloud/docs/pull-requests/)
- [Jira and Bitbucket Integration Setup](https://support.atlassian.com/jira-software-cloud/docs/integrate-with-bitbucket/)
- [Bitbucket Branch Permissions](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/)
- [Smart Commits Documentation](https://support.atlassian.com/bitbucket-cloud/docs/use-smart-commits/)
- [Code Review Best Practices](https://www.atlassian.com/blog/add-ons/code-review-best-practices)