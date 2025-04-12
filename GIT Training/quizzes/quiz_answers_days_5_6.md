## 📚 **Detailed Quiz Answers & Explanations**

### **Question 1**  
**Correct Answer:** B) Two branches containing changes to the same lines of code.  
**Explanation:**  
- **A (Incorrect):** Author count doesn’t trigger conflicts.
- **B (Correct):** Conflicts arise when Git can't auto-merge overlapping edits.
- **C (Incorrect):** Branch count alone does not cause conflicts.
- **D (Incorrect):** Pulling doesn’t cause conflicts unless line-level changes conflict.

### **Question 2**  
**Correct Answer:** A) `git status`  
**Explanation:**  
- **A (Correct):** Shows clearly which files are conflicted after merge.
- **B (Incorrect):** Shows commit history, not current conflicts.
- **C (Incorrect):** Initiates merges but does not specifically list conflicts.
- **D (Incorrect):** Views file changes but not directly useful to list conflicts.

### **Question 3**  
**Correct Answer:** B) Run `git commit`  
**Explanation:**  
- **A (Incorrect):** `git reset` undoes recent changes, losing conflict resolutions.
- **B (Correct):** Commit the conflict resolution to finalize merge.
- **C (Incorrect):** Never delete conflicted files; always resolve them.
- **D (Incorrect):** You must commit resolved conflicts before pushing.

### **Question 4**  
**Correct Answer:** A) `<<<`, `===`, `>>>`  
**Explanation:**  
- **A (Correct):** Git clearly marks conflicts with these symbols in files.
- **B, C, D (Incorrect):** Git doesn't use these markers.

### **Question 5**  
**Correct Answer:** B) Cancels the merge and returns the repository to its previous state.  
**Explanation:**  
- **A (Incorrect):** Does not delete branches.
- **B (Correct):** Useful if conflicts seem unmanageable.
- **C (Incorrect):** Does not resolve automatically.
- **D (Incorrect):** Doesn’t force merges.

### **Question 6**  
**Correct Answer:** C) Git GUI or visualization tools like `gitk`  
**Explanation:**  
- **C (Correct):** Visualization helps in understanding conflict points clearly.
- Others are commands or processes, not visualization tools.

### **Question 7**  
**Correct Answer:** B) It simplifies linear project history by applying changes sequentially.  
**Explanation:**  
- **B (Correct):** Rebase reapplies commits onto a target branch sequentially, simplifying resolution.
- **Other options (Incorrect):** Rebase doesn't automatically fix or prevent conflicts; manual intervention is usually needed.

### **Question 8**  
**Correct Answer:** A) When preserving linear commit history is important.  
**Explanation:**  
- **A (Correct):** Rebase avoids merge commits, maintaining a linear and clean history.
- Others are either risky or impractical use-cases.

### **Question 9**  
**Correct Answer:** B) Frequently pulling changes from shared branches.  
**Explanation:**  
- **B (Correct):** Regular pulls minimize divergence, significantly reducing conflicts.
- Others either increase likelihood of conflict or are poor Git practices.

### **Question 10**  
**Correct Answer:** B) The push is rejected; conflicts must be resolved locally.  
**Explanation:**  
- **B (Correct):** Git never allows unresolved conflicts to be pushed.
- Other options inaccurately describe Git behavior or workflow expectations.
