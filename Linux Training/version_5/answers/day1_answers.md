Below is a **separate answer key** for the Day 1 quiz. Each answer includes an **explanation** to clarify why it is correct.

---

## **Answer Sheet and Explanations**

### 🟢 Beginner (Tier 1)

1. **Question**: Which command shows your current working directory?  
   **Options**:  
   A) `pwd`  
   B) `ls`  
   C) `cd`  

   **Correct Answer**: **A) `pwd`**  
   **Explanation**:  
   - `pwd` stands for **Print Working Directory**. It returns the exact directory path in which you’re currently working, making it the right choice for confirming your location.

2. **Question**: How do you list **all** files, including hidden ones?  
   **Options**:  
   A) `ls -h`  
   B) `ls -l`  
   C) `ls -a`  

   **Correct Answer**: **C) `ls -a`**  
   **Explanation**:  
   - The `-a` option in `ls` displays all files, **including hidden files** (those starting with a dot). The other options do not reveal hidden files by default.

3. **Question**: Which directory is considered the top-level (root) of the Linux filesystem?  
   **Options**:  
   A) `/home`  
   B) `/`  
   C) `/root`  

   **Correct Answer**: **B) `/`**  
   **Explanation**:  
   - The single forward slash (`/`) is the **root** of the entire filesystem, from which all other directories branch.

---

### 🟡 Intermediate (Tier 2)

4. **Question**: To **reverse** the order of a long listing, you would use:  
   **Options**:  
   A) `ls -lr`  
   B) `ls -ar`  
   C) `ls -ra`  

   **Correct Answer**: **A) `ls -lr`**  
   **Explanation**:  
   - `ls -l` generates a long listing (permissions, timestamps, etc.). Adding `-r` **reverses** the sorting order. The other combinations (`-ar`, `-ra`) do not specifically produce a reversed long listing in the typical sense.

5. **Question**: What does `pwd -P` provide that `pwd` alone might not?  
   **Options**:  
   A) Physical path without following symlinks  
   B) Permission details of the current directory  
   C) Printing all files in the directory  

   **Correct Answer**: **A) Physical path without following symlinks**  
   **Explanation**:  
   - The `-P` flag ensures that `pwd` resolves to the **physical directory** rather than the symlinked path. This is often vital for scripting or verifying you’re actually in the real directory.

6. **Question**: In which directory would you typically expect to find **system configuration** files?  
   **Options**:  
   A) `/usr/bin`  
   B) `/tmp`  
   C) `/etc`  

   **Correct Answer**: **C) `/etc`**  
   **Explanation**:  
   - The `/etc` directory stores most **system-wide configuration files**, such as those for services, daemons, and the operating system.

---

### 🔴 SRE-Level (Tier 3)

7. **Question**: During an outage, you need to find logs mentioning “timeout.” What combination of commands might you use?  
   **Options**:  
   A) `cd /etc && man logs`  
   B) `pwd -P /var/log && ls -l`  
   C) `cd /var/log && ls -lt | grep "timeout"` or `grep -Ri "timeout" /var/log`  

   **Correct Answer**: **C)**  
   - `cd /var/log && ls -lt | grep "timeout"` or `grep -Ri "timeout" /var/log`  
   **Explanation**:  
   - Changing directory to `/var/log` or directly grepping `/var/log` is the typical approach to **search logs** for a specific string like “timeout.” The other options either don’t search logs or don’t address the keyword “timeout.”

8. **Question**: Why might an SRE use `ls -lt` in the `/var/log` directory when troubleshooting?  
   **Options**:  
   A) To see the largest files first  
   B) To identify which logs changed most recently  
   C) To hide any files from non-root users  

   **Correct Answer**: **B) To identify which logs changed most recently**  
   **Explanation**:  
   - The `-t` option sorts files by **modification time** (most recent first). This allows you to see which logs have been written to most recently and can be crucial for pinpointing active issues.

9. **Question**: When writing a script that deploys code, what is an essential check before performing destructive actions?  
   **Options**:  
   A) Confirm the user has run `pwd` in the past hour  
   B) Verify you’re in the correct directory using `pwd -P`  
   C) Always run `ls -a` to check for hidden files  

   **Correct Answer**: **B) Verify you’re in the correct directory using `pwd -P`**  
   **Explanation**:  
   - Especially in production, you want to be **certain** you are in the intended directory (e.g., `/var/www/production`) before deleting or overwriting files. `pwd -P` ensures you see the **physical** directory path, which is crucial if symlinks are involved.

---

**End of Answer Key**