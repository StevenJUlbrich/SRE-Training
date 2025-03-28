# **Day 5 Quiz – Answer Key with Detailed Explanations**

## Here are the detailed answers and explanations for Day 5’s quiz questions

---

### **Question 1:**

**How would you replace all instances of "linux" with "Linux" in `notes.txt` using `sed`?**

✅ **Correct Answer (fill-in-the-blank):**

```bash
sed 's/linux/Linux/g' notes.txt
```

**Explanation:**  

- `sed 's/pattern/replacement/g'`: Performs substitution globally (`g`) throughout the file.  
- Without `g`, only the first match per line is replaced.

---

### **Question 2:**

**Which command sorts numerical data from highest to lowest?**

✅ **Correct Answer:**  
**b)** `sort -nr file.txt`

**Explanation:**  

- **Option a)** `sort -n`: Sorts numerically from lowest to highest.  
- **Option c)** `sort -r`: Reverses sorting, but not numerically unless combined with `-n`.  

The correct combination is `-n` (numerical) and `-r` (reverse) for descending numeric sorting.

---

### **Question 3:**

**To print only the second and third fields from `data.txt` using `awk`, you'd use:**

✅ **Correct Answer:**  
**a)** `awk '{print $2, $3}' data.txt`

**Explanation:**  

- **Option b)** `awk '{print 2,3}'`: Incorrect syntax; this would literally print numbers "2 3".
- **Option c)** `awk '{print fields[2,3]}'`: Incorrect syntax; `awk` uses `$` notation for fields.

---

### **Question 4:**

**How do you count duplicate lines in a sorted file?**

✅ **Correct Answer:**  
**b)** `uniq -c file.txt`

**Explanation:**  

- **Option a)** `uniq -d`: Displays only duplicate lines without counts.
- **Option c)** `uniq -u`: Displays only unique lines.

The correct option `-c` provides counts of occurrences.

---

### **Question 5:**

**Which command gives you the number of lines in a file?**

✅ **Correct Answer:**  
**b)** `wc -l filename`

**Explanation:**  

- **Option a)** `wc -w`: Counts words.
- **Option c)** `wc -c`: Counts characters.

`wc -l` specifically counts lines.

---

🎯 **Great work today!**  
Your command-line proficiency has significantly advanced. Tomorrow, you'll learn process management and system monitoring tools (`ps`, `top`, `kill`, and more) to oversee and maintain Linux systems effectively.

Keep up the excellent practice!
