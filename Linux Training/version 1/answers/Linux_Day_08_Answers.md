# ✅ **Day 8 Quiz – Answer Key with Detailed Explanations**

## Here are the answers and explanations for Day 8’s quiz questions

---

### **Question 1:**  

**How would you add a new user called `john` with a home directory?**

✅ **Correct Answer (fill-in-the-blank):**

```bash
useradd -m john
```

**Explanation:**  

- The `-m` option creates the user's home directory (`/home/john`). Without it, no home directory is created automatically.

---

### **Question 2:**  

**Which command completely removes a user named `john` and their home directory?**

✅ **Correct Answer:**  
**b)** `userdel -r john`

**Explanation:**  

- **Option a)** `userdel john`: Removes user but keeps their home directory.
- **Option c)** `usermod -r john`: Invalid syntax; `usermod` modifies users but does not remove them.

`userdel -r` correctly removes the user and deletes their home directory and associated files.

---

### **Question 3:**  

**Which command changes the password for user `john`?**

✅ **Correct Answer (fill-in-the-blank):**

```bash
passwd john
```

**Explanation:**  

- The `passwd` command is specifically used to update user passwords.

---

### **Question 4:**  

**How do you add user `john` to the group `staff` without removing him from other groups?**

✅ **Correct Answer:**  
**a)** `usermod -aG staff john`

**Explanation:**  

- **Option b)** `usermod -g staff john`: Sets the primary group to `staff`, removing the user from existing supplementary groups.
- **Option c)** `groupadd staff john`: Invalid syntax; `groupadd` creates groups, doesn't assign users.

`-aG` correctly adds the user to additional groups without affecting existing memberships.

---

### **Question 5:**  

**Which command shows detailed information about the group named `admins`?**

✅ **Correct Answer:**  
**b)** `getent group admins`

**Explanation:**  

- **Option a)** `cat /etc/passwd admins`: Incorrect; `/etc/passwd` stores user details, not group information.
- **Option c)** `passwd admins`: Incorrect; used to change passwords, not view group details.

`getent group admins` accurately retrieves detailed group information.

---

🎯 **Great job today!**  
You've mastered critical user and group management commands necessary for securing and managing Linux environments.

Tomorrow, you'll delve into archiving, compression, and package management, enhancing your Linux management capabilities even further.

Keep up the excellent practice!
