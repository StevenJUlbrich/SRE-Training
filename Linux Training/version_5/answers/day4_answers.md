# Day 4: Quiz Answer Sheet with Explanations

Below are the answer keys for each quiz question from the Day 4 module, along with detailed explanations.

---

## 🟢 Beginner Questions

**1. Which flag in `grep` makes the search case-insensitive?**

- **Answer**: `-i`
- **Explanation**: `-i` tells `grep` to ignore the difference between uppercase and lowercase letters, so `ERROR`, `Error`, and `error` are all matched.

**2. What does `>` do when used after a command?**

- **Answer**: It overwrites the output into a file.
- **Explanation**: `>` is a redirection operator that takes the standard output (stdout) of a command and writes it to a specified file, replacing any existing content in that file.

**3. Which command searches for `.conf` files in `/etc`? (Fill in the blank: `find /etc ______ "*.conf"`)**

- **Answer**: `find /etc -name "*.conf"`
- **Explanation**: The `-name` option is used to match files by name. You must enclose wildcards like `*.conf` in quotes to avoid shell expansion.

---

## 🟡 Intermediate Questions

**1. How do you show line numbers with `grep`? (Which option?)**

- **Answer**: `-n`
- **Explanation**: The `-n` flag tells `grep` to display line numbers before each matching line. This is useful for pinpointing exactly where a match occurs in a file.

**2. Which command locates files over 100MB in size? (Fill in the blank: `find /var/log ______ +100M`)**

- **Answer**: `find /var/log -size +100M`
- **Explanation**: The `-size +100M` parameter in `find` looks for files bigger than 100 megabytes. Adjusting the letter (like `k` for kilobytes or `G` for gigabytes) changes the unit.

**3. What does the `|` operator do in `ls | grep script`?**

- **Answer**: It sends the output of the `ls` command into `grep` as input.
- **Explanation**: The pipe operator `|` allows you to chain commands such that the output of one command becomes the input of another command, letting you filter results without using temporary files.

---

## 🔴 SRE-Level Questions

**1. How can you redirect both stdout and stderr to the same file? (Provide the redirection operator)**

- **Answer**: `&>` (in Bash) or using `> file 2>&1`.
- **Explanation**: There are two primary ways:
  - `command &> file` is a shorthand in some shells (like Bash) to merge both standard output (stdout) and standard error (stderr) into the specified file.
  - Alternatively, `command > file 2>&1` merges stderr into stdout, effectively capturing all output in a single file.

**2. In a pipeline (`cmd1 | cmd2 | cmd3`), which command receives the output of `cmd2`?**

- **Answer**: `cmd3`
- **Explanation**: A pipe directs the output of `cmd2` into the input of the next command in the chain, which is `cmd3`. So `cmd3` gets whatever `cmd2` emits to stdout.

**3. Name one reason why searching logs with `grep -r /` might be risky in production.**

- **Answer**: It can cause massive I/O, potentially locking up the server or impacting performance.
- **Explanation**: Running a recursive grep on the entire filesystem (`/`) scans every file. This can overwhelm server resources, read through device files or virtual file systems, and lead to high load or I/O contention.

---

## Notes

- Always double-check the commands before running them in production.
- For large-scale queries, narrow your search scope (e.g., `grep -r /var/log/app`) to avoid high resource usage.

---

_This concludes the Day 4 quiz answer sheet with explanations._
