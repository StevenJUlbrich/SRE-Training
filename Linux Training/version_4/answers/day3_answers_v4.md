# **Answer Sheet with Explanations** for the **Day 3 Quiz** from your Linux SRE training material

---

## ✅ **Day 3 Quiz – Answer Sheet & Explanations**

---

### **1. What does `chmod 640 file.txt` do?**

**✅ Correct Answer:** b) Read/write for user, read for group

**Explanation:**

- `6` = 4 (read) + 2 (write) → User has **read/write**
- `4` = 4 → Group has **read only**
- `0` = No permissions for others

This is a common setting for config files that should be editable by the owner and readable by group members, but hidden from others.

---

### **2. How do you add execute permission for user only?**

**✅ Correct Answer:** b) `chmod u+x file`

**Explanation:**

- `u` = user (owner)
- `+x` = add execute permission
- Symbolic mode allows targeted changes without altering other permissions

Option a (`chmod +x`) affects *all classes* (user, group, others), which is less precise.

---

### **3. To change file owner and group:**

**✅ Correct Command:**  

```bash
chown user:group file.txt
```

**Explanation:**

- `chown` changes ownership.
- The format `user:group` assigns both at once.
- Requires `sudo` privileges in most cases.

Example:

```bash
sudo chown nginx:www-data /etc/nginx/nginx.conf
```

---

### **4. What’s the sticky bit used for?**

**✅ Correct Answer:** b) Allow only owners to delete

**Explanation:**

- Sticky bit is represented as `t` in permissions.
- Used on **shared directories** (e.g., `/tmp`).
- Prevents users from deleting each other's files, even if directory is world-writable.

Set with:

```bash
chmod +t /shared/folder
```

---

### **5. Which numeric permission represents `rwxr-xr--`?**

**✅ Correct Answer:** c) 754

**Explanation:**

- Breakdown:
  - `rwx` = 7 (user)
  - `r-x` = 5 (group)
  - `r--` = 4 (others)

So:

```bash
chmod 754 filename
```

---

## 🔁 Summary Table

| Question | Correct Answer | Reason |
|----------|----------------|--------|
| Q1       | b              | Numeric mode breakdown: 6 (rw), 4 (r), 0 (-) |
| Q2       | b              | Symbolic mode for user-specific execute permission |
| Q3       | `chown user:group file` | Ownership change syntax |
| Q4       | b              | Sticky bit limits delete access |
| Q5       | c              | Permission digits: 7 (rwx), 5 (r-x), 4 (r--) |

---

Would you like me to embed this directly in the Day 3 V3 document or keep it as a separate companion file for your learners?
