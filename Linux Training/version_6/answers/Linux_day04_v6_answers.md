# Day 4 Answer Sheet

Below is a suggested **Answer Sheet** for the Day 4 quiz. Each answer includes an explanation to clarify the reasoning behind it.

---

## **Answer Key with Explanations**

### **🟢 Beginner**

1. **Which flag in `grep` makes the search case-insensitive?**  
   **Answer:** `-i`  
   **Explanation:** The `-i` flag tells `grep` to ignore case differences, meaning it treats uppercase and lowercase letters as the same. For example, it will match "Error," "ERROR," or "error" equally.

2. **What is the purpose of `>` in a command?**  
   **Answer:** It overwrites the output to a file.  
   **Explanation:** When you run `command > file`, the standard output (stdout) of `command` is redirected into `file`, overwriting any existing content. This is useful for creating new files or replacing the content of old ones with fresh output.

3. **What command finds `.conf` files in `/etc`? (Fill in the blank: `find /etc ____ "*.conf"`)**  
   **Answer:** `-name`  
   **Explanation:** The `-name` option of `find` searches for files whose names match a given pattern. Writing `find /etc -name "*.conf"` will locate any files that end with `.conf` in the `/etc` directory tree.

---

### **🟡 Intermediate**

4. **How do you show line numbers with `grep`? (Which option?)**  
   **Answer:** `-n`  
   **Explanation:** The `-n` option instructs `grep` to prefix each matching line with its line number. This is particularly helpful when you need to quickly pinpoint the location of a match in a file.

5. **Which `find` option locates files over 100MB in size? (Fill in the blank: `find /var/log ____ +100M`)**  
   **Answer:** `-size`  
   **Explanation:** The `-size` flag allows you to filter files by their size. `+100M` means larger than 100 megabytes. So `find /var/log -size +100M` identifies any file in `/var/log` exceeding 100MB.

6. **What does the `|` operator do in `ls | grep script`?**  
   **Answer:** It pipes (sends) the output of `ls` into the input of `grep`.  
   **Explanation:** The pipe operator `|` takes the standard output from the command on its left (`ls`) and redirects it as the standard input to the command on its right (`grep`). In this example, `grep` will only see filenames that came from `ls`, and then filter those for occurrences of the word "script."

---

### **🔴 SRE-Level**

7. **Which operator redirects both stdout and stderr to the same file?**  
   **Answer:** `&>`  
   **Explanation:** In many shells (including Bash), using `command &> file` sends both standard output (file descriptor 1) and standard error (file descriptor 2) into the same file, simplifying log capture.

8. **In the pipeline `cmd1 | cmd2 | cmd3`, which command receives the output of `cmd2`?**  
   **Answer:** `cmd3`  
   **Explanation:** The pipeline `cmd1 | cmd2 | cmd3` means:
   - `cmd1` sends output to `cmd2`.
   - `cmd2` receives `cmd1`'s output and processes it, then sends its own output to `cmd3`.
   - `cmd3` receives the output of `cmd2`.  
   Thus, `cmd3` is the final command in the chain and operates on whatever `cmd2` outputs.

9. **Why might using `grep -r /` be risky on a production system?**  
   **Answer:** It can scan the entire filesystem, potentially causing high CPU/I/O usage or returning massive output that could destabilize the system.  
   **Explanation:** The `-r` flag makes `grep` search recursively through every directory. Using `/` as the starting point means searching from the root of the filesystem, which includes all mounted drives, system folders, and files. This can overwhelm system resources, slow down production services, and create performance bottlenecks.

---

**Note:** In real-world SRE practice, always confirm potentially destructive or large-scope commands by running them on small directories first or using safe checks (like `-exec echo`) before performing permanent actions.
