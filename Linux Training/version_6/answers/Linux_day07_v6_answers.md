# Day 7 Networking Basics module

This should help you or your learners verify and deepen your understanding of networking fundamentals, intermediate concepts, and SRE-level concerns.

---

## 🟢 Beginner Level

### 1) (MCQ) “Which command tests basic connectivity?”

```bash
a) ssh
b) ping
c) scp
d) netstat
```

**Correct Answer:** **(b) ping**  
**Explanation:**  

- `ping` is specifically designed to send ICMP Echo requests to verify reachability and measure response time.  
- `ssh` connects securely to a remote shell, `scp` is for secure file copy, and `netstat` lists network connections.  

---

### 2) (Short Answer) “What command lists IP addresses in the modern approach?”

**Correct Answer:** `ip addr` (often shown as `ip addr show`)  
**Explanation:**  

- `ip addr` is the newer, more powerful command from the `iproute2` suite, replacing the older `ifconfig`.  
- In many modern Linux distros, `ifconfig` may not be installed by default, making `ip addr` the recommended approach.  

---

### 3) (MCQ) “Which option in `ping` sets how many packets are sent?”

```bash
a) -w
b) -c
c) -i
d) -p
```

**Correct Answer:** **(b) -c**  
**Explanation:**  

- `-c <count>` tells `ping` how many ICMP packets to send before stopping.  
- `-w` sets a deadline (in seconds) for how long `ping` should run.  
- `-i` sets the interval between packets.  
- `-p` (on some systems) can set a custom pattern to fill out the packet payload.  

---

### 4) (Short Answer) “Which command shows open/listening ports on your system?”

**Correct Answer:** `netstat -tln` or `ss -tln`  
**Explanation:**  

- `-t` displays TCP, `-l` limits output to listening sockets, and `-n` shows numeric IP/port data (avoiding DNS lookups for speed).  
- Both `netstat` (older) and `ss` (newer) can do this job; `ss` is typically faster and more feature-rich.  

---

## 🟡 Intermediate Level

### 1) (MCQ) “Which command logs you into a remote host via the default SSH port?”

```bash
a) ssh user@host
b) ssh -p 25 user@host
c) scp user@host:/file .
```

**Correct Answer:** **(a) ssh user@host**  
**Explanation:**  

- By default, SSH uses port 22. `ssh user@host` attempts to connect on port 22 unless otherwise specified.  
- `-p 25` would try to connect on port 25, which is typically for SMTP, not SSH.  
- `scp` is a file transfer command, not an interactive login.  

---

### 2) (Short Answer) “Which command do you use to remove a route?”

**Correct Answer:** `ip route del <route>`  
**Explanation:**  

- For example, `ip route del 10.0.2.0/24 dev eth0` removes a route to the 10.0.2.0 network.  
- This is part of the `iproute2` suite, which replaces older commands like `route del`.  

---

### 3) (Scenario) “You tried to connect with `ssh -i ~/.ssh/key user@host` but got ‘Permission denied’. What might be wrong?”

**Possible Causes & Explanations:**

- **Key Not Authorized**: The public key may not be in `~/.ssh/authorized_keys` on the remote server.  
- **Wrong Username**: Using the wrong username can lead to a mismatch with authorized keys.  
- **File Permissions**: The private key file `~/.ssh/key` may have incorrect permissions. It usually must be `chmod 600`.  
- **Server-Side Config**: The server might be configured to refuse key-based authentication or only allow certain user accounts.  

---

### 4) (MCQ) “Which command can show the process ID bound to a specific port?”

```bash
a) netstat -p
b) ss -p
c) Both a & b
d) Neither
```

**Correct Answer:** **(c) Both a & b**  
**Explanation:**  

- Both `netstat -p` and `ss -p` can display the PID/program name that owns a particular socket, but **usually require sudo/root** to see full details.  

---

## 🔴 SRE-Level

### 1) (Scenario) “You suspect port 8080 is used by a rogue process. How do you confirm?”

**Recommended Approach & Explanation:**  

- Use a command like `sudo ss -tlnp | grep :8080` **or** `sudo netstat -tlnp | grep :8080`.  
- **Explanation**:  
  - `-tlnp` means TCP, listening sockets, numeric addresses, plus process info.  
  - This will show which PID and command is binding to port 8080.  

---

### 2) (MCQ) “For zero-downtime route changes, which step is essential?”

```bash
a) Immediately remove the existing route
b) Add a backup route and test connectivity
c) Wait for traffic to fail before making changes
```

**Correct Answer:** **(b) Add a backup route and test connectivity**  
**Explanation:**  

- Removing the existing route too soon (option a) could cause dropped connections or lock you out.  
- Waiting for traffic to fail (option c) is risky and not aligned with proactive SRE best practices.  

---

### 3) (Scenario) “You need to copy logs from 10 servers to a central location every night. Suggest an efficient approach.”

**Possible Approaches & Explanation:**  

- **Automated Script with scp/rsync**:  
  1. Create a script that loops over a list of servers.  
  2. Use `scp` or `rsync` to pull logs from each server (e.g., in parallel or via background jobs).  
  3. Schedule the script via cron.  
- **Configuration Management / Orchestration**:  
  - Tools like Ansible can gather files from multiple hosts efficiently.  
- **Explanation**:  
  - `rsync` is more efficient for partial updates, but `scp` can work for simple daily pulls.  
  - Running them in parallel speeds up transfers, important if logs are large or numerous.  

---

### 4) (Short Answer) “Write a command using `ss` to filter for established connections on port 443.”

**Correct Answer Example:**  

```bash
ss -tn state established '( sport = :443 or dport = :443 )'
```

**Explanation:**  

- `-t` filters for TCP connections.  
- `state established` narrows results to active, established sessions.  
- `( sport = :443 or dport = :443 )` checks for connections whose source or destination port is 443 (HTTPS).  
- Alternatively, a quicker approach is `ss -tna | grep :443` to see all 443 usage, but the above uses the built-in ss filtering syntax.  

---

## Wrap-Up

These answers provide **both the correct response and the reasoning behind them**, helping learners not only see what’s right but **why** it’s right. By reviewing the explanations, students can **solidify their knowledge** of Linux networking commands, usage contexts, and SRE best practices.
