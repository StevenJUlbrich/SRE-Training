
# Quiz Questions for Git Training Modules

Below is a set of quiz questions for each module (corresponding to the days of the 2-week learning plan). The quizzes include multiple-choice questions, scenarios, and practical prompts to test your understanding.

## Module 1 Quiz – Git Basics (Days 1–2)

1. **Which of the following best describes Git?**  
   A. A programming language for version control  
   B. A distributed version control system for tracking changes in file ([Git - Wikipedia](https://en.wikipedia.org/wiki/Git#:~:text=Git%20,who%20are%20developing%20software%20collaboratively))】  
   C. A hosted platform for deploying web applications  
   D. A project management methodology  
2. **What command would you use to create a copy of an existing remote repository onto your local machine?**  
   A. `git fork`  
   B. `git clone ([ Basic Git Commands | Atlassian Git Tutorial ](https://www.atlassian.com/git/glossary#:~:text=Git%20clone))】  
   C.`git pull` 
   D. `git init`  
3. **After modifying a file, which sequence of commands will correctly save those changes to the repository?**  
   A. `git add <file>`, then `git commit -m "message" ([ Basic Git Commands | Atlassian Git Tutorial ](https://www.atlassian.com/git/glossary#:~:text=Git%20commit))】  
   B.`git commit -m "message"`, then`git push` 
   C. `git pull`, then`git commit` 
   D. `git stage <file>`, then`git push origin main`  
4. **True or False:** The `git status` command shows you which files are untracked, modified, or staged in preparation for a commit.  
   **Answer:** True. (`git status` displays the state of the working directory and staging are ([Basic Git Commands | Atlassian Git Tutorial](https://www.atlassian.com/git/glossary#:~:text=git%20status))】.)  
5. **Scenario:** You’ve just committed a change, but realize you want to add one more file to that same commit. Which command can help you modify the last commit (instead of making a new one)?  
   A. `git commit --amend ([ Basic Git Commands | Atlassian Git Tutorial ](https://www.atlassian.com/git/glossary#:~:text=git%20commit%20))】  
   B.`git reset --soft HEAD~1` 
   C. `git cherry-pick` 
   D. `git revert HEAD`  
6. **Which command is used to update your local repository with changes from a remote repository, potentially merging them into your current branch?**  
   A. `git fetch`  
   B. `git pull ([ Basic Git Commands | Atlassian Git Tutorial ](https://www.atlassian.com/git/glossary#:~:text=git%20pull))】  
   C.`git push` 
   D. `git merge`  
7. **Multiple Choice:** What information does a Git commit contain?  
   A. A snapshot of all files in the repository at that point, an author, date, and message  
   B. Only the diff (changes) made in that commit and the author’s username  
   C. The entire repository history up to that point  
   D. A list of contributors on that commit  
8. **Fill in the blank:** To configure your identity in Git globally, you would run `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`. This ensures that your commits are labeled with the correct _______.  
   **Answer:** name and email (user identity).  
9. **Scenario:** After running `git add .`, you realize one file contains changes you don’t want to include in the commit. What is a simple way to remove that file from the staging area?  
   A. Delete the file from the disk  
   B. Run `git reset HEAD <file>` to unstage it  
   C. Commit, then use `git revert`  
   D. Run `git checkout <file>`  
   **Explanation:** `git reset HEAD <file>` will unstage the file (remove it from staging, keeping changes in working directory).  
10. **True or False:** Git can only be used when you have internet access, since it’s a distributed version control that always communicates with a remote server.  
    **Answer:** False. (Git is fully capable of local commits/branching; internet is only needed when pushing or pulling to/from remote.)

## Module 2 Quiz – Branching Strategies (Days 3–4)

1. **Multiple Choice:** In the Feature Branching workflow, when should a feature branch be merged back into the main branch?  
   A. After every commit  
   B. Only when the feature is complete and teste ([Git Feature Branch Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow#:~:text=The%20Feature%20Branch%20Workflow%20assumes,menu))】  
   C. Whenever the developer feels like merging  
   D. Never; feature branches stay separate permanently  
2. **Which branching model introduces long-lived branches like `develop`, `release/*`, and `hotfix/*` in addition to the main branch?**  
   A. Feature Branch Workflow  
   B. Trunk-Based Development  
   C. GitFlow Workflo ([Gitflow Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20is%20an%20alternative%20Git,can%20also%20introduce%20conflicting%20updates))】  
   D. Centralized Workflow  
3. **True or False:** Trunk-based development encourages frequent integration of code into a single main branch, often multiple times a da ([Trunk-based Development | Atlassian](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development#:~:text=Trunk,software%20delivery%20and%20organizational%20performance))】.  
   **Answer:** True.  
4. **Scenario:** Your team follows GitFlow. You have finished a feature on a `feature/login` branch. According to GitFlow, which branch should you merge this into first?  
   A. `main`  
   B. `develop ([ Gitflow Workflow | Atlassian Git Tutorial ](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Step%201))】  
   C.`release`  
   D. A new branch named after the feature  
5. **Multiple Choice:** What is one primary advantage of using short-lived feature branches (as in GitHub Flow or feature branching) over long-lived branches?  
   A. It eliminates the need for code reviews.  
   B. It reduces merge conflicts by integrating changes soone ([Git Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows#:~:text=Short))】.  
   C. It guarantees tests will always pass.  
   D. It allows developers to work completely in isolation without ever communicating.  
6. **GitFlow vs Trunk-Based:** In GitFlow, a release is typically prepared on a dedicated release branch. How is this different in a pure Trunk-Based approach?  
   A. Trunk-based uses two release branches instead of one.  
   B. In trunk-based, you generally deploy directly from the main/trunk branch without a separate release branch (possibly using feature flags for incomplete features ([Trunk-based Development | Atlassian](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development#:~:text=Gitflow%2C%20which%20was%20popularized%20first%2C,to%20iterate%20quickly%20and%20implement%C2%A0CI%2FCD))】.  
   C. Trunk-based development doesn’t allow releases at all.  
   D. They are actually the same in how they handle releases.  
7. **Scenario:** The team wants to adopt continuous deployment, releasing small changes very frequently. Which strategy is most aligned with this goal?  
   A. GitFlow (with its structured release cycles)  
   B. Trunk-Based Development (rapid integration ([Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=Consequently%2C%20trunk,CD))】  
   C. Long-lived feature branches that merge quarterly  
   D. Subversion-like Centralized with one commit at end of project  
8. **Fill in the blanks:** In GitFlow, after finishing work in a `release` branch, you merge it into ____ and ___ ([Gitflow Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=%24%C2%A0git%C2%A0flow%C2%A0init)) ([Gitflow Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Feature%20branches))】.  
   **Answer:** main (production) and develop.  
   _(This merges the release changes back into develop as well as main.)_  
9. **True or False:** In a feature branch workflow (like GitHub Flow), the default branch (main) always contains deployable code, and all new development is done on branches that are merged via pull requests.  
   **Answer:** True.  
10. **Multiple Choice (Scenario):** Your project is currently at version 2.0 in production. You need to work on a 3.0 major release while also being able to issue emergency fixes to 2.0. Which strategy might you use?  
    A. Trunk-based with feature toggles for 3.0 features  
    B. GitFlow, using the `develop` branch for 3.0 development and hotfix branches from main for urgent 2.0 fixe ([Gitflow Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=match%20at%20L653%20Image%3A%20Hotfix,branch%20within%20git%20workflow))】  
    C. Only feature branches off main for both and hope they don't conflict  
    D. Stop all new development until 2.0 is retired  
    **Explanation:** GitFlow (or variations of it) handles parallel streams (develop vs main with hotfixes) well. In trunk-based, you'd need other mechanisms or possibly separate maintenance branches anyway.

## Module 3 Quiz – Merge Conflicts and Resolution Techniques (Days 5–6)

1. **What is a merge conflict in Git?**  
   A. An error that occurs when Git is out of date  
   B. A situation where two branches have changes that Git cannot automatically merg ([Resolving a merge conflict using the command line - GitHub Docs](https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line#:~:text=Merge%20conflicts%20occur%20when%20competing,information%2C%20see%20About%20merge%20conflicts))】  
   C. A type of Git commit  
   D. When a repository has too many branches  
2. **True or False:** Merge conflicts only happen with GitFlow and never with trunk-based development.  
   **Answer:** False. (Conflicts can happen with any workflow if concurrent changes overlap; though frequency can be reduced by frequent integration.)  
3. **Multiple Choice:** Which of the following is NOT a typical cause of merge conflicts?  
   A. Two branches edited the same lines in a file differently.  
   B. One branch deleted a file while another branch modified it.  
   C. Two branches added completely different files (no overlapping content) ([Resolving a merge conflict using the command line - GitHub Docs](https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line#:~:text=Merge%20conflicts%20occur%20when%20competing,information%2C%20see%20About%20merge%20conflicts))】  
   D. Two branches renamed the same file in different ways.  
   **Explanation:** Adding different files doesn’t conflict since they don’t touch same content; all others can cause conflicts.  
4. **Scenario:** You attempt to merge branch “featureX” into “main” and get a conflict in `config.json`. Git shows conflict markers. What is your next step to resolve this?  
   A. Delete the `config.json` file and run merge again.  
   B. Open `config.json`, find `<<<<<<`, `======`, `>>>>>>` markers, and edit the content to what it should be, then remove the marker ([How to resolve merge conflicts in Git](https://graphite.dev/guides/how-to-resolve-merge-conflicts-in-git#:~:text=Terminal))】.  
   C. Run `git reset --hard` to undo everything and try again.  
   D. Use `git blame` to decide who is at fault.  
5. **Fill in the blanks:** In a conflicted file, Git divides the conflicting sections with `<<<<<<< HEAD` and `>>>>>>> otherbranch`. The code between `<<<<<<< HEAD` and `=======` is the version from ____ , and the code between `=======` and `>>>>>>>` is the version from ____.  
   **Answer:** the current branch (HEAD); the other branch (being merged).  
6. **Multiple Choice:** Which Git command would you use to abort a merge in progress (for instance, if you want to cancel resolving and go back to the pre-merge state)?  
   A. `git merge --abort`  
   B. `git merge --stop`  
   C. `git reset --merge HEAD`  
   D. `git abort`  
7. **Scenario:** After resolving conflicts in several files, how do you tell Git that you’ve finished resolving them so you can complete the merge?  
   A. Run `git complete` command.  
   B. Stage the files (`git add resolvedFile.txt`) and then run `git commit` to finalize the merge.  
   C. Just push to remote; Git will know.  
   D. Delete the conflict markers and that's it (Git auto-commits).  
   **Explanation:** After editing, you must `git add` the files (marking them resolved) and commit.  
8. **True or False:** It’s a good practice to run your test suite after resolving a merge conflict, before pushing, to ensure you resolved the conflict in a correct way.  
   **Answer:** True.  
9. **Multiple Choice:** During an interactive rebase, you encounter a conflict. How is resolving that conflict similar to resolving one during a normal merge?  
   A. It’s completely different; you must use special rebase commands to fix.  
   B. It’s the same process: edit the files to resolve, `git add` them, then run `git rebase --continue`.  
   C. You have to abort the rebase; conflicts can’t be resolved.  
   D. Git automatically handles it in rebase, unlike merge.  
   **Explanation:** Resolving conflicts in rebase uses the same manual editing and staging process; then you continue the rebase.  
10. **Scenario (Understanding conflict markers):** You see this in a file after a failed merge:  

    ```  
    <<<<<<< HEAD  
    int timeout = 30;  
    =======  
    int timeout = 45;  
    >>>>>>> origin/main  
    ```  

    What does this mean and how might you resolve it?  
    **Answer:** It means your branch (HEAD) set `timeout` to 30, while the `origin/main` branch set it to 45, causing a conflict. To resolve, decide on the correct value (30 or 45 or another value), edit that line to the chosen value, and remove the conflict markers. Then stage and commit the resolution.

## Module 4 Quiz – Bitbucket Collaboration (Days 7–8)

1. **Multiple Choice:** What is a pull request in the context of Git and Bitbucket?  
   A. A request to clone a repository  
   B. A mechanism to propose and discuss merging a set of commits from one branch into anothe ([Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request#:~:text=In%20their%20simplest%20form%2C%20pull,branch))】  
   C. A command-line Git operation  
   D. The process of pulling the latest changes from remote  
2. **True or False:** On Bitbucket, you can only create pull requests for merging into the main branch.  
   **Answer:** False. (You can create a PR to merge between any two branches in the same repo, or even across forks.)  
3. **Scenario:** Alice pushes a feature branch and opens a PR to merge into main. Bob reviews and requests changes. What should Alice do to address Bob’s feedback via the PR?  
   A. Edit the code on her feature branch, commit, and push again. The PR will update automatically with the new commits.  
   B. Open a brand new PR with a different branch.  
   C. Merge the PR anyway and fix later.  
   D. Add a comment saying “will fix later”.  
   **Explanation:** Pushing new commits to the same branch will update the open PR for further review.  
4. **Multiple Choice:** What is one key benefit of requiring pull requests (with reviews) before merging code?  
   A. It speeds up deployment without any oversight.  
   B. It enables code review, catching bugs or issues and promoting team knowledge sharing before code enters mai ([Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request#:~:text=But%2C%20the%20pull%20request%20is,inside%20of%20the%20pull%20request))】.  
   C. It completely prevents conflicts from ever happening.  
   D. It allows developers to bypass CI checks.  
5. **Fill in the Blank:** Bitbucket’s branch permissions can be configured to prevent direct pushes to certain branches (like `main`), ensuring that all changes come through ______ ______.  
   **Answer:** pull requests.  
6. **Scenario:** Your team uses Bitbucket and Jira. You see in a Jira issue “Development: 1 pull request, 3 commits”. What does this indicate?  
   A. The issue is not yet started.  
   B. There is an open PR related to this Jira issue with 3 commits linke ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Include%20the%20work%20item%20key,to%20your%20Jira%20work%20item)) ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Commits))】.  
   C. Jira has 3 commits of its own.  
   D. Bitbucket is disconnected from Jira.  
7. **True or False:** In Bitbucket, you can configure a repository so that a pull request requires at least one approval and a passing build before it can be merged.  
   **Answer:** True. (Using merge checks in repository settings.)  
8. **Multiple Choice:** If you want to restrict who can merge to the `main` branch, which Bitbucket feature would you use?  
   A. Branch permissions (e.g., only allow specific users or groups to merge to `main` ([Use branch permissions | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/#:~:text=,write%20directly%20to%20main))】.  
   B. Forking  
   C. Snippets  
   D. Issue tracker  
9. **Scenario:** A commit message says “JIRA-101 #comment Fixed typo”. What will happen in Jira because of this (assuming Jira integration is active)?  
   A. The commit will be ignored by Jira.  
   B. A comment will be added to the Jira issue JIRA-101 stating “Fixed typo ([Use Smart Commits | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-smart-commits/#:~:text=Comment))】.  
   C. The Jira issue will be transitioned to “Fixed”.  
   D. Bitbucket will prompt for more info.  
10. **Practical Prompt:** Suppose you want to create a link between a Bitbucket commit and a Jira issue. How should you format your commit message? Give an example.  
    **Answer:** Include the Jira issue key in the commit message. For example: `"PROJ-123: add null check to prevent crash"`. This will associate the commit with Jira issue PROJ-12 ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Commits))】. _(Optionally mention that smart commit syntax like `#close` can be added if you want to transition the issue.)_

## Module 5 Quiz – CI/CD with Bitbucket Pipelines (Days 9–10)

1. **Multiple Choice:** What is Bitbucket Pipelines?  
   A. A manual deployment service  
   B. An integrated CI/CD service in Bitbucket Cloud for automated building, testing, and deploymen ([Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to))】  
   C. A logging tool  
   D. Another name for pull requests  
2. **True or False:** To use Bitbucket Pipelines, you must define your build steps in a file named `bitbucket-pipelines.yml` in your repositor ([Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to))】.  
   **Answer:** True.  
3. **Scenario:** You want your pipeline to run tests every time code is pushed, but only deploy when code is pushed to the main branch. How can you achieve this in bitbucket-pipelines.yml (conceptually)?  
   A. You cannot – you need separate repos.  
   B. Use branch conditions: define a default step for tests on all branches, and under a `branches: main:` section, define the deploy step.  
   C. Hard-code an `if` in the script to check branch name.  
   D. Only run pipelines on main branch.  
   **Explanation:** Using branch-specific pipelines in YAML is the intended approach.  
4. **Multiple Choice:** In a pipeline YAML, what does the following snippet do?  

   ```yaml
   pipelines:  
     default:  
       - step:  
           script:  
             - echo "Hello"  
     branches:  
       develop:  
         - step:  
             script:  
               - echo "Deploying to staging"
   ```  

   A. Always deploys to staging on every push.  
   B. Prints “Hello” on every push, and additionally prints “Deploying to staging” only on pushes to the develop branch.  
   C. It’s invalid YAML.  
   D. It will deploy to staging on every branch except develop.  
5. **Fill in the Blank:** In Bitbucket Pipelines, each step runs in a fresh Docker ______, which provides a clean environment for consistenc ([Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to))】.  
   **Answer:** container (image).  
6. **True or False:** If a pipeline fails (e.g., tests fail), Bitbucket will prevent merging the associated pull request if merge checks are configured to require passing builds.  
   **Answer:** True.  
7. **Scenario:** You have a Node.js project. Which of the following pipeline configurations will install dependencies and run your tests?  
   A.

   ```yaml
   image: node:14  
   pipelines:  
     default:  
       - step: { script: ["npm install", "npm test"] }
   ```  

   B.

   ```yaml
   image: node:14  
   pipelines:  
     default:  
       - step:  
           script:  
             - npm install  
             - npm test
   `` ([ Continuous Integration Tutorial | Atlassian ](https://www.atlassian.com/devops/continuous-delivery-tutorials/continuous-integration-tutorial#:~:text=Test%20automation%20exists%20to%20solve,pushed%20to%20the%20main%20repository))】  
   C. 
   ```yaml
   pipelines:  
     default:  
       - node install && node test
   ```  

   D.

   ```yaml
   image: node:14  
   pipelines:  
     default:  
       - npm install  
       - npm test
   ```  

   **Explanation:** B is correctly formatted (YAML requires nested script lines). A is shorthand that _might_ also be valid (if using JSON-like inline, but B is clearer). C and D are incorrect syntax.  
8. **Multiple Choice:** What is one advantage of integrating Jira with Bitbucket Pipelines deployments?  
   A. Jira can automatically create pipelines for you.  
   B. You can see on a Jira issue if a fix has been deployed to an environment (via the Releases panel and deployment markers).  
   C. Pipelines will run only if the issue is in “In Progress”.  
   D. There’s no direct integration; trick question.  
   **Explanation:** When using deployments in Pipelines, Jira’s Releases or Deployments view can show which issues are deployed in which releases.  
9. **Scenario:** Your pipeline needs to publish a Docker image to Docker Hub. Where should you store your Docker Hub credentials for use in the pipeline?  
   A. In the repository README (in plaintext).  
   B. As secure environment variables configured in Bitbucket Pipeline settings (Repository > Settings > Pipelines environment variables).  
   C. Hard-code them in the bitbucket-pipelines.yml.  
   D. You can’t use Docker Hub with Pipelines.  
   **Answer Explanation:** Storing credentials as secured environment vars is the safe approach.  
10. **Practical Prompt:** Write a simple bitbucket-pipelines.yml snippet that runs a build (you can assume any language) and then, only on the main branch, echoes “Deploying”.  
    **Example Answer:**  

    ```yaml
    pipelines:
      default:
        - step:
            name: Build
            script:
              - echo "Building project"
      branches:
        main:
          - step:
              name: Deploy
              script:
                - echo "Deploying"
    ```  

    This pipeline runs “Building project” on every push (any branch), and if the branch is main, it also runs the “Deploying” step.
