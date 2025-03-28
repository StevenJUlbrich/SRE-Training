# ✅ **Day 7 Quiz – Answer Key with Detailed Explanations**

## Here are the answers and detailed explanations for Day 7’s quiz questions

---

### **Question 1:**  

**How do you ping `example.com` exactly 5 times?**

✅ **Correct Answer (fill-in-the-blank):**  

```bash
ping -c 5 example.com
```

**Explanation:**  

- The option `-c` specifies the exact number of ping packets sent.

---

### **Question 2:**  

**Which command shows IP addresses assigned to your network interfaces?**

✅ **Correct Answer:**  
**a)** `ifconfig -a`

**Explanation:**  

- `ifconfig -a` lists detailed information on all network interfaces, including their IP addresses.
- **Option b)** `ip route`: Shows routing tables rather than specific IP addresses of interfaces.
- **Option c)** `ss -l`: Lists listening sockets, not network interfaces.

---

### **Question 3:**  

**What command lists active TCP listening ports?**

✅ **Correct Answer:**  
**b)** `netstat -tulpn`

**Explanation:**  

- **Option a)** `netstat -an`: Shows all connections without explicitly differentiating listening ports clearly.
- **Option c)** `ping localhost`: Checks local connectivity but doesn't list ports.

`netstat -tulpn` clearly lists TCP and UDP listening ports with process information.

---

### **Question 4:**  

**How do you connect to a remote host `server1` using SSH as user `alice`?**

✅ **Correct Answer (fill-in-the-blank):**  

```bash
ssh alice@server1
```

**Explanation:**  

- The syntax `ssh user@hostname` is used to initiate an SSH connection.

---

### **Question 5:**  

**Which command securely copies a local file `notes.txt` to a remote host’s directory `/home/user`?**

✅ **Correct Answer:**  
**a)** `scp notes.txt user@remotehost:/home/user`

**Explanation:**  

- **Option b)** `ssh notes.txt user@remotehost`: Incorrect syntax; `ssh` does not transfer files directly.
- **Option c)** `cp notes.txt /home/user`: Copies locally only; doesn't handle remote transfers.

The correct command for secure remote file copy is `scp`.

---

🎯 **Great job mastering Linux networking basics today!**  
Tomorrow, you'll learn user and group management—critical skills for Linux system administration.

Keep up the excellent practice!
