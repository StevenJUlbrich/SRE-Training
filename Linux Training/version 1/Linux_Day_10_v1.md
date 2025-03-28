# 🚀 **Day 10: Shell Scripting Basics & Advanced Concepts**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 9:**

Yesterday, you learned how to efficiently manage archives and compression (`tar`, `gzip`, `zip`), and explored software package management using `apt` and `yum/dnf`.

### 📅 **Today's Topics and Importance:**

Today marks the final day of your intensive Linux course, focusing on **shell scripting**. Shell scripting allows automation, saving time and improving efficiency, making it an essential skill for any Linux user or administrator.

### 🎯 **Learning Objectives:**

By the end of Day 10, you will be able to:

- Understand and use variables and environment variables.
- Write basic shell scripts using loops (`for`), conditionals (`if`), and command substitution.
- Customize your shell environment with `.bashrc`/`.zshrc`.

---

## 📚 **Core Concepts Explained**

- **Shell Scripting**: Automating repetitive tasks with scripts containing command sequences.
- **Variables**: Storage for data values used by scripts.
- **Loops and Conditionals**: Control script flow and perform actions based on conditions or repetition.
- **Command substitution (`$(...)`)**: Embedding command output within other commands.

---

## 💻 **Commands & Concepts to Learn (Detailed)**

### **1. Variables & Environment Variables**

- Assigning variables:

```bash
name="John"
echo "Hello, $name"
```

- Using environment variables:

```bash
export PATH="$PATH:/home/user/scripts"
```

---

### **2. Basic Shell Scripting**

- Script file example (`script.sh`):

```bash
#!/bin/bash
echo "Starting script..."
echo "Today is $(date)"
```

- Make script executable:

```bash
chmod +x script.sh
./script.sh
```

---

### **3. Loops (`for`)**

- Loop through files:

```bash
for file in *.txt; do
  echo "Processing $file"
done
```

- Numerical loop:

```bash
for i in {1..5}; do
  echo "Iteration: $i"
done
```

---

### **4. Conditionals (`if`)**

- Check file existence:

```bash
if [ -f "file.txt" ]; then
  echo "File exists."
else
  echo "File does not exist."
fi
```

- Numerical comparisons:

```bash
num=10
if [ $num -gt 5 ]; then
  echo "$num is greater than 5."
fi
```

---

### **5. Command Substitution**

- Capture command output:

```bash
current_date=$(date)
echo "Today is $current_date"
```

---

### **6. Customizing Shell Environment (`.bashrc` or `.zshrc`)**

- Edit `.bashrc`:

```bash
nano ~/.bashrc
```

- Example `.bashrc` modification:

```bash
alias ll='ls -la'
export EDITOR=nano
```

---

## 🎯 **Practical Exercise Suggestion**

Practice these tasks independently:

1. Write a script `backup.sh` that archives a specified directory.
2. Use a `for` loop to create multiple directories (`dir1`, `dir2`, `dir3`).
3. Write an `if` statement to check if a directory exists before creating it.
4. Set a custom alias in your `.bashrc` or `.zshrc` and test it.

---

## 📝 **Quiz Section (End of Day)**

**1.** How do you correctly declare a variable named `username` with the value `admin`?

- a) `username==admin`
- b) `username="admin"`
- c) `$username="admin"`

**2.** Which command correctly makes `script.sh` executable?

- Fill in the blank:

```bash
chmod ____ script.sh
```

**3.** How would you start a loop that iterates over all `.log` files in a directory?

- a) `for log in *.log; do`
- b) `loop *.log`
- c) `for *.log do`

**4.** What syntax correctly checks if `myfile.txt` exists?

- a) `if [ -f myfile.txt ]; then`
- b) `check myfile.txt`
- c) `if myfile.txt exist then`

**5.** How do you permanently add a new directory to your `PATH`?

- a) `export PATH=$PATH:/new/dir`
- b) `echo PATH=/new/dir`
- c) `set path=/new/dir`

---

## ❓ **FAQ Section**

**Q1:** What's the difference between `.bashrc` and `.bash_profile`?

- **A:** `.bashrc` executes on each new interactive shell session; `.bash_profile` typically executes once at login.

**Q2:** How do I run a shell script?

- **A:** First make it executable (`chmod +x script.sh`), then execute with `./script.sh`.

**Q3:** What does `#!/bin/bash` mean?

- **A:** It specifies the interpreter (bash) for executing your script.

---

## 🚧 **Common Issues Section**

### **Issue 1:** `"Permission denied"` when running script

- **Reason:** Script not executable.
- **Solution:** Use `chmod +x script.sh`.

### **Issue 2:** Variable not expanding correctly (prints literal `$name`)

- **Reason:** Using single quotes (`'`) instead of double (`"`).
- **Solution:** Always use double quotes for variable expansion:

```bash
echo "Hello, $name"
```

---

## 🎯 **Congratulations! You've completed the 10-Day Intensive Linux Course!**

You now possess essential command-line and scripting skills, significantly enhancing your proficiency in Linux environments.

### 🏅 **Next Steps & Recommendations:**

- Practice scripting regularly.
- Automate routine tasks.
- Explore advanced scripting and system administration topics.

Keep up the fantastic work and continue your Linux journey with confidence!
