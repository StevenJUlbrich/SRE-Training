# 🚀 Module 5: CI/CD Concepts & Bitbucket Pipelines (Days 9-10)

## 🎯 Learning Objectives

By the end of this module, participants will be able to:

- Understand CI/CD principles and benefits
- Configure Bitbucket Pipelines for automated testing and deployment
- Write and manage `.bitbucket-pipelines.yml` files
- Implement effective deployment strategies
- Troubleshoot common CI/CD issues
- Integrate CI/CD into your workflow

---

## 📖 1. CI/CD Fundamentals

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Continuous Integration (CI)** | The practice of frequently integrating code changes and verifying them with automated tests[^1] |
| **Continuous Delivery (CD)** | Automatically prepare releases for deployment (manual trigger) |
| **Continuous Deployment (CD)** | Automatically deploy every change that passes tests (no human intervention) |

[^1]: [Continuous Integration Tutorial | Atlassian](https://www.atlassian.com/devops/continuous-delivery-tutorials/continuous-integration-tutorial)

### Benefits for SREs & Platform Engineers

CI/CD provides several key benefits:

- **Faster feedback** on changes
- **Reduced integration problems**
- **More frequent, reliable releases**
- **Better visibility** into development status
- **Reduced risk of outages** by testing and validating code early
- **Faster recovery** through repeatable deployments
- **Improved consistency** across environments
- **Audit trails** for compliance and observability

---

## 🤔 2. Real-World Case Study

### Infrastructure Reliability Team

An infrastructure reliability team was struggling with long downtimes caused by manual and inconsistent deployments. After adopting Bitbucket Pipelines:

- Deployment times were reduced by 70%
- Issues were identified earlier in the development cycle
- Mean Time To Recovery (MTTR) decreased by 45%
- Overall service reliability improved due to consistent deployments
- Team was able to deploy 3x more frequently with confidence

The key improvements included automating test environments, standardizing build processes, and implementing consistent deployment practices.

---

## 🔍 3. Bitbucket Pipelines Overview

Bitbucket Pipelines is a built-in CI/CD service that runs builds in Docker containers based on your configuration[^2].

[^2]: [Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/)

### Key Concepts

- **Pipeline**: The full automation process (build, test, deploy)
- **Step**: A stage within the pipeline
- **Image**: The Docker image that defines the execution environment
- **Trigger**: Events like push or tag that start the pipeline
- **Artifact**: Files passed between steps (e.g., build outputs)
- **Cache**: Speeds up builds by reusing dependencies

---

## 🧠 4. Pipeline Configuration Basics

Pipelines are defined in `bitbucket-pipelines.yml` at the repository root. Here's a simple example:

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

---

## 🛠️ 5. Advanced Pipeline Configuration

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

---

## 📋 6. Hands-On Lab: Setting Up Your First Pipeline

### Step 1: Enable Pipelines

1. In your Bitbucket repository, go to **Pipelines** section
2. Click **Enable Pipelines**

### Step 2: Create Pipeline Configuration

Create a file named `bitbucket-pipelines.yml` in your repository root:

```yaml
image: node:14

pipelines:
  default:
    - step:
        name: Test
        script:
          - npm install
          - npm test
```

### Step 3: Commit and Push Your Configuration

```bash
git add bitbucket-pipelines.yml
git commit -m "Add basic CI pipeline"
git push
```

### Step 4: Watch It Run

Go to the **Pipelines** tab in Bitbucket to see your build execute in real time.

---

## 🔐 7. Managing Secrets & Environment Variables

Use Bitbucket's **Repository Settings → Variables** to securely store sensitive information:

- `DEPLOY_API_KEY`
- `STAGING_URL`
- `DATABASE_PASSWORD`

Then reference them in your pipeline:

```yaml
script:
  - curl -X POST "$STAGING_URL" -H "Authorization: Bearer $DEPLOY_API_KEY"
```

**Never** hard-code secrets in your pipeline configuration file or expose them in logs.

---

## 🔄 8. Implementing a CI/CD Workflow

A typical workflow using Bitbucket Pipelines:

### Continuous Integration

- Every push runs tests automatically
- Pull requests show build status
- Block merging if tests fail

### Continuous Delivery

- Merges to main trigger staging deployment
- Tagged releases deploy to production
- Use manual triggers for sensitive environments

### Release Management

- Use semantic versioning for releases
- Create tags for versions: `git tag -a v1.2.3 -m "Release v1.2.3"`
- Push tags to trigger deployment: `git push --tags`

---

## 🎨 9. CI/CD Pipeline Visualization

```
Developer → Push code → Trigger pipeline → Automated tests → Build artifacts → Deploy to staging → Manual/Auto deploy to prod
```

---

## ⚠️ 10. Common Pitfalls & Troubleshooting

| Issue | Fix |
|------|-----|
| Pipeline fails due to missing dependency | Ensure correct Docker image or add install step |
| Secrets are exposed in logs | Never echo secret vars directly; use secure variables |
| Pipeline not triggering | Check if `.yml` file exists and Pipelines is enabled |
| Can't deploy to server | Confirm SSH key or API token setup and correct permissions |
| Tests pass locally but fail in pipeline | Ensure environment parity; check Docker image version |
| Slow pipelines | Implement caching and parallel steps |
| Broken deployment | Add rollback steps to production deployments |

---

## 📌 11. CI/CD Best Practices

1. **Fast feedback**: Optimize for quick builds (use caching, parallel steps)
2. **Comprehensive testing**: Include unit, integration, and security tests
3. **Environment parity**: Test environments should mirror production
4. **Deployment strategies**: Use techniques like blue-green deployments or canary releases
5. **Monitoring**: Track your deployments and set up alerts for issues
6. **Security**: Store sensitive data in secure variables, not in code
7. **Small commits**: Make small, frequent changes to reduce risk
8. **Branch-specific behavior**: Configure different behaviors for different branches
9. **Notifications**: Set up alerts for pipeline failures (Slack, email)
10. **Documentation**: Document your pipeline setup and deployment process

---

## ✅ 12. Knowledge Check (Mini Quiz)

**Q1:** What is the difference between Continuous Delivery and Continuous Deployment?

**Q2:** What section in `.bitbucket-pipelines.yml` defines the Docker image to use?

**Q3:** How would you configure a pipeline to deploy only when code is pushed to the main branch?

**Q4:** Where should you store sensitive information like API keys for use in pipelines?

**Q5:** What happens when a pipeline step fails?

### 💡 Open-Ended Task

Write a pipeline that:
1. Runs unit tests on every push
2. Deploys to staging on `main` branch pushes
3. Deploys to production only on tagged releases (v*)
4. Uses a secret `DEPLOY_KEY`

---

## 📗 13. FAQ

**Q:** Can Bitbucket Pipelines be used for complex deployments?  
**A:** Yes, pipelines can integrate with various deployment environments and complex deployment scripts.

**Q:** How do I securely manage secrets in pipelines?  
**A:** Store sensitive variables in Bitbucket's built-in secure variables system under repository settings.

**Q:** Can I run pipeline steps in parallel?  
**A:** Yes, use the `parallel` keyword to define steps that can run simultaneously.

**Q:** How do I debug a failing pipeline?  
**A:** Check the logs in the Pipelines UI, and try running the same commands locally in a similar environment.

**Q:** Are there usage limits for Bitbucket Pipelines?  
**A:** Yes, Bitbucket has usage limits based on your plan. Check their documentation for details.

---

## 🧠 14. Advanced Challenges

- Add branch-specific behavior (`main`, `dev`, `release/*`)
- Set up conditional deploys only for tagged versions (`v*`)
- Integrate with Docker Hub or AWS for image publishing
- Add Slack notifications using Pipes
- Create a multi-stage deployment pipeline with approval gates
- Implement automated rollbacks on failed deployments
- Integrate security scanning tools into your pipeline

---

## 📚 15. Additional Resources

- [Bitbucket Pipelines Documentation](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/)
- [CI/CD Pipeline Best Practices](https://www.atlassian.com/devops/continuous-delivery-tutorials)
- [Bitbucket Pipelines Examples](https://bitbucket.org/product/features/pipelines)
- [YAML Validator & Previewer](https://yaml-online-parser.appspot.com/)
- [GitLab vs Bitbucket CI Comparison](https://about.gitlab.com/devops-tools/bitbucket-vs-gitlab/)