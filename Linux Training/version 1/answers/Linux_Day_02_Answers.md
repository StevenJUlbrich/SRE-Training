# 🗒️ **Day 2 Quiz – Answer Key with Explanations**

Below are the detailed answers and explanations for Day 2's quiz:

---

**1. Which command creates nested directories such as `work/project1`?**

✅ **Correct Answer:**  
**b)** `mkdir -p work/project1`

**Explanation:**

- **a)** `mkdir -r work/project1`:  
Incorrect because `-r` is not a valid option for `mkdir`. It's used with commands like `rm` or `cp`.

- **c)** `mkdir -f work/project1`:  
Incorrect because `-f` (force) is not a valid `mkdir` option.

---

**2. To rename a file `old.txt` to `new.txt`, what command would you use?**

✅ **Correct Answer (fill-in-the-blank):**  

```bash
mv old.txt new.txt
```

**Explanation:**

- `mv` is used for moving or renaming files.  
- Commands like `cp` would create a copy rather than rename, and `rm` would delete, not rename.

---

**3. What command lets you safely delete a file by prompting confirmation?**

✅ **Correct Answer:**  
**b)** `rm -i file.txt`

**Explanation:**

- **a)** `rm -f file.txt`:  
Deletes without prompting (`force`), making it less safe.

- **c)** `rm -r file.txt`:  
Used to recursively delete directories/files without prompting unless combined with `-i`.

---

**4. Which command shows only the last 15 lines of a file?**

✅ **Correct Answer:**  
**b)** `tail -n 15 file.txt`

**Explanation:**

- **a)** `head -n 15 file.txt`:  
Shows the first 15 lines, not the last.

- **c)** `cat -15 file.txt`:  
Invalid syntax; `cat` doesn’t use numerical options to limit lines.

---

**5. Which command would you use to interactively scroll through the contents of a file?**

✅ **Correct Answer:**  
**b)** `less file.txt`

**Explanation:**

- **a)** `cp file.txt`:  
Copies the file; it doesn’t display contents.

- **c)** `touch file.txt`:  
Creates a new empty file or updates timestamps, without displaying contents.

- `less` provides an interactive, scrollable view, ideal for viewing large files.
