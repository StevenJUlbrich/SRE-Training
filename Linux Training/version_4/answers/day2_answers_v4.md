# **Day 2 V3 Quiz Answer Key**

with real-world SRE context, command walkthroughs, and learning rationale for every question:

---

## ✅ **Day 2 Full Answer Key with Explanations**

---

### 🧑‍🏫 **Beginner Level**

---

**1. What does `touch file.txt` do?**  

- a) Deletes it  
- b) Views its content  
- ✅ c) **Creates it**

🔍 **Explanation:**  
The `touch` command is primarily used to create an empty file if it doesn't exist. It can also update the **modification** timestamp of an existing file.  
📌 **SRE Context:** Often used in automation scripts to prepare placeholder logs or trigger file watchers.

---

**2. Which option makes `mkdir` create parent directories as needed?**  

- ✅ a) `-p`  
- b) `-r`  
- c) `-m`

🔍 **Explanation:**  
The `-p` flag instructs `mkdir` to create intermediate directories along the path if they don’t already exist — making directory creation scripts idempotent.  
📌 **SRE Context:** In automation pipelines, using `mkdir -p` avoids failures when parent paths are missing.

---

**3. How do you view the top 5 lines of a config file?**  

- a) `less -n config`  
- b) `tail -n 5 config`  
- ✅ c) `head -n 5 config`

🔍 **Explanation:**  
`head` outputs the first lines of a file. `-n 5` limits the output to just five lines.  
📌 **SRE Context:** Useful when verifying that configs begin with expected headers or structure.

---

### 🧩 **Intermediate Level**

---

**4. Which command shows the most recent 25 lines of a log?**  

- ✅ `tail -n 25 filename`

🔍 **Explanation:**  
`tail` is designed to show the end of a file — typically logs. With `-n`, it lets you control how many lines to show.  
📌 **SRE Context:** Helps pinpoint recent events during live debugging or postmortem.

---

**5. Which `cp` option preserves file metadata and structure during copying?**  

- a) `-f`  
- ✅ b) `-a`

🔍 **Explanation:**  
The `-a` (archive) flag ensures that symbolic links, file permissions, timestamps, and ownership are preserved.  
📌 **SRE Context:** Essential when backing up configuration directories to ensure an identical restore state.

---

**6. What does this command do?**  

```bash
cp config.conf config.conf.bak.$(date +%F-%H%M)
```  

- ✅ a) Copies config.conf with a timestamped name  
- b) Compresses the config file  
- c) Deletes the original file

🔍 **Explanation:**  
This creates a backup copy of the config file, using the current date/time to ensure uniqueness and tracking.  
📌 **SRE Context:** Timestamped backups allow safe rollback and simplify audits.

---

### ⚙️ **SRE Application Level**

---

**7. Which command sequence is most appropriate during a \"disk full\" incident?**  

- a) `rm -rf /var/log/*`  
- b) `du -sh /var/* | sort -rh | head -10`  
- c) `mkdir /backup && mv /var/log/* /backup/`  
- ✅ d) **Both b and c**

🔍 **Explanation:**  
Option **b** helps identify the biggest space consumers. Option **c** safely moves data instead of deleting it. Option **a** is dangerous and irreversible.  
📌 **SRE Context:** Root-cause analysis, rollback, and auditing are impossible if logs are deleted blindly. Always prioritize preservation and analysis.

---

**8. Before modifying a production configuration, what should you do?**  

- a) Edit it directly  
- b) Run `rm` on the old file  
- ✅ c) Use `cp -a` to back it up

🔍 **Explanation:**  
`cp -a` ensures a faithful backup of the config with full metadata. Editing directly without a backup is risky, and deleting the original removes history.  
📌 **SRE Context:** Backups protect you during incidents, audits, and rollbacks.

---

**9. You want to track live error messages in a growing log. Which command fits?**  

```bash
tail -f /var/log/app.log | grep ERROR
```  

- ✅ a) Tracks ERROR messages in real-time  
- b) Deletes all errors  
- c) Compresses log on the fly

🔍 **Explanation:**  
This command continuously monitors new lines appended to the log and filters only those containing “ERROR”.  
📌 **SRE Context:** Ideal during active outages or post-deploy monitoring to catch issues as they happen.

---
