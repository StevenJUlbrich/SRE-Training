# Git Training Curriculum (Self-Paced 2-Week Plan)

## Module 1: Git Basics (Days 1–2)

### Overview of Version Control and Git

Git is a **distributed version control system** that tracks changes in files and allows multiple developers to collaborate on code ([Git - Wikipedia](https://en.wikipedia.org/wiki/Git#:~:text=Git%20,who%20are%20developing%20software%20collaboratively)). Unlike older centralized systems, every user of Git has a full copy of the repository history locally, enabling work offline and fast operations ([Git - Wikipedia](https://en.wikipedia.org/wiki/Git#:~:text=As%20with%20most%20other%20distributed,A)). Git was originally created by Linus Torvalds in 2005 during Linux kernel development ([Git - Wikipedia](https://en.wikipedia.org/wiki/Git#:~:text=Git%20was%20originally%20created%20by,source%20community)). It has since become the most popular source code management tool, with services like **Bitbucket**, **GitHub**, and **GitLab** providing remote hosting for Git repositories.

**Why Git?** Using Git for version control lets you:

- Keep a history of all changes to your code, with each change recorded as a **commit** (snapshot).
- Revert to earlier versions if needed, compare changes, and identify when and where bugs were introduced.
- Branch and merge code to support multiple streams of development (e.g. developing new features without disturbing the main code).
- Collaborate via platforms like Bitbucket (primary focus in this training), GitHub, or GitLab, which add features like pull requests and issue tracking.

### Core Git Concepts

Git’s architecture has a few key concepts:

- **Repository (repo):** The collection of all version-tracked files and the history of changes. Repositories can be local (on your machine) or remote (e.g. on Bitbucket).
- **Working Directory:** The files in your current checkout of the project. This is where you edit code.
- **Staging Area (Index):** A preparatory area where you place changes (using `git add`) that you plan to include in the next commit. This allows grouping specific changes together.
- **Commit:** A snapshot of the repository state, containing staged changes along with a message describing the changes. Each commit has a unique ID (a hash) for reference.
- **Branch:** A movable pointer to a series of commits. Typically, there is a default branch (often named **main** or **master**) that represents the official project history. Other branches can be created to work on features or fixes.
- **Remote:** A copy of the repository hosted on a server (like Bitbucket) that team members push to or pull from. By default, a cloned repository has a remote named “origin”.

### Essential Git Commands and Usage

Below are some of the most commonly used Git commands, with their purpose and usage:

- **git init:** Initialize a new Git repository in the current directory. This creates the `.git` folder that tracks version history. (Use this when starting a project from scratch in Git.)
- **git clone `<repository-url>`:** Clone an existing remote repository from Bitbucket (or GitHub/GitLab) to your local machine. This creates a local working copy linked to the remote.
- **git status:** Show the status of changes as _untracked_ (new files), _modified_ (edited but not yet staged), or _staged_ (added to staging area). This helps you see what will go into the next commit.
- **git add `<file>`:** Stage a file’s changes to the index (staging area). For example, `git add app.js` moves changes from the working directory to staging ([Basic Git Commands | Atlassian Git Tutorial](https://www.atlassian.com/git/glossary#:~:text=Moves%20changes%20from%20the%20working,it%20to%20the%20official%20history)). Use `git add .` to stage all changes in the current directory.
- **git commit -m "Message":** Commit the staged changes to the repository history with a descriptive message. This takes a snapshot of the staged state of the project ([Basic Git Commands | Atlassian Git Tutorial](https://www.atlassian.com/git/glossary#:~:text=Git%20commit)). (Example: `git commit -m "Implement user login feature"`)
- **git commit --amend:** Amend the last commit (for example, if you forgot to include a file or want to edit the commit message) ([Basic Git Commands | Atlassian Git Tutorial](https://www.atlassian.com/git/glossary#:~:text=git%20commit%20)).
- **git log:** View the history of commits. You can add options like `--oneline` (brief) or `--graph` (show branch/merge structure) for readability.
- **git branch:** List all local branches, with an asterisk indicating the current branch. `git branch <name>` creates a new branch, and `git branch -d <name>` deletes a branch.
- **git checkout `<branch>`:** Switch your working directory to the specified branch. This updates your files to match that branch’s latest commit. (In newer versions of Git, the combined `git switch` command can also be used for changing branches.)
- **git checkout -b `<new-branch>`:** Create a new branch and switch to it immediately.
- **git merge `<branch>`:** Merge changes from the specified branch into the current branch. This is how you integrate work from different branches.
- **git pull:** Update your current branch with changes from its remote counterpart. This command is essentially a combination of `git fetch` (download changes) and then `git merge` (merge them into your branch) ([Basic Git Commands | Atlassian Git Tutorial](https://www.atlassian.com/git/glossary#:~:text=Pulling%20is%20the%20automated%20version,Git%20equivalent%20of%20svn%20update)). For example, running `git pull origin main` will fetch and merge updates from the `main` branch on the `origin` remote into your current branch.
- **git push:** Upload your commits from a local branch to the corresponding remote branch on Bitbucket (or other remote). This “publishes” your local commits so others can see them ([Basic Git Commands | Atlassian Git Tutorial](https://www.atlassian.com/git/glossary#:~:text=Comparing%20workflows%3A%20Forking%20workflow)). For example, `git push origin feature-1` sends your local `feature-1` branch commits to the remote repo. (Typically, you need to push new branches explicitly with `--set-upstream` the first time.)
- **git remote -v:** List the remote connections (URLs) for the repository. After a clone, “origin” is the default remote name for the source repository.
- **git fetch:** Download updates from the remote without merging. This retrieves new commits (and branches) from the remote repository, but your local working branch remains unchanged. After fetching, you can inspect the new commits or merge them manually.
- **git diff:** Show differences between commits, or between the working directory and staging area, etc. For example, `git diff HEAD` shows changes in your working directory not yet committed.
- **git reset HEAD `<file>`:** Unstage a file (remove it from staging, but keep the changes in the working directory). Useful if you added something by mistake to the staging area.
- **git restore `<file>`:** Discard changes in the working directory for a file (restoring the last committed version). Use with caution, as changes will be lost.
- **git tag `<tagname>`:** Create a lightweight tag for a specific commit (often used to mark release versions). Tags are like labels on commits – e.g., tagging a commit as `v1.0`.

**Tip:** A typical workflow for adding a new feature might be:

1. Create and switch to a new branch for the feature: `git checkout -b feature/login-page`.
2. Work on the code, periodically using `git status` to check changes.
3. Stage the changes you want to include: `git add .` (or specific files).
4. Commit the changes: `git commit -m "Add login page UI and form"`.
5. Repeat editing and committing as needed.
6. Push the branch to Bitbucket with `git push -u origin feature/login-page` (the first push of a new branch requires the `-u` to set the upstream tracking branch).
7. Open a pull request on Bitbucket to merge your feature branch into the main branch (this will be covered in Module 4).

### Practical Examples

- **Initializing a Repository:**  
  Imagine you’re starting a new project. In your project folder, run `git init`. Now create a file `README.md` and save it. If you run `git status`, Git will show the file as **untracked** (red). Stage it with `git add README.md` (now `git status` shows it as staged in green), then commit it with `git commit -m "Add initial README"`. This sequence creates your first commit in the repository, capturing the state of `README.md` at that point.

- **Cloning and Making a Commit:**  
  For practice, create a repository on Bitbucket (via the Bitbucket website, e.g., an empty repo named “demo-repo”). Then on your local machine, run:  

  ```bash
  git clone https://bitbucket.org/yourusername/demo-repo.git  
  cd demo-repo  
  ```  

  This copies the remote repository to a folder. Create a new file `hello.txt` with some content. Do `git add hello.txt` and `git commit -m "Add hello.txt with greeting"`. Now your local repo has one commit that the Bitbucket remote doesn’t know about yet. Push your commit to Bitbucket with:  

  ```bash
  git push origin main  
  ```  

  (assuming your default branch is `main`). Now if you refresh the Bitbucket page for the repo, you’ll see the `hello.txt` file and the commit in the history.  ([Git Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows#:~:text=Once%20John%20finishes%20his%20feature%2C,git%20push%20command%2C%20like%20so)) ([Git Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows#:~:text=Let%E2%80%99s%20see%20what%20happens%20if,the%20exact%20same%20push%20command))

- **Making Changes and Viewing History:**  
  Edit the `hello.txt` file to add another line. Run `git status` – it will show the file as modified. Use `git diff` to see exactly what changed (the new line will be shown with a `+` prefix). Stage and commit the change (`git add hello.txt`, `git commit -m "Update greeting"`). Now run `git log --oneline` to see a summary of commits: you should see two commits (most recent "Update greeting", and an older "Add hello.txt..."). This history is linear because we have been working on one branch.

- **Introducing a Branch:**  
  Suppose you want to try a different greeting without disturbing the main line of development. Create a new branch `git checkout -b experiment/greeting-2`. This copies the state of `main` into a new branch and switches to it. Edit `hello.txt` with a different message. Commit this change on the new branch. Now the `main` branch and your `experiment/greeting-2` branch have diverged (they have different commits after the point of branching). Use `git checkout main` to switch back to main – you’ll see `hello.txt` revert to the content of the last commit on main. To bring the new greeting into main, you could run `git merge experiment/greeting-2` while on main. Git will combine the histories; if there’s no conflict, the merge happens automatically, creating a new merge commit on main. If there _is_ a conflict, Git will pause the merge and you’ll need to resolve it (see Module 3 for conflict resolution). After merging, you can delete the feature branch with `git branch -d experiment/greeting-2` if you’re done with it.

- **Comparing Bitbucket vs GitHub vs GitLab (basics):** The fundamental Git commands and workflows are the same across all platforms. For example, `git push` to a Bitbucket repository is the same as pushing to GitHub or GitLab. The differences are mainly in the user interface and extra features. In this training, we use Bitbucket Cloud for remote repositories, which integrates nicely with Atlassian tools like Jira. Keep in mind that GitLab uses the term “merge requests” for what Bitbucket/GitHub call “pull requests,” and GitHub’s default branch name is typically **main** (as is Bitbucket’s for new repos), whereas older Git repositories might use **master** by default. We’ll highlight platform-specific differences where relevant.

### Hands-On Lab – Getting Started with Git and Bitbucket

**Goal:** Set up a local Git repository, track changes, and push to Bitbucket. This exercise solidifies the basic Git lifecycle: edit → stage → commit → push.

**Lab Steps:**

1. **Install Git (if not already installed):** Ensure you have Git on your system. On the command line, run `git --version`. If Git is not installed, download it from the official site or use a package manager.
2. **Configure Git:** Set your name and email, which will appear in your commits:  

   ```bash
   git config --global user.name "Your Name"  
   git config --global user.email "you@example.com"  
   ```  

   (These settings are stored in your Git configuration. You only need to do this once per machine.)
3. **Create a Bitbucket Cloud repository:** Log in to Bitbucket and create a new repository (e.g., **git-training-demo**). You can create it empty (no README) for this exercise. Make note of the repository URL (HTTPS URL will be something like `https://bitbucket.org/yourusername/git-training-demo.git`).
4. **Clone the repository:** On your local machine, navigate to a directory where you want the project to live. Run:  

   ```bash
   git clone https://bitbucket.org/yourusername/git-training-demo.git  
   ```  

   This will create a folder `git-training-demo` and initialize it with a local Git repo connected to Bitbucket (the remote is automatically named `origin`).
5. **Create a file and commit:** Change directory into the new project folder: `cd git-training-demo`. Create a new text file named `story.txt` with one line of text (any content). Save the file. Now:  
   - Run `git status` to see the new untracked file.  
   - Stage the file: `git add story.txt`.  
   - Commit the file: `git commit -m "Add story.txt with initial content"`.  
   - Run `git status` again; it should report nothing to commit (clean working directory), meaning your changes are now committed.
6. **Push to Bitbucket:** Push your new commit to the Bitbucket remote:  

   ```bash
   git push origin main  
   ```  

   After this, check your Bitbucket repository page in the browser – you should see `story.txt` and the commit message in the repo’s source and commit list.
7. **Make a change and push again:** Open `story.txt` and add another line (e.g., “This is an update.”). Save the file. Use `git status` to verify Git sees the modification. Stage and commit the change (`git add story.txt`; `git commit -m "Update story.txt"`). Then `git push`. Refresh Bitbucket – the commit history should show the new commit. You can click on commits in Bitbucket to see diffs of what changed.
8. **Explore history and branches (optional):** Run `git log` to view your commit history locally. Try creating a branch (`git checkout -b test-branch`), making an edit on that branch, and committing. Notice that pushing a new branch will require `git push -u origin test-branch` to set the upstream. This is a preview of branching which we will cover next.

By the end of this lab, you have created a repository, made commits, and pushed them to a Bitbucket remote. You can now share this repository URL with teammates or view the code on Bitbucket. These foundations — tracking changes locally and syncing with a remote — are essential for all Git collaboration.

## Module 2: Branching Strategies (GitFlow, Trunk-Based, Feature Branching) (Days 3–4)

### Introduction to Branching Strategies

When working with Git in a team, a **branching strategy** is a set of conventions that defines how your team uses branches and merges to develop features, fix bugs, and release code. A good strategy brings order to collaboration by delineating what each branch is for and when changes should be merged back. Different teams and organizations adopt different workflows to balance speed, stability, and complexity.

In this module, we explore three common Git branching strategies:

1. **Feature Branching (Feature Branch Workflow)** – Each feature or bug fix is developed in its own branch and merged into the main branch when complete.
2. **GitFlow Workflow** – A more structured model with multiple long-lived branches (e.g. main, develop) and support branches (feature, release, hotfix), designed around release cycles.
3. **Trunk-Based Development** – A fast-paced model where developers integrate small, frequent updates directly into a single main (trunk) branch, using short-lived branches or none at all.

Understanding these strategies will help you choose the right workflow for your project and use Bitbucket effectively to enforce it. We will describe each strategy, their pros/cons, and how they relate to Bitbucket (our primary platform) as well as parallels in GitHub/GitLab.

### Feature Branching Workflow

In the **Feature Branch** workflow, all development for a feature or bugfix is done in a dedicated branch, then merged into the main line once complete ([Git Feature Branch Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow#:~:text=The%20Feature%20Branch%20Workflow%20assumes,menu)). The main branch (often called **main** or **master**) always contains production-ready code, and new work is isolated until it’s ready to be integrated.

**Key Characteristics:**

- Two primary branch types: a permanent **main** branch, and many transient **feature** branches.
- Developers create a new branch from main for each feature or issue (e.g. `feature/login-page` or `bugfix/signin-null-pointer`). Work is committed to that branch.
- When the feature is complete (and tested), the branch is merged back into main (often via a pull request for code review). After merging, the feature branch is usually deleted.
- Main thus remains stable; unfinished work never lives directly on main.
- Teams often tag releases on the main branch (e.g., create a Git **tag** like `v1.0` on a particular commit on main).

**Pros:** Simple to understand, and leverages Git’s lightweight branching. It cleanly isolates concurrent work – multiple developers can work on different feature branches without interfering with each other. Code review is naturally integrated by using pull requests when merging to main. This strategy is common on platforms like Bitbucket, GitHub, and GitLab (GitHub Flow is essentially a simplified feature branch model focusing on a single main branch and short-lived feature branches).

**Cons:** There is a need to regularly update feature branches with changes from main (to avoid drifting too far apart). If feature branches live too long, integration can become complex, leading to more merge conflicts.

**In Bitbucket:** Bitbucket supports feature branching natively. You can create branches from the UI or via Git command line, and Bitbucket can be configured with branch permissions and merge checks to ensure feature branches are reviewed before merging. The nomenclature “feature branch” isn’t unique to Bitbucket – GitHub and GitLab use the same concept (GitLab additionally uses “merge request” but the workflow is the same).

**Example Workflow (Feature Branching):**

1. **Branch** – Developer Alice checks out `main` and then creates a new branch: `git checkout -b feature/upgrade-authentication`. This branch is where she will make a set of related commits for the authentication upgrade.
2. **Develop** – Alice commits her changes to `feature/upgrade-authentication` over a couple of days. Meanwhile, Bob is working on a different branch `feature/ui-redesign`. They don’t interfere with each other’s work.
3. **Sync Main** – Periodically, Alice pulls updates from `main` into her feature branch (using `git merge main` or rebase) to incorporate any changes that happened on main while she was developing. This minimizes surprises when merging back.
4. **Push** – Alice pushes her branch to Bitbucket: `git push -u origin feature/upgrade-authentication`.
5. **Pull Request** – Alice creates a pull request in Bitbucket to merge her feature branch into `main`. Teammates review the PR, commenting on code if needed. Bitbucket shows the diff and can even indicate if the branch is up-to-date or if there are merge conflicts with main.
6. **Merge** – After approval and passing CI tests, the PR is merged. Bitbucket adds those commits to the main branch (often as a merge commit or fast-forward merge). The feature branch can then be deleted.
7. **Main Updated** – The main branch now includes the authentication upgrade feature. If Bitbucket Pipelines (CI) is set up, a deployment or build might be triggered by this merge.

Feature branching is straightforward and works well for many teams. It aligns with the idea of “one feature, one branch” and ensures production code is protected in the main branch. It does require discipline to not let branches diverge for too long. Many teams practicing continuous integration and continuous delivery use feature branches but keep them short-lived (sometimes merging multiple times a day).

### GitFlow Workflow

GitFlow is a classic branching strategy introduced by Vincent Driessen in 2010 that became widely adopted, especially for projects with a formal release cycle ([Gitflow Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20is%20an%20alternative%20Git,can%20also%20introduce%20conflicting%20updates)). GitFlow defines a robust framework of branches and rules for how changes flow between them. It uses multiple long-lived branches beyond just main, primarily a **develop** branch in addition to main, and specific branches for features, releases, and hotfixes.

**Key Branches in GitFlow:**

- **main** (or **master**): Holds the code for the latest production release. This is the “sacred” stable branch. Every commit on main is a released version (often tagged with version numbers).
- **develop**: Integrates all completed features for the _next_ release. Think of develop as the staging area for the next production release. Feature branches are merged into develop, not directly into main.
- **feature/*** (e.g., feature/feature-name): Branched off **develop** for developing new features or non-urgent bug fixes. When done, merge back into develop.
- **release/*** (e.g., release/2.0): Branched off develop when preparing a new version release. In this branch, the team focuses on final testing, bug fixes, and versioning for a release. Once ready, the release branch is merged into **main** (to publish the release) _and_ back into **develop** (to incorporate any final fixes).
- **hotfix/*** (e.g., hotfix/critical-issue): Branched off **main** when an urgent fix is needed on top of the latest release. After the fix, the hotfix is merged into **main** (deploying the fix) and also into **develop** (so that develop branch also gets the fix).

**Flow of Work in GitFlow:**

1. Day-to-day development happens on **feature** branches, which are forked from **develop** ([Gitflow Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Step%201)). Multiple features may be in progress concurrently.
2. Completed feature branches merge into **develop**. The develop branch accumulates these changes.
3. When it’s time for a release, a **release** branch is created from develop. Teams do final polishing on this branch: update version numbers, documentation, fix last-minute bugs, etc.
4. The release branch is then merged into **main**. This merge is the moment the code is released (and you tag the commit on main with the release version, e.g., v2.0). The release branch is also merged back into develop (so develop catches up with any fixes made during the release).
5. If bugs in production require immediate patching, a **hotfix** branch is created from main (because main represents production code). After fixing, the hotfix is merged into main (deploying the fix) and into develop (so that the fix is included in the ongoing development line).

**Pros:** GitFlow’s strength is in organizing work for projects with clearly defined release cycles. The main branch is always production-ready, and develop always contains the latest changes for the next release (but not yet released). This separation can be useful for parallel work: e.g., developers can continue adding new features on develop while a release branch is in testing phase. Hotfix branches ensure urgent issues can be addressed without disrupting ongoing work. The workflow is very systematic, reducing confusion about where code should go.

**Cons:** GitFlow introduces complexity. There are many branches to manage and remember. Merging changes multiple times (feature -> develop -> release -> main -> develop) can create overhead. If not disciplined, develop can become a long-lived integration branch that diverges significantly from main, making merges heavy. GitFlow also doesn’t align well with practices like continuous deployment—holding features in develop until a formal release can slow down delivering value. In fast-paced environments or small teams, GitFlow may be overkill and even counterproductive ([Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=match%20at%20L611%20Indeed%2C%20due,continuous%20integration%20and%20continuous%20delivery)) ([Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=GitLab%20Flow%20is%20a%20simpler,feature%20branching%20with%20issue%20tracking)). Atlassian notes that GitFlow has fallen out of favor for many modern DevOps teams in favor of simpler, trunk-based approaches ([Gitflow Workflow | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20is%20a%20legacy%20Git,details%20Gitflow%20for%20historical%20purposes)), in part because GitFlow’s complexity can hinder continuous integration and delivery ([Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=Indeed%2C%20due%20to%20GitFlow%E2%80%99s%20complexity%2C,continuous%20integration%20and%20continuous%20delivery)).

**In Bitbucket:** Bitbucket (and other Git platforms) can support GitFlow easily, as it’s just a set of conventions on branches. Bitbucket even allows you to define a **branching model** in the repository settings, where you can specify branch name prefixes (like `feature/`, `release/`, `hotfix/`) and have Bitbucket create those with one click. Pull requests in GitFlow are typically used for merging feature branches into develop, and for merging release/hotfix branches into their targets. Bitbucket’s **merge checks** and **branch permissions** can be configured to require certain approvals or CI passes on these branches. For example, you can restrict direct commits to main and develop, forcing all changes to go through PRs.

**Visualizing GitFlow:** (Each bullet represents a commit, ➔ indicates a merge)

- Main branch: `o----o--------o` (each circle might be a release, e.g., 1.0, 1.1, 1.2)
- Develop branch: `o---------o-------o` (accumulating features for next releases)
- Feature branches: diverge from develop and merge back into develop:
  - `develop o---o---o➔` (merge feature1) `---o`
  - `develop o---------o➔` (merge feature2)  
- Release branch: created off develop, then merged to main and develop:
  - `develop ----o (release branch) ----➔ main` (release merges to main) and `➔ develop` (merged back).
- Hotfix branch: off main, merged to main and develop:
  - `main ---o (hotfix) ---➔ main` (hotfix release) and `➔ develop`.

**Note:** The above is a textual representation; refer to diagrams in external GitFlow tutorials for a clearer picture.

**Example Scenario (GitFlow in action):**

- The project is currently at version 1.0 on `main`. The `develop` branch has accumulated several features for the upcoming 1.1.
- Alice finishes “Feature A” on a `feature/A` branch (based off develop). She opens a PR and merges it into `develop`.
- Bob is working on “Feature B” on `feature/B`. Meanwhile, it’s decided to start preparing the 1.1 release. A `release/1.1` branch is created from the current `develop`. Carol, the release manager, begins testing on `release/1.1` and finds a minor bug to fix there.
- Bob finishes Feature B and merges `feature/B` into `develop`. (Feature B will not be in release 1.1 if the release branch was cut before B was merged; it will be part of the next release.)
- Carol fixes the bug on `release/1.1`. When testing is complete, she merges `release/1.1` into `main` (tagging `v1.1` on that commit) and also merges the changes from `release/1.1` back into `develop` (so develop now has the bugfix too, and is up-to-date).
- Production (main) is now at 1.1. Later, a serious issue is discovered in 1.1 in production. Dave creates a `hotfix/issue-123` branch from `main`, fixes the issue, and merges it back into `main` (tagging `v1.1.1`) and into `develop` (so develop, which might have moved on with new features, also has this fix).
- The team continues developing features on develop for version 1.2, and the cycle repeats.

GitFlow provides clear segregation: main (production), develop (next release), feature branches (in-progress work), release (stabilization), hotfix (urgent fixes). If your project requires maintaining multiple versions (e.g., a current release and a next major release in parallel), GitFlow or a variant might be useful. However, if your team deploys continuously or wants simplicity, you might lean toward feature branching or trunk-based development.

### Trunk-Based Development

**Trunk-Based Development (TBD)** is a branching model that emphasizes a single, central branch (often called “trunk”, analogous to main) where all developers integrate their changes rapidly and continuously ([Trunk-based Development | Atlassian](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development#:~:text=Trunk,software%20delivery%20and%20organizational%20performance)) ([Trunk-based Development | Atlassian](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development#:~:text=Gitflow%2C%20which%20was%20popularized%20first%2C,to%20iterate%20quickly%20and%20implement%C2%A0CI%2FCD)). In its purest form, trunk-based development means **developers commit directly to the main branch**, avoiding long-lived side branches altogether. In practice, teams often still use short-lived feature branches or use feature flags, but the key is that branches are extremely short-lived (hours or a day or two, not weeks), and code flows into the trunk quickly.

**Key Principles:**

- There is **one primary branch** (trunk/main) that all work converges into. This branch is always kept in a deployable state.
- Developers collaborate by integrating small updates very frequently (often multiple times a day) to trunk. This reduces integration challenges because changes are small and conflicts are resolved continuously.
- Feature development can still happen on branches, but these branches are usually short-lived (they might only exist for the duration of a code review) and merged as soon as possible. Some teams using trunk-based dev forego branches entirely by committing straight to main and using feature toggles to disable unfinished features in production.
- There are no separate “develop” or “release” branches. For a release, you might directly tag a commit on main as a release version. If a hotfix is needed, it can be committed to main (possibly under a feature flag if needed to turn it off/on).
- Continuous Integration (CI) is essential: every commit to trunk triggers automated builds and tests (and possibly deployments) to ensure nothing is broken. This gives fast feedback to developers.

**Pros:** Trunk-based development is **CI/CD friendly** – it’s recommended for achieving continuous integration and continuous delivery ([Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=Consequently%2C%20trunk,CD)). By integrating changes continuously, you avoid the “merge hell” that can happen when branches diverge for too long ([Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=Because%20trunk,any%20conflicts%20that%20may%20arise)). It simplifies the repository structure: no complex branch management or lengthy merge cycles. Teams can deliver updates to users quickly and frequently. It enforces discipline to keep code always in a deployable state (often via practices like feature flags for incomplete features).

**Cons:** It requires a high level of team coordination and maturity. Committing straight to main or very frequently merging means everyone must be careful not to break the build/tests. Without proper automated testing, trunk-based development can lead to instability. Also, for organizations that need to support multiple versions (for example, a long-term support release and a current release), having only one branch could be limiting – trunk-based might be better suited when you always deploy the latest version. Code review can still happen (e.g., using pull requests on short branches or using paired programming) but teams must ensure the rapid pace doesn’t bypass proper review or testing.

**In Bitbucket:** Trunk-based development can be implemented by using the main branch as the integration point. You might still use pull requests for each change (from a short-lived branch) but the expectation is that PRs are small and merged quickly. Bitbucket’s branch permissions might be configured to restrict pushing directly to main (so that all changes go through PRs with CI checks). Unlike GitFlow, you wouldn’t have persistent develop or release branches. Bitbucket Pipelines (CI/CD) would run on each commit to main, possibly deploying to a staging or production environment as appropriate. On GitHub/GitLab, similar settings are used (in fact, GitHub’s own workflow “GitHub Flow” is essentially trunk-based: all changes go to main via PRs, and deployments are continuous).

**Comparison:** If GitFlow is like a well-planned highway system with multiple lanes and exit ramps, trunk-based is like a single high-speed rail line. Everyone is on the same track, so collisions must be avoided by keeping each train (change) small and well-timed. Google and other large tech companies have famously used trunk-based development on massive codebases to great success, relying on automation to keep things running smoothly.

**Example Workflow (Trunk-Based):**

- The repository has one main branch: `main`. All developers branch off `main` for their tasks, but only briefly.
- Developer Alice starts working on a small feature. She could commit directly to main (perhaps behind a feature flag), or she creates a branch `alice/small-feature` for a very short time. She makes a couple of commits and within a few hours opens a pull request and merges into `main`. The feature is behind a toggle, so even though the code is in main, it’s not active until ready.
- Developer Bob, concurrently, is fixing a bug. He directly commits the fix to `main` (with a good test). Continuous integration runs, all tests pass, and his fix is deployed immediately in the next deployment cycle.
- There are no “integration hell” moments because Alice and Bob integrate their changes the same day they start them. If a conflict arises, they resolve it quickly since the context is fresh.
- The team cuts releases simply by tagging the `main` branch at certain points (or every commit could be a potential release). If something must be patched, it’s just another commit on `main` (or a revert commit if something needs to be undone).
- Over time, this strategy produces a linear-ish history on main. Developers might use techniques like **feature flags** to ensure incomplete features do not affect end-users even though code lives in main.

**When to use which strategy?** It depends on your project needs:

- **Trunk-Based** is ideal for rapid delivery and continuous deployment environments. It aligns with agile and DevOps practices where you ship small increments frequently. Bitbucket Pipelines and Jira can be used to track this constant flow (e.g., each commit could reference a Jira issue that moves to “Done” when the commit is merged).
- **GitFlow** is useful if you have strict release cycles, need to maintain multiple versions, or prefer structured isolation of work until release. It’s heavier weight and generally not needed for small teams or cloud services deploying often.
- **Feature Branching** (sometimes called GitHub Flow when there’s just main + short branches) is a middle ground. It’s very common because it’s simpler than GitFlow but still provides isolation of work. Many teams use feature branches with PR reviews and practice a form of trunk-based by keeping those branches short-lived.
- **GitLab Flow** (not a focus here, but worth a mention) is another variant which ties branches to environments (development, staging, production branches) – it attempts to unify ideas of feature branching with environment-specific branches. If you come across the term, know it’s yet another strategy blending concepts of GitFlow and trunk.

### Hands-On Lab – Experimenting with Branching Strategies

In this lab, you will simulate elements of the different branching strategies on your own, using a single repository. This will help you understand how code flows in each model.

**Preparation:** You can continue using the repository from Module 1 (or create a new one) on Bitbucket. Ensure you have at least one more file besides README (for example, use the `story.txt` from earlier).

### Lab Part A: Feature Branch and Pull Request

1. **Feature Branch Creation:** Make sure you’re on the `main` branch (`git checkout main`). Create a new branch for a hypothetical feature:  

   ```bash
   git checkout -b feature/cool-feature
   ```  

2. **Do Work on Feature:** Open `story.txt` and add a line “Feature: Cool feature implemented.” Save it. Commit this change on the feature branch:  

   ```bash
   git add story.txt  
   git commit -m "Add cool feature line to story"  
   ```  

3. **Simulate Collaboration (optional):** If you have a collaborator or want to simulate one, you could have them also commit to this feature branch or to main while you’re working, to later practice merging.
4. **Push Feature Branch:** Push your feature branch to Bitbucket:  

   ```bash
   git push -u origin feature/cool-feature  
   ```  

   Go to Bitbucket in your browser. You should see the new branch under the repository’s branches. Initiate a Pull Request to merge `feature/cool-feature` into `main`.
5. **Review and Merge via Bitbucket:** In the PR interface, you can see the diff of changes. (If you have a teammate, they would review; if not, just note the process.) Merge the pull request. Bitbucket will merge the branch into main. Fetch the changes back to your local main:  

   ```bash
   git checkout main && git pull origin main  
   ```  

   Confirm that the changes from the feature branch are now in main (the new line appears in `story.txt` on main). The feature branch can now be deleted:  

   ```bash
   git branch -d feature/cool-feature  
   git push origin --delete feature/cool-feature  
   ```  

   (Delete the remote branch as well to keep things tidy.)

This part simulated a simple feature branch workflow: isolated work, code review, and merge into main.

**Lab Part B: Simulate GitFlow main vs develop:**

1. **Create a develop branch:** In a GitFlow scenario, `develop` is created off main initially. Do:  

   ```bash
   git checkout -b develop  
   git push -u origin develop  
   ```  

   Now your repository has a `main` (production) and `develop` (integration) branch.
2. **Feature on develop:** Create a feature branch from develop, e.g. `git checkout -b feature/awesome-feature develop`. Make a change in `story.txt` (e.g., add “This is awesome feature on develop.”), commit it, and merge it back into develop (you can merge via command line or create a PR from feature->develop in Bitbucket).
3. **Release branch:** Imagine the `develop` now has code ready to release. Create a release branch:  

   ```bash
   git checkout -b release/1.0 develop  
   ```  

   On this release branch, simulate a version bump: open `README.md` or create a `VERSION.txt` file indicating version 1.0. Commit this change (`git add VERSION.txt; git commit -m "Set version to 1.0"`). Merge this release into main:  

   ```bash
   git checkout main  
   git merge --no-ff release/1.0 -m "Merge release 1.0 to main"  
   ```  

   (We use `--no-ff` to force a merge commit, simulating how a release might be merged.) Tag this commit as v1.0: `git tag -a v1.0 -m "Release 1.0"`. Also, merge the release back into develop:  

   ```bash
   git checkout develop  
   git merge --no-ff release/1.0 -m "Merge release 1.0 back into develop"  
   ```  

   Now `develop` has the version bump as well. You can delete the release branch (`git branch -d release/1.0`).
4. **Hotfix:** Immediately simulate a hotfix: Switch to main and create a hotfix branch:  

   ```bash
   git checkout main  
   git checkout -b hotfix/issue-001  
   ```  

   Fix something (e.g., add a line “Hotfix applied” in `story.txt` or fix a typo). Commit the fix. Merge it into main:  

   ```bash
   git checkout main  
   git merge hotfix/issue-001 -m "Merge hotfix issue-001"  
   git tag -a v1.0.1 -m "Release 1.0.1 hotfix"  
   ```  

   Then merge into develop as well:  

   ```bash
   git checkout develop  
   git merge hotfix/issue-001 -m "Merge hotfix issue-001 into develop"  
   ```  

   Delete the hotfix branch.

Observe how the commit history looks. It will be more complex (especially if you visualize with `git log --graph --all`). This is expected in GitFlow. You practiced the mechanics of multiple branches. (In a real environment, you’d likely use PRs and have multiple people on different branches, but this solo simulation still gives insight.)

**Lab Part C: Trunk-Based (Continuous Integration) practice:**

1. Go back to working just with the main branch. Make sure `main` is up-to-date with all changes (`git checkout main; git pull`).
2. Enable Bitbucket Pipelines for this repository (if not already on). In Bitbucket, add a simple pipeline that runs on every push (we will cover CI in Module 5, but for now, a sample pipeline can just echo a message). For example, add a file `bitbucket-pipelines.yml` in the root with:  

   ```yaml
   pipelines: 
     default: 
       - step: 
           script: 
             - echo "CI test: Build successful" 
   ```  

   Commit this file on main and push. This simulates that every commit triggers CI.
3. Now try a rapid small change: edit `story.txt` by adding a word, commit directly to main (this is mimicking an immediate trunk commit), and push. Watch Bitbucket Pipelines run the build. It should pass (echo script runs). This is the essence of trunk-based: small commit, integrate, test immediately.
4. Optionally, try using a feature flag concept: Add a line like `FEATURE_X_ENABLED = false` in a config file on main (to “turn off” a feature by default). Then create a branch to add code for “Feature X” that only runs if that flag is true. Merge it quickly into main even if FEATURE_X_ENABLED is false, meaning the code is in main but inactive. Later you can simulate "turning it on" by changing the flag to true in a quick commit on main. This mimics how teams add incomplete features safely in trunk-based development.

Through these lab exercises, you have touched on all three workflows:

- **Feature branching:** isolated branch merged via PR.
- **GitFlow:** multiple long-lived branches with a release cycle.
- **Trunk-based:** rapid direct integration into main.

Think about which felt simplest and which provides more control. There’s no one-size-fits-all solution – the goal is to find a balance that suits your team’s size, release frequency, and risk tolerance. Bitbucket can accommodate all these workflows with its tools (branches, pull requests, permissions, and CI pipelines).

## Module 3: Merge Conflicts and Resolution Techniques (Days 5–6)

### Understanding Merge Conflicts

A **merge conflict** occurs when Git cannot automatically reconcile differences between two commits during a merge or rebase operation. This typically happens when changes from different branches overlap in the same part of a file. For example, if you edited the same line of a file on two branches, Git won’t know whose change to keep during a merge – this situation is a conflict that needs manual intervention ([Resolving a merge conflict using the command line - GitHub Docs](https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line#:~:text=Merge%20conflicts%20occur%20when%20competing,information%2C%20see%20About%20merge%20conflicts)). Conflicts can also arise if one branch edits a file while another branch deletes it, or any scenario where the history has diverged and changes are incompatible.

In simpler terms, Git will flag a conflict when it encounters **competing changes**:

- **Same line conflict:** Two branches modify the same lines differently ([Resolving a merge conflict using the command line - GitHub Docs](https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line#:~:text=Merge%20conflicts%20occur%20when%20competing,information%2C%20see%20About%20merge%20conflicts)).
- **Delete vs modify:** One branch deletes a file that another branch has modified.
- **Complex changes:** Overlapping changes in a region of a file or changes to file structure that cannot be merged automatically.

When a merge conflict occurs, Git pauses the merge process and gives you an opportunity to resolve the conflicts manually. It’s important to note that merge conflicts are a normal part of collaboration – they _will_ happen occasionally even with good planning, so learning to resolve them is essential.

### Why Merge Conflicts Occur and How to Minimize Them

Merge conflicts often happen due to lack of communication or long-lived branches:

- **Long-Lived Branches:** The longer two branches exist without merging, the higher the chance that two people will touch the same code in different ways. Frequent integration (as in trunk-based or short feature branches) reduces this risk.
- **Large Commits:** If a single commit or branch has massive changes (like a refactor touching many files), it increases the surface area for conflict with others’ changes.
- **Multiple People on Same Area:** If multiple team members are working in the same file or component, conflicts are more likely. This can be mitigated by coordinating who works on what, or breaking work into distinct parts.

To minimize conflicts:

- **Integrate Often:** Pull from the main branch (or shared branch) regularly into your working branch. This way you resolve small conflicts incrementally rather than a huge one at the end.
- **Communicate:** Let others know if you’re making changes in a tricky part of the code. They might avoid touching the same area or at least be aware.
- **Use Smaller Focused Commits/Branches:** The smaller your changes, the less likely they collide with someone else’s. Also, it’s easier to resolve a conflict in a small change than one that spans many files.
- **Leverage Tools:** Use git’s ability to highlight and even automatically resolve trivial conflicts. And when merging, consider if rebasing would simplify the history (though note rebasing can also lead to conflicts, but you resolve them on your side before pushing).
- **Feature Flags:** In trunk-based development, feature flags allow merging incomplete features (to avoid long separate branches) and thus reduce long divergence, though conflict can still happen, at least code is in main sooner.

Despite best practices, some conflicts are inevitable. Next, we’ll see how to handle them.

### Merge vs. Rebase (Conflict Context)

Both **git merge** and **git rebase** can result in conflicts, but the approach to resolution is the same – you must edit the code to reconcile differences. A quick note:

- `git merge` combines two branches by creating a merge commit. If conflicts occur, they must be resolved, then `git commit` to finalize the merge.
- `git rebase` moves your commits onto a new base (often used to incorporate upstream changes by replaying your changes on top). If a commit in the rebase sequence conflicts with the new base, Git will stop at that commit and let you fix the conflict, then continue (`git rebase --continue`).

Regardless of method, the conflict markers and resolution process are similar.

### How Git Marks Conflicts

When a conflict happens, Git modifies the affected files by inserting **conflict markers** directly into the file to show you the two versions of code in conflict. It looks like this in the file:

```diff
<<<<<<< HEAD
// Your changes (the version from your current branch, HEAD)
=======
// Their changes (the version from the branch you are merging in)
>>>>>>> branch-name
```

The section between `<<<<<<< HEAD` and `=======` is the code from your side (HEAD, the branch you had checked out when you initiated the merge), and the section between `=======` and `>>>>>>> branch-name` is the code from the other branch (here labeled by its name) ([How to resolve merge conflicts in Git](https://graphite.dev/guides/how-to-resolve-merge-conflicts-in-git#:~:text=Terminal)). Your task as the developer is to edit this file and decide what the code should finally look like.

For example, if both branches edited a line in a function:

```diff
<<<<<<< HEAD
total = calculate_sum(data);  // code on your branch
=======
total = computeSum(data);     // code on other branch
>>>>>>> feature/new-api
```

You need to choose which implementation to keep (or combine them in some way). Maybe the other branch’s `computeSum` function is the updated one you want, so you would accept their change and possibly adjust it. Or maybe both changes are needed, in which case you might refactor that section to incorporate both ideas.

**Important:** The conflict markers `<<<<<<<`, `=======`, `>>>>>>>` are not valid code – they are there to guide you. You must remove these markers after resolving, leaving the file in a valid state with the chosen code.

### Techniques to Resolve Merge Conflicts

1. **Manual Edit (Most Common):** Open the conflicted file in a text editor or IDE. Look for the conflict markers. Decide what the code should be. You might:
   - Pick one side’s changes over the other.
   - Combine the changes (for example, if both added different lines that don’t actually conflict logically, you might keep both).
   - Rewrite the section entirely in a new way that satisfies both purposes.
   After editing, remove all the conflict markers. Save the file. Then stage the resolved file (`git add <file>`).
2. **Use a Merge Tool:** Git can launch visual merge tools (like KDiff3, Beyond Compare, WinMerge, VS Code’s merge editor, etc.) via the command `git mergetool`. These tools present a three-pane view: your version, their version, and a result pane where you craft the merged output. They can make conflict resolution more intuitive by showing differences side by side. Modern IDEs (e.g., IntelliJ, Visual Studio Code) have built-in merge conflict resolvers that highlight conflicts and provide buttons to choose one side or the other.
3. **Ours/Theirs Merge Strategy (for specific cases):** Git has some merge strategies where you can tell it to favor one side automatically. For example, `git merge -X ours <branch>` will favor the current branch’s changes on conflicted hunks, and `-X theirs` would favor the incoming branch’s changes ([Git Merge Theirs Explained - Built In](https://builtin.com/articles/git-merge-theirs#:~:text=Git%20Merge%20Theirs%20Explained%20,branch%2C%20resolving%20git%20merge%20conflicts)). However, use these with caution and understanding – they automatically resolve by discarding one side, which might not be what you always want. This is more for scenarios where you know one branch should override (e.g., perhaps in a hotfix scenario you want to take “theirs” for everything).
4. **Abort or Reset (if needed):** If a merge is overwhelming or mistaken, you can always abort it and try again. Running `git merge --abort` (during a merge conflict) will restore the state before the merge attempt. Similarly, `git rebase --abort` during a rebase will go back to pre-rebase state. This is useful if you want to get back and maybe approach the integration differently (or merge in smaller pieces).

After resolving conflicts in all files:

- Use `git status` to ensure all conflicted files are staged (marked as resolved).
- Complete the merge by committing (`git commit` if it’s a merge, which you may have to do manually if you didn’t use `git mergetool` which often stages for you; for a rebase, use `git rebase --continue`).
- The conflict resolution will now be part of the new commit.

### Example of Resolving a Conflict (Manual Resolution)

Let’s say we have a file **config.txt** that on branch A (HEAD) contains:

```text
timeout=30  
mode=active  
```

and on branch B (the branch being merged) it contains:

```text
timeout=45  
mode=active  
```

These changes conflict on the same line (timeout value). After attempting a merge, Git will pause and mark the file like so:

```diff
<<<<<<< HEAD
timeout=30
mode=active
=======
timeout=45
mode=active
>>>>>>> branch-B
```

We need to decide the intended timeout. Suppose the team decides the timeout should be 45 (the change from branch B). We edit the file to that value and remove the markers:

```text
timeout=45  
mode=active  
```

Now the conflict is resolved according to our decision. We save the file, `git add config.txt`, and `git commit` to finalize the merge (Git will use a default merge message if you didn’t specify one).

In another scenario, if both branches added a different entry to a list in a file, the resolution might be to keep both entries. For instance:

```diff
<<<<<<< HEAD
fruits = ["Apple", "Banana", "Cherry"]
=======
fruits = ["Apple", "Banana", "Date"]
>>>>>>> new-fruit
```

Maybe both intended to add a fruit. The resolved file should include both "Cherry" and "Date":

```python
fruits = ["Apple", "Banana", "Cherry", "Date"]
```

Thus, we merged the lists. We then remove markers and save.

 ([How to resolve merge conflicts in Git](https://graphite.dev/guides/how-to-resolve-merge-conflicts-in-git#:~:text=Conflicted%20files%20will%20contain%20sections,marked%20like%20this))In summary, resolving a conflict means **choosing the final content** for the affected file that satisfies what both sides were trying to achieve, and making sure the code compiles/passes tests after resolution.

### After Resolving: Testing and Commit History

After you resolve conflicts and commit, it’s wise to run your test suite or compile the code to ensure that the merged result is working as expected. Because conflicts imply human decision, there’s a risk of introducing mistakes (like omitting necessary code). Running tests or the application can catch these issues.

Your repository’s history will show the merge commit (if you merged) or the rebased commits (if you rebased). If you did a merge commit, that commit will include both parents (the two branches that were merged). If you rebased, your commits will now be on top of the other branch as if they were written after it.

### Dealing with Conflicts in Pull Requests (on Bitbucket/GitHub)

When using pull requests, sometimes the PR will indicate it “can’t be merged automatically” due to conflicts. Bitbucket (and GitHub) will list the files in conflict. You typically need to pull the latest changes to your local, merge locally, resolve conflicts, then push the resolved merge. Some platforms allow you to resolve simple text conflicts in the web interface (GitHub has a web editor for conflicts, Bitbucket Server (Data Center) has an interface for conflict resolution as well). However, for anything non-trivial, it’s usually easier to handle it in your development environment where you have your tools.

**Rebasing to avoid conflicts:** Another practice is to rebase your feature branch onto the latest main before opening (or updating) a PR. By doing `git pull --rebase origin main` on your branch, you incorporate the latest changes linearly, potentially resolving conflicts yourself, and then push. This can make the eventual merge a fast-forward with no conflict. Bitbucket can be configured to fast-forward merge if no conflicts, which results in a cleaner history (no merge commits). But rebase vs merge is often a team preference – the important part is conflicts must be handled one way or another.

### Hands-On Lab – Creating and Resolving a Merge Conflict

This lab will guide you through intentionally creating a merge conflict and then resolving it. This exercise is best done with a collaborator, but you can simulate both roles yourself by using two branches.

**Scenario:** Two developers, Alice and Bob, will both edit the same file (for example, `story.txt` from earlier) in different ways, then try to merge their changes.

**Steps:**

1. Ensure you have a repository with a file to conflict on. We’ll use `story.txt` again. Make sure the file has at least one line of text that we can modify.
2. **Branch for Alice and Bob:**  
   - Alice’s branch: `git checkout -b alice-edit`.  
   - Bob’s branch: Keep `main` for Bob, or create `bob-edit` from main. To simulate concurrently, open another terminal as “Bob” or just switch branches later.
3. **Alice’s change:** On branch `alice-edit`, open `story.txt`. Append a line: “Alice was here.” Commit this change:  

   ```bash
   git add story.txt  
   git commit -m "Alice adds her line"  
   ```  

   Don’t merge yet; Alice’s change is isolated on her branch.
4. **Bob’s change:** Switch to the main branch (or `bob-edit` if you made one):  

   ```bash
   git checkout main  
   ```  

   Open `story.txt` and (in the same location Alice did, e.g., end of file or same paragraph) append a _different_ line: “Bob was here.” Save and commit:  

   ```bash
   git add story.txt  
   git commit -m "Bob adds his line"  
   ```  

   Now main has Bob’s change, Alice’s branch has Alice’s change, both to the same area of the file.
5. **Merge (introduce conflict):** Try to merge Alice’s branch into main:  

   ```bash
   git checkout main  
   git merge alice-edit  
   ```  

   Git will output a conflict message because both branches edited `story.txt`. You will see something like:  
   `Auto-merging story.txt`  
   `CONFLICT (content): Merge conflict in story.txt`  
   `Automatic merge failed; fix conflicts and then commit the result.`  
   Run `git status` and note that `story.txt` is in conflict.
6. **Resolve the conflict:** Open `story.txt`. It will contain conflict markers around the area with Alice’s and Bob’s lines. For example:  

   ```diff
   <<<<<<< HEAD
   ... (earlier content) ...  
   Bob was here.
   =======
   ... (earlier content) ...  
   Alice was here.
   >>>>>>> alice-edit
   ```  

   Because both appended at the end, it might look like both lines under conflict. The correct resolution in this scenario might be to **keep both lines** (assuming they don’t actually conflict in meaning). Decide on an order – perhaps we want “Alice was here.” followed by “Bob was here.” Remove the markers and make it:  

   ```text
   ... (earlier content) ...  
   Alice was here.  
   Bob was here.
   ```  

   Save the file.
7. **Mark as resolved:** After editing, run `git add story.txt`. This tells Git that the conflict in that file is resolved. (Git removes the conflict markers from its staging area.)
8. **Complete the merge:** Commit the merge resolution:  

   ```bash
   git commit -m "Resolve conflict between Alice's and Bob's changes"
   ```  

   If you omit the `-m`, Git will open a default commit message in your editor, often listing which files were merged. You can write a message or accept the default.
9. **Verify:** Run `git log` – you should see the merge commit. The content of `story.txt` on main should now have both Alice’s and Bob’s lines, in the order you decided. You have successfully resolved the conflict.
10. **Push and clean up:** Push the updated main to Bitbucket: `git push origin main`. If Alice’s branch also was pushed (or if this were a PR scenario), you would close the PR now or mark it merged. You can delete the `alice-edit` branch with `git branch -d alice-edit` (and `git push origin --delete alice-edit` if it was on the remote).

**Simulate alternative outcome:** For learning, you might repeat and instead of keeping both lines, choose one over the other to see how that works. Or move lines around. The key is ensuring the final file is exactly how you want it and free of conflict markers.

**Using a GUI tool (optional):** If you have an IDE like VS Code, try triggering the conflict again and using the GUI to accept incoming vs current changes. This gives a feel for different tooling.

After this lab, you should be comfortable recognizing conflict markers and following the process: identify conflicting sections, decide and edit, stage, and commit. Always remember to test your code after a merge. In our trivial example, it’s just text lines, but in real projects, conflicts might be in code logic, so run the application or tests to confirm everything still works.

Merge conflicts can be intimidating at first, but with practice, they become just another part of development. The key is to stay calm, understand what each side was doing, and craft a solution that integrates the intents of both sets of changes.

## Module 4: Bitbucket Collaboration (Pull Requests, Permissions, Jira Integration) (Days 7–8)

### Collaborative Workflows with Pull Requests

In modern development, simply pushing code to a shared repository isn’t the end of the story – teams use **Pull Requests (PRs)** (also called _Merge Requests_ in GitLab) as a mechanism for code review and collaboration. A pull request is a formal request to merge changes from one branch into another, and it provides a space to discuss those changes.

**What is a Pull Request?** It’s essentially a discussion thread around a proposed code change. When you open a PR, Bitbucket shows the diffs (changes) your branch introduces, and your teammates can comment on specific lines, ask questions, or approve the changes. The PR can be updated if you push additional commits to the branch. Ultimately, the PR is either merged (bringing the changes into the target branch) or declined if the changes won’t be integrated.

Pull requests make collaboration more efficient by providing a dedicated place to review code before it integrates into the main codebase ([Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request#:~:text=In%20their%20simplest%20form%2C%20pull,branch)). Compared to emailing patch files or just sharing a branch, PRs have the advantage of being tightly integrated with the repository: you see exactly what will change, CI results for the branch, and you can even enforce that certain conditions (like approvals or passing builds) are met before merging.

 ([Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request#:~:text=Pull%20requests%20are%20a%20feature,them%20into%20the%20official%20project))Bitbucket’s PR interface is user-friendly, showing diffs, commits, comments, and build statuses in one place. It tracks all activity related to the merge request, serving as a record of why certain changes were made if you look back later.

**Basic Pull Request Workflow in Bitbucket:**

1. A developer pushes a branch with their changes to Bitbucket.
2. In Bitbucket, they create a Pull Request, specifying the source branch (e.g., `feature/new-login`) and destination branch (e.g., `main` or `develop`).
3. They add reviewers (team members) to the PR. Those reviewers get notified (e.g., by email or in their Bitbucket dashboard).
4. Reviewers examine the code differences. They can leave comments or suggestions. They might request changes, which the author can address by pushing new commits.
5. When reviewers are satisfied, they approve the PR. Bitbucket can show how many approvals have been given.
6. Integration with CI: Bitbucket Pipelines or other CI systems will often run tests on the PR branch. The PR will display the build status (e.g., ✅ passing or ❌ failing). Many teams require that all builds pass before a PR can be merged.
7. Once approvals are in (and CI is green), the code is merged. Bitbucket offers merge options: a normal merge commit, a squash merge (squash all commits into one), or a rebase merge depending on settings. After merging, Bitbucket can automatically delete the source branch if desired.
8. The PR is now closed, and the changes are part of the target branch. Everyone can sync and get the updates.

**Pull Request Example Scenario:**

- Developer Carol works on a branch `feature/refactor-logging`. She pushes her branch and opens a PR to merge into `develop`. She adds Dave and Erin as reviewers.
- Dave reviews and sees a potential issue in the error handling. He comments on the specific line in the PR, suggesting a change.
- Carol replies to Dave’s comment, perhaps asking a clarification or agreeing. She then pushes a new commit to fix the issue. The PR automatically updates with the new commit; Dave and Erin see the update.
- Erin approves the PR (she found everything in order). Dave, after seeing the fix, also approves.
- Meanwhile, Bitbucket Pipelines ran the test suite on Carol’s branch and shows “✅ 1 successful check” on the PR.
- With two approvals and CI passing, Carol (or a team lead) clicks **Merge** in Bitbucket. The branch’s commits are merged into develop. Bitbucket adds a merge commit by default (unless configured otherwise). The PR gets marked as merged.
- The team’s Jira is integrated, and Carol included the Jira issue key in the PR title. The Jira issue automatically transitions to “Done” (for example) because the PR was merged (this uses Jira+Bitbucket integration features).

 ([Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request#:~:text=1,branch%20in%20their%20local%20repo))The general process is: branch -> push -> pull request -> review/discuss -> refine -> merge and close ([Pull Requests | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/making-a-pull-request#:~:text=1,branch%20in%20their%20local%20repo)).

**Tips for Effective Pull Requests:**

- Keep PRs focused and relatively small. It’s easier to review 5 files changed than 50. If a PR is too large, consider breaking it into logical parts.
- Write a clear PR **title and description**. The title often becomes part of the commit message on merge. In the description, mention what the change is about, link to Jira issues, and include screenshots or GIFs for UI changes if applicable (Bitbucket allows embedding images in PR descriptions/comments).
- Use Bitbucket’s **mention** system: you can mention users by @username in comments to get their attention on specific points.
- If the PR is still in progress (not ready for full review), mark it as a **Draft Pull Request** (Bitbucket Cloud recently introduced a “draft” status) so reviewers know not to merge yet.
- Resolve conversations: When a comment is addressed, you can “resolve” it in the UI, which hides it from the active list. This helps to keep track of what’s still open.
- Squash merge if appropriate: If your branch has many “fix typo” or intermediate commits, you might squash on merge to keep main history clean. Bitbucket allows this if enabled.
- Remember, pull requests are not just about merging code, but also knowledge sharing. They allow others to see and understand changes, even if they don’t deeply review every line. Over time, this improves overall code quality and team familiarity with the codebase.

 ([Draft pull requests | Bitbucket Data Center 9.6 | Atlassian Documentation](https://confluence.atlassian.com/display/BitbucketServer/Draft+pull+requests)) _Figure: Bitbucket pull request interface (showing a draft PR with indicators for draft status and a "Mark as ready" button). Pull requests in Bitbucket provide an overview of changes, discussion threads, and integrate build status checks, making code reviews collaborative and transparent._

**Comparing with GitHub/GitLab:** All these platforms use a very similar pull request model. GitHub also calls them “Pull Requests” and has largely the same features. GitLab calls them “Merge Requests” but the concept is identical. One minor difference: Bitbucket and GitLab let you create a PR from the website or automatically prompt after pushing a new branch; GitHub typically you go to the site and it suggests recently pushed branches for PR. Also, Bitbucket has a close integration with Jira for referencing issues in PRs, whereas GitHub might integrate with its own Issues or other trackers.

### Repository Permissions in Bitbucket

As teams grow, controlling who can do what in a repository becomes important. Bitbucket provides permission levels at both the repository and branch level to enforce workflow and security.

**Repository Level Permissions:**
In Bitbucket Cloud, repository permissions are typically:

- **Admin:** Full control over the repository (can change settings, add users, delete the repo, etc.).
- **Write:** Can push to the repository, create branches, and create pull requests. (By default, this means they could push directly to any branch unless restricted).
- **Read:** Can view and clone the repository but not push or merge.

In a team setting, you might give most developers Write access and a few leads Admin access. Or if it’s an open source project, perhaps most people have Read and only core team has Write.

**Branch Permissions (Branch Restrictions):**
Branch permissions (also called branch restrictions or protected branches) allow finer control over important branches like `main` or `develop`. With branch permissions, you can:

- **Prevent direct pushes** to certain branches (requiring all changes to come via PRs). For example, protect `main` so nobody can `git push origin main` directly.
- **Restrict who can merge** pull requests into certain branches. For instance, only allow the project maintainers to merge into main, even though others can open PRs.
- **Require certain PR approvals or status checks** before merging. Bitbucket Cloud has a feature called **Merge Checks** where you can mandate that e.g. at least 2 approvals are given, and CI passes, before the PR can be merged.
- **Pattern-based rules:** You can set rules like “branches matching `release/*` require at least 1 approval and only QA team can merge.”

 ([Use branch permissions | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/#:~:text=Branch%20permissions%20help%20enforce%20specific,member%20deleting%20the%20main%20branch))Branch permissions help enforce workflows and prevent mistakes, like a new developer accidentally deleting or force-pushing to the main branch ([Use branch permissions | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/#:~:text=Branch%20permissions%20help%20enforce%20specific,member%20deleting%20the%20main%20branch)). They basically act as gatekeepers for your repository’s critical branches.

For example, a common setup:

- `main` branch: No direct pushes (must use PR), require 1 or 2 approvals, perhaps only Team Leads group can merge.
- `develop` branch (if using GitFlow): maybe allow developers to merge via PR but still no direct push without PR.
- All other branches (feature branches): no restrictions, since they are for dev use.
- Perhaps protect tags or certain long-lived branches like `release/*` or old version branches similarly.

Bitbucket’s UI allows you to configure these under Repository settings > Branch restrictions. You specify a branch name or pattern and then add rules (like no deletes, no pushes, etc.) ([Use branch permissions | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-branch-permissions/#:~:text=,or%20merge%20to%20any%20branch)).

**Use Case Scenario:**
Suppose on your team:

- Alice and Bob are senior devs (admins on the repo).
- There is a policy that all code to main goes through PRs with at least 1 review.
- You set a branch permission: Branch = `main`. Only allow pushes from admins (Alice/Bob) – effectively others cannot push (they’ll use PRs and Alice/Bob or automation will merge). And require 1 approval on PR.
- Optionally, set a merge check that build status must be successful (Bitbucket can block the merge button if the CI pipeline failed).

Now, Charlie (a developer with write access) tries to push to main: Bitbucket rejects it with “push declined due to branch restrictions”. Charlie must open a PR from his feature branch to main, and get it approved. Once approved and CI passes, he or an admin can merge it.

This setup guards the quality of main and ensures process is followed.

**Comparing with GitHub/GitLab:** They have similar concepts called **Protected Branches**. GitHub’s protected branch rules allow requiring PRs, approvals, etc., and blocking pushes. GitLab does similarly and also can restrict roles that can push/merge. The idea is universal: protect critical branches with rules.

### Bitbucket and Jira Integration

One powerful aspect of Atlassian’s ecosystem is the seamless integration between **Bitbucket** (source code) and **Jira** (issue tracking). When these tools are linked (usually by connecting Bitbucket Cloud to Jira Cloud in the project settings), you gain a lot of automation and traceability:

- You can reference Jira issues in commit messages, branch names, or PR titles, and Jira will automatically update to show those dev activities.
- In Jira, you’ll see a panel of “Development” info, e.g., how many branches, commits, and pull requests are associated with that issue ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=1,item)) ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Development%20actions%20that%20affect%20your,work%20items)).
- In Bitbucket, you can see the Jira issue key, and often there’s a link that shows the issue status.

**How to Reference Jira Issues:**
The key is using the issue key (e.g., PROJ-123) in your commits or branches:

- **Branches:** If you include the Jira key in the branch name (e.g., branch `feature/PROJ-123-add-login`), Jira will detect that branch ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Branches)). The Jira issue PROJ-123 will show that a branch exists for it. Bitbucket even has a feature: from Jira you can click “Create branch” and it will create a Bitbucket branch with the issue key in the name automatically ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=This%20works%20by%20default%20in,GitHub%20Enterprise%2C%20and%20Fisheye%20tools)).
- **Commits:** If you mention the issue key in a commit message, that commit will be linked to the Jira issue ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Commits)). In Jira, under Development, you’ll see the commit and can click to view it in Bitbucket.
- **Pull Requests:** Including the issue key in the PR title will link the PR to the issue ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Pull%20requests)). Also, if the branch name or commit messages had the key, Jira will show an open PR is associated.
- **Smart Commits:** By using special syntax in commit messages, you can even transition issues or log time. For instance, a commit message `"PROJ-123 #close Fixed the bug"` can move issue PROJ-123 to Done (if smart commits are enabled) ([Reference work items in your development projects | Jira Cloud](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Cloud%20support,Bitbucket%2C%20GitLab%2C%20GitHub%2C%20GitHub)). `#comment` adds a comment to Jira issue ([Use Smart Commits | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-smart-commits/#:~:text=When%20you%20manage%20your%20project%27s,called%20Smart%20Commits%2C%20in%C2%A0your%C2%A0commit%20messages)), `#time` can log work, `#transition` can move status. (This requires the Bitbucket-Jira link and appropriate permissions.)

From Jira’s perspective, this integration means at any time, an issue will show exactly what code work is in progress or completed:

- If an issue is “In Progress” and there’s a branch and maybe a PR, Jira will show e.g., “1 branch, 1 pull request” on the issue. A developer or PM can click those and see code context.
- When the PR is merged, Jira can automatically transition the issue to a new status (if configured, e.g., to “Done” when a PR is merged to main).
- It reduces the need for manual updates like “DEV complete” comments because the source control activity itself provides that info.

**Setting Up Integration:** Typically, you (or an admin) links the Bitbucket repo to a Jira project by:

- In Jira Cloud, go to Project Settings > DVCS accounts (for older integration) or use the new development integration in Jira which uses your Atlassian account link to Bitbucket.
- Once linked, any branch or commit with the proper issue keys will start showing in Jira. Also, Bitbucket will show Jira issues in branch names as clickable links.

**Practical Usage Tips:**

- Always include the Jira issue key in commit messages for work related to an issue. A common convention is to start the commit message with the key, like `"PROJ-456: Add validation for email format"`. This way the link is made ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Commits)), and it’s easy to scan commit logs to see which issue a commit was for.
- When creating branches for an issue, include the key, e.g., `git checkout -b PROJ-456-form-validation`. Jira will automatically pick it up ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Branches)).
- Use Jira smart commit syntax in at least one commit (perhaps the final commit or merge commit) to trigger closure or transitions. For example, to close an issue: `"PROJ-456 #resolve Fixed form validation"`. This will mark the issue as resolved (assuming Jira workflow uses “Done” or “Resolved” on that command). Make sure your team agrees on using smart commits to avoid unexpected status changes.
- In Bitbucket, you’ll notice that if your commit message has an issue key, Bitbucket will hyperlink it to Jira. Same for branch names and PR titles.

**Example Scenario (Bitbucket–Jira in action):**

- Issue **DOC-101** is in Jira, status “To Do”.
- Developer creates a branch `feature/DOC-101-api-endpoint` to work on it. Jira immediately shows “1 branch” linked to DOC-101.
- Developer makes commits:  
  `DOC-101: initial commit for API`  
  `DOC-101: implement POST logic #comment implemented core logic`  
  The `#comment` triggers a comment on the Jira ticket saying “implemented core logic” by that developer ([Use Smart Commits | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-smart-commits/#:~:text=Comment)).
- The developer opens a pull request titled **"DOC-101 Add new API endpoint for item creation"**. Jira now shows “1 pull request” linked. The PR is reviewed and merged.
- The merge commit message is auto-generated and includes DOC-101 (Bitbucket might include it if PR title had it). Or the dev could manually do a squash commit with a message containing `DOC-101 #close Completed API endpoint`.
- The `#close` (or `#resolve`) will transition the Jira issue to Done ([Use Smart Commits | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/use-smart-commits/#:~:text=When%20you%20manage%20your%20project%27s,called%20Smart%20Commits%2C%20in%C2%A0your%C2%A0commit%20messages)). Even if that wasn’t used, if configured, merging the PR could trigger an issue transition in Jira (some teams rely on smart commits, some use Jira automation rules to transition issues when PRs merged).
- Now in Jira, DOC-101 is marked Done, and it shows the commit and branch for traceability. Years later, someone can open DOC-101 and jump to the Bitbucket commit that implemented it.

This integration ensures that your project management (Jira) and development (Bitbucket) activities are connected. It answers the common questions like “Which commit fixed this bug?” or “Is this feature deployed?” (Jira can even show deployment info if Bitbucket Pipelines deploy with the issue key, appearing under Releases in Jira).

### Additional Bitbucket Collaboration Features

Aside from PRs and integration with Jira, Bitbucket offers other collaboration tools:

- **Code Search:** If enabled, to search across your code for references (useful for impact analysis).
- **Snippets:** A way to share code snippets or configs outside of the main repo context.
- **Wikis:** Each repo can have a wiki for documentation (perhaps not heavily used if you use Confluence or other docs).
- **Issues (deprecated in favor of Jira):** Bitbucket has a basic issue tracker, but if you use Jira, you likely disable the Bitbucket issues in favor of Jira’s more robust features.

### Hands-On Lab – Bitbucket Collaboration

This lab focuses on using Bitbucket features for collaboration. You’ll create a pull request and see the integration with Jira in action.

### Lab A: Pull Request and Code Review

1. Ensure you have at least two branches in your repo (e.g., `main` and one feature branch with some new commits). If you followed previous labs, you can reuse a feature branch or create a new small one.
2. In Bitbucket (web), navigate to your repository. Find the **Pull Requests** section and click **Create pull request**. Choose your feature branch as the source and `main` as the destination. Give the PR a title like “My Feature - add X functionality”. In the description, write a few notes about the changes. (If you have a Jira issue, include the issue key in the title or description.)
3. Add a reviewer (if you’re alone, just note you could add someone from your team). Create the PR.
4. Browse the pull request view. Notice the “Diff” tab showing file changes. Add a comment to one of the lines (e.g., find a line and click the blue comment icon, write “This looks good” or a question).
5. Optional: If you have a second user (or can use the Bitbucket UI’s “View as different user” by inviting a friend to the repo), have them reply or approve. If not, imagine the feedback and perhaps add another commit to the branch addressing a comment.
6. Merge the pull request: Since you are the only participant, you can click **Merge** (Bitbucket will warn if no approvals, but as admin you can merge anyway). Use a merge strategy of your choice (the default “merge commit” is fine). After merging, notice Bitbucket offers to delete the source branch – do so to keep things clean.
7. Verify the `main` branch now contains the changes. In Bitbucket, check the Commits list or the file changes on main. Pull the latest main locally (`git pull origin main`) to sync your environment.

### Lab B: Setting Branch Permissions

1. Go to **Repository settings** (you need to be admin on the repo). Find **Branch restrictions** (or Branch permissions).
2. Add a restriction: Choose branch pattern “main” (or select main from dropdown). Then check “Prevent all changes” (which means no pushes, effectively). You could also specify exceptions, but for now, just set it so nobody can push to main.
3. To test, try pushing directly to main from your local: create a trivial commit on main (maybe edit README) and attempt `git push origin main`. Bitbucket should reject it (you’ll see an error message about branch permissions). This confirms the rule works.
4. Remove or adjust the restriction after testing if you want to allow normal operation (or keep it if you intend to enforce PR-only workflow).

**Lab C: Jira Integration (if you have Jira)**
_Prerequisite:_ If you have a Jira Software project and your Bitbucket is linked, use a real issue key. If you don’t have Jira, you can skip this or just read through.

1. Create an issue in Jira, e.g., “TEST-1: Sample Issue for Integration”.
2. In your Git commit on a branch, include “TEST-1” in the message:  
   `git commit -m "TEST-1: Implement sample feature"`  
   Push this branch.
3. In Jira, open TEST-1. You should see under Development that 1 commit is linked (it might show the Bitbucket icon and commit message) ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Commits)).
4. In Bitbucket, create a PR for this branch, and ensure “TEST-1” is in the title. In Jira, you’ll then see “1 pull request” linked as well ([Reference work items in your development projects | Jira Cloud | Atlassian Support](https://support.atlassian.com/jira-software-cloud/docs/reference-issues-in-your-development-work/#:~:text=Pull%20requests)).
5. Merge the PR. If you want to test smart commits, maybe in the final commit message or PR merge commit, put “TEST-1 #close” or use the Jira workflow trigger. After merging, check Jira – TEST-1 should perhaps move to Done. If not automatically, you still see that the PR was merged and commit present.
6. In Jira, click the commit or PR links – they should take you to Bitbucket to view the code.

This lab demonstrates how Bitbucket and Jira talk to each other. This traceability is extremely useful for audits or simply understanding the context of changes.

**Wrap up:** By completing these steps, you practiced:

- Using pull requests for code review on Bitbucket.
- Enforcing workflow with branch permissions.
- Linking commits/PRs to Jira issues for integrated tracking.

Your team’s actual practices might vary, but now you have hands-on experience with the key collaboration features that Bitbucket offers. Remember that good collaboration also involves human elements: timely code reviews, clear communication in PR comments, and consensus on workflow (e.g., when to require PRs or how many approvals are needed).

Module 4 covered the “people side” of Git – how we collaborate around the code. Next, we’ll dive into CI/CD with Bitbucket Pipelines to see how automation plays a role in the development lifecycle.

## Module 5: CI/CD Concepts with Bitbucket Pipelines (Days 9–10)

### Introduction to CI/CD

Modern development practises emphasize not just writing code, but also continuously **building**, **testing**, and **deploying** that code. This is where CI/CD comes in:

- **CI (Continuous Integration):** Regularly merging code changes into a shared repository and automatically building and testing them. CI aims to detect problems early by running tests on every change integrated ([Continuous Integration Tutorial | Atlassian](https://www.atlassian.com/devops/continuous-delivery-tutorials/continuous-integration-tutorial#:~:text=Test%20automation%20exists%20to%20solve,pushed%20to%20the%20main%20repository)). A strong CI pipeline ensures that the codebase remains in a healthy, working state.
- **CD (Continuous Delivery or Deployment):** Automating the release process so that changes can be deployed to production (or a staging environment) easily and frequently. Continuous Delivery usually means every change that passes tests could be deployed (and the team manually decides when to deploy), whereas Continuous Deployment means the process is fully automated to deploy every change that passes tests.

Bitbucket Pipelines is a tool built into Bitbucket Cloud that enables CI/CD for your repositories. Instead of needing an external Jenkins server or a separate CI service, Bitbucket Pipelines lets you define your build and deployment steps in a YAML file right in your repo and runs them in the cloud on each push.

 ([Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to))**What is Bitbucket Pipelines?** Bitbucket Pipelines is an integrated CI/CD service built into Bitbucket Cloud ([Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to)). It automatically spins up a fresh environment (via Docker containers) to run the pipeline steps defined in your repo’s configuration file. You can use it to compile code, run tests, perform linting, and even deploy or publish artifacts. Essentially, any operation you can script (in Bash, or a chosen shell) can be part of the pipeline.

Key features of Bitbucket Pipelines:

- **Pipeline as Code:** You define the pipeline in a file named `bitbucket-pipelines.yml` at the root of your repo ([Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to)). This YAML file outlines what should happen on certain events (like pushes, or pull request creation, or tags).
- **Containers:** Each pipeline step runs in a Docker container. You can specify an image that has the environment you need (e.g., a Node image if building a Node.js app, or a Python image, etc.). Bitbucket sets up this container, runs your script, then destroys it. This ensures a clean, isolated build environment for each run.
- **Automatic Triggers:** By default, Pipelines runs on every push to the repository (you can configure which branches to auto-run on). You can also trigger on pull requests or tags or schedules.
- **Build Minutes:** Bitbucket gives a certain amount of free build minutes. If you have a lot of pipelines, ensure you have enough minutes or consider purchasing more or using runners.
- **Parallel Steps and Deployments:** You can define steps to run in parallel (for example, run tests on Linux and Windows concurrently, or split tests for speed). You can also define deployment steps with environment-specific variables (like deploying to a dev vs prod environment).
- **Environment Variables and Secrets:** You can store secrets (like API keys) in Bitbucket Pipeline settings so they aren’t in code, and use them in the pipeline (e.g., as environment variables in your script).
- **Status Checks:** Pipeline results integrate with pull requests – a failing pipeline will show a ❌ on the PR and can block merging if you require CI to pass.

### Configuring a Pipeline (bitbucket-pipelines.yml)

A basic pipeline configuration looks like this:

```yaml
image: maven:3.8.1  # base image (in this case, Maven with Java)

pipelines:
  default:
    - step:
        name: Build and Test
        caches:                        # caches can speed up subsequent runs
          - maven                      # using maven cache as example
        script:
          - mvn install -B            # non-interactive Maven build with tests
    - step:
        name: Code Analysis
        script:
          - mvn sonar:sonar           # run SonarQube analysis (for example)
    - step:
        name: Package
        script:
          - mvn package
        artifacts:                   # artifacts to pass to later steps or download
          - target/*.jar

  branches:
    develop:
      - step:
          name: Deploy to Staging
          script:
            - ./deploy.sh staging

  tags:
    v*:
      - step:
          name: Deploy to Production
          script:
            - ./deploy.sh production
```

Explanation:

- `image` at top sets the default Docker image. Here we chose a Maven image to build a Java project.
- Under `pipelines`, the `default` section defines what happens on every push (to any branch, unless overridden by a branch-specific section). We defined three steps running sequentially: build/test, then code analysis, then packaging. The result of the first two steps (like compiled classes) might be reused via the Maven cache or artifacts.
- The `branches` section allows customizing for certain branches. Here, for pushes to the `develop` branch, after the default steps (it inherits default unless we override fully), we add a step to deploy to staging.
- The `tags` section defines a pipeline when a tag matching pattern `v*` (like v1.0, v1.1.2) is pushed. In this case, perhaps we only deploy to production when we create a version tag.

This is just an illustration. For a simpler scenario, consider a Node.js project:

```yaml
image: node:14

pipelines:
  default:
    - step:
        name: Install and Test
        script:
          - npm install
          - npm test
```

This would, on every push, run `npm install` and then `npm test` in a Node 14 environment. If tests pass, the pipeline is green; if tests fail (exit code non-zero), pipeline turns red/fails.

**Bitbucket Pipeline YAML reference:** Atlassian provides docs for all possible options (like specifying multiple steps, parallel steps, services like databases, etc.). Common keys:

- `services`: to run e.g. a database container alongside your step (for integration tests).
- `artifacts`: to persist files between steps (since each step runs fresh by default).
- `caches`: to cache dependencies between runs (like node_modules, or .m2 for Maven).
- `conditions`: like only run certain steps for certain branches or only when files changed (Bitbucket’s conditions are somewhat basic, not as rich as some CI).
- `definitions`: advanced feature to define custom steps or pipelines to reuse.

 ([Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to))Remember: The pipeline runs in a clean container each time, giving you consistency and preventing “works on my machine” issues ([Get started with Bitbucket Pipelines | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/#:~:text=Bitbucket%20Pipelines%20is%20an%20integrated,a%20YAML%20file%2C%20refer%20to)). However, any state not saved as artifact or cache will be lost after the step.

### Integrating CI into Workflow

How does Pipelines fit into your workflow? Usually:

- Every push triggers CI. If something fails, developers fix it ASAP (to maintain the integrity of the main branch).
- Pull Requests show pipeline status. Team may require PR builds to pass before merging.
- On merges to main (or certain branches), pipelines can trigger deployments or publishing of packages.
- For example, if you practice continuous deployment: merging to main triggers the pipeline to run tests and then deploy automatically to production (maybe behind a feature flag if needed).
- If continuous delivery: merging to main could deploy to a staging environment automatically, and then a release manager triggers production deploy maybe by pushing a tag or pressing a manual trigger.

Bitbucket pipelines can also be triggered manually or on a schedule (Cron). For example, you might have a nightly build or scheduled integration test run.

### Deployment Environments

Bitbucket has a concept of Deployments which tracks certain steps as deployment steps to environments (like test, staging, production). You can configure environment-specific variables and see on the Bitbucket interface which commits are deployed where (which is nice for tracking). The YAML snippet above with `branches: develop -> deploy to staging` and `tags: v* -> deploy to prod` is an example of how you might structure it.

### CI/CD with other platforms

For perspective, **GitHub Actions** is the analogous feature on GitHub, and **GitLab CI** for GitLab. They all share the principle of YAML-defined pipelines and containerized execution. The specifics differ:

- GitHub Actions uses workflows triggered by events, with jobs and steps, etc.
- GitLab CI uses a `.gitlab-ci.yml` file with jobs that run in stages.

If you know one, it’s not too hard to adapt to another; the main difference is syntax and some features. Bitbucket Pipelines is straightforward and tightly integrated into Bitbucket Cloud’s UI.

**Benefits of using Bitbucket Pipelines:**

- No separate CI server maintenance.
- Easy setup (just add the YAML file and enable Pipelines).
- Visible next to your code – e.g., commit list in Bitbucket shows a tick or cross for pipeline.
- Great for keeping a small to medium project fully in Atlassian ecosystem.

**Limitations:**

- Build minutes are metered (could be a cost factor).
- Might not be as customizable as something like Jenkins (though for most uses it’s enough).
- If you need specialized build executors or environments not supported by Docker images (rare these days), you might need a different solution.
- For very large monorepos or complex workflows, other CI solutions might provide more control or concurrency. But Bitbucket has added features like pipelines Runners (for self-hosted execution) if needed.

### Example Pipeline Use Cases

- **Compile and Test:** For almost any project, set up pipeline to run the test suite on each push. This alone significantly improves code quality by catching broken tests or builds immediately.
- **Lint and Code Quality:** Run linters (ESLint, PyLint, etc.) and tools like SonarCloud or Snyk for security scanning as part of CI.
- **Building Docker Images:** If your project is containerized, the pipeline can build a Docker image and even push it to a registry (Docker Hub, AWS ECR, etc.), perhaps on merges to main.
- **Deploying to Environments:** Use pipeline to deploy. For example, a step might SCP or rsync files to a server, or use Terraform to provision infra, or use kubectl/helm to update a Kubernetes cluster, or trigger a deployment on a platform (Netlify, Heroku, etc.). Many integrations exist; often it’s just running shell commands or calling APIs.
- **Semantic Release:** You can set up pipeline to automatically bump version numbers and create tags/releases when merging to main, using tools like semantic-release for Node or similar in other ecosystems.
- **Notifications:** Pipeline can output to Slack or other channels by calling webhooks or using built-in Slack pipe. For instance, notify team if a deploy to production succeeded or if a build fails on main.

### Hands-On Lab – Continuous Integration with Bitbucket Pipelines

In this lab, you will enable Bitbucket Pipelines on your repository and configure a basic CI pipeline to run on each push. We’ll assume a simple scenario (e.g., a Node.js project, but you can adapt to whatever stack).

**Lab Setup:** If you have a repository with code and maybe some tests (e.g., a Node project with `npm test` script, or a Python project with some tests), use that. If not, you can still follow by having it echo messages.

**Steps:**

1. Go to your repository on Bitbucket. Click on **Pipelines** in the sidebar. Bitbucket might show a prompt like “Enable Pipelines” – click to enable it for this repo.
2. Bitbucket often offers some starter configurations (detecting your language). For example, it might suggest a Node.js pipeline YAML if it sees a package.json. You can accept a suggestion or create your own.
3. Create a file in the root of your repo named `bitbucket-pipelines.yml` with the following content (for Node.js example):

   ```yaml
   image: node:14

   pipelines:
     default:
       - step:
           name: Install and Test
           script:
             - npm install
             - npm test
   ```

   Commit and push this to your repository (ideally on a branch or directly to main if you want to test on main).
4. Once pushed, go to the Pipelines section in Bitbucket. You should see a pipeline run triggered by that push. It will go through the steps: pulling Node image, running npm install, then npm test. If your project has tests, you’ll see output here. If tests pass, the step ends with exit code 0 and Bitbucket marks it success; if a test fails (non-zero exit), it marks it failed.
5. Experiment: break something to see a failing pipeline. For instance, introduce a failing test or a syntax error, then push. Observe that the pipeline fails. In Bitbucket’s UI, drill into the logs to see where it failed (error output from test).
6. Fix the issue, push again, and watch the pipeline go green.
7. (Optional) Add another step to the pipeline, e.g., after tests, add:

   ```yaml
       - step:
           name: Echo Deployment (simulate)
           script:
             - echo "Deploying build (simulation)"
   ```

   Commit, push, and see the pipeline run both steps in order.
8. (Optional advanced) Simulate a branch-specific pipeline: Add a section to only deploy when pushing to main. For example:

   ```yaml
   pipelines:
     default:    # as above
       - step: ...
     branches:
       main:
         - step:
             script:
               - echo "This runs only on main branch"
   ```

   Push this config. Then push a commit to a feature branch – you should see just the default step(s). Merge or push to main – you’ll see the additional step from the branches: main section executing.

9. Check integration with PR: If you open a PR now (with an update that triggers pipeline), the PR in Bitbucket will show the pipeline’s status in the overview. Try making a PR and see under “Builds” or at the top if it shows the pipeline status.

Through this lab, you’ve implemented a basic CI pipeline. In real scenarios, you’d adjust the YAML to your technology:

- For a Java/Maven project, use a Maven Docker image and run `mvn test`.
- For Python, use a Python image and do `pip install -r requirements.txt && pytest`.
- For .NET, use a microsoft dotnet SDK image and run `dotnet build` and `dotnet test`.
- etc.

**Lab (Optional) – Deployment pipeline:**
If you have something to deploy (for example, a static site), you could integrate a deployment step. A simple example: deploy to GitHub Pages or Netlify might involve pushing files or calling an API. Since our focus is Bitbucket, you might skip this, but think about how you’d extend the pipeline to deploy:

- Possibly add at branch: main, a step that, say, uses scp to copy files to a server (you’d need to add the server credentials as secure environment variables).
- Or if deploying to a cloud service, maybe use their CLI (e.g., AWS CLI to upload to S3, Heroku CLI to push an app, etc.).

The key takeaway: Bitbucket Pipelines allows you to automate builds/tests and even releases, which achieves continuous integration and deployment. By having this in place, your team gets immediate feedback on code changes (which reduces bugs) and can release software faster and more reliably.

### Conclusion

In Module 5, we set up CI/CD pipelines using Bitbucket Pipelines, demonstrating how automated processes improve software quality and delivery speed. Combined with everything else:

- You use Git (Module 1) to version your code,
- follow a branching strategy (Module 2) to manage work,
- resolve conflicts and integrate changes smoothly (Module 3),
- collaborate via pull requests and manage your repo (Module 4),
- and ensure quality and delivery with CI/CD pipelines (Module 5).

With this training, you have a structured understanding of Git in both theory and practice, specifically tailored to Bitbucket and Atlassian’s ecosystem. You’re now equipped to apply these in a real project to streamline development workflow. Happy committing, and may your builds be green! 🚀
