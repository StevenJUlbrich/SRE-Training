# 🚀 **Day 8: User & Group Management – Managing Access and Security**

## 📌 **Introduction**

### 🔄 **Recap of Day 7:**

Yesterday, you gained essential networking skills, including connectivity testing (`ping`), interface management (`ifconfig`, `ip addr`), monitoring active connections (`netstat`, `ss`), and secure remote operations (`ssh`, `scp`). These skills enable you to diagnose network issues and securely transfer data between systems.

### 📅 **Today's Topics and Importance:**

Today, we'll explore **User & Group Management** in Linux. Understanding how to properly manage users and groups is fundamental for:

- Controlling who can access your systems
- Implementing the principle of least privilege
- Organizing users with similar access needs
- Managing file and resource permissions
- Maintaining system security and accountability
- Supporting multiple users on shared resources

### 🎯 **Learning Objectives:**

By the end of Day 8, you will be able to:

- Create, delete, and modify users (`useradd`, `userdel`, `usermod`)
- Create and manage groups (`groupadd`, `groupdel`, `groupmod`)
- Manage passwords and authentication (`passwd`)
- View user information in system files and using commands
- Understand the relationship between users, groups, and permissions
- Apply these skills to create secure, manageable Linux environments

---

## 📚 **Core Concepts Explained**

### **Linux User and Group Model**

> **Beginner's Note:** Think of Linux users and groups like an access card system in an office building. Each person has their own ID card, and different doors open depending on which groups (departments) they belong to.

Linux uses a multi-user model where each user has their own identity, represented by a unique **user ID (UID)**. Users can belong to one or more **groups**, each with a unique **group ID (GID)**. This model enables fine-grained access control and resource sharing.

Think of this model as an office building:

- **Users** are like individual employees with unique ID badges
- **Groups** are like departments or project teams
- **Permissions** are like access controls for different rooms and resources
- **Home directories** are like personal offices
- **Root user** is like the building manager with master keys

### **User Types in Linux**

> **Intermediate Insight:** System accounts typically have UIDs below 1000, while regular user accounts have UIDs starting at 1000 or higher (depending on distribution). This separation helps distinguish between human users and system services.

Linux systems typically have several types of users:

1. **Root (UID 0)**: The superuser with unlimited privileges
2. **System Users**: Used for running services and daemons
3. **Regular Users**: Human users with limited privileges
4. **Service Accounts**: Special-purpose accounts for applications

### **The Role of Groups**

> **SRE Perspective:** Properly configured groups are essential for implementing least privilege access control in production environments. Well-designed group structures make it easier to maintain security as team members change roles or leave the organization.

Groups serve several important purposes:

1. **Simplified Permission Management**: Assign permissions to groups rather than individual users
2. **Logical Organization**: Group users based on roles, departments, or access needs
3. **Collaboration**: Allow multiple users to access shared resources
4. **Privilege Separation**: Limit access based on function or responsibility

Each user has a **primary group** (set during account creation) and can belong to multiple **supplementary groups** to gain additional privileges.

---

## 💻 **Commands to Learn Today**

### **1. User Management (`useradd`, `userdel`, `usermod`)**

#### **Beginner Section: Basic User Management**

**`useradd` – Create new users**

```bash
sudo useradd alice            # Adds a new user 'alice'
sudo useradd -m bob           # Adds 'bob' and creates home directory
```

**`userdel` – Remove existing users**

```bash
sudo userdel alice            # Removes user 'alice' but keeps home directory
sudo userdel -r bob           # Removes user 'bob' and deletes home directory
```

**`usermod` – Modify existing users**

```bash
sudo usermod -aG developers alice    # Adds 'alice' to 'developers' group
sudo usermod -l newname oldname      # Renames user 'oldname' to 'newname'
```

> **Beginner's Note:** Always remember to use `-m` with `useradd` if you want to create a home directory for the user, and remember that `-r` with `userdel` will delete all the user's files.

#### **Intermediate Section: Advanced User Management**

**`useradd` – More options**

```bash
# Create a user with specific home directory, shell, and comment
sudo useradd -m -d /home/dbadmin -s /bin/bash -c "Database Administrator" dbadmin

# Create a system user for a service (no login)
sudo useradd -r -s /bin/false -d /opt/appservice -c "App Service" appuser

# Create a user with multiple supplementary groups
sudo useradd -m -G developers,docker,sudo -c "Jane Smith" jsmith
```

**`usermod` – Additional modifications**

```bash
# Change a user's shell
sudo usermod -s /bin/zsh alice

# Change a user's home directory
sudo usermod -d /newhome alice

# Lock a user account (disable password login)
sudo usermod -L alice

# Unlock a user account
sudo usermod -U alice
```

> **Intermediate Insight:** The `-a` flag with `-G` in `usermod` is crucial—it means "append" and prevents accidentally removing existing group memberships. Without `-a`, the `-G` option will replace all existing supplementary groups.

#### **SRE Application: Service Account Management**

> **SRE Perspective:** Properly configured service accounts are critical for security in production environments. They should follow the principle of least privilege and never run with root privileges.

```bash
# Create a service account for a web application
sudo useradd -r -s /sbin/nologin -c "Web Application Service" webapp

# Set up proper directories for the service
sudo mkdir -p /opt/webapp/{logs,data,config}
sudo chown -R webapp:webapp /opt/webapp

# Add the service user to appropriate groups
sudo usermod -aG logging webapp

# Verify the setup
sudo -u webapp ls -la /opt/webapp
```

### **2. Group Management (`groupadd`, `groupdel`, `groupmod`)**

#### **Beginner Section: Basic Group Management**

**`groupadd` – Create groups**

```bash
sudo groupadd developers     # Creates a group 'developers'
```

**`groupdel` – Delete groups**

```bash
sudo groupdel developers     # Deletes the 'developers' group
```

> **Beginner's Note:** You cannot delete a group that is the primary group of an existing user. You'll need to change the user's primary group first.

#### **Intermediate Section: Advanced Group Management**

**`groupadd` – More options**

```bash
# Create a system group (lower GID range)
sudo groupadd -r appgroup

# Create a group with a specific GID
sudo groupadd -g 1500 project42
```

**`groupmod` – Modify existing groups**

```bash
# Rename a group
sudo groupmod -n engineering developers

# Change a group's GID
sudo groupmod -g 1600 engineering
```

> **Intermediate Insight:** System groups (created with `-r`) are used for system services and typically have lower GIDs. Regular groups are used for human users and have higher GIDs.

#### **SRE Application: Role-Based Access Control**

> **SRE Perspective:** Creating appropriate functional groups is essential for implementing role-based access control (RBAC), a crucial security practice in enterprise environments.

```bash
# Create functional groups for a microservices architecture
sudo groupadd app_read       # Read-only access
sudo groupadd app_write      # Read/write access
sudo groupadd app_admin      # Administrative access

# Assign users to appropriate groups
sudo usermod -a -G app_read viewer1
sudo usermod -a -G app_read,app_write editor1
sudo usermod -a -G app_read,app_write,app_admin admin1

# Set directory permissions based on groups
sudo chown root:app_read /data/application
sudo chmod 750 /data/application
sudo chown root:app_admin /data/application/config
sudo chmod 770 /data/application/config
```

### **3. Password Management (`passwd`)**

#### **Beginner Section: Basic Password Management**

**`passwd` – Set or change passwords**

```bash
passwd                        # Change your own password
sudo passwd alice             # Change password for user 'alice'
```

> **Beginner's Note:** Regular users can only change their own passwords, while root (or users with sudo privileges) can change any user's password.

#### **Intermediate Section: Advanced Password Management**

**`passwd` – More options**

```bash
# Lock a user account (disable password login)
sudo passwd -l jsmith

# Unlock a user account
sudo passwd -u jsmith

# Delete a password (make account passwordless)
sudo passwd -d jsmith

# Force password change at next login
sudo passwd -e jsmith

# Set maximum days before password change required
sudo passwd -x 90 jsmith

# Set minimum days between password changes
sudo passwd -n 7 jsmith
```

> **Intermediate Insight:** Password aging policies help enforce security by ensuring users regularly update their passwords. In enterprise environments, these policies are often defined in `/etc/login.defs`.

#### **SRE Application: Security Hardening**

> **SRE Perspective:** Strong password management is fundamental to system security. In production environments, consider implementing more robust authentication methods like SSH keys or 2FA.

```bash
# Set up a complex password policy system-wide
sudo vi /etc/login.defs
# Set values for:
# PASS_MAX_DAYS 90
# PASS_MIN_DAYS 1
# PASS_WARN_AGE 7

# Force all users to update passwords
for user in $(awk -F: '$3 >= 1000 && $3 <= 60000 {print $1}' /etc/passwd); do
  sudo passwd -e $user
done

# Lock a compromised account immediately
sudo passwd -l compromised_user
```

### **4. User Information and Management**

#### **Beginner Section: Viewing User Information**

**`/etc/passwd` – View basic user info**

```bash
cat /etc/passwd               # Displays all users
grep alice /etc/passwd        # Find specific user details
```

**`getent` – Detailed info about users/groups**

```bash
getent passwd alice           # Retrieves info for user 'alice'
getent group developers       # Retrieves info for group 'developers'
```

> **Beginner's Note:** The format of `/etc/passwd` entries is: `username:password:UID:GID:comment:home_directory:shell`. The password field contains an 'x' which means the password is stored in `/etc/shadow`.

#### **Intermediate Section: Understanding User Information Files**

**System Files for User and Group Management**

```bash
# View users with their UIDs and GIDs
cat /etc/passwd

# View groups and their members
cat /etc/group

# Check which groups a user belongs to
groups username
id username
```

> **Intermediate Insight:** The `/etc/passwd` file is world-readable, but `/etc/shadow` (which contains the encrypted passwords) is readable only by root. This is an important security feature to prevent unauthorized access to password hashes.

#### **SRE Application: User Auditing**

> **SRE Perspective:** Regular user auditing is essential for maintaining security in production environments. This helps identify unauthorized accounts, dormant accounts, or accounts with excessive privileges.

```bash
# Find users with UID 0 (root privileges)
awk -F: '$3 == 0 {print $1}' /etc/passwd

# List all users with a valid login shell
grep -v '/sbin/nologin\|/bin/false' /etc/passwd

# Find accounts with empty passwords
sudo awk -F: '($2 == "" ) { print $1 }' /etc/shadow

# Check for users who haven't logged in recently
lastlog | grep 'Never logged in'

# Audit sudo privileges
sudo grep -v '#' /etc/sudoers | grep -v '^$'
sudo ls -la /etc/sudoers.d/
```

### **5. Additional User Management Commands**

#### **Intermediate Section: Additional User Commands**

**`su` – Switch User**

```bash
su -                          # Switch to root (login shell)
su - username                 # Switch to specified user
su - username -c "command"    # Run a command as another user
```

**`sudo` – Execute Command as Another User**

```bash
sudo command                 # Execute command as root
sudo -u username command     # Execute command as specified user
sudo -l                      # List allowed sudo commands
```

> **Intermediate Insight:** Using `su -` with the hyphen creates a login shell, which loads the target user's environment. Without the hyphen, you'll keep your current environment variables.

#### **SRE Application: Proper Access Control Implementation**

> **SRE Perspective:** Implementing proper access control through sudo is more secure than giving multiple users the root password. Limit sudo privileges to only what's necessary for each role.

```bash
# Create a sudoers entry for specific commands
sudo visudo -f /etc/sudoers.d/monitoring
# Add: monitoring ALL=(ALL) NOPASSWD: /usr/bin/systemctl status *

# Create a sudoers entry for a group
sudo visudo -f /etc/sudoers.d/developers
# Add: %developers ALL=(ALL) /usr/bin/docker

# Check effective permissions
sudo -l -U username

# Safely test a service as its service user
sudo -u webapp /opt/webapp/bin/test_script.sh
```

---

## 🎯 **Practical Exercises**

### **Beginner Exercise: Basic User and Group Management**

1. Create a new user named `practiceuser` with a home directory:

   ```bash
   sudo useradd -m practiceuser
   ```

2. Set a password for the user:

   ```bash
   sudo passwd practiceuser
   ```

3. Create a new group called `practice`:

   ```bash
   sudo groupadd practice
   ```

4. Add the user to the group:

   ```bash
   sudo usermod -aG practice practiceuser
   ```

5. Verify the user was added to the group:

   ```bash
   groups practiceuser
   ```

6. Switch to the new user and check their groups:

   ```bash
   su - practiceuser
   groups
   exit
   ```

7. Delete the user and their home directory:

   ```bash
   sudo userdel -r practiceuser
   ```

8. Delete the group:

   ```bash
   sudo groupdel practice
   ```

### **Intermediate Exercise: Managing Multiple Users and Groups**

1. Create a project directory structure:

   ```bash
   sudo mkdir -p /opt/project/{code,docs,data}
   ```

2. Create groups for different access levels:

   ```bash
   sudo groupadd project_read
   sudo groupadd project_write
   sudo groupadd project_admin
   ```

3. Create users with different roles:

   ```bash
   sudo useradd -m -c "Project Viewer" viewer
   sudo useradd -m -c "Project Editor" editor
   sudo useradd -m -c "Project Admin" padmin
   ```

4. Set passwords for all users:

   ```bash
   sudo passwd viewer
   sudo passwd editor
   sudo passwd padmin
   ```

5. Assign users to appropriate groups:

   ```bash
   sudo usermod -aG project_read viewer
   sudo usermod -aG project_read,project_write editor
   sudo usermod -aG project_read,project_write,project_admin padmin
   ```

6. Set appropriate permissions on the project directories:

   ```bash
   sudo chown root:project_read /opt/project
   sudo chmod 755 /opt/project
   
   sudo chown root:project_read /opt/project/docs
   sudo chmod 755 /opt/project/docs
   
   sudo chown root:project_write /opt/project/code
   sudo chmod 770 /opt/project/code
   
   sudo chown root:project_admin /opt/project/data
   sudo chmod 770 /opt/project/data
   ```

7. Test access for each user:

   ```bash
   # As viewer
   sudo -u viewer touch /opt/project/docs/test.txt  # Should fail
   sudo -u viewer ls -la /opt/project/docs  # Should succeed
   
   # As editor
   sudo -u editor touch /opt/project/code/test.txt  # Should succeed
   sudo -u editor touch /opt/project/data/test.txt  # Should fail
   
   # As padmin
   sudo -u padmin touch /opt/project/data/test.txt  # Should succeed
   ```

8. Clean up (optional):

   ```bash
   sudo userdel -r viewer
   sudo userdel -r editor
   sudo userdel -r padmin
   sudo groupdel project_read
   sudo groupdel project_write
   sudo groupdel project_admin
   sudo rm -rf /opt/project
   ```

### **SRE Exercise: Setting Up a Service Account with Proper Security**

1. Create a service account for a web application:

   ```bash
   sudo useradd -r -s /sbin/nologin -c "Web Application Service" webapp
   ```

2. Create groups for different access levels:

   ```bash
   sudo groupadd -r webapp
   sudo groupadd -r webapp_logs
   ```

3. Add the service user to the appropriate groups:

   ```bash
   sudo usermod -aG webapp,webapp_logs webapp
   ```

4. Create the application directory structure:

   ```bash
   sudo mkdir -p /opt/webapp/{bin,config,data,logs}
   ```

5. Set secure permissions:

   ```bash
   # Base directory
   sudo chown root:root /opt/webapp
   sudo chmod 755 /opt/webapp
   
   # Binaries - owned by root, executable
   sudo chown root:root /opt/webapp/bin
   sudo chmod 755 /opt/webapp/bin
   
   # Configuration - restrictive
   sudo chown webapp:webapp /opt/webapp/config
   sudo chmod 750 /opt/webapp/config
   
   # Data - owned by service, private
   sudo chown webapp:webapp /opt/webapp/data
   sudo chmod 770 /opt/webapp/data
   
   # Logs - group writable for log monitoring
   sudo chown webapp:webapp_logs /opt/webapp/logs
   sudo chmod 770 /opt/webapp/logs
   sudo chmod g+s /opt/webapp/logs  # Set SGID bit
   ```

6. Create a test application script:

   ```bash
   cat << 'EOF' | sudo tee /opt/webapp/bin/test.sh
   #!/bin/bash
   echo "Web application test"
   echo "Running as $(whoami)"
   echo "Writing to config file"
   echo "test=value" > /opt/webapp/config/test.conf
   echo "Writing to data file"
   echo "data" > /opt/webapp/data/test.data
   echo "Writing to log file"
   echo "$(date) - Test log entry" >> /opt/webapp/logs/app.log
   EOF
   
   sudo chmod 755 /opt/webapp/bin/test.sh
   ```

7. Test the application as the service user:

   ```bash
   sudo -u webapp /opt/webapp/bin/test.sh
   ```

8. Check the results:

   ```bash
   ls -la /opt/webapp/config
   ls -la /opt/webapp/data
   ls -la /opt/webapp/logs
   ```

9. Create a systemd service file (optional):

   ```bash
   sudo bash -c 'cat > /etc/systemd/system/webapp.service << EOF
   [Unit]
   Description=Web Application Service
   After=network.target
   
   [Service]
   Type=simple
   User=webapp
   Group=webapp
   ExecStart=/opt/webapp/bin/test.sh
   Restart=on-failure
   WorkingDirectory=/opt/webapp
   
   [Install]
   WantedBy=multi-user.target
   EOF'
   ```

10. Test the service (optional):

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start webapp
    sudo systemctl status webapp
    ```

---

## 📝 **Quiz: User and Group Management**

### **Beginner Level Questions**

**1.** How would you add a new user called `john` with a home directory?

- a) `useradd john`
- b) `useradd -h john`
- c) `useradd -m john`
- d) `usermod -m john`

**2.** Which command completely removes a user named `john` and their home directory?

- a) `userdel john`
- b) `userdel -r john`
- c) `usermod -r john`
- d) `rmuser -r john`

**3.** Which command changes the password for user `john`?

- a) `passwd john`
- b) `chpasswd john`
- c) `usermod -p john`
- d) `password john`

### **Intermediate Level Questions**

**4.** You need to add user `john` to the group `staff` without removing him from other groups. Which command would you use?

- a) `usermod -aG staff john`
- b) `usermod -g staff john`
- c) `groupadd staff john`
- d) `groupmod -a john staff`

**5.** Which file contains the encrypted passwords for user accounts?

- a) `/etc/passwd`
- b) `/etc/shadow`
- c) `/etc/group`
- d) `/etc/users`

**6.** How would you force user `john` to change his password at next login?

- a) `passwd -e john`
- b) `passwd --expire john`
- c) `usermod -e john`
- d) `chage -d 0 john`

### **SRE Application Questions**

**7.** To create a service account (system user) for running a web service, which command is most appropriate?

- a) `useradd -m webservice`
- b) `useradd -r -s /bin/false webservice`
- c) `usermod -s /bin/nologin webservice`
- d) `groupadd -r webservice`

**8.** You need to audit all users with sudo privileges. Which command would be most effective?

- a) `cat /etc/passwd | grep sudo`
- b) `getent group sudo`
- c) `grep -v '^#' /etc/sudoers && ls -la /etc/sudoers.d/`
- d) `getent passwd | grep root`

**9.** Which approach follows best security practices for a service account that runs a database?

- a) Run the database as root for maximum capabilities
- b) Create a regular user (`useradd dbuser`) with full sudo access
- c) Create a system user (`useradd -r dbuser`) with specific directory permissions and limited capabilities
- d) Use the nobody user to minimize security risks

---

## ❓ **FAQ for SREs: User and Group Management**

**Q1: What's the difference between removing a user with `userdel` vs. `userdel -r`?**

**A:** The difference is what happens to the user's home directory and mail spool:

- `userdel username` removes only the user account from the system (entries in `/etc/passwd`, `/etc/shadow`, etc.) but leaves their home directory and mail spool intact.
  
- `userdel -r username` does a more complete removal, deleting:
  - The user account
  - The user's home directory and all its contents
  - The user's mail spool
  
As an SRE, which option you choose depends on your data retention policies. Using `userdel` without `-r` is safer when you need to preserve user data after their departure. The `-r` option is better when you want to completely clean up all traces of the account.

**Q2: What's the difference between primary and supplementary groups?**

**A:** The key differences are:

- **Primary Group**:
  - Every user has exactly one primary group
  - Set with `-g` in `useradd` or `usermod`
  - Used as the default group for new files created by the user
  - Stored in `/etc/passwd` as the GID field

- **Supplementary Groups**:
  - A user can belong to multiple supplementary groups (or none)
  - Set with `-G` in `useradd` or `-aG` in `usermod`
  - Provide additional access permissions beyond the primary group
  - Stored in `/etc/group`

For example, a user's primary group might be their team (`development`), while they belong to supplementary groups based on the resources they need to access (`docker`, `deployment`, `monitoring`).

The `-a` option with `-G` in `usermod` is critical—it means "append" and prevents removing existing group memberships.

**Q3: How do I create a non-interactive system account for running a service?**

**A:** For service accounts that should never be used for interactive logins:

```bash
# Create a system user (-r) with no login shell and no home directory
sudo useradd -r -s /sbin/nologin -M -c "Service Description" service_name

# Alternatively, with a specific home directory
sudo useradd -r -s /sbin/nologin -d /opt/service -c "Service Description" service_name
sudo mkdir -p /opt/service
sudo chown service_name:service_name /opt/service
```

Key options:

- `-r`: Create a system account with UID in the system range (typically below 1000)
- `-s /sbin/nologin`: Prevent interactive login
- `-M`: No home directory (or specify one with `-d`)
- `-c`: Comment field (for documentation)

Once created, use `sudo -u service_name command` to run commands as this user.

**Q4: How do I manage sudo privileges for different user types?**

**A:** The `/etc/sudoers` file (edited with `visudo`) controls sudo privileges. Here's how to set up different levels of access:

```bash
# Give full sudo access (all commands as any user, no password)
admin ALL=(ALL) NOPASSWD: ALL

# Allow specific commands with password
operator ALL=(ALL) /usr/bin/systemctl restart application, /usr/bin/systemctl status application

# Allow specific commands without password
monitor ALL=(ALL) NOPASSWD: /usr/bin/tail -f /var/log/application.log

# Allow a group to run specific commands
%developers ALL=(ALL) /usr/bin/docker
```

Best practices:

1. Create separate groups for different privilege levels
2. Limit commands to only what's needed for each role
3. Use `NOPASSWD:` sparingly
4. Consider creating separate files in `/etc/sudoers.d/` for better organization

**Q5: Can I change a username directly?**

**A:** Yes, you can change a username with `usermod -l`, but several other steps are needed for a complete rename:

```bash
# Change the username
sudo usermod -l newname oldname

# Change the home directory
sudo usermod -d /home/newname -m newname

# Change the primary group name (if it matches the username)
sudo groupmod -n newname oldname

# Check for files owned by the old UID elsewhere
sudo find / -user oldname -exec chown newname {} \;
```

This approach preserves the user's UID, so all file ownerships remain intact.

**Q6: How can I lock or disable user accounts temporarily?**

**A:** There are several ways to temporarily disable accounts:

```bash
# Lock a user account (prevents password login)
sudo passwd -l username
# or
sudo usermod -L username

# Disable the login shell
sudo usermod -s /sbin/nologin username

# Set account expiration date
sudo usermod -e $(date -d "today" +%Y-%m-%d) username
```

To re-enable:

```bash
# Unlock the account
sudo passwd -u username
# or
sudo usermod -U username

# Restore the login shell
sudo usermod -s /bin/bash username

# Remove account expiration
sudo usermod -e "" username
```

---

## 🚧 **Common Issues and Troubleshooting**

### **Issue 1: User Cannot Log In Despite Correct Password**

**Possible causes:**

- Account is locked
- Shell is set to `/sbin/nologin` or `/bin/false`
- Account is expired
- Home directory issues
- PAM configuration problems

**Diagnosis and solutions:**

```bash
# Check if account is locked (L flag in second field)
sudo grep username /etc/shadow

# Check shell setting
grep username /etc/passwd | cut -d: -f7

# Check account expiration
sudo chage -l username

# Unlock account if locked
sudo passwd -u username

# Change shell if needed
sudo usermod -s /bin/bash username

# Check home directory permissions
ls -ld /home/username
sudo chmod 750 /home/username
sudo chown username:username /home/username
```

### **Issue 2: User Added to Group but Still Gets "Permission Denied"**

**Possible causes:**

- User hasn't logged out and back in (new group membership requires new login)
- File permissions are too restrictive
- SELinux or AppArmor restrictions

**Diagnosis and solutions:**

```bash
# Check current group membership (effective groups)
groups

# Get a new shell with updated group membership without logging out
newgrp groupname

# Alternatively, start a new login shell
su - $USER

# Check file permissions
ls -la /path/to/file

# Check SELinux context
ls -Z /path/to/file
sudo setenforce 0  # Temporarily disable SELinux to test
```

### **Issue 3: "useradd: user 'john' already exists"**

**Possible causes:**

- Username already taken
- User exists in LDAP/AD but not in local `/etc/passwd`
- Previous incomplete user deletion

**Solutions:**

```bash
# Check if user exists in local files
grep john /etc/passwd

# Check LDAP/AD (if configured)
getent passwd john

# Choose another username or remove the existing one if appropriate
sudo userdel john  # If you want to delete

# For a complete cleanup of a problematic user
sudo userdel -f john
sudo find / -user john -exec ls -la {} \; 2>/dev/null  # Find leftover files
sudo find / -user john -exec chown newowner {} \; 2>/dev/null  # Change ownership
```

### **Issue 4: "usermod: group 'staff' does not exist"**

**Possible causes:**

- The group doesn't exist
- Typo in group name
- Group exists in LDAP/AD but not locally

**Solutions:**

```bash
# Check if group exists
grep staff /etc/group
getent group staff

# Create the group if needed
sudo groupadd staff

# List all available groups to check for typos
getent group | cut -d: -f1 | sort
```

---

## 🔄 **Real-World SRE Scenario: Deploying a New Microservice**

**Situation:** Your team is deploying a new microservice that will process customer data. As the SRE responsible for the deployment, you need to set up the service with proper user management and security controls.

**Requirements:**

- The service needs a dedicated system account
- It should have access to specific data directories
- Different teams need different access levels to the service
- The service must not run as root
- Log files need to be accessible to the monitoring team

**Implementation Steps:**

1. **Create service groups for different access levels:**

```bash
sudo groupadd -r microservice
sudo groupadd -r microservice_logs
sudo groupadd -r microservice_admin
```

2. **Create a system user for the service:**

```bash
sudo useradd -r -s /sbin/nologin -c "Microservice Application" microservice
sudo usermod -aG microservice,microservice_logs microservice
```

3. **Set up the directory structure:**

```bash
sudo mkdir -p /opt/microservice/{bin,config,data,logs}

# Base directory
sudo chown root:root /opt/microservice
sudo chmod 755 /opt/microservice

# Binaries - owned by root, executable
sudo chown root:root /opt/microservice/bin
sudo chmod 755 /opt/microservice/bin

# Configuration - restrictive
sudo chown microservice:microservice_admin /opt/microservice/config
sudo chmod 770 /opt/microservice/config

# Data - owned by service
sudo chown microservice:microservice /opt/microservice/data
sudo chmod 750 /opt/microservice/data

# Data - owned by service
sudo chown microservice:microservice /opt/microservice/data
sudo chmod 750 /opt/microservice/data

# Logs - group writable for monitoring team
sudo chown microservice:microservice_logs /opt/microservice/logs
sudo chmod 770 /opt/microservice/logs
sudo chmod g+s /opt/microservice/logs  # Set SGID bit to preserve group ownership
```

4. **Add team members to appropriate groups:**

```bash
# Add developers to basic microservice group
sudo usermod -aG microservice dev1
sudo usermod -aG microservice dev2

# Add operations team to logs group
sudo usermod -aG microservice_logs ops1
sudo usermod -aG microservice_logs ops2

# Add senior engineers to admin group
sudo usermod -aG microservice_admin senior1
sudo usermod -aG microservice_admin senior2
```

5. **Configure sudo permissions for service management:**

```bash
sudo bash -c 'cat > /etc/sudoers.d/microservice << EOF
# Allow microservice admins to manage the service
%microservice_admin ALL=(ALL) /bin/systemctl start microservice, /bin/systemctl stop microservice, /bin/systemctl restart microservice

# Allow developers to check service status
%microservice ALL=(ALL) /bin/systemctl status microservice

# Allow ops team to view logs
%microservice_logs ALL=(ALL) NOPASSWD: /usr/bin/tail -f /opt/microservice/logs/*, /usr/bin/grep * /opt/microservice/logs/*
EOF'

sudo chmod 440 /etc/sudoers.d/microservice
```

6. **Create a systemd service file:**

```bash
sudo bash -c 'cat > /etc/systemd/system/microservice.service << EOF
[Unit]
Description=Customer Data Microservice
After=network.target

[Service]
Type=simple
User=microservice
Group=microservice
ExecStart=/opt/microservice/bin/microservice
Restart=on-failure
WorkingDirectory=/opt/microservice
# Set strict security limits
ProtectSystem=full
PrivateTmp=true
NoNewPrivileges=true
ProtectHome=true
ReadWritePaths=/opt/microservice/data /opt/microservice/logs
ReadOnlyPaths=/opt/microservice/config

[Install]
WantedBy=multi-user.target
EOF'

sudo systemctl daemon-reload
```

7. **Implement a log rotation policy:**

```bash
sudo bash -c 'cat > /etc/logrotate.d/microservice << EOF
/opt/microservice/logs/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 microservice microservice_logs
    sharedscripts
    postrotate
        systemctl reload microservice
    endscript
}
EOF'
```

8. **Create a test script to validate the setup:**

```bash
sudo bash -c 'cat > /opt/microservice/bin/test-permissions.sh << EOF
#!/bin/bash
echo "Testing Microservice Permissions"
echo "=============================="

echo "Testing as microservice user:"
sudo -u microservice touch /opt/microservice/data/test.dat
sudo -u microservice touch /opt/microservice/logs/test.log
echo "Write to config (should fail):"
sudo -u microservice touch /opt/microservice/config/test.conf

echo -e "\nTesting as developer (dev1):"
sudo -u dev1 ls -la /opt/microservice/logs/
echo "Write to logs (should fail):"
sudo -u dev1 touch /opt/microservice/logs/dev.log

echo -e "\nTesting as operations (ops1):"
sudo -u ops1 ls -la /opt/microservice/logs/
echo "Read log file:"
sudo -u ops1 cat /opt/microservice/logs/test.log
echo "Write to logs (should fail):"
sudo -u ops1 touch /opt/microservice/logs/ops.log

echo -e "\nTesting as admin (senior1):"
sudo -u senior1 ls -la /opt/microservice/config/
sudo -u senior1 touch /opt/microservice/config/admin.conf
EOF'

sudo chmod 755 /opt/microservice/bin/test-permissions.sh
```

9. **Run the test script and review results:**

```bash
sudo /opt/microservice/bin/test-permissions.sh
```

10. **Document the setup for team reference:**

```bash
sudo bash -c 'cat > /opt/microservice/README.md << EOF
# Microservice User and Group Management

## Service Account
- System user: microservice
- No login shell
- Home directory: /opt/microservice

## Groups
- microservice: Basic service access
- microservice_logs: Log access for monitoring
- microservice_admin: Administrative access

## Directory Structure
- /opt/microservice/bin: Executables (755 root:root)
- /opt/microservice/config: Configuration (770 microservice:microservice_admin)
- /opt/microservice/data: Application data (750 microservice:microservice)
- /opt/microservice/logs: Log files (770 microservice:microservice_logs)

## Sudo Permissions
- microservice_admin: Manage service (start/stop/restart)
- microservice: Check service status
- microservice_logs: View log files

## Adding New Team Members
\`\`\`bash
# Developers
sudo usermod -aG microservice username

# Operations
sudo usermod -aG microservice,microservice_logs username

# Administrators
sudo usermod -aG microservice,microservice_logs,microservice_admin username
\`\`\`
EOF'
```

This comprehensive approach ensures:
- The service runs securely with minimal privileges
- Team members have access appropriate to their roles
- System administrators can easily understand and maintain the setup
- Security best practices are followed

## 🔒 **Security Best Practices for User Management**

### **Beginner's Note: Security Fundamentals**
> Always follow the principle of least privilege: give users and services only the access they absolutely need to do their job, nothing more.

### **Intermediate Insight: Implementing Security Layers**
> Using both user/group permissions and sudo privileges provides multiple layers of security. If one is compromised, the other can still protect your systems.

### **SRE Perspective: Security Automation and Auditing**
> Consider implementing automated user management with tools like Ansible, Chef, or Puppet to ensure consistent security practices across all systems.

1. **Use Strong Password Policies**:

   ```bash
   # Set password complexity and expiration
   sudo vi /etc/login.defs
   # Set PASS_MAX_DAYS to 90
   # Set PASS_MIN_DAYS to 1
   # Set PASS_WARN_AGE to 7
   
   # Configure PAM for password complexity
   sudo vi /etc/pam.d/common-password
   # Add: password requisite pam_pwquality.so retry=3 minlen=12 lcredit=-1 ucredit=-1 dcredit=-1 ocredit=-1
   ```

2. **Implement Secure Authentication**:

   ```bash
   # Enforce SSH key authentication instead of passwords
   sudo vi /etc/ssh/sshd_config
   # Set PasswordAuthentication no
   # Set PubkeyAuthentication yes
   
   # Restart SSH to apply changes
   sudo systemctl restart sshd
   ```

3. **Regularly Audit User Accounts**:

   ```bash
   # List all users with login shells
   grep -v '/sbin/nologin\|/bin/false' /etc/passwd
   
   # Check for users with UID 0 (root privileges)
   awk -F: '$3 == 0 {print $1}' /etc/passwd
   
   # Find accounts with empty passwords
   sudo awk -F: '($2 == "" ) { print $1 }' /etc/shadow
   
   # Check for users who haven't logged in recently
   lastlog | grep 'Never logged in'
   ```

4. **Limit Access to the Root Account**:

   ```bash
   # Disable direct root login via SSH
   sudo vi /etc/ssh/sshd_config
   # Set PermitRootLogin no
   
   # Use sudo with minimal necessary privileges instead
   sudo visudo
   # Configure specific permissions rather than ALL=(ALL)
   ```

5. **Implement User Session Limits**:

   ```bash
   # Set session timeout for idle users (bash)
   echo "TMOUT=900" | sudo tee -a /etc/profile.d/timeout.sh
   sudo chmod +x /etc/profile.d/timeout.sh
   
   # Limit login attempts in PAM
   sudo vi /etc/pam.d/login
   # Add: auth required pam_tally2.so deny=5 unlock_time=1800
   ```

6. **Use Restricted Shells for Limited Access**:

   ```bash
   # Install restricted shell
   sudo apt-get install rssh  # Debian/Ubuntu
   
   # Limit SFTP/SCP only users
   sudo usermod -s /usr/bin/rssh sftpuser
   ```

These security practices create a layered defense approach that significantly reduces the risk of unauthorized access and limits the potential damage from compromised accounts.

---

## 📚 **Further Learning Resources**

### **Beginner Resources**
- [Linux User Management Basics (LinuxConfig)](https://linuxconfig.org/how-to-manage-users-on-linux)
- [Understanding Linux Users and Groups (DigitalOcean)](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-permissions)
- [Linux Journey - Users and Groups](https://linuxjourney.com/lesson/users-and-groups)

### **Intermediate Resources**
- [Linux User Administration (Red Hat Documentation)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/managing-users-groups-and-permissions_configuring-basic-system-settings)
- [Advanced User Management in Linux (DigitalOcean)](https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart)
- [Linux Permissions Advanced Concepts (Linux Journal)](https://www.linuxjournal.com/article/7727)

### **SRE-Specific Resources**
- [Google SRE Book - Chapter 5: Eliminating Toil](https://sre.google/sre-book/eliminating-toil/)
- [Essential System Administration, 3rd Edition (O'Reilly)](https://www.oreilly.com/library/view/essential-system-administration/0596003439/)
- [PAM (Pluggable Authentication Modules) Configuration](https://www.redhat.com/sysadmin/pluggable-authentication-modules-pam)
- [Implementing Multi-Factor Authentication in Linux](https://www.redhat.com/sysadmin/mfa-linux)
- [User Management Best Practices for Cloud Environments](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)

---

🎓 **Day 8 completed!** Tomorrow, we'll explore archiving, compression, and package management in Linux. You'll learn how to efficiently bundle and compress files, manage software installations, and keep your systems up to date – all critical skills for maintaining well-organized and current Linux environments.