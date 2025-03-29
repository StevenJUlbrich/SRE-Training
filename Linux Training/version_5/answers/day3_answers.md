# 🚀 **Linux SRE Training Module - Day 3: Permissions & Ownership (V3) - Instructor Key**

Below is an answer key with clarifications and explanations for the quizzes in the Day 3 module. Refer to the original Day 3 content for the specific quiz questions.

---

## 📝 **Quiz Solutions and Explanations**

### **Beginner Tier Answers**

1. **Which permission bits are represented by `755`?**
   - **Correct Answer**: B) Owner can read/write/execute, group can read/execute, others can read/execute.
     - **Explanation**: `7` is (rwx), `5` is (r-x). The final `5` is again (r-x).

2. **True/False**: `chmod +x script.sh` sets execute permission for all users.
   - **Correct Answer**: **False**.
     - **Explanation**: By default, `chmod +x script.sh` modifies the execute bit for the file’s owner, group, and others *only if* the shell interprets `+x` as applying to all (equivalent to `a+x`). On some shells or contexts, `+x` might only apply to the current user’s permission set (symbolic usage can differ). Typically, `a+x` ensures all user categories get execute.
     - **Additional Note**: The nuance can depend on your shell environment or default chmod behavior. Symbolic mode is generally explicit with `u+x`, `g+x`, or `o+x`. If you typed exactly `chmod +x`, many Linux distros interpret that as `a+x`. It's a good practice to specify, for clarity: `chmod u+x script.sh` or `chmod a+x script.sh`.

3. **Fill in the Blank**: To change the owner of `fileA.txt` to user `bob`, you would use `____ bob fileA.txt`.
   - **Correct Answer**: `chown bob fileA.txt`.
     - **Explanation**: `chown` changes file ownership.

---

### **Intermediate Tier Answers**

1. **Match the numeric notation to symbolic notation**:
   - **`600`** → `rw-------` (Owner: rw, Group: --, Others: --)
   - **`775`** → `rwxrwxr-x` (Owner: rwx, Group: rwx, Others: r-x)
   - **`444`** → `r--r--r--` (Owner: r, Group: r, Others: r)

   - **Explanation**:
     - `600` → 6 (4+2 = rw) for owner, 0 for group, 0 for others → `rw-------`
     - `775` → 7 (rwx) for owner, 7 (rwx) for group, 5 (r-x) for others → `rwxrwxr-x`
     - `444` → 4 (r) for owner, 4 (r) for group, 4 (r) for others → `r--r--r--`

2. **Scenario**: A file `report.csv` has permissions `rw-r--r--`. Which command restricts it so only the owner can read and write?
   - **Correct Answer**: B) `chmod 600 report.csv`
     - **Explanation**: `600` sets the owner to (rw) and denies all permissions to group and others.

3. **Multiple Choice**: You need to give the group write permission but not others on `shared_notes.txt`. Which symbolic option is correct?
   - **Correct Answer**: A) `chmod g+w,o-r shared_notes.txt`
     - **Explanation**: This specifically adds write permission to the group (`g+w`) and removes read permission from others (`o-r`).

4. **True/False**: Using `sudo chown -R user:group /home/user` will also change hidden files inside `/home/user`.
   - **Correct Answer**: **True**.
     - **Explanation**: The `-R` (recursive) option includes hidden files (e.g., `.bashrc`, `.gitignore`) unless specifically excluded by patterns.

---

### **SRE-Level Tier Answers**

1. **Short Answer**: Name two reasons setuid bits are considered high risk.
   - **Sample Correct Reasons**:
     1. If a setuid binary has a vulnerability, attackers can escalate privileges to the file owner (often root).
     2. Misconfiguration or unintended setuid can expose system resources or break least-privilege principles.

2. **Multiple Choice**: You see `-rwsr-xr-x` on `/usr/bin/passwd`. Which statement is **true**?
   - **Correct Answer**: A) The setuid bit is set, so it runs with the owner’s permissions.
     - **Explanation**: The `s` in the owner’s execute position indicates the setuid bit. `/usr/bin/passwd` typically runs with root privileges to modify system password files securely.

3. **Scenario**: A service fails to read its config file in `/etc/app`. Which command best helps you confirm if permissions are the cause?
   - **Correct Answer**: C) `stat /etc/app/config.yaml`
     - **Explanation**: `stat` provides a detailed breakdown of ownership, permissions, and additional attributes like SELinux context.

4. **True/False**: Setting the sticky bit on a file ensures only the root user can execute it.
   - **Correct Answer**: **False**.
     - **Explanation**: The **sticky bit** applies mostly to directories (prevents users from deleting files they don’t own in a shared directory). On a file in modern Unix systems, the sticky bit has minimal to no effect on execution. It’s the **setuid** bit that grants special execution privileges.

---

## 🔍 **Additional Clarifications**

1. **Beginner-level `chmod +x`**: On many systems, `+x` without specifying the target typically applies to all user classes—**but** that might vary by shell or environment. Encourage novices to use `u+x` (for the owner only) or `a+x` (for everyone) for absolute clarity.
2. **Recursive Ownership**: Remember to double-check directory content after `chown -R`, especially if large or symbolic links are involved.
3. **setuid vs. sudo**: The question about setuid and sudo highlights a classic difference in how Linux handles privilege escalation. Students should know that `sudo` can be more flexible and auditable, while `setuid` can be riskier.

---

**End of Instructor Key**

This key should help you provide comprehensive feedback to learners and clarify any confusion regarding permissions, ownership, and usage of `sudo`. Be sure to adapt this key to your specific environment or distribution as needed!
