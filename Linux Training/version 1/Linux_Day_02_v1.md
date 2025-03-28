# 🚀 **Day 2: File Manipulation – Creating, Viewing, Copying, Moving, and Deleting Files and Directories**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 1:**

Yesterday, you were introduced to Linux, the shell environment, basic navigation (`pwd`, `ls`, `cd`), the Filesystem Hierarchy Standard (FHS), and methods to find help (`man`, `--help`, `info`).  

### 📅 **Today's Topics and Importance:**

Today, you'll learn essential commands for manipulating files and directories in Linux. Managing files is foundational in Linux administration, software development, troubleshooting, and daily operations. These skills will help you effectively organize your workspace and handle files confidently.

### 🎯 **Learning Objectives:**

By the end of Day 2, you will be able to:

- Create and organize directories and files (`touch`, `mkdir`).
- View file contents (`cat`, `less`, `more`, `head`, `tail`).
- Copy and move files (`cp`, `mv`).
- Delete files and directories (`rm`, `rmdir`).

---

## 📚 **Core Concepts Explained**

Linux treats everything as a file. Documents, directories, configuration settings, devices, and more—all represented as files. Think of your Linux filesystem as a virtual filing cabinet, where you can create folders (directories), store documents (files), move items around, copy important papers, and throw away (delete) unnecessary ones.

Here's an analogy:

- **Creating** files/directories is like adding new documents or folders.
- **Viewing** files is like reading papers.
- **Copying/Moving** is duplicating or relocating documents/folders.
- **Deleting** files is discarding unnecessary documents.

---

## 💻 **Commands to Learn (Detailed)**

### 1. **Creating Files and Directories (`touch`, `mkdir`)**

**`touch` – Create an empty file or update timestamp**

- **Syntax:**

```bash
touch [filename]
```

- **Examples:**

```bash
touch notes.txt           # Creates an empty file named notes.txt
touch report.log script.sh  # Creates two empty files
```

**`mkdir` – Create new directories**

- **Syntax:**

```bash
mkdir [options] [directory_name]
```

- **Common options:**
  - `-p`: Creates nested directories.

- **Examples:**

```bash
mkdir projects           # Creates a directory called projects
mkdir -p projects/java   # Creates nested directories (projects and java inside it)
```

---

### 2. **Viewing Files (`cat`, `less`, `more`, `head`, `tail`)**

- **`cat`** – Displays entire file content quickly.

```bash
cat notes.txt
```

- **`less`** – View file content interactively (scrollable).

```bash
less notes.txt
```

(*Use arrows to navigate; press `q` to quit.*)

- **`more`** – Paginated view of file content.

```bash
more notes.txt
```

(*Press `space` to navigate pages; press `q` to quit.*)

- **`head`** – Displays first few lines of a file.

```bash
head -n 5 notes.txt    # First 5 lines
```

- **`tail`** – Displays last few lines of a file.

```bash
tail -n 10 notes.txt   # Last 10 lines
```

---

### 3. **Copying and Moving Files (`cp`, `mv`)**

- **`cp` – Copy files/directories**

```bash
cp source destination
```

- **Common options:**
  - `-r`: Recursively copies directories.

- **Examples:**

```bash
cp notes.txt backup.txt          # Copies notes.txt to backup.txt
cp -r projects projects_backup   # Copies entire directory recursively
```

- **`mv` – Move or rename files/directories**

```bash
mv source destination
```

- **Examples:**

```bash
mv notes.txt documents/           # Moves file into documents directory
mv oldname.txt newname.txt        # Renames file from oldname.txt to newname.txt
```

---

### 4. **Deleting Files and Directories (`rm`, `rmdir`)**

- **`rm` – Remove files/directories**

```bash
rm [options] file
```

- **Common options:**
  - `-r`: Recursively deletes directories and their contents.
  - `-i`: Interactive prompt before deletion (safer).

- **Examples:**

```bash
rm oldnotes.txt                # Deletes file oldnotes.txt
rm -i unwanted.txt             # Asks confirmation before deleting
rm -r unused_folder            # Deletes directory recursively
```

- **`rmdir` – Removes empty directories**

```bash
rmdir directory_name
```

- **Example:**

```bash
rmdir empty_folder             # Removes empty_folder only if it's empty
```

---

## 🎯 **Practical Exercise Suggestion**

Perform these steps independently in your Linux environment to reinforce today's concepts:

1. Create a directory named `Day2` in your home folder.
2. Inside `Day2`, create files: `file1.txt`, `file2.txt`.
3. Create subdirectories: `docs`, `backup`.
4. View and explore file contents using `cat`, `less`, `more`, `head`, `tail`.
5. Copy `file1.txt` into `backup`.
6. Rename `file2.txt` to `notes.txt`.
7. Delete `file1.txt`.
8. Remove the empty `docs` directory.

---

## 📝 **Quiz Section (End of Day)**

**1.** Which command creates nested directories such as `work/project1`?

- a) `mkdir -r work/project1`
- b) `mkdir -p work/project1`
- c) `mkdir -f work/project1`

**2.** To rename a file `old.txt` to `new.txt`, what command would you use?

- Fill in the blank:

```bash
____ old.txt new.txt
```

**3.** What command lets you safely delete a file by prompting confirmation?

- a) `rm -f file.txt`
- b) `rm -i file.txt`
- c) `rm -r file.txt`

**4.** Which command shows only the last 15 lines of a file?

- a) `head -n 15 file.txt`
- b) `tail -n 15 file.txt`
- c) `cat -15 file.txt`

**5.** Which command would you use to interactively scroll through the contents of a file?

- a) `cp file.txt`
- b) `less file.txt`
- c) `touch file.txt`

---

## ❓ **FAQ Section**

**Q1:** What’s the difference between `less` and `more`?

- **A:** Both allow viewing large files. `less` supports scrolling forward and backward, while `more` only scrolls forward.

**Q2:** Does `rm` permanently delete files?

- **A:** Yes, deleted files usually can't be recovered easily. Always double-check before deleting.

**Q3:** Can `mv` overwrite existing files?

- **A:** Yes, `mv` overwrites files without warning. Use `mv -i` for safety prompts.

**Q4:** Why does `rmdir` fail to delete my directory?

- **A:** `rmdir` only removes empty directories. Use `rm -r` for directories containing files.

---

## 🚧 **Common Issues Section**

### **Issue 1:** `"rm: cannot remove 'folder': Is a directory"`

- **Reason:** You're trying to delete a directory without `-r`.
- **Solution:** Use `rm -r folder`.

### **Issue 2:** `"rmdir: failed to remove 'folder': Directory not empty"`

- **Reason:** `rmdir` only deletes empty directories.
- **Solution:** Delete contents first or use `rm -r folder`.

---

🎯 **Next Steps:**  
Tomorrow, we will explore file permissions, ownership, and security fundamentals.

---

📌 **Note:** Your detailed quiz **Answer Key** is provided separately for reference and review.

Great progress today—keep practicing!
