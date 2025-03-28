# 🚀 **Day 5: Intermediate Text/Data Manipulation – sed, awk, sort, uniq, wc, and Advanced Pipes**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 4:**

Yesterday, you mastered powerful tools for text searching (`grep`), file finding (`find`), command chaining (`|` pipes), and redirection (`>`, `>>`, `<`). These tools enhanced your capability to quickly find and manage information in Linux.

### 📅 **Today's Topics and Importance:**

Today, you'll learn intermediate text and data manipulation commands: **`sed`**, **`awk`**, **`sort`**, **`uniq`**, and **`wc`**, combined with advanced pipe usage. These commands significantly enhance your ability to automate data processing, formatting, extraction, and reporting tasks.

### 🎯 **Learning Objectives:**

By the end of Day 5, you will be able to:

- Perform text substitutions and editing with `sed`.
- Extract and manipulate text fields with `awk`.
- Sort data efficiently using `sort`.
- Identify and handle duplicate entries using `uniq`.
- Count lines, words, and characters with `wc`.
- Combine commands into powerful pipelines.

---

## 📚 **Core Concepts Explained**

- **sed (Stream Editor):** Used primarily for text transformations, substitutions, and editing. Imagine it as "find-and-replace" on steroids.

- **awk:** A powerful scripting language for text manipulation, capable of extracting fields, performing calculations, and formatting output.

- **sort:** Organizes file content alphabetically, numerically, or by custom criteria.

- **uniq:** Removes or reports duplicate lines from sorted data.

- **wc (Word Count):** Counts lines, words, or characters in files or streams.

Combining these commands with pipes (`|`) lets you create advanced workflows for data manipulation tasks.

---

## 💻 **Commands to Learn (Detailed)**

### **1. sed – Text Transformation & Editing**

- **Purpose:** Edit streams or files via command-line substitutions.

- **Syntax:**

```bash
sed 's/pattern/replacement/g' filename
```

- Common options:
  - `-i`: Edit files in place.

**Examples:**

```bash
sed 's/error/ERROR/g' logfile.txt     # Replace 'error' with 'ERROR'
sed -i 's/http:/https:/g' urls.txt    # Replace http with https (in-place)
```

---

### **2. awk – Text Processing & Field Extraction**

- **Purpose:** Extract specific fields or perform calculations.

- **Syntax:**

```bash
awk '{ print $N }' filename
```

*(`$N` represents field number)*

**Examples:**

```bash
awk '{print $1}' names.txt           # Prints first column/field
awk '{print $2, $4}' data.txt        # Prints 2nd and 4th fields
awk '/error/{print}' logfile.txt     # Prints lines containing 'error'
```

---

### **3. sort – Sorting Data**

- **Purpose:** Sort lines alphabetically or numerically.

- **Syntax:**

```bash
sort [options] filename
```

- Common options:
  - `-n`: Numeric sort.
  - `-r`: Reverse sort.
  - `-k`: Sort based on specific column/field.

**Examples:**

```bash
sort names.txt                        # Sort alphabetically
sort -n numbers.txt                   # Numeric sort (ascending)
sort -nr scores.txt                   # Numeric reverse sort (descending)
sort -k 2 data.txt                    # Sort by second column
```

---

### **4. uniq – Handling Duplicates**

- **Purpose:** Report or remove duplicate lines from sorted data.

- **Syntax:**

```bash
uniq [options] filename
```

- Common options:
  - `-c`: Count duplicates.
  - `-d`: Display duplicates only.
  - `-u`: Display unique lines only.

**Examples:**

```bash
sort names.txt | uniq                 # Removes duplicates
sort names.txt | uniq -c              # Counts occurrences of each line
sort names.txt | uniq -d              # Lists only duplicates
```

---

### **5. wc – Word, Line, and Character Count**

- **Purpose:** Count words, lines, and characters.

- **Syntax:**

```bash
wc [options] filename
```

- Common options:
  - `-l`: Line count.
  - `-w`: Word count.
  - `-c`: Character count.

**Examples:**

```bash
wc -l logfile.txt                    # Line count
wc -w article.txt                    # Word count
wc -c file.txt                       # Character count
```

---

## 🎯 **Practical Exercise Suggestion**

Practice independently to solidify today's concepts:

1. Create a file `names.txt` containing several duplicate entries.
2. Sort the file alphabetically and remove duplicates, saving results to `unique_names.txt`.
3. Count and print how many unique names exist.
4. Use `sed` to replace a common typo (like "teh" to "the") in a sample text file.
5. Extract the first two columns from a structured data file using `awk`.

---

## 📝 **Quiz Section (End of Day)**

**1.** How would you replace all instances of "linux" with "Linux" in `notes.txt` using `sed`?

- Fill in the blank:

```bash
sed '_________' notes.txt
```

**2.** Which command sorts numerical data from highest to lowest?

- a) `sort -n file.txt`
- b) `sort -nr file.txt`
- c) `sort -r file.txt`

**3.** To print only the second and third fields from `data.txt` using `awk`, you'd use:

- a) `awk '{print $2, $3}' data.txt`
- b) `awk '{print 2,3}' data.txt`
- c) `awk '{print fields[2,3]}' data.txt`

**4.** How do you count duplicate lines in a sorted file?

- a) `uniq -d file.txt`
- b) `uniq -c file.txt`
- c) `uniq -u file.txt`

**5.** Which command gives you the number of lines in a file?

- a) `wc -w filename`
- b) `wc -l filename`
- c) `wc -c filename`

---

## ❓ **FAQ Section**

**Q1:** Why does `uniq` only remove consecutive duplicates?

- **A:** `uniq` processes line by line sequentially. You must use `sort` first to group duplicates together.

**Q2:** Can `sed` edit multiple files at once?

- **A:** Yes. Example: `sed -i 's/old/new/g' *.txt`.

**Q3:** What's the difference between `awk` and `grep`?

- **A:** `grep` finds patterns in lines, whereas `awk` extracts/manipulates specific fields within those lines.

**Q4:** Can `wc` count multiple files at once?

- **A:** Yes, example: `wc -l file1.txt file2.txt`.

---

## 🚧 **Common Issues Section**

### **Issue 1:** `"sed: -e expression #1, char 1: unknown command"`

- **Reason:** Missing or incorrect quotes around the substitution.
- **Solution:** Ensure correct quotes and syntax:

  ```bash
  sed 's/pattern/replacement/g' file.txt
  ```

### **Issue 2:** `"uniq doesn't remove all duplicates"`

- **Reason:** Input isn't sorted; `uniq` requires sorted input.
- **Solution:** Sort input first:

  ```bash
  sort file.txt | uniq
  ```

---

## 🎯 **Fantastic effort today!**

You've learned powerful text manipulation commands, greatly increasing your Linux command-line productivity.

Tomorrow, we'll focus on managing processes and system monitoring, empowering you to effectively oversee and maintain Linux systems.

Keep practicing!
