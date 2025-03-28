# ✅ **Day 9 Quiz – Answer Key with Detailed Explanations**

## Below are the answers and detailed explanations for Day 9’s quiz questions

---

### **Question 1:**  

**Which command creates a compressed (`gzip`) archive named `backup.tar.gz` from `backup/`?**

✅ **Correct Answer (fill-in-the-blank):**

```bash
tar -czvf backup.tar.gz backup/
```

**Explanation:**  

- `-c`: create archive  
- `-z`: gzip compression  
- `-v`: verbose output  
- `-f`: specify filename  

---

### **Question 2:**  

**Which command extracts files from `archive.zip`?**

✅ **Correct Answer:**  
**c)** `unzip archive.zip`

**Explanation:**  

- **Option a)** `gzip archive.zip`: incorrect, used for compressing `.gz` files only.  
- **Option b)** `tar -xvf archive.zip`: incorrect, `tar` cannot directly extract `.zip` files without additional flags or formats.

`unzip` directly handles `.zip` files.

---

### **Question 3:**  

**To compress a file named `logs.txt` using `gzip`, which command is correct?**

✅ **Correct Answer:**  
**b)** `gzip logs.txt`

**Explanation:**  

- **Option a)** `tar logs.txt`: invalid syntax without additional options.  
- **Option c)** `gunzip logs.txt`: decompresses `.gz` files rather than compressing.

`gzip logs.txt` correctly compresses the file.

---

### **Question 4:**  

**How do you install the package `nano` on Ubuntu?**

✅ **Correct Answer:**  
**b)** `sudo apt install nano`

**Explanation:**  

- **Option a)** `sudo apt remove nano`: removes the package.  
- **Option c)** `sudo apt update nano`: invalid syntax (`apt update` doesn't install packages directly).

The correct syntax to install packages on Ubuntu is `sudo apt install`.

---

### **Question 5:**  

**On CentOS, how do you check available software updates?**

✅ **Correct Answer:**  
**b)** `yum check-update`

**Explanation:**  

- **Option a)** `yum remove`: removes packages, doesn't check for updates.  
- **Option c)** `yum upgrade`: performs updates immediately, rather than just listing available updates.

`yum check-update` correctly displays available updates without installing.

---

🎯 **Excellent work today!**  
Tomorrow, you'll wrap up your intensive training with shell scripting basics, unlocking powerful automation capabilities.

Keep up the strong momentum!
