# Day 3 Answer Sheet

Below is a complete answer key for all the quiz questions from the enhanced module, with full explanations. 

---

## **Beginner Tier Answers**

1. **Which numeric permission grants the owner read and write, group read, and others read?**  
   **Answer:** A) 644  

   **Explanation:**  
   - The digits in numeric permissions correspond to *owner*, *group*, and *others* (in that order).  
   - Each digit is the sum of: **read (4)**, **write (2)**, **execute (1)**.  
   - **644** means:  
     - Owner = 6 → Read (4) + Write (2) = rw  
     - Group = 4 → Read only  
     - Others = 4 → Read only  

2. **In `-rwxr-xr--`, which permissions does the group have?**  
   **Answer:** B) Read and execute  

   **Explanation:**  
   - The string `-rwxr-xr--` can be broken down as:  
     - Owner: rwx (read, write, execute)  
     - Group: r-x (read, execute)  
     - Others: r-- (read only)  
   - Thus, the group portion `r-x` equates to read + execute.  

3. **True/False: `chmod +x script.sh` sets execute permission for all users.**  
   **Answer:** **True**  

   **Explanation:**  
   - By default, `chmod +x filename` is interpreted as `chmod a+x filename`, meaning “add execute permission for **all** (owner, group, others).”  
   - If you intended to grant execute only to the file owner, you would explicitly use `chmod u+x script.sh`.  

4. **To change the owner of `example.txt` to `alice`, which command is correct?**  
   **Answer:** A) `chown alice example.txt`  

   **Explanation:**  
   - The `chown` command changes file ownership. A basic usage is `chown newowner filename`.  
   - `chmod` changes permissions, not ownership; `chgrp` changes group ownership.  
   - Therefore, `sudo chown alice example.txt` (or just `chown alice example.txt` if you own the file) is the valid approach.  

---

## **Intermediate Tier Answers**

1. **Which command recursively sets a directory’s permissions to `770`?**  
   **Answer:** B) `chmod -R 770 directory/`  

   **Explanation:**  
   - The `-R` (recursive) option applies changes to **all** files and subdirectories within `directory/`.  
   - `chmod 770 directory/` (without `-R`) would only change the permissions of the top-level directory itself, not its contents.  

2. **A file has permissions `-rw-r--r--`. Which command makes it so only the owner can read/write it, with no access for group or others?**  
   **Answer:** B) `chmod 600 file`  

   **Explanation:**  
   - `-rw-r--r--` is numeric 644. Changing to 600:  
     - Owner = 6 → rw  
     - Group = 0 → no permissions  
     - Others = 0 → no permissions  
   - That effectively restricts read/write to the owner only.  

3. **True/False: Using `chown :developers file.txt` changes the owner to `developers`.**  
   **Answer:** **False**  

   **Explanation:**  
   - `chown :developers file.txt` changes **only** the group ownership to `developers`. It does **not** change the file’s owner.  
   - The syntax for changing both user and group is `chown user:group file`.  

4. **Match the numeric notation**:  
   - **700** → `rwx------`  
   - **755** → `rwxr-xr-x`  
   - **666** → `rw-rw-rw-`  

   **Explanation:**  
   - **700** means owner has 7 (rwx), group has 0 (---), others have 0 (---).  
   - **755** means owner has 7 (rwx), group has 5 (r-x), others have 5 (r-x).  
   - **666** means owner has 6 (rw-), group has 6 (rw-), others have 6 (rw-).  

---

## **SRE-Level Tier Answers**

1. **Why is a setuid binary risky?**  
   **Answer (Short Explanation):**  
   - A setuid binary runs with the file owner’s privileges—often root. Any vulnerabilities in that program can be exploited to gain elevated privileges (privilege escalation).  

   **Extended Explanation:**  
   - When the setuid bit is set (shown as an `s` in the owner’s execute position, e.g., `-rwsr-xr-x`), anyone running that binary effectively assumes the privileges of its owner. If that owner is `root`, a bug in the binary can allow a malicious user to execute arbitrary code with root access, a critical security risk.  

2. **You see `-rwsr-xr-x` on `/usr/bin/passwd`. What does the `s` indicate?**  
   **Answer:** B) The setuid bit  

   **Explanation:**  
   - The `s` in the owner’s execute position (rws) means the setuid bit is set, not the sticky bit. The sticky bit usually appears in the **others** execute position as `t`.  

3. **True/False: SELinux or AppArmor can override traditional file permissions.**  
   **Answer:** **True**  

   **Explanation:**  
   - SELinux (Security-Enhanced Linux) and AppArmor are **mandatory access control** (MAC) systems that impose additional security layers beyond standard discretionary access control (DAC). They can deny access even if `rwx` bits would normally allow it.  

4. **Which command best helps confirm a file’s permission bits and extended attributes?**  
   **Answer:** B) `stat /path/file`  

   **Explanation:**  
   - `stat` provides comprehensive metadata, including permissions, ownership, timestamps, and special extended attributes (like SELinux labels).  
   - `ls -l` shows basic permissions but not all extended attributes or SELinux contexts in detail.  
   - `cat /path/file` just shows file content, not permission metadata.  

---

### **Additional Notes:**

- Some of the quiz questions revolve around how symbolic and numeric permissions differ and how setuid/sticky bits work, which are key to mastering advanced Linux security.
- Always practice on non-production systems or test directories before applying changes to critical files.  

Feel free to ask for clarification if you need deeper insights into any of these answers!
