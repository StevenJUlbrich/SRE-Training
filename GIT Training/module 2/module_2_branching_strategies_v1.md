
# Module 2: Branching Strategies (Days 3-4)

## Learning Objectives

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

   ```cmd
   git checkout main
   git pull                             # Get latest main
   git checkout -b feature/new-feature  # Create feature branch
   # Make changes and commit
   git push -u origin feature/new-feature
   # Create pull request in Bitbucket
   ```

2. **GitFlow Simulation**:

   ```cmd
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

   ```cmd
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
