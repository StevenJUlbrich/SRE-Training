# ✅ **Day 4 Quiz – Answer Key with Detailed Explanations**

## Below are the detailed answers and explanations for Day 4’s quiz questions

---

### **Question 1:**

**Which command finds all `.txt` files recursively under the current directory?**

✅ **Correct Answer (fill-in-the-blank):**  

``` bash
find . -type f -name '*.txt'
```

**Explanation:**  

- `-type f` specifies the search for **files** (not directories or links).  
- `-name '*.txt'` searches specifically for files ending with `.txt`.

---

### **Question 2:**

**How do you search the file `logs.txt` for lines containing the word "FAILED" (case-insensitive)?**

✅ **Correct Answer:**  
**b)** `grep -i FAILED logs.txt`

**Explanation:**  

- **Option a)** `grep FAILED logs.txt`: Case-sensitive; wouldn't match "failed" or "Failed".
- **Option c)** `grep -n FAILED logs.txt`: Displays line numbers but still case-sensitive.

---

### **Question 3:**

**Which pipe (`|`) command lists processes related to `python`?**

✅ **Correct Answer:**  
**a)** `ps aux | grep python`

**Explanation:**  

- **Option b)** `ps aux > grep python`: Incorrect, `>` is redirection to a file named 'grep'.
- **Option c)** `ps aux >> grep python`: Incorrect, `>>` appends output to a file named 'grep'.

Only option **a** correctly pipes the process list (`ps aux`) to `grep`.

---

### **Question 4:**

**Which command appends output to an existing file without overwriting?**

✅ **Correct Answer:**  
**b)** `ls >> file.txt`

**Explanation:**  

- **Option a)** `ls > file.txt`: Overwrites existing file content.
- **Option c)** `ls < file.txt`: Redirects file content as input; doesn’t append output.

---

### **Question 5:**

**What's the purpose of `<` in `grep error < logfile.txt`?**

✅ **Correct Answer:**  
**b)** Redirects `logfile.txt` content as input to `grep`

**Explanation:**  

- **Option a)** "Redirects error messages": Incorrect, errors typically redirect with `2>`.
- **Option c)** "Saves grep output into logfile.txt": Incorrect, would require `>` or `>>`.

The `<` redirects file content **into** the command as input.

---

🎯 **Fantastic Job!** You've sharpened your Linux skills significantly.  
Tomorrow, we'll delve deeper into text and data manipulation using powerful tools such as `sed`, `awk`, `sort`, and `uniq`.

Keep practicing and building your command-line proficiency!
