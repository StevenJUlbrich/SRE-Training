# 🚀 Day 3: Permissions & Ownership for SRE – Securing Access and Resources

---

## 📌 Introduction

### 🔄 Recap of Day 2

You previously learned how to create, view, copy, move, and delete files and directories. These foundational operations now lead us to controlling *who* can do *what* with these files—a critical part of Linux system security.

### 📅 Today's Focus

Today is all about **Linux permissions and ownership**. This knowledge is essential for:

- Preventing unauthorized access
- Enabling secure file sharing
- Managing service and user interactions
- Troubleshooting common "Permission Denied" errors

### 🎯 Learning Objectives

By the end of Day 3, you will be able to:

- Understand permission structure (`rwx`) and ownership model (User, Group, Others)
- View and interpret permissions with `ls -l`
- Modify permissions using symbolic and numeric modes with `chmod`
- Change file ownership using `chown` and `chgrp`
- Use `sudo` for administrative changes
- Recognize and manage special permissions (setuid, setgid, sticky bit)

---

## 🧰 Beginner Section – Understanding Permissions & Ownership

### 🔐 Linux Permission Model

Each file/directory has **three types of access** for **three classes of users**:

| Class       | Who It Refers To       |
|-------------|-------------------------|
| User (u)    | File owner              |
| Group (g)   | Users in file's group   |
| Others (o)  | Everyone else           |

**Permissions:**

- `r` = read
- `w` = write
- `x` = execute

```bash
-rwxr-xr-- 1 sre sre 1024 Mar 25 10:00 deploy.sh
```

Breakdown:

- `-` → regular file
- `rwx` → User (owner) has read/write/execute
- `r-x` → Group has read/execute
- `r--` → Others have read only

### 📁 Ownership

Each file/directory has two owners:

- **User owner** (usually the creator)
- **Group owner** (used for shared access)

---

## ⚙️ Intermediate Section – Key Commands and Techniques

### 🔍 Viewing Permissions

```bash
ls -l filename
ls -la      # includes hidden files
```

### ✏️ Modifying Permissions: `chmod`

#### Symbolic Mode

```bash
chmod u+x script.sh         # Add execute for user
chmod go-w report.txt       # Remove write for group and others
chmod a=r config.yaml       # Set read-only for all
```

#### Numeric Mode

| Permission | Value |
|------------|--------|
| r          | 4      |
| w          | 2      |
| x          | 1      |

```bash
chmod 755 script.sh   # rwxr-xr-x
chmod 644 config.cfg  # rw-r--r--
chmod 700 secrets.txt # rwx------
```

#### Recursive Changes

```bash
chmod -R 755 /var/www/html
```

> 🧑‍🏫 **Beginner’s Note:** Use `chmod` with caution. Recursive changes (`-R`) can break things if misused.

---

### 👤 Changing Ownership

#### `chown` – Change file owner (user or user:group)

```bash
sudo chown webuser file.txt
sudo chown appuser:devteam /opt/app
sudo chown -R nginx:nginx /var/www/html
```

#### `chgrp` – Change group ownership

```bash
sudo chgrp developers report.txt
sudo chgrp -R devteam /opt/project
```

---

### 🔐 Special Permissions

| Special Bit | Use Case                          | Symbol | Numeric |
|-------------|------------------------------------|--------|---------|
| setuid      | Run as file owner's user ID       | `s` on user  | 4       |
| setgid      | Run with group’s GID              | `s` on group | 2       |
| sticky bit  | Only owner can delete in dir      | `t` on others| 1       |

```bash
chmod 4755 binary_with_setuid
chmod 2750 group_script.sh
chmod +t /shared/directory
```

---

## 🔧 SRE Application Section – Real-World Use Cases

### 🔍 Scenario 1: Web Server Cannot Read Config

```bash
sudo chown nginx:nginx /etc/nginx/nginx.conf
sudo chmod 644 /etc/nginx/nginx.conf
```

### 📉 Scenario 2: Logs Not Writable by App

```bash
sudo chown appuser:logwriters /var/log/myapp/
sudo chmod 770 /var/log/myapp/
```

### 🛡️ Scenario 3: Protect Shared Directory

```bash
sudo chmod 1777 /tmp/shared_workspace  # sticky bit for safe multi-user deletion
```

### 🔍 SRE Troubleshooting Patterns

- Check permissions: `ls -l`
- Check file owner: `stat filename`
- Check running user: `ps aux | grep process`
- Test access: `sudo -u user cat /file`
- Log errors: `grep -i denied /var/log/*`

> 💡 **SRE Perspective:** Many outages are traced back to incorrect permissions on config, log, or data files. Always verify permissions and ownership during incident triage.

---

## 🧪 Practical Exercises

### 🟢 Beginner

1. Create a file `demo.sh` and give execute permission only to the owner.
2. Create a directory `project` and allow only the group to read/write.

### 🟡 Intermediate

3. Use `chown` to transfer ownership of a file to a user in your system.
4. Use `chmod` to recursively apply 755 to a test directory tree.

### 🔴 SRE

5. Simulate an "access denied" by removing permissions, then restore access.
6. Audit all world-writable files:

```bash
find / -type f -perm -o=w 2>/dev/null
```

---

## 📝 Quiz – Test Your Knowledge

**1.** What does `chmod 640 file.txt` do?

- a) Full access to all
- b) Read/write for user, read for group
- c) Execute for user only

**2.** How do you add execute permission for user only?

- a) `chmod +x file`
- b) `chmod u+x file`
- c) `chmod o+x file`

**3.** To change file owner and group:

```bash
____ user:group file.txt
```

**4.** What’s the sticky bit used for?

- a) Prevent reading
- b) Allow only owners to delete
- c) Make files invisible

**5.** Which numeric permission represents `rwxr-xr--`?

- a) 777
- b) 755
- c) 754

---

## ❓ FAQ & Troubleshooting

**Q1:** What's the difference between `chmod 777` and `755`?

- `777` = Full access to everyone (NOT secure)
- `755` = Full for user, read/execute for others (common for scripts)

**Q2:** How do I fix a "Permission Denied" on a config file?

- Check: `ls -l`
- Correct: `sudo chown user:group file && sudo chmod 644 file`

**Q3:** Can I apply different permissions to subfolders?

- Yes, using `find`:

```bash
find /opt/project -type d -exec chmod 750 {} \;
find /opt/project -type f -exec chmod 640 {} \;
```

**Q4:** Why use `sudo` with `chown`?

- Only root can change file ownership in most cases.

---

## 🛠️ Real-World SRE Scenario – Deployment Failure due to Log Permissions

### 🧩 Problem

An app fails to start during deployment. Logs show:

```
ERROR: Failed to write to /var/log/myapp/output.log: Permission denied
```

### 🔎 Investigation

```bash
ls -l /var/log/myapp
# -rw-r--r-- 1 root root 0 Mar 27 08:00 output.log
ps aux | grep myapp
# appuser ...
```

### ✅ Solution

```bash
sudo chown -R appuser:logwriters /var/log/myapp
sudo chmod 770 /var/log/myapp
sudo systemctl restart myapp
```

### 🧠 Lesson

Set appropriate ownership **before** deployment or container spin-up. Use a pre-deploy script to fix permissions automatically.

---

## 📚 Additional Resources

### 🟢 Beginner

- [Linux File Permissions Guide (Linux Handbook)](https://linuxhandbook.com/file-permissions/)
- `man chmod`, `man chown`, `man chgrp`

### 🟡 Intermediate

- `find` with permission filters: `man find`
- Directory permission case studies: `tldr chmod`

### 🔴 SRE Focused

- [Understanding Sticky Bit and setuid/setgid (RedHat)](https://access.redhat.com/solutions/70077)
- [Filesystem Security (Linux From Scratch)](https://www.linuxfromscratch.org/)
- [Auditd for Tracking Permission Changes](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-using_the_audit_service)

---

🏁 **Day 3 Complete – Excellent work!**
