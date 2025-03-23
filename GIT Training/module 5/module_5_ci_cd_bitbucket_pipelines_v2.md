
# 🚀 Module 5: CI/CD Concepts & Bitbucket Pipelines (Days 9–10)

## 🎯 Learning Outcomes
By the end of this module, learners will be able to:
- Understand the principles of Continuous Integration and Continuous Delivery/Deployment
- Use Bitbucket Pipelines to automate build, test, and deployment processes
- Write and manage `.bitbucket-pipelines.yml` files
- Leverage CI to catch issues early and deploy with confidence
- Troubleshoot common CI/CD issues and integrate with real-world SRE workflows

---

## 📖 1. Theory – What is CI/CD?

| Concept | Description |
|--------|-------------|
| **CI (Continuous Integration)** | Developers regularly merge changes into a shared branch. Each change is verified by automated builds and tests. |
| **CD (Continuous Delivery)** | Code is always in a deployable state. Deployments are prepared and can be triggered manually. |
| **CD (Continuous Deployment)** | Every change that passes CI is automatically deployed to production, with no human intervention. |

---

## 🤔 2. Why It Matters for SREs & Platform Engineers

CI/CD:
- Reduces **risk of outages** by testing and validating code early
- Enables **faster recovery** through repeatable deployments
- Improves **consistency** across environments
- Provides **audit trails** for compliance and observability

---

## 🔍 3. Bitbucket Pipelines Overview

Bitbucket Pipelines is a CI/CD service built into Bitbucket Cloud. It uses a YAML file to define build steps.

### 🔹 Key Concepts:
- **Pipeline**: The full automation process (build, test, deploy)
- **Step**: A stage within the pipeline
- **Image**: The Docker image that defines the execution environment
- **Trigger**: Events like push or tag that start the pipeline
- **Artifact**: Files passed between steps (e.g., build outputs)

---

## 🧠 4. Sample Pipeline YAML Explained

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

  branches:
    main:
      - step:
          name: Deploy to Staging
          deployment: staging
          script:
            - echo "Deploying to staging..."
```

---

## 🛠️ 5. Hands-On Lab – Build Your First Pipeline

### Step-by-Step

```bash
# Step 1: Enable Pipelines in Bitbucket GUI
# Repo > Pipelines > Enable

# Step 2: Create pipeline config file
touch bitbucket-pipelines.yml

# Step 3: Add content (for Node.js project)
```

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

```bash
# Step 4: Commit and push
git add bitbucket-pipelines.yml
git commit -m "Add basic CI pipeline"
git push
```

---

## 🔐 6. Secure Secrets & Environment Variables

Use Bitbucket’s **Repository Settings → Variables** to define:
- `DEPLOY_API_KEY`
- `STAGING_URL`

Then reference in pipeline like:

```yaml
script:
  - curl -X POST "$STAGING_URL" -H "Authorization: Bearer $DEPLOY_API_KEY"
```

---

## 🧯 7. Troubleshooting Tips

| Issue | Fix |
|------|-----|
| Pipeline fails due to missing dependency | Ensure correct Docker image or add install step |
| Secrets are exposed in logs | Never echo secret vars directly |
| Pipeline not triggering | Check if `.yml` file exists and Pipelines is enabled |
| Can't deploy to server | Confirm SSH key or API token setup and correct permissions |

---

## ✅ 8. Knowledge Check (Mini Quiz)

**Q1:** What is the difference between Continuous Delivery and Continuous Deployment?  
**Q2:** What section in `.bitbucket-pipelines.yml` defines the Docker image to use?  
**Q3:** What happens when you push to the `main` branch with a pipeline configured?

💡 **Open Task:**  
Write a pipeline that:
1. Runs unit tests on every push
2. Deploys to staging on `main` branch pushes
3. Uses a secret `DEPLOY_KEY`

---

## 📌 9. Summary / Key Takeaways

- CI/CD improves velocity, reliability, and recoverability
- Bitbucket Pipelines integrates directly with your Git repo
- Use YAML to define jobs, builds, and deployments
- Set up secrets safely for production deploys
- Monitor builds and pipelines for every PR or commit

---

## 🧠 10. Advanced Learner Challenges

- Add branch-specific behavior (`main`, `dev`, `release/*`)
- Set up conditional deploys only for tagged versions (`v*`)
- Integrate with Docker Hub or AWS for image publishing
- Add Slack notifications using Pipes

---

## 🎮 Bonus: CI/CD Simulators & Visual Builders

- [Bitbucket Pipelines Documentation](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/)
- [Pipelines Demo Lab (Atlassian)](https://bitbucket.org/product/features/pipelines)
- [YAML Validator & Previewer](https://yaml-online-parser.appspot.com/)
- [GitLab vs Bitbucket CI Comparison](https://about.gitlab.com/devops-tools/bitbucket-vs-gitlab/)
