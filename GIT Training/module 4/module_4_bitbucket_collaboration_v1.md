# Module 4: Bitbucket Collaboration (Days 7-8)

### Learning Objectives
- Master pull request workflows for code review
- Configure repository permissions and branch protection
- Integrate Bitbucket with Jira for ticket management
- Implement effective code review practices

### Pull Request Workflow

Pull requests (PRs) are Bitbucket's core mechanism for code review and collaboration. They provide a dedicated place to discuss changes before integrating them into the main codebase[^13].

[^13]: [Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request#:~:text=In%20their%20simplest%20form%2C%20pull,branch)

#### Creating a Pull Request

1. Push your branch to Bitbucket: `git push -u origin feature/new-feature`
2. In Bitbucket, navigate to your repository
3. Click "Create pull request" and select your source branch and target branch
4. Add a descriptive title and details about your changes
5. Assign reviewers and submit

The general process is: branch → push → pull request → review/discuss → refine → merge and close[^14].

[^14]: [Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request#:~:text=1,branch%20in%20their%20local%20repo)

#### Reviewing Code

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

#### PR Best Practices

1. **Keep PRs focused and small** (easier to review)
2. **Write meaningful descriptions** explaining the "why" not just the "what"
3. **Link to relevant Jira issues** for context
4. **Respond to feedback** constructively and promptly
5. **Run tests before creating the PR** to avoid obvious issues
6. **Use draft PRs** for work in progress[^15]

[^15]: [Draft pull requests | Bitbucket Data Center 9.6 | Atlassian Documentation](https://confluence.atlassian.com/display/BitbucketServer/Draft+pull+requests)

### Repository Permissions

Bitbucket lets you control access at repository and branch levels:

#### Repository Permissions
- **Admin**: Full control, can change settings
- **Write**: Can push branches and create PRs
- **Read**: Can clone and view code only

#### Branch Permissions
Configure under Repository settings > Branch permissions[^16]:

[^16]: [Use branch permissions | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/#:~:text=Branch%20permissions%20help%20enforce%20specific,member%20deleting%20the%20main%20branch)

1. **Require pull requests**: Prevent direct pushes to protected branches
2. **Require approvals**: Set minimum number of reviewers
3. **Require successful builds**: Ensure CI passes before merging
4. **Restrict who can merge**: Limit merging to specific users/groups

Example protection for main branch:
- No direct pushes (require PR)
- 1+ approvals required
- CI must pass
- Only project leads can execute merges

Branch permissions help enforce workflows and prevent mistakes, like a new developer accidentally deleting or force-pushing to the main branch[^17].

[^17]: [Use branch permissions | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/#:~:text=,or%20merge%20to%20any%20branch)

### Jira Integration

Bitbucket integrates with Jira to connect code and tickets:

#### Setting Up Integration
1. Go to Jira > Project Settings > DVCS accounts
2. Link your Bitbucket repository
3. Grant appropriate permissions

#### Using the Integration
1. **Branch naming**: Include the issue key in branch names:
   `feature/PROJ-123-add-login`[^18]
2. **Commit messages**: Reference issues in commits:
   `PROJ-123: Implement login form validation`[^19]
3. **PR titles**: Include issue keys:
   `PROJ-123: Add user authentication`[^20]
4. **Smart commits**: Use special syntax to update Jira:
   `PROJ-123 #comment Implemented login UI #time 2h`[^21]

[^18]: [Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Branches)
[^19]: [Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Commits)
[^20]: [Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Pull%20requests)
[^21]: [Use Smart Commits | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-smart-commits/#:~:text=When%20you%20manage%20your%20project%27s,called%20Smart%20Commits%2C%20in%C2%A0your%C2%A0commit%20messages)

#### Benefits
- See all related code activity directly in Jira
- Track which issues are in development, ready for review, or deployed
- Automatically transition issues based on code activity

For example, when you create a branch from Jira, it automatically includes the issue key in the branch name[^22].

[^22]: [Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=This%20works%20by%20default%20in,GitHub%20Enterprise%2C%20and%20Fisheye%20tools)

### Hands-On Exercise: Collaboration Workflow

1. **Create and push a feature branch**:
   ```
   git checkout -b feature/DEMO-101-new-feature
   # Make changes and commit with issue key
   git commit -m "DEMO-101: Add new feature"
   git push -u origin feature/DEMO-101-new-feature
   ```

2. **Create a pull request**:
   - In Bitbucket, create a PR with the issue key in the title
   - Add detailed description and assign reviewers

3. **Configure branch permissions**:
   - In Bitbucket, go to Repository settings > Branch permissions
   - Add a rule for the main branch to require pull requests
   - Require at least one approval

4. **Review flow**:
   - As reviewer, add comments and request changes
   - As author, push fixes to address feedback
   - Approve and merge the PR
   - Verify the Jira issue updates
