# 🚀 **Day 7: Networking Basics – Essential Networking Tools and Commands**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 6:**

Yesterday, you learned to manage and monitor Linux processes (`ps`, `top`, `htop`), control process execution (`kill`, `bg`, `fg`, `jobs`), and gathered system insights (`uname`, `df`, `du`, `free`).

### 📅 **Today's Topics and Importance:**

Today you'll dive into essential Linux networking commands and concepts. Effective networking skills are critical for troubleshooting, connecting remotely, transferring files, and understanding system communication.

### 🎯 **Learning Objectives:**

By the end of Day 7, you will be able to:

- Diagnose network connectivity using `ping`.
- View and manage network interfaces (`ifconfig`, `ip addr`).
- Check active network connections (`netstat`, `ss`).
- Remotely connect and securely transfer files using `ssh` and `scp`.

---

## 📚 **Core Concepts Explained**

- **Network Connectivity (`ping`):** Quickly checks the reachability and response time of a host.

- **Network Interfaces (`ifconfig`, `ip addr`):** Tools to display and configure network interfaces and IP addresses.

- **Active Connections (`netstat`, `ss`):** Monitor network connections and listening ports.

- **Remote Access and File Transfer (`ssh`, `scp`):** Securely connect to remote systems (`ssh`) and transfer files securely (`scp`).

---

## 💻 **Commands to Learn (Detailed)**

### **1. ping – Network Reachability**

- **Purpose:** Check connectivity and response time.

- **Syntax:**

```bash
ping [hostname/IP]
```

- **Examples:**

```bash
ping google.com             # Ping Google's server
ping -c 4 192.168.1.10      # Ping local device, sending 4 packets
```

---

### **2. Network Interfaces (`ifconfig`, `ip addr`)**

- **`ifconfig` (traditional):**

  ```bash
  ifconfig                   # Display all interfaces
  ifconfig eth0              # Display specific interface details
  ```

- **`ip addr` (modern):**

  ```bash
  ip addr                    # Show all interfaces and IP addresses
  ip addr show eth0          # Display eth0 details specifically
  ```

---

### **3. Checking Active Connections (`netstat`, `ss`)**

- **`netstat` (traditional):**

  ```bash
  netstat -tulpn             # Display listening TCP/UDP ports
  netstat -an                # Display all active connections
  ```

- **`ss` (modern alternative):**

  ```bash
  ss -tulpn                  # Display TCP/UDP listening ports
  ss -s                      # Display network connection statistics
  ```

---

### **4. Remote Access and File Transfer (`ssh`, `scp`)**

- **`ssh` – Secure Shell for remote connections:**

  ```bash
  ssh user@hostname          # Connect as 'user' to 'hostname'
  ssh user@192.168.1.5       # Connect using IP address
  ```

- **`scp` – Secure Copy for file transfers:**

  ```bash
  scp file.txt user@remotehost:/home/user   # Copy file to remote host
  scp user@remotehost:/home/user/file.txt . # Copy file from remote host to local
  ```

---

## 🎯 **Practical Exercise Suggestion**

Perform the following tasks to reinforce your networking skills:

1. Ping a well-known server (e.g., `ping google.com`) and observe the results.
2. Use `ip addr` or `ifconfig` to identify your local IP address.
3. Check active listening ports using `netstat -tulpn` or `ss -tulpn`.
4. Establish a remote SSH connection to another accessible system (if available).
5. Practice securely transferring a file using `scp`.

---

## 📝 **Quiz Section (End of Day)**

**1.** How do you ping `example.com` exactly 5 times?

- Fill in the blank:

```bash
ping ____ 5 example.com
```

**2.** Which command shows IP addresses assigned to your network interfaces?

- a) `ifconfig -a`
- b) `ip route`
- c) `ss -l`

**3.** What command lists active TCP listening ports?

- a) `netstat -an`
- b) `netstat -tulpn`
- c) `ping localhost`

**4.** How do you connect to a remote host `server1` using SSH as user `alice`?

- Fill in the blank:

```bash
ssh ____@____
```

**5.** Which command securely copies a local file `notes.txt` to a remote host’s directory `/home/user`?

- a) `scp notes.txt user@remotehost:/home/user`
- b) `ssh notes.txt user@remotehost`
- c) `cp notes.txt /home/user`

---

## ❓ **FAQ Section**

**Q1:** What's the difference between `ifconfig` and `ip addr`?

- **A:** `ifconfig` is older but common; `ip addr` is newer, more powerful, and now the recommended standard.

**Q2:** How can I check if SSH is running on a remote host?

- **A:** Use `ssh user@remotehost`. If SSH is active, you'll be prompted to authenticate. Alternatively, `netstat -tulpn | grep :22` on the remote host checks SSH service status.

**Q3:** Why prefer `scp` over FTP?

- **A:** `scp` is encrypted and secure, whereas FTP transmits data in plaintext, posing security risks.

---

## 🚧 **Common Issues Section**

### **Issue 1:** `"ssh: connect to host port 22: Connection refused"`

- **Reason:** SSH service may be stopped or firewall blocking connection.
- **Solution:** Start SSH service on remote host or verify firewall settings:

```bash
sudo systemctl start sshd
```

### **Issue 2:** `"ping: unknown host"`

- **Reason:** DNS issue or typo in hostname.
- **Solution:** Check DNS (`nslookup hostname`) or confirm hostname spelling.

---

## 🎯 **Well done today!**

You've gained important foundational networking skills critical for managing and troubleshooting Linux systems.

Tomorrow, we'll cover User & Group Management, allowing you to effectively manage system users, groups, and permissions in a multi-user Linux environment.

Keep practicing!
