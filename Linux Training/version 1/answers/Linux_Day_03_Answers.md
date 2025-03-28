# ✅ **Day 3 Quiz – Answer Key with Detailed Explanations**

## Here are the answers and explanations for Day 3’s quiz questions

---

### **Question 1:**

**Which permission set allows everyone to read and execute, but only the owner to write?**

✅ **Correct Answer:**  
**a)** `chmod 755`

**Explanation:**  

- `7` → **owner:** read(4), write(2), execute(1) → total: 4+2+1=7 (`rwx`)  
- `5` → **group:** read(4), execute(1) → total: 4+0+1=5 (`r-x`)  
- `5` → **others:** read(4), execute(1) → total: 4+0+1=5 (`r-x`)

- **Option b) 644:** Owner(rw-), Group(r--), Others(r--) no execute permission.
- **Option c) 777:** All (owner, group, others) get read, write, execute permissions.

---

### **Question 2:**

**Which command changes the group ownership of `file.txt` to `admins`?**

✅ **Correct Answer (fill-in-the-blank):**  

```bash
chgrp admins file.txt
```

**Explanation:**  

- `chgrp` specifically changes group ownership.  
- `chown` changes the file’s owner (user), not just the group.

---

### **Question 3:**

**Which command adds execute permission for the file's owner only?**

✅ **Correct Answer:**  
**b)** `chmod u+x script.sh`

**Explanation:**  

- **Option a) `chmod +x script.sh`**: Adds execute permissions for **owner, group, and others**.
- **Option c) `chmod o+x script.sh`**: Adds execute permission only for **others** (not the owner).

---

### **Question 4:**

**To run a command with root privileges, you'd use:**

✅ **Correct Answer:**  
**a)** `sudo`

**Explanation:**  

- **Option b) `chown`**: Changes file ownership.
- **Option c) `chmod`**: Changes file permissions.

Only `sudo` executes commands with root (administrative) privileges.

---

### **Question 5:**

**What's the numeric representation of permissions: owner (read/write), group (read), others (none)?**

✅ **Correct Answer (fill-in-the-blank):**  

```bash
chmod 640 filename
```

**Explanation:**

- Owner (read/write): read(4)+write(2)= **6**
- Group (read only): read(4)+0+0= **4**
- Others (no permissions): **0**

Thus, permission is: **640**

---

🎯 **Great Job!** You're now comfortable with managing Linux permissions and ownership.  

Let's continue your learning journey—tomorrow we'll explore text processing and searching, essential tools for productivity in Linux environments.
