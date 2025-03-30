# Day 2 Answer Sheet

Below is an **answer key** for all quiz questions from Beginner, Intermediate, and SRE-Level tiers, complete with explanations of **why** each choice is correct (or incorrect). Use this as a reference to check and understand your responses.

---

## **Beginner Level (4 Questions)**

1. **Question**: Which command creates an empty file named `notes.txt`?  
   A) `mkdir notes.txt`  
   B) `touch notes.txt`  
   C) `less notes.txt`  
   D) `rm -i notes.txt`  

   **Correct Answer**: **B) `touch notes.txt`**  
   **Explanation**:  
   - `mkdir notes.txt` attempts to create a directory, not a file.  
   - `less notes.txt` simply opens a pager to view a file (and shows an error if the file doesn’t exist).  
   - `rm -i notes.txt` tries to remove a file with interactive prompting.  
   - **`touch`** is the standard command to create an empty file if it doesn’t exist (or update its timestamp if it does).

2. **Question**: How do you view the last 5 lines of `app.log`?  
   A) `head -5 app.log`  
   B) `cat app.log 5`  
   C) `tail -n 5 app.log`  
   D) `more -d app.log`  

   **Correct Answer**: **C) `tail -n 5 app.log`**  
   **Explanation**:  
   - `head -5 app.log` shows the *first* 5 lines, not the last 5.  
   - `cat app.log 5` is invalid syntax for what we need.  
   - `more -d app.log` pages through the file from the beginning.  
   - **`tail -n 5`** is specifically for displaying the last 5 lines of a file.

3. **Question**: What happens if you run `rmdir mydir` when `mydir` has files inside?  
   A) `mydir` is removed along with all files  
   B) `rmdir` fails because the directory isn’t empty  
   C) The files are automatically moved to `/tmp`  
   D) The command partially deletes some files  

   **Correct Answer**: **B) `rmdir` fails because the directory isn’t empty**  
   **Explanation**:  
   - `rmdir` only removes *empty* directories.  
   - It does not delete files nor move them automatically. If you must remove a directory with contents, you’d use `rm -r mydir`.

4. **Question**: Which command shows the entire file contents in one go (no interactive scrolling)?  
   A) `less file.txt`  
   B) `cat file.txt`  
   C) `head file.txt`  
   D) `more file.txt`  

   **Correct Answer**: **B) `cat file.txt`**  
   **Explanation**:  
   - `less` (A) and `more` (D) are pagers that let you scroll through the file interactively.  
   - `head` (C) only shows the first lines by default.  
   - **`cat file.txt`** dumps the entire file immediately to your terminal, with no paging.

---

## **Intermediate Level (4 Questions)**

1. **Question**: Which command and option combination creates the entire path `/data/projects/logs` if none of the folders exist?  
   A) `mkdir /data /data/projects /data/projects/logs`  
   B) `mkdir -p /data/projects/logs`  
   C) `mkdir -r /data/projects/logs`  
   D) `rmdir -p /data/projects/logs`  

   **Correct Answer**: **B) `mkdir -p /data/projects/logs`**  
   **Explanation**:  
   - `mkdir /data /data/projects /data/projects/logs` (A) would work but is not a single command. You’d have to run it multiple times or chain them.  
   - The `-r` option (C) isn’t valid for creating directories; `-r` is often used for removing recursively.  
   - `rmdir -p ...` (D) removes directories, not creates them.  
   - **`mkdir -p`** creates parent directories automatically, making it a single, complete solution.

2. **Question**: If you want to copy `/etc/nginx` into `/backup/nginx` and preserve permissions, ownership, and symlinks, which flag should you use?  
   A) `cp -r /etc/nginx /backup/nginx`  
   B) `cp -p /etc/nginx /backup/nginx`  
   C) `cp -a /etc/nginx /backup/nginx`  
   D) `cp -i /etc/nginx /backup/nginx`  

   **Correct Answer**: **C) `cp -a /etc/nginx /backup/nginx`**  
   **Explanation**:  
   - `cp -r` (A) copies recursively but doesn’t preserve full permissions/ownership or symlinks by default.  
   - `cp -p` (B) preserves permissions and timestamps but not necessarily symbolic links or special files in a fully consistent manner.  
   - **`cp -a`** (archive mode) is the most comprehensive for preserving all attributes, including symlinks, ownership, timestamps, and more.  
   - `cp -i` (D) prompts for overwrites but doesn’t address preserving metadata.

3. **Question**: You accidentally wrote secrets into `credentials.txt`. You must remove it without any confirmation prompts. Which command ensures no prompt?  
   A) `rm credentials.txt`  
   B) `rm -i credentials.txt`  
   C) `rm -f credentials.txt`  
   D) `mv credentials.txt /dev/null`  

   **Correct Answer**: **C) `rm -f credentials.txt`**  
   **Explanation**:  
   - `rm credentials.txt` might ask for confirmation if there are alias or permissions issues, depending on the shell environment.  
   - `rm -i` (B) always prompts for each file, which is the opposite of what we want.  
   - `mv credentials.txt /dev/null` (D) is an unusual approach and may fail or cause confusion; it doesn’t guarantee all shells treat `/dev/null` like a directory.  
   - **`rm -f`** forcibly removes the file without asking for confirmation.

4. **Question**: Which command helps you avoid overwriting an existing file?  
   A) `cp -f source.txt dest.txt`  
   B) `cp -i source.txt dest.txt`  
   C) `cp -r source.txt dest.txt`  
   D) `cp -n source.txt dest.txt` (assuming your cp supports `-n`)  

   **Correct Answer**:  
   - If your system supports `-n`, then **D) `cp -n`** (no-clobber) **completely avoids overwriting** an existing file, doing so *without* any prompt; it simply skips copying if the destination exists.  
   - If the question is interpreted in the sense of standard usage with a warning/prompt, **B) `cp -i`** would be correct because it asks for permission before overwriting.  

   **Explanation**:  
   - `cp -f` overwrites forcibly.  
   - `cp -r` is about copying directories recursively, not preventing overwrite.  
   - **`cp -n`** is the literal “no-clobber” option: it never overwrites an existing file. This is often the best direct method to avoid overwriting entirely.  
   - **`cp -i`** also prevents inadvertent overwrites, but it does so by prompting (i.e., you’ll see a warning and choose yes or no).  

   Depending on your distribution and course materials, either “**-n**” or “**-i**” can be considered correct for “avoiding overwrite.” However, `-n` does it silently (no overwrite, no prompt), while `-i` does it interactively.

---

## **SRE-Level Tier (4 Questions)**

1. **Question**: During an incident, which command is most appropriate for real-time monitoring of a frequently rotated log file?  
   A) `tail -f app.log`  
   B) `tail -F app.log`  
   C) `head -f app.log`  
   D) `less -N app.log`  

   **Correct Answer**: **B) `tail -F app.log`**  
   **Explanation**:  
   - `tail -f app.log` works for a log file that isn’t rotated. Once the file is rotated/renamed, `tail -f` loses track.  
   - `head -f` (C) doesn’t exist in that sense; `head` is not typically used for following.  
   - `less -N` (D) shows line numbers, but it doesn’t auto-follow rotations.  
   - **`tail -F`** not only follows the file but also continues following after rotation (common in production logrotate scenarios).

2. **Question**: You have a script that renames config files atomically. Which approach is best?  
   A) `mv config.yml config.yml.bak && cp config_new.yml config.yml`  
   B) `mv config.yml config.yml.bak && mv config_new.yml config.yml`  
   C) `cp config_new.yml config.yml.bak && rm config.yml`  
   D) `tail -f config.yml && cp config_new.yml config.yml`  

   **Correct Answer**: **B) `mv config.yml config.yml.bak && mv config_new.yml config.yml`**  
   **Explanation**:  
   - (A) copies new config over but leaves the old config in `config.yml` momentarily before the copy completes, which might cause partial overwrites.  
   - (C) is more convoluted and does not directly swap the main config file in a single atomic step.  
   - (D) is nonsensical (`tail -f config.yml` does nothing to rename it).  
   - **B)** first moves the original to a backup, then *moves* the new config into place, ensuring an instant rename step if on the same filesystem—this is the “atomic” approach.

3. **Question**: Which command usage is best for removing large, old logs while displaying each file removed?  
   A) `rm -rf /var/log/old/`  
   B) `rm -rv /var/log/old/`  
   C) `rm -rfv /var/log/old/`  
   D) `rm -iv /var/log/old/`  

   **Correct Answer**: **C) `rm -rfv /var/log/old/`**  
   **Explanation**:  
   - `-r` (recursive) ensures directories and subdirectories are removed.  
   - `-f` (force) proceeds without interrupting the script for confirmation. This is typical in an automated job.  
   - `-v` (verbose) prints each file name as it’s removed.  
   - So **`-rfv`** together is ideal for large-scale automated deletions with logged output.

4. **Question**: To avoid losing file ownership, permissions, timestamps, and SELinux context during a directory backup, which `cp` option is recommended?  
   A) `-a`  
   B) `-r`  
   C) `-p`  
   D) `-i`  

   **Correct Answer**: **A) `-a`**  
   **Explanation**:  
   - `-r` copies recursively but doesn’t preserve all file attributes.  
   - `-p` preserves ownership/timestamps but does not always capture symlinks or special files as thoroughly.  
   - `-i` is only interactive for overwrites.  
   - **`-a`** is “archive” mode, combining recursion, preservation of all attributes (including SELinux context where supported), and symlinks.

---

### **Summary of Correct Answers**

- **Beginner**:  
  1) B, 2) C, 3) B, 4) B  
- **Intermediate**:  
  1) B, 2) C, 3) C, 4) (Typically D if your shell supports `-n`, otherwise B for interactive avoidance)  
- **SRE-Level**:  
  1) B, 2) B, 3) C, 4) A  

Use these explanations to understand not just the “correct” choice, but also **why** the other options don’t fulfill the required behavior. This helps deepen your command-line and SRE-level knowledge.
