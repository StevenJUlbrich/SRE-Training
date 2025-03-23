# 🤝 Module 4: Bitbucket Collaboration & Code Reviews – Comprehensive SRE Workshop

---

## 🎯 Learning Objectives

By the end of this module, participants will:

- Master Bitbucket pull request workflows for efficient code reviews and collaboration.
- Configure repository and branch permissions effectively to protect critical code.
- Leverage Bitbucket integration with Jira for seamless ticket management.
- Implement best practices for code reviews and team collaboration.
- Avoid common pitfalls in the collaboration process.

---

## 📖 Core Concept Breakdown: Understanding Pull Requests

### What is a Pull Request?

A **Pull Request (PR)** in Bitbucket is a structured way to review and discuss code changes before integrating them into the main branch. It serves as a collaborative hub where code modifications are clearly visible, discussed, tested, and approved.

### Pull Request Workflow Overview:

```ascii
Feature branch created → PR opened → Review process → Approval → Merge
```

---

## 📚 Real-World Context: Case Study

### Scenario: Software Development Team

A software engineering team consistently faced issues due to uncontrolled merges into the main branch. After implementing structured pull request workflows and branch protections in Bitbucket, the team:
- Improved deployment reliability and reduced downtime.
- Enhanced collaboration and accountability through peer reviews.
- Improved integration with Jira, streamlining issue tracking and project management.

---

## 📋 Practical Code Examples: Bitbucket Collaboration Workflow

### Hands-On Exercise: Creating and Managing Pull Requests

```bash
# Clone and set up a new feature branch
git clone https://bitbucket.org/yourrepo/project.git
cd project
git checkout -b feature/JIRA-456-logging-enhancement

# Develop feature and commit changes
git add .
git commit -m "JIRA-456: Enhance logging mechanisms"
git push -u origin feature/JIRA-456-logging-enhancement
```

### Creating a Pull Request in Bitbucket:

1. Navigate to your repository on Bitbucket.
2. Select **Create Pull Request**.
3. Choose:
   - Source: `feature/JIRA-456-logging-enhancement`
   - Destination: `main`
4. Provide a detailed title and description, including Jira ticket references.
5. Assign reviewers and submit.

---

## 🎨 Visualization Support: Pull Request Lifecycle

```ascii
feature/JIRA-456
   ●──A──B──C ← PR opened
               \
main            ●──D ← review, approval, merge
```

---

## 🎯 Implementation Reasoning

Structured pull request processes:
- Maintain high-quality code through peer reviews.
- Allow traceability and auditability for changes.
- Protect critical branches from unintended or risky changes.

---

## 🚧 Common Pitfalls

| Pitfall                                    | Mitigation Strategy                                |
|--------------------------------------------|----------------------------------------------------|
| Large, unfocused PRs                       | Create small, focused, easily reviewable PRs       |
| Missing Jira linkage                       | Always use Jira issue keys in branch/PR titles     |
| Ignoring CI/CD feedback                    | Enforce merge restrictions based on CI/CD results  |
| Direct commits to protected branches       | Use strict branch permissions to enforce PR reviews|

---

## 🎓 Interactive Elements

**Mini-Quiz:**
- What is the main benefit of using pull requests?
- How can Jira integration benefit your workflow?

**Scenario:**
- Create a pull request linked to a Jira ticket, review it with your peers, respond to feedback, and merge upon approval.

---

## 📈 Performance Optimization

- Regularly update your branch from `main` to minimize merge conflicts.
- Use Bitbucket's automated merge checks and pipelines for robust code integration.

---

## 🔧 Troubleshooting Guide

| Issue                                     | Resolution                                           |
|-------------------------------------------|------------------------------------------------------|
| Cannot push directly to protected branch  | Check branch permissions; push via PR instead        |
| Jira issues not linking correctly         | Confirm correct Jira keys and integration settings   |
| Reviewer unable to approve                | Verify reviewer has necessary Bitbucket permissions  |

---

## ✅ Module Summary: Key Takeaways

- Pull requests facilitate structured reviews and safe integration.
- Branch permissions and protections are crucial for code stability.
- Jira and Bitbucket integration improves issue traceability and team collaboration.

---

## 🚀 Advanced Challenges

- Set up custom merge checks (approval requirements, successful builds).
- Automate Jira transitions using Bitbucket smart commits.
- Create and use PR templates to standardize your team's PR process.

---

## 📗 FAQ

**Q:** How do I ensure all PRs meet code quality standards?  
**A:** Use Bitbucket merge checks to enforce approvals, CI passing, and code coverage thresholds.

**Q:** Can I automatically transition Jira issues when PRs are merged?  
**A:** Yes, use smart commits in your PR and commit messages.

---

## 📚 Recommended Additional Resources

- [Atlassian's Bitbucket Pull Request Guide](https://support.atlassian.com/bitbucket-cloud/docs/pull-requests/)
- [Jira and Bitbucket Integration Setup](https://support.atlassian.com/jira-software-cloud/docs/integrate-with-bitbucket/)
- [Bitbucket Branch Permissions](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/)
