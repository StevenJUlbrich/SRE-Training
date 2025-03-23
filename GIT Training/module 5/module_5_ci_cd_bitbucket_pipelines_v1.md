# Module 5: CI/CD Concepts with Bitbucket Pipelines (Days 9-10)

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
