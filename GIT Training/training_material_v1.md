# Comprehensive Git Training Program: From Fundamentals to Advanced Workflows

## Introduction

This training program will guide you through Git, Bitbucket collaboration, and CI/CD concepts in a structured, hands-on approach. Whether you're new to version control or looking to enhance your skills, this training offers a brick-by-brick learning experience with practical exercises.

## Program Structure

The program spans two weeks, with focused modules that build on each other:

1. **Git Fundamentals** (Days 1-2)
2. **Branching Strategies** (Days 3-4)
3. **Conflict Resolution** (Days 5-6)
4. **Bitbucket Collaboration** (Days 7-8)
5. **CI/CD Concepts** (Days 9-10)

Let's begin our journey with clear learning objectives for each module.

## Module 1: Git Fundamentals (Days 1-2)

### Learning Objectives
- Understand version control concepts and Git's distributed nature
- Master essential Git commands for daily workflows
- Create and manage repositories locally and on Bitbucket
- Track changes with effective commit practices

### Key Concepts

#### What is Git?
Git is a distributed version control system that tracks changes in files, allowing multiple developers to collaborate efficiently. Unlike centralized systems, Git gives each user a complete copy of the repository history locally[^1]. Created by Linus Torvalds in 2005 during Linux kernel development, Git has become the most popular source code management tool, with services like Bitbucket, GitHub, and GitLab providing remote hosting.

[^1]: [Git - Wikipedia](https://en.wikipedia.org/wiki/Git#:~:text=As%20with%20most%20other%20distributed,A)

#### Core Components
- **Repository (repo)**: The collection of tracked files and change history
- **Working Directory**: Your current files where you make changes
- **Staging Area (Index)**: The intermediate area where changes are prepared for committing
- **Commit**: A snapshot of your changes with a descriptive message
- **Branch**: A parallel line of development (we'll explore this deeply in Module 2)
- **Remote**: A copy of the repository hosted on a server (like Bitbucket)

#### Essential Commands

```
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
   ```
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

2. **Create a repository**:
   ```
   mkdir my-first-repo
   cd my-first-repo
   git init
   ```

3. **Create and track files**:
   ```
   echo "# My Project" > README.md
   git status                    # See untracked file
   git add README.md             # Stage file
   git commit -m "Initial commit with README"  # Commit file
   ```

4. **Make changes**:
   ```
   # Edit README.md to add more content
   git diff                      # See what changed
   git add README.md
   git commit -m "Update README with project description"
   ```

5. **Connect to Bitbucket**:
   - Create a new repository on Bitbucket
   - Follow Bitbucket's instructions to add a remote
   - Push your local repository:
     ```
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

## Module 2: Branching Strategies (Days 3-4)

### Learning Objectives
- Understand how branches isolate work and enable parallel development
- Compare popular branching strategies and their use cases
- Implement effective branch management for different workflows
- Use proper naming conventions and maintenance practices

### Key Branching Strategies

#### 1. Feature Branching
In feature branching, each new feature or bug fix is developed in its own dedicated branch. This isolates work until it's ready to be integrated[^3].

[^3]: [Git Feature Branch Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow#:~:text=The%20Feature%20Branch%20Workflow%20assumes,menu)

**Workflow**:
1. Create a branch from main for your feature: `git checkout -b feature/login-page`
2. Make changes, commit frequently
3. Push branch to remote: `git push -u origin feature/login-page`
4. Create a pull request to merge into main
5. After review and approval, merge and delete the feature branch

**Pros**: Simple to understand, isolates work, good for teams of any size
**Cons**: Frequent integration needed to avoid drift, potential for merge conflicts

#### 2. GitFlow
GitFlow is a more structured model with multiple branch types for different purposes, introduced by Vincent Driessen in 2010[^4].

[^4]: [Gitflow Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20is%20an%20alternative%20Git,can%20also%20introduce%20conflicting%20updates)

**Branch Types**:
- `main`: Holds production-ready code
- `develop`: Integration branch for features
- `feature/*`: Individual feature development
- `release/*`: Preparing releases
- `hotfix/*`: Urgent fixes for production

**Workflow**:
1. Feature development happens on branches from `develop`
2. Completed features merge back to `develop`
3. Release branches fork from `develop` when ready
4. Releases merge to both `main` (with version tag) and back to `develop`
5. Hotfixes branch from `main` and merge to both `main` and `develop`

**Pros**: Well-structured, supports release cycles, parallel development
**Cons**: Complex, can slow down rapid deployment, overhead for small teams

Many modern DevOps teams have moved away from GitFlow in favor of simpler, trunk-based approaches due to its complexity potentially hindering continuous integration and delivery[^5].

[^5]: [Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=Indeed%2C%20due%20to%20GitFlow%E2%80%99s%20complexity%2C,continuous%20integration%20and%20continuous%20delivery)

#### 3. Trunk-Based Development
Trunk-based development emphasizes frequent integration directly to the main branch[^6].

[^6]: [Trunk-based Development | Atlassian](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development#:~:text=Trunk,software%20delivery%20and%20organizational%20performance)

**Workflow**:
1. Make small, frequent commits directly to main, or
2. Use very short-lived feature branches (hours or 1-2 days)
3. Use feature flags to disable incomplete features in production
4. Rely heavily on automated tests and CI/CD

**Pros**: Promotes continuous integration, reduces merge conflicts, simpler history
**Cons**: Requires discipline and excellent test coverage, may not suit all projects

Trunk-based development is particularly CI/CD friendly and recommended for achieving continuous integration and delivery[^7].

[^7]: [Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=Consequently%2C%20trunk,CD)

### Choosing the Right Strategy

Consider these factors when selecting a branching strategy:
- Team size and experience
- Release frequency
- Project complexity
- Deployment requirements
- Testing infrastructure

For rapid development with good test coverage, trunk-based or simple feature branching often works best. For formal release cycles with multiple versions, GitFlow may be more appropriate.

### Hands-On Exercise: Branching Practice

1. **Feature Branch Workflow**:
   ```
   git checkout main
   git pull                             # Get latest main
   git checkout -b feature/new-feature  # Create feature branch
   # Make changes and commit
   git push -u origin feature/new-feature
   # Create pull request in Bitbucket
   ```

2. **GitFlow Simulation**:
   ```
   # Setup
   git checkout -b develop main
   git push -u origin develop
   
   # Feature branch
   git checkout -b feature/cool-feature develop
   # Work, commit, and push
   
   # Prepare release
   git checkout -b release/1.0 develop
   # Version bumps, final fixes
   
   # Finalize release
   git checkout main
   git merge --no-ff release/1.0 -m "Release 1.0"
   git tag -a v1.0 -m "Version 1.0"
   git checkout develop
   git merge --no-ff release/1.0 -m "Merge release back to develop"
   ```

3. **Trunk-Based Practice**:
   ```
   git checkout main
   # Make small change
   git commit -am "Add small feature behind feature flag"
   git push
   ```

### Best Practices

1. **Use descriptive branch names** with prefixes: `feature/`, `bugfix/`, `hotfix/`, etc.
2. **Delete branches after merging** to keep the repository clean[^8]
3. **Regularly update feature branches** with changes from main
4. **Keep branches focused** on a single task or feature
5. **Document your team's branching strategy** for consistency

[^8]: [Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=match%20at%20L611%20Indeed%2C%20due,continuous%20integration%20and%20continuous%20delivery)

## Module 3: Conflict Resolution (Days 5-6)

### Learning Objectives
- Understand why merge conflicts occur
- Develop strategies to minimize conflicts
- Master techniques for resolving conflicts when they arise
- Compare merging and rebasing approaches

### Understanding Conflicts

A merge conflict occurs when Git cannot automatically reconcile differences between branches. This typically happens when[^9]:

[^9]: [Resolving a merge conflict using the command line - GitHub Docs](https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line#:~:text=Merge%20conflicts%20occur%20when%20competing,information%2C%20see%20About%20merge%20conflicts)

1. **Same line conflicts**: Two branches modify the same lines differently
2. **Delete vs. modify**: One branch deletes a file another branch modified
3. **Complex structural changes**: Overlapping changes that can't be automatically merged

### Conflict Markers Explained

When Git encounters a conflict, it inserts markers in the affected files[^10]:

[^10]: [How to resolve merge conflicts in Git](https://graphite.dev/guides/how-to-resolve-merge-conflicts-in-git#:~:text=Terminal)

```
<<<<<<< HEAD
Your changes (current branch)
=======
Their changes (branch being merged)
>>>>>>> branch-name
```

Your task is to edit these files, decide on the final content, and remove the markers.

### Resolution Process

1. **Identify conflicted files**: Use `git status` to see which files are in conflict
2. **Understand both changes**: Review the conflict markers to understand both versions
3. **Decide on resolution**: Choose one version, combine them, or rewrite as needed
4. **Remove conflict markers**: Edit the file to contain only the final content
5. **Mark as resolved**: Use `git add <file>` to stage the resolved file
6. **Complete the merge**: Run `git commit` to finalize (or `git rebase --continue` if rebasing)
7. **Test the result**: Ensure your code still works after resolution

### Merge vs. Rebase

Both `git merge` and `git rebase` can cause conflicts, but they approach integration differently:

**Merge**:
- Creates a new commit combining changes from both branches
- Preserves complete history with branch structure
- Better when the branch structure is meaningful

**Rebase**:
- Replays your commits on top of the target branch
- Creates a linear history as if you started work later
- Better for cleaning up history before sharing

### Minimizing Conflicts

Prevention is better than cure:

1. **Communicate with your team** about who works on what
2. **Pull changes frequently** to stay in sync[^11]
3. **Keep branches short-lived** to reduce divergence
4. **Make smaller, focused commits** to reduce conflict surface area
5. **Structure code to minimize overlap** between team members

[^11]: [Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=Because%20trunk,any%20conflicts%20that%20may%20arise)

### Hands-On Exercise: Creating and Resolving Conflicts

1. **Simulate a conflict**:
   ```
   # Create conflicting changes on two branches
   git checkout main
   echo "Line added by main" >> conflict.txt
   git commit -am "Main branch change"
   
   git checkout -b feature-branch
   echo "Line added by feature" >> conflict.txt
   git commit -am "Feature branch change"
   
   # Try to merge
   git checkout main
   git merge feature-branch
   # Conflict will occur
   ```

2. **Resolve the conflict**:
   - Edit conflict.txt to clean up markers and decide on content
   - Stage the resolved file: `git add conflict.txt`
   - Complete the merge: `git commit`

3. **Practice rebasing**:
   ```
   git checkout feature-branch
   git rebase main
   # If conflicts occur, resolve them
   # After resolving: git add <file>
   # Then: git rebase --continue
   ```

### Resolving with Tools

Many tools can help visualize and resolve conflicts:

1. **Visual editors**: VS Code, IntelliJ, etc. have built-in conflict resolution
2. **Git mergetool**: Run `git mergetool` to use your configured visual merger
3. **Simpler scenarios**: Use `git checkout --ours <file>` or `git checkout --theirs <file>` to choose one version entirely
4. **Merge strategies**: For specific cases, Git supports different merge strategies like `git merge -X ours <branch>` to favor current branch changes[^12]

[^12]: [Git Merge Theirs Explained - Built In](https://builtin.com/articles/git-merge-theirs#:~:text=Git%20Merge%20Theirs%20Explained%20,branch%2C%20resolving%20git%20merge%20conflicts)

## Module 4: Bitbucket Collaboration (Days 7-8)

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

## Module 5: CI/CD Concepts with Bitbucket Pipelines (Days 9-10)

### Learning Objectives
- Understand CI/CD principles and benefits
- Configure Bitbucket Pipelines for automated testing
- Implement deployment strategies
- Integrate CI/CD into your workflow

### CI/CD Fundamentals

**Continuous Integration (CI)** is the practice of frequently integrating code changes and verifying them with automated tests[^23].

[^23]: [Continuous Integration Tutorial | Atlassian](https://www.atlassian.com/devops/continuous-delivery-tutorials/continuous-integration-tutorial#:~:text=Test%20automation%20exists%20to%20solve,pushed%20to%20the%20main%20repository)

**Continuous Delivery/Deployment (CD)** extends CI by automating the release process:
- **Continuous Delivery**: Automatically prepare releases for deployment (manual trigger)
- **Continuous Deployment**: Automatically deploy every change that passes tests

Benefits include:
- Faster feedback on changes
- Reduced integration problems
- More frequent, reliable releases
- Better visibility into development status

### Bitbucket Pipelines

Bitbucket Pipelines is a built-in CI/CD service that runs builds in Docker containers based on your configuration[^24].

[^24]: [Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to)

#### Configuration Basics

Pipelines are defined in `bitbucket-pipelines.yml` at the repository root:

```yaml
image: node:14  # Docker image to use

pipelines:
  default:      # Runs on every push (unless overridden)
    - step:
        name: Build and Test
        script:
          - npm install
          - npm test
```

#### Key Concepts

1. **Steps**: Individual units of work in the pipeline
2. **Parallel Steps**: Tasks that run simultaneously
3. **Images**: Docker containers that define the environment
4. **Caches**: Speed up builds by reusing dependencies
5. **Artifacts**: Pass files between steps
6. **Triggers**: When pipelines run (pushes, PRs, tags, etc.)
7. **Variables**: Store configuration and secrets

The pipeline runs in a clean container each time, giving you consistency and preventing "works on my machine" issues[^25].

[^25]: [Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to)

#### Advanced Configuration

```yaml
image: node:14

definitions:
  caches:
    npm: ~/.npm
  
pipelines:
  default:
    - step:
        name: Build and Test
        caches:
          - npm
        script:
          - npm install
          - npm test
  
  branches:
    main:
      - step:
          name: Build and Test
          caches:
            - npm
          script:
            - npm install
            - npm test
      - step:
          name: Deploy to Staging
          deployment: staging
          script:
            - npm install
            - npm run deploy:staging
  
  tags:
    'v*':
      - step:
          name: Deploy to Production
          deployment: production
          trigger: manual
          script:
            - npm install
            - npm run deploy:production
```

### Implementing a CI/CD Workflow

A typical workflow using Bitbucket Pipelines:

1. **Continuous Integration**:
   - Every push runs tests automatically
   - Pull requests show build status
   - Block merging if tests fail

2. **Continuous Delivery**:
   - Merges to main trigger staging deployment
   - Tagged releases deploy to production
   - Use manual triggers for sensitive environments

3. **Release Management**:
   - Use semantic versioning for releases
   - Create tags for versions: `git tag -a v1.2.3 -m "Release v1.2.3"`
   - Push tags to trigger deployment: `git push --tags`

### Hands-On Exercise: Setting Up Pipelines

1. **Enable Pipelines**: In your Bitbucket repository, go to Pipelines and enable the feature

2. **Create basic pipeline**:
   - Create `bitbucket-pipelines.yml` in your repository root
   - For a Node.js project:
     ```yaml
     image: node:14
     
     pipelines:
       default:
         - step:
             name: Build and Test
             caches:
               - node
             script:
               - npm install
               - npm test
     ```
   - Commit and push this file

3. **Watch it run**: Check the Pipelines tab in Bitbucket to see your build execute

4. **Add branch-specific pipeline**:
   - Update your YAML to add a section for main branch:
     ```yaml
     branches:
       main:
         - step:
             name: Build and Test
             script:
               - npm install
               - npm test
         - step:
             name: Deploy (Simulation)
             script:
               - echo "Deploying to staging environment"
     ```
   - Commit, push, and observe the difference when pushing to main

### CI/CD Best Practices

1. **Fast feedback**: Optimize for quick builds (use caching, parallel steps)
2. **Comprehensive testing**: Include unit, integration, and security tests
3. **Environment parity**: Test environments should mirror production
4. **Deployment strategies**: Use techniques like blue-green deployments or canary releases
5. **Monitoring**: Track your deployments and set up alerts for issues
6. **Security**: Store sensitive data in secure variables, not in code

## Review and Assessment

Each module includes a quiz to test your understanding of key concepts. The quizzes and detailed answers are provided in separate sections.

## Quiz Questions

### Module 1: Git Fundamentals Quiz

1. What is the command to create a new Git repository locally?
   A) git new
   B) git init
   C) git start
   D) git create

2. What does git clone do?
   A) Creates a new repository locally from a remote repository
   B) Sends your local changes to remote repository
   C) Shows the history of commits
   D) Creates a new commit

3. What is a commit in Git?
   A) A remote server
   B) A saved snapshot of your project's files
   C) A branch of your repository
   D) The current state of your repository

4. How do you stage files for a commit?
   A) git commit
   B) git stage
   C) git add
   D) git push

5. What command lets you see the status of your working directory?
   A) git status
   B) git check
   C) git verify
   D) git log

6. Which command pushes committed changes to a remote repository?
   A) git pull
   B) git push
   C) git commit
   D) git send

7. How can you display the commit history?
   A) git history
   B) git commits
   C) git log
   D) git track

8. What is the command to create a branch?
   A) git branch new-branch
   B) git create branch new-branch
   C) git new branch
   D) git make branch

9. When you perform git pull, what operations does Git execute?
   A) git fetch and git push
   B) git merge and git clone
   C) git fetch and git merge
   D) git fetch and git commit

10. What is the default branch name traditionally used in Git?
    A) default
    B) primary
    C) master or main
    D) root

### Module 2: Branching Strategies Quiz

1. What is the main advantage of using branching strategies in Git?
   A) Eliminates the need for code testing.
   B) Allows multiple developers to work simultaneously without conflicts.
   C) Automatically merges all code changes.
   D) Reduces the number of commits.

2. In GitFlow, what is the purpose of the `develop` branch?
   A) To deploy code directly to production.
   B) To develop and integrate new features.
   C) For hotfixes only.
   D) To test production-ready code.

3. Which workflow is best suited for continuous integration and frequent deployments?
   A) GitFlow Workflow
   B) Trunk-Based Development
   C) Feature Branch Workflow
   D) Release Branch Workflow

4. What is the recommended lifecycle of a feature branch?
   A) Maintained indefinitely.
   B) Deleted after merging into the main branch.
   C) Kept active permanently for future enhancements.
   D) Immediately pushed to production.

5. Which command is used to switch to an existing branch?
   A) `git branch <branch-name>`
   B) `git checkout -b <branch-name>`
   C) `git switch <branch-name>`
   D) `git merge <branch-name>`

6. In GitFlow, which branch is used specifically for production-ready releases?
   A) `master` (or `main`)
   B) `develop`
   C) `feature`
   D) `hotfix`

7. What characteristic best describes trunk-based development?
   A) Long-lived feature branches.
   B) Frequent direct commits to a single main branch.
   C) Multiple release branches.
   D) Isolated integration of code.

# Comprehensive Git Training Program: From Fundamentals to Advanced Workflows (continued)

## Quiz Questions (continued)

### Module 2: Branching Strategies Quiz (continued)

8. What's a primary purpose of creating pull requests?
   A) Immediate deployment of changes.
   B) Avoiding code review processes.
   C) Facilitating code review and discussion.
   D) Automatic conflict resolution.

9. In Git, how do you create and switch immediately to a new branch?
   A) `git branch <branch-name>`
   B) `git checkout <branch-name>`
   C) `git checkout -b <branch-name>`
   D) `git switch --create <branch-name>`

10. Why is writing descriptive commit messages considered a best practice?
    A) It speeds up automatic merges.
    B) It removes the need for branching.
    C) It provides context and clarity for changes.
    D) It automatically resolves conflicts.

### Module 3: Conflict Resolution Quiz

1. What causes a merge conflict in Git?
   A) Multiple commits from the same author.
   B) Two branches containing changes to the same lines of code.
   C) Creating too many branches.
   D) Pulling changes from a remote repository.

2. Which command is used to view conflicted files after a merge conflict?
   A) `git status`
   B) `git log`
   C) `git merge`
   D) `git show`

3. After resolving a conflict manually, what must you do next?
   A) Run `git reset`
   B) Run `git commit`
   C) Delete the conflicted file
   D) Immediately run `git push`

4. What markers indicate merge conflicts within a file?
   A) `<<<`, `===`, `>>>`
   B) `[conflict-start]` and `[conflict-end]`
   C) `{conflict}` and `{end}`
   D) `(start)` and `(end)`

5. What does the command `git merge --abort` accomplish?
   A) Deletes the current branch.
   B) Cancels the merge and returns the repository to its previous state.
   C) Automatically resolves conflicts.
   D) Forces a merge despite conflicts.

6. What Git tool can help visualize merge conflicts and history?
   A) Git Merge
   B) Git Rebase
   C) Git GUI or visualization tools like `gitk`
   D) Git Clone

7. Why is rebasing considered useful for conflict management?
   A) It permanently deletes conflicting commits.
   B) It simplifies linear project history by applying changes sequentially.
   C) It automatically resolves all conflicts.
   D) It prevents conflicts completely.

8. When might you prefer using `git rebase` over `git merge`?
   A) When preserving linear commit history is important.
   B) When working directly on production branches.
   C) When you never want to edit commit history.
   D) When you always prefer multiple merge commits.

9. Which practice helps minimize the frequency of merge conflicts?
   A) Avoiding committing frequently.
   B) Frequently pulling changes from shared branches.
   C) Working on a single branch indefinitely.
   D) Committing massive amounts of code at once.

10. What happens if you push conflicted files without resolving conflicts?
    A) Git automatically resolves the conflicts.
    B) The push is rejected; conflicts must be resolved locally.
    C) Conflicts are ignored and the code is pushed.
    D) Git prompts other developers to resolve the conflicts.

### Module 4: Bitbucket Collaboration Quiz

1. What is the primary purpose of a pull request in Bitbucket?
   A) To directly deploy code to production.
   B) To review code changes collaboratively before merging.
   C) To resolve merge conflicts automatically.
   D) To archive code permanently.

2. Which action should you typically perform after a peer leaves feedback on your pull request?
   A) Ignore their suggestions and merge immediately.
   B) Discuss or address the feedback and update the code if necessary.
   C) Immediately close the pull request without changes.
   D) Delete the branch.

3. In Bitbucket, who can typically approve a pull request?
   A) Only the repository administrator.
   B) Any user with repository read access.
   C) Users with designated reviewer or write permissions.
   D) Any external user.

4. Which practice enhances the effectiveness of code reviews?
   A) Reviewing very large batches of changes at once.
   B) Providing clear, constructive, and specific feedback.
   C) Ignoring small issues to save time.
   D) Skipping documentation in pull requests.

5. What does it mean to "decline" a pull request in Bitbucket?
   A) Merging code immediately.
   B) Rejecting proposed changes without merging.
   C) Approving changes without further review.
   D) Automatically resolving conflicts.

6. What is a common best practice for commit messages when working in Bitbucket?
   A) Keep them vague and short.
   B) Write detailed, descriptive messages explaining the changes.
   C) Skip commit messages if changes are minor.
   D) Always use the default message provided by Bitbucket.

7. How does Bitbucket integrate with Jira?
   A) Automatically deploys code to Jira.
   B) Allows linking commits and pull requests directly to Jira tickets.
   C) Only supports manual ticket creation.
   D) Blocks Jira access during code reviews.

8. What role does the "Diff" view serve in a pull request?
   A) Displays only the commit history.
   B) Shows differences between proposed changes and existing code.
   C) Deploys changes directly.
   D) Deletes files from the repository.

9. After merging a pull request, what is a recommended next step regarding the feature branch?
   A) Keep it indefinitely for future changes.
   B) Rename the branch immediately.
   C) Delete the feature branch to maintain repository cleanliness.
   D) Push the branch directly to production.

10. What is one advantage of using branch permissions in Bitbucket?
    A) Allows anyone to directly push code to production branches.
    B) Restricts who can merge or push changes, ensuring code quality.
    C) Prevents pull requests entirely.
    D) Automatically writes commit messages.

### Module 5: CI/CD Concepts Quiz

1. What does CI/CD stand for?
   A) Continuous Improvement / Continuous Delivery
   B) Continuous Integration / Continuous Deployment (or Delivery)
   C) Constant Inspection / Constant Development
   D) Continual Iteration / Code Deployment

2. What is the primary goal of Continuous Integration (CI)?
   A) Immediate deployment to production
   B) Automatic conflict resolution
   C) Frequent merging of code into a shared repository to detect integration issues early
   D) Avoiding code reviews

3. What distinguishes Continuous Deployment from Continuous Delivery?
   A) Continuous Deployment requires manual approval; Continuous Delivery deploys automatically.
   B) Continuous Delivery requires manual approval; Continuous Deployment deploys automatically.
   C) Continuous Deployment always skips testing.
   D) Continuous Delivery does not integrate code frequently.

4. In a CI/CD pipeline, which step usually occurs first?
   A) Deployment to production
   B) Running automated tests
   C) Building the application
   D) Monitoring production systems

5. Which Bitbucket feature facilitates CI/CD workflows?
   A) Bitbucket Pages
   B) Bitbucket Pipelines
   C) Bitbucket Snippets
   D) Bitbucket Pull Requests

6. Why are automated tests critical in a CI/CD pipeline?
   A) They guarantee zero defects.
   B) They eliminate the need for manual testing entirely.
   C) They provide fast feedback on code changes, catching issues early.
   D) They automatically deploy code to production.

7. What is a typical best practice for deploying applications using CI/CD?
   A) Directly deploying every code change to production without testing.
   B) Using feature flags or phased rollouts to manage risk.
   C) Skipping monitoring after deployment.
   D) Manually merging every commit.

8. Which tool is commonly used alongside Bitbucket for Continuous Integration?
   A) Jenkins
   B) Jira
   C) Trello
   D) Confluence

9. What benefit does Continuous Delivery primarily offer businesses?
   A) Slower deployment processes
   B) Increased manual control at every step
   C) Faster, more reliable releases with reduced risk
   D) Avoidance of code integration

10. What is a common monitoring practice after deployment in CI/CD?
    A) Ignoring the system post-deployment
    B) Immediate rollback regardless of results
    C) Continuous monitoring and alerting to identify issues quickly
    D) Manual code review only

## Quiz Answers

### Module 1: Git Fundamentals Quiz Answers

1. **B) git init**  
   Explanation: Initializes a new local repository in your directory, creating the .git directory.

2. **A) Creates a new repository locally from a remote repository**  
   Explanation: git clone copies a repository from a remote location into your local environment.

3. **B) A saved snapshot of your project's files**  
   Explanation: A commit in Git captures the current state of your repository and records changes.

4. **C) git add**  
   Explanation: git add stages files, preparing them for inclusion in the next commit.

5. **A) git status**  
   Explanation: git status provides an overview of the current state of your working directory and staging area.

6. **B) git push**  
   Explanation: git push sends committed changes to the remote repository.

7. **C) git log**  
   Explanation: git log displays commit history, showing each commit's author, date, and commit message.

8. **A) git branch new-branch**  
   Explanation: This creates a new branch from the current branch's commit.

9. **C) git fetch and git merge**  
   Explanation: git pull first fetches remote commits and then merges them into your current branch.

10. **C) master or main**  
    Explanation: Traditionally, the default branch has been called master, though many now use main.

### Module 2: Branching Strategies Quiz Answers

1. **B) Allows multiple developers to work simultaneously without conflicts.**  
   Explanation: Branches isolate development tasks, enabling parallel work without disrupting others.

2. **B) To develop and integrate new features.**  
   Explanation: The `develop` branch integrates new features before release.

3. **B) Trunk-Based Development**  
   Explanation: Trunk-based emphasizes continuous integration directly into a main branch, suited for CI/CD.

4. **B) Deleted after merging into the main branch.**  
   Explanation: Best practice dictates feature branches should be short-lived and removed after merging.

5. **C) `git switch <branch-name>`**  
   Explanation: Explicitly switches to an existing branch.

6. **A) `master` (or `main`)**  
   Explanation: Holds stable, production-ready code.

7. **B) Frequent direct commits to a single main branch.**  
   Explanation: Encourages continuous integration directly into a single trunk (main branch).

8. **C) Facilitating code review and discussion.**  
   Explanation: Allows peer reviews and discussion before merging.

9. **C) `git checkout -b <branch-name>`**  
   Explanation: Creates and switches immediately to a new branch.

10. **C) It provides context and clarity for changes.**  
    Explanation: Clear commit messages help teams understand changes, improving maintainability.

### Module 3: Conflict Resolution Quiz Answers

1. **B) Two branches containing changes to the same lines of code.**  
   Explanation: Conflicts arise when Git can't auto-merge overlapping edits.

2. **A) `git status`**  
   Explanation: Shows clearly which files are conflicted after merge.

3. **B) Run `git commit`**  
   Explanation: Commit the conflict resolution to finalize merge.

4. **A) `<<<`, `===`, `>>>`**  
   Explanation: Git clearly marks conflicts with these symbols in files.

5. **B) Cancels the merge and returns the repository to its previous state.**  
   Explanation: Useful if conflicts seem unmanageable.

6. **C) Git GUI or visualization tools like `gitk`**  
   Explanation: Visualization helps in understanding conflict points clearly.

7. **B) It simplifies linear project history by applying changes sequentially.**  
   Explanation: Rebase reapplies commits onto a target branch sequentially, simplifying resolution.

8. **A) When preserving linear commit history is important.**  
   Explanation: Rebase avoids merge commits, maintaining a linear and clean history.

9. **B) Frequently pulling changes from shared branches.**  
   Explanation: Regular pulls minimize divergence, significantly reducing conflicts.

10. **B) The push is rejected; conflicts must be resolved locally.**  
    Explanation: Git never allows unresolved conflicts to be pushed.

### Module 4: Bitbucket Collaboration Quiz Answers

1. **B) To review code changes collaboratively before merging.**  
   Explanation: Pull requests facilitate peer review and discussion before code integration.

2. **B) Discuss or address the feedback and update the code if necessary.**  
   Explanation: Addressing feedback ensures higher quality and collaboration.

3. **C) Users with designated reviewer or write permissions.**  
   Explanation: Typically, reviewers or team members with write access approve PRs.

4. **B) Providing clear, constructive, and specific feedback.**  
   Explanation: Clear feedback helps developers improve code quality effectively.

5. **B) Rejecting proposed changes without merging.**  
   Explanation: Declining clearly signals rejection of proposed changes.

6. **B) Write detailed, descriptive messages explaining the changes.**  
   Explanation: Good commit messages increase clarity and maintainability.

7. **B) Allows linking commits and pull requests directly to Jira tickets.**  
   Explanation: Integration improves traceability and workflow efficiency.

8. **B) Shows differences between proposed changes and existing code.**  
   Explanation: Diff views help reviewers clearly identify modifications.

9. **C) Delete the feature branch to maintain repository cleanliness.**  
   Explanation: Removing merged branches maintains repository hygiene.

10. **B) Restricts who can merge or push changes, ensuring code quality.**  
    Explanation: Branch permissions safeguard critical branches (e.g., main/master).

### Module 5: CI/CD Concepts Quiz Answers

1. **B) Continuous Integration / Continuous Deployment (or Delivery)**  
   Explanation: CI/CD commonly refers to integrating code frequently (CI) and delivering or deploying automatically (CD).

2. **C) Frequent merging of code into a shared repository to detect integration issues early**  
   Explanation: CI focuses on early issue detection via frequent integration.

3. **B) Continuous Delivery requires manual approval; Continuous Deployment deploys automatically.**  
   Explanation: Continuous Delivery makes code ready for deployment but usually requires manual approval; Continuous Deployment automatically deploys changes.

4. **C) Building the application**  
   Explanation: Building the app comes first, ensuring code compiles correctly before tests.

5. **B) Bitbucket Pipelines**  
   Explanation: Pipelines automate building, testing, and deploying code.

6. **C) They provide fast feedback on code changes, catching issues early.**  
   Explanation: Automated tests rapidly detect issues, shortening feedback loops.

7. **B) Using feature flags or phased rollouts to manage risk.**  
   Explanation: This practice reduces risk by progressively exposing features.

8. **A) Jenkins**  
   Explanation: Jenkins is a widely-used tool for CI, commonly integrated with Bitbucket.

9. **C) Faster, more reliable releases with reduced risk**  
   Explanation: Continuous Delivery accelerates reliable and frequent software delivery.

10. **C) Continuous monitoring and alerting to identify issues quickly**  
    Explanation: Monitoring post-deployment ensures quick identification and resolution of issues.

## Conclusion

By completing this training, you've gained practical skills in Git, Bitbucket, and CI/CD workflows. You should now be able to:

- Manage code changes with Git's version control
- Implement effective branching strategies for your team
- Resolve conflicts confidently when they arise
- Collaborate effectively through pull requests and code reviews
- Automate testing and deployment with CI/CD pipelines

The combination of these skills will help you build higher quality software more efficiently, with fewer integration issues and faster delivery cycles.

Remember that mastering Git is an ongoing journey - continue to refine your workflows and explore advanced features as your projects evolve.