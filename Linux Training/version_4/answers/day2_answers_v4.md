# Day 2 Quiz Answers

## 🟢 Beginner Tier

**1. Multiple-choice:**  
Which command explicitly creates nested directories such as `app/logs/errors`?

- **Answer:** `mkdir -p app/logs/errors`
- **Explanation:** The `-p` (parents) flag explicitly tells `mkdir` to create all required intermediate directories, ensuring no errors if intermediate directories don't exist.

---

**2. Fill-in-the-blank:**  
To explicitly view only the first 20 lines of a file, the command is `head ___ 20 file.txt`.

- **Answer:** `-n`
- **Explanation:** The `-n` option explicitly specifies the exact number of lines to display from the start of a file.

Corrected explicit command:

```bash
head -n 20 file.txt
```

---

**3. Multiple-choice:**  
Explicitly, which command removes an empty directory named `oldlogs`?

- **Answer:** `rmdir oldlogs`
- **Explanation:** The `rmdir` command explicitly removes only empty directories, making it the safest choice for deleting directories without accidentally removing contents.

---

## 🟡 Intermediate Tier

**1. Scenario-based:**  
You explicitly want to copy `config.conf` to `backup.conf`, explicitly preserving permissions and timestamps. Which explicit command achieves this?

- **Answer:** `cp -a config.conf backup.conf`
- **Explanation:** The `-a` (archive) flag explicitly preserves file attributes such as permissions, timestamps, ownership, and symbolic links during copy operations.

---

**2. Multiple-choice:**  
Explicitly, which command continuously displays new log entries in real-time?

- **Answer:** `tail -f /var/log/app.log`
- **Explanation:** The `tail -f` command explicitly follows file content in real-time, making it ideal for monitoring logs continuously during troubleshooting or incidents.

---

**3. Fill-in-the-blank:**  
To explicitly rename a file from `error.log` to `error_old.log`, you explicitly use the command: `mv _____ _____`.

- **Answer:** `error.log error_old.log`
- **Explanation:** The `mv` command explicitly renames (moves) a file from the first argument (`error.log`) to the second argument (`error_old.log`).

Corrected explicit command:

```bash
mv error.log error_old.log
```

---

**4. Scenario-based:**  
Explicitly, you accidentally deleted a critical file. What explicit preventive measure could have avoided this?

- **Answer:** Using `rm -i`
- **Explanation:** The interactive option (`-i`) explicitly prompts for confirmation before deleting each file, reducing the risk of accidental deletions.

---

## 🔴 SRE-Level Tier

**1. Scenario-based:**  
Explicitly during an incident, you need real-time monitoring of an application log file explicitly to detect errors instantly. Which explicit command is best suited?

- **Answer:** `tail -f /var/log/application.log`
- **Explanation:** `tail -f` explicitly provides immediate, continuous updates to logs, enabling rapid detection and response to real-time events.

---

**2. Fill-in-the-blank:**  
Explicitly removing directories containing files requires the command: `rm ____ directoryname`.

- **Answer:** `-r`
- **Explanation:** The recursive option (`-r`) explicitly allows `rm` to remove directories along with all their contents. Use with caution.

Corrected explicit command:

```bash
rm -r directoryname
```

---

**3. Multiple-choice:**  
Explicitly, to securely delete multiple files interactively, which explicit command would you use?

- **Answer:** `rm -i file*`
- **Explanation:** Using the `-i` (interactive) flag explicitly ensures each file deletion is confirmed individually, significantly reducing the risk of errors.

---

**4. Scenario-based:**  
Explicitly, you must create multiple empty log files (`app.log`, `db.log`, `web.log`) explicitly in a single command. What explicit command do you run?

- **Answer:** `touch {app,db,web}.log`
- **Explanation:** Brace expansion explicitly allows creating multiple files efficiently in one concise command, a technique frequently used by SREs to streamline operations.

Corrected explicit command:

```bash
touch {app,db,web}.log
```
