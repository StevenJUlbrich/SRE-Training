
# 📚 **Detailed Quiz Answers & Explanations**

## **Question 1**

**Correct Answer:** B) Allows multiple developers to work simultaneously without conflicts.  
**Explanation:**  

- **A (Incorrect):** Testing remains crucial regardless of branching strategies.
- **B (Correct):** Branches isolate development tasks, enabling parallel work without disrupting others.
- **C (Incorrect):** Automatic merging isn't guaranteed by branching alone.
- **D (Incorrect):** Branching does not reduce the number of commits; it may increase clarity and structure.

### **Question 2**

**Correct Answer:** B) To develop and integrate new features.  
**Explanation:**  

- **A (Incorrect):** Production deployments happen from the `master/main` branch.
- **B (Correct):** The `develop` branch integrates new features before release.
- **C (Incorrect):** Hotfixes have their own specific branches.
- **D (Incorrect):** Production-ready code testing occurs on release branches or staging environments.

### **Question 3**

**Correct Answer:** B) Trunk-Based Development  
**Explanation:**  

- **A (Incorrect):** GitFlow involves multiple branches and formal releases, slowing down rapid deployment.
- **B (Correct):** Trunk-based emphasizes continuous integration directly into a main branch, suited for CI/CD.
- **C (Incorrect):** Feature branches are helpful but require more integration overhead.
- **D (Incorrect):** Release branches are used for periodic releases, less ideal for continuous delivery.

### **Question 4**

**Correct Answer:** B) Deleted after merging into the main branch.  
**Explanation:**  

- **A (Incorrect):** Keeping feature branches indefinitely leads to confusion and clutter.
- **B (Correct):** Best practice dictates feature branches should be short-lived and removed after merging.
- **C (Incorrect):** Long-lived branches cause maintenance overhead.
- **D (Incorrect):** Immediate production push bypasses testing and quality checks.

### **Question 5**

**Correct Answer:** C) `git switch <branch-name>`  
**Explanation:**  

- **A (Incorrect):** This creates a branch but does not switch to it.
- **B (Incorrect):** This creates and switches to a new branch.
- **C (Correct):** Explicitly switches to an existing branch.
- **D (Incorrect):** Merging is unrelated to switching branches.

### **Question 6**

**Correct Answer:** A) `master` (or `main`)  
**Explanation:**  

- **A (Correct):** Holds stable, production-ready code.
- **B (Incorrect):** Used for integration and feature development.
- **C (Incorrect):** Used temporarily for individual features.
- **D (Incorrect):** Used for urgent production bug fixes only.

### **Question 7**

**Correct Answer:** B) Frequent direct commits to a single main branch.  
**Explanation:**  

- **A (Incorrect):** Trunk-based discourages long-lived branches.
- **B (Correct):** Encourages continuous integration directly into a single trunk (main branch).
- **C (Incorrect):** Multiple release branches are characteristic of GitFlow.
- **D (Incorrect):** Code integration should be frequent and continuous, not isolated.

### **Question 8**

**Correct Answer:** C) Facilitating code review and discussion.  
**Explanation:**  

- **A (Incorrect):** PRs don't directly deploy code.
- **B (Incorrect):** PRs explicitly facilitate code reviews.
- **C (Correct):** Allows peer reviews and discussion before merging.
- **D (Incorrect):** PRs identify conflicts but don't automatically resolve them.

### **Question 9**

**Correct Answer:** C) `git checkout -b <branch-name>`  
**Explanation:**  

- **A (Incorrect):** Creates but doesn't switch immediately.
- **B (Incorrect):** Switches only if the branch already exists.
- **C (Correct):** Creates and switches immediately to a new branch.
- **D (Incorrect):** Incorrect syntax; `git switch -c <branch-name>` would be valid, but provided syntax is incorrect.

### **Question 10**

**Correct Answer:** C) It provides context and clarity for changes.  
**Explanation:**  

- **A (Incorrect):** Commit messages don't influence merge automation.
- **B (Incorrect):** Commit messages don't affect the necessity of branching.
- **C (Correct):** Clear commit messages help teams understand changes, improving maintainability.
- **D (Incorrect):** Commit messages alone do not resolve conflicts.
