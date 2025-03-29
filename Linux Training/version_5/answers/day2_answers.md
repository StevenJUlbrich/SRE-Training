# **Answer Key** to the quiz questions from the Day 2 module

Each answer includes a brief **explanation** for why it is correct. Use these as a reference for checking your understanding or guiding discussions.

---

## **Beginner Tier (4 Questions)**

1. **Which command creates an empty file named `notes.txt`?**  
   - **Answer**: **B) `touch notes.txt`**  
   - **Explanation**:  
     - `touch filename` is the standard way to create a new, empty file in Linux.  
     - `mkdir notes.txt` would try to create a directory, not a file.  
     - `less` only views file content.  
     - `rm -i` removes a file, not creates one.

2. **How do you view the last 5 lines of `app.log`?**  
   - **Answer**: **C) `tail -n 5 app.log`**  
   - **Explanation**:  
     - `tail -n 5` displays the last 5 lines.  
     - `head -5 app.log` would show the first 5 lines.  
     - `cat app.log 5` isn’t valid syntax for showing only 5 lines.  
     - `more -d app.log` shows content page by page, not specifically the last 5 lines.

3. **What happens if you run `rmdir mydir` when `mydir` has files?**  
   - **Answer**: **B) `rmdir` fails because the directory is not empty.**  
   - **Explanation**:  
     - `rmdir` only removes empty directories. If the directory has files, you must remove them (or use `rm -r`) first.  
     - It does not automatically move or delete the files.

4. **Which command shows file contents in one continuous flow (no interactive scrolling)?**  
   - **Answer**: **B) `cat file.txt`**  
   - **Explanation**:  
     - `cat` dumps the entire file content at once to the screen.  
     - `less` and `more` provide interactive paging.  
     - `head` only shows the first lines.

---

## **Intermediate Tier (4 Questions)**

1. **You need to create multiple directories at once (`/mnt/data/reports/logs`). Which command should you use?**  
   - **Answer**: **B) `mkdir -p /mnt/data/reports/logs`**  
   - **Explanation**:  
     - The `-p` option creates all necessary parent directories in one command.  
     - Simply typing `mkdir /mnt/data /mnt/data/reports /mnt/data/reports/logs` manually can work, but it’s not a single, automated step.  
     - `mkdir -r` is not valid syntax for making nested directories.

2. **If you want to copy `/etc/nginx` to `/backup/nginx` while keeping permissions and symlinks, which option is best?**  
   - **Answer**: **D) `cp -a /etc/nginx /backup/nginx`**  
   - **Explanation**:  
     - The `-a` (archive) option preserves ownership, permissions, timestamps, symlinks, and more, making it ideal for full backups.  
     - `-r` alone copies directories recursively but doesn’t necessarily preserve all attributes.  
     - `-p` preserves only some attributes but not symlinks the same way `-a` does.

3. **You accidentally wrote sensitive data into `credentials.txt`. You must remove it without a prompt. Which command ensures no prompts?**  
   - **Answer**: **C) `rm -f credentials.txt`**  
   - **Explanation**:  
     - The `-f` (force) option removes the file without asking for confirmation or showing errors about missing files.  
     - `rm credentials.txt` could prompt if the file is write-protected, while `rm -i` explicitly prompts for confirmation.  
     - `mv credentials.txt /dev/null` is not valid, because `/dev/null` is not a directory—this would fail.

4. **Which command prevents overwriting an existing file without warning?**  
   - **Answer**: **B) `cp -i`**  
   - **Explanation**:  
     - The `-i` (interactive) flag prompts you for confirmation before overwriting an existing file.  
     - `cp -f` forces overwrites without prompting.  
     - `cp -r` is for recursive copying, and `cp -n` (on some systems) is “no overwrite,” but it’s less common than `-i` for interactive checks.

---

## **SRE-Level Tier (4 Questions)**

1. **During an incident, you suspect new log entries in `app.log`. Which command is most appropriate for real-time monitoring if log rotation is frequent?**  
   - **Answer**: **B) `tail -F app.log`**  
   - **Explanation**:  
     - `tail -f` follows a file but can break when the file is rotated.  
     - `tail -F` automatically reopens the file if it gets moved or replaced during rotation, making it ideal for production logs.

2. **You have a script that renames config files atomically. Which is the best approach?**  
   - **Answer**: **B) `mv config.yml config.yml.bak && mv config_new.yml config.yml`**  
   - **Explanation**:  
     - This sequence renames the existing config to a backup, then renames the new file into place. If there’s an issue, you can easily roll back.  
     - The other options involve partial removal, copying, or don’t keep an immediate fallback in place.

3. **Which command usage is best for removing large, old logs while seeing the details of each deletion?**  
   - **Answer**: **C) `rm -rfv /logs/old/`**  
   - **Explanation**:  
     - `-r` removes directories recursively, `-f` forces removal without prompt, and `-v` provides verbose output of every file/directory removed.  
     - `rm -iv` would prompt for every file—slowing you down if you have hundreds of files.  
     - Just `rm -rf` would not show details.

4. **To avoid losing file attributes (ownership, timestamps, SELinux context) during a directory backup, which copy approach is recommended?**  
   - **Answer**: **A) `cp -a`**  
   - **Explanation**:  
     - `cp -a` is “archive mode,” which preserves all attributes including SELinux context, symlinks, ownership, permissions, and timestamps.  
     - `-r` alone doesn’t guarantee preserving everything.  
     - `mv -f` moves rather than copies, and can’t be used if you want to keep the original intact.  
     - `cp -n` is “no overwrite,” not for preserving attributes.

---

### **Key Points:**

- Use **interactive flags** (`-i`) for safety to avoid accidental overwrites or deletions in critical environments.  
- **Preserving attributes** (`-a`) is crucial for backups of system directories.  
- **Following logs** with `-F` is the best practice in production to handle log rotation seamlessly.  

These explanations should help clarify **why** each answer is correct and offer insight into proper usage and typical pitfalls.
