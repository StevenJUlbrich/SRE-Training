# ✅ **Day 10 Quiz – Answer Key with Detailed Explanations**

## Here are the answers and detailed explanations for Day 10’s quiz questions

---

### **Question 1:**  

**How do you correctly declare a variable named `username` with the value `admin`?**

✅ **Correct Answer:**  
**b)** `username="admin"`

**Explanation:**  

- **Option a)** `username==admin`: Incorrect syntax, double equal signs are invalid here.
- **Option c)** `$username="admin"`: Incorrect; `$` is for referencing variables, not assigning.

---

### **Question 2:**  

**Which command correctly makes `script.sh` executable?**

✅ **Correct Answer (fill-in-the-blank):**  

```bash
chmod +x script.sh
```

**Explanation:**  

- `chmod +x` adds execute permission, making scripts executable.

---

### **Question 3:**  

**How would you start a loop that iterates over all `.log` files in a directory?**

✅ **Correct Answer:**  
**a)** `for log in *.log; do`

**Explanation:**  

- **Option b)** `loop *.log`: Invalid syntax.
- **Option c)** `for *.log do`: Missing variable name and incorrect syntax.

The correct loop syntax in bash is `for variable in pattern; do`.

---

### **Question 4:**  

**What syntax correctly checks if `myfile.txt` exists?**

✅ **Correct Answer:**  
**a)** `if [ -f myfile.txt ]; then`

**Explanation:**  

- **Option b)** `check myfile.txt`: Not valid syntax.
- **Option c)** `if myfile.txt exist then`: Incorrect and invalid bash syntax.

The correct syntax to check file existence is `[ -f filename ]`.

---

### **Question 5:**  

**How do you permanently add a new directory to your `PATH`?**

✅ **Correct Answer:**  
**a)** `export PATH=$PATH:/new/dir`

**Explanation:**  

- **Option b)** `echo PATH=/new/dir`: Incorrectly sets `PATH`, not permanently.
- **Option c)** `set path=/new/dir`: Incorrect syntax and won't permanently change `PATH`.

For permanent effect, place `export PATH=$PATH:/new/dir` in your `~/.bashrc` or `~/.bash_profile`.

---

🎯 **Outstanding!**  
You've successfully completed the 10-day Linux intensive course and gained substantial Linux knowledge. Continue to practice, automate tasks, and explore advanced scripting to further enhance your skills.

Keep up the excellent work!
