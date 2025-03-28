# 🚀 **Day 8: User & Group Management – Managing Access and Security**

---

## 📌 **Introduction**

### 🔄 **Recap of Day 7:**

Yesterday, you gained essential networking skills, including connectivity testing (`ping`, `traceroute`, `mtr`), interface management (`ip`, `ifconfig`), monitoring active connections (`netstat`, `ss`), and secure remote operations (`ssh`, `scp`, `rsync`). These skills enable you to diagnose network issues and securely transfer data between systems.

### 📅 **Today's Topics and Importance:**

Today, we'll explore **User & Group Management** in Linux. Understanding how to properly manage users and groups is fundamental for:

- Controlling who can access your systems
- Implementing the principle of least privilege
- Organizing users with similar access needs
- Managing file and resource permissions
- Maintaining system security and accountability
- Supporting multiple users on shared resources

For SREs, these skills are particularly important as you'll often need to create service accounts for applications, manage access rights across teams, and ensure proper security practices are followed.

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

Linux uses a multi-user model where each user has their own identity, represented by a unique **user ID (UID)**. Users can belong to one or more **groups**, each with a unique **group ID (GID)**. This model enables fine-grained access control and resource sharing.

Think of this model as an office building:

- **Users** are like individual employees with unique ID badges
- **Groups** are like departments or project teams
- **Permissions** are like access controls for different rooms and resources
- **Home directories** are like personal offices
- **Root user** is like the building manager with master keys

This analogy helps understand how Linux manages access: just as different employees have different access privileges within an office building, different Linux users have different permissions to files and resources.

### **User Types in Linux**

Linux systems typically have several types of users:

1. **Root (UID 0)**: The superuser with unlimited privileges
2. **System Users**: Used for running services and daemons
3. **Regular Users**: Human users with limited privileges
4. **Service Accounts**: Special-purpose accounts for applications

As an SRE, you'll need to understand when to use each type. For example, system services should never run as root; instead, they should use dedicated service accounts with minimal permissions.

### **The Role of Groups**

Groups serve several important purposes:

1. **Simplified Permission Management**: Assign permissions to groups rather than individual users
2. **Logical Organization**: Group users based on roles, departments, or access needs
3. **Collaboration**: Allow multiple users to access shared resources
4. **Privilege Separation**: Limit access based on function or responsibility

Each user has a **primary group** (set during account creation) and can belong to multiple **supplementary groups** to gain additional privileges.

---

## 💻 **Commands to Learn Today**

### **1. User Management (`useradd`, `userdel`, `usermod`)**

#### **`useradd` – Create New Users**

**Purpose**: Create new user accounts.

**SRE Context**: Used to create human user accounts, service accounts for applications, and system user accounts.

**Syntax:**

```bash
useradd [options] username
```

**Common options:**

- `-m`: Create home directory
- `-d /path`: Specify home directory
- `-s /path/to/shell`: Specify login shell
- `-g group`: Specify primary group
- `-G group1,group2`: Specify supplementary groups
- `-r`: Create a system account (lower UID range)
- `-c "comment"`: Add a comment (typically full name)

**Examples:**

Create a standard user with default settings:

```bash
[sre@prod-server ~]$ sudo useradd jsmith
```

Create a user with a home directory and specific shell:

```bash
[sre@prod-server ~]$ sudo useradd -m -d /home/dbadmin -s /bin/bash dbadmin
```

Create a service account (system user) for running an application:

```bash
[sre@prod-server ~]$ sudo useradd -r -s /bin/false -d /opt/appservice -c "App Service" appuser
```

Create a user with specific groups and comment:

```bash
[sre@prod-server ~]$ sudo useradd -m -G developers,docker -c "Jane Smith" jsmith
```

#### **`userdel` – Delete Users**

**Purpose**: Remove user accounts from the system.

**SRE Context**: Used when decommissioning accounts or removing unused service accounts.

**Syntax:**

```bash
userdel [options] username
```

**Common options:**

- `-r`: Remove home directory and mail spool
- `-f`: Force removal even if user is logged in

**Examples:**

Delete a user account but keep their home directory:

```bash
[sre@prod-server ~]$ sudo userdel jsmith
```

Delete a user account and their home directory:

```bash
[sre@prod-server ~]$ sudo userdel -r jsmith
```

Force removal of a user account:

```bash
[sre@prod-server ~]$ sudo userdel -f jsmith
```

#### **`usermod` – Modify Users**

**Purpose**: Modify existing user accounts.

**SRE Context**: Used to update account properties, change groups, or lock accounts.

**Syntax:**

```bash
usermod [options] username
```

**Common options:**

- `-a -G group1,group2`: Add to supplementary groups (use -a to append)
- `-g group`: Change primary group
- `-d /path`: Change home directory
- `-s /path/to/shell`: Change login shell
- `-L`: Lock the account (disable password login)
- `-U`: Unlock the account
- `-c "comment"`: Change the comment field
- `-l new_name`: Change the username

**Examples:**

Add a user to the docker group (without removing from other groups):

```bash
[sre@prod-server ~]$ sudo usermod -a -G docker jsmith
```

Change a user's primary group:

```bash
[sre@prod-server ~]$ sudo usermod -g developers jsmith
```

Lock a user account temporarily:

```bash
[sre@prod-server ~]$ sudo usermod -L jsmith
```

Change a user's shell:

```bash
[sre@prod-server ~]$ sudo usermod -s /bin/zsh jsmith
```

Rename a user account:

```bash
[sre@prod-server ~]$ sudo usermod -l john jsmith
```

### **2. Group Management (`groupadd`, `groupdel`, `groupmod`)**

#### **`groupadd` – Create New Groups**

**Purpose**: Create new user groups.

**SRE Context**: Used to create functional groups for organizing users and managing permissions.

**Syntax:**

```bash
groupadd [options] groupname
```

**Common options:**

- `-g GID`: Specify the group ID
- `-r`: Create a system group (lower GID range)

**Examples:**

Create a new group:

```bash
[sre@prod-server ~]$ sudo groupadd developers
```

Create a system group:

```bash
[sre@prod-server ~]$ sudo groupadd -r appgroup
```

Create a group with specific GID:

```bash
[sre@prod-server ~]$ sudo groupadd -g 1500 project42
```

#### **`groupdel` – Delete Groups**

**Purpose**: Remove groups from the system.

**SRE Context**: Used when reorganizing group structures or removing obsolete groups.

**Syntax:**

```bash
groupdel groupname
```

**Example:**

Delete a group:

```bash
[sre@prod-server ~]$ sudo groupdel oldproject
```

#### **`groupmod` – Modify Groups**

**Purpose**: Modify existing groups.

**SRE Context**: Used to rename groups or change group IDs.

**Syntax:**

```bash
groupmod [options] groupname
```

**Common options:**

- `-n new_name`: Rename the group
- `-g GID`: Change the group ID

**Examples:**

Rename a group:

```bash
[sre@prod-server ~]$ sudo groupmod -n engineering developers
```

Change a group's GID:

```bash
[sre@prod-server ~]$ sudo groupmod -g 1600 engineering
```

### **3. Password Management (`passwd`)**

**Purpose**: Set or change user passwords and manage account expiration.

**SRE Context**: Used for initial password setup, requiring password changes, and managing password policies.

**Syntax:**

```bash
passwd [options] [username]
```

**Common options:**

- `-l`: Lock a user account
- `-u`: Unlock a user account
- `-d`: Delete a password (make it empty)
- `-e`: Expire a password (force change at next login)
- `-n days`: Minimum days between password changes
- `-x days`: Maximum days a password remains valid
- `-w days`: Warning days before password expires

**Examples:**

Change your own password:

```bash
[sre@prod-server ~]$ passwd
Changing password for user sre.
Current password: 
New password: 
Retype new password: 
passwd: all authentication tokens updated successfully.
```

Change another user's password (as root):

```bash
[sre@prod-server ~]$ sudo passwd jsmith
New password: 
Retype new password: 
passwd: all authentication tokens updated successfully.
```

Force password change at next login:

```bash
[sre@prod-server ~]$ sudo passwd -e jsmith
passwd: password expiry information changed.
```

Lock a user account:

```bash
[sre@prod-server ~]$ sudo passwd -l jsmith
passwd: password changed.
```

### **4. User Information and Management**

#### **`id` – Display User and Group Information**

**Purpose**: Show numeric user/group IDs and group membership.

**SRE Context**: Used to check a user's UID, GID, and group memberships for troubleshooting.

**Syntax:**

```bash
id [options] [username]
```

**Example:**

Display user information:

```bash
[sre@prod-server ~]$ id jsmith
uid=1001(jsmith) gid=1001(jsmith) groups=1001(jsmith),1000(developers),998(docker)
```

#### **`groups` – Show Group Memberships**

**Purpose**: Display which groups a user belongs to.

**SRE Context**: Quick way to check a user's access rights based on group membership.

**Syntax:**

```bash
groups [username]
```

**Example:**

Show a user's groups:

```bash
[sre@prod-server ~]$ groups jsmith
jsmith developers docker
```

#### **System Files for User and Group Management**

**Purpose**: Store user and group information.

**SRE Context**: Understanding these files helps with troubleshooting and advanced configurations.

**Key files:**

- `/etc/passwd`: User account information
- `/etc/shadow`: Encrypted passwords and expiration data
- `/etc/group`: Group definitions and memberships
- `/etc/gshadow`: Group passwords and administrators

**Examples:**

View user information in `/etc/passwd`:

```bash
[sre@prod-server ~]$ grep jsmith /etc/passwd
jsmith:x:1001:1001:Jane Smith:/home/jsmith:/bin/bash
```

View group information in `/etc/group`:

```bash
[sre@prod-server ~]$ grep developers /etc/group
developers:x:1000:jsmith,anotheruser
```

#### **`getent` – Get Entries from Name Service Switch Libraries**

**Purpose**: Retrieve entries from administrative databases.

**SRE Context**: Works well even when users/groups are defined in external systems like LDAP.

**Syntax:**

```bash
getent database key
```

**Examples:**

Get information about a user:

```bash
[sre@prod-server ~]$ getent passwd jsmith
jsmith:x:1001:1001:Jane Smith:/home/jsmith:/bin/bash
```

Get information about a group:

```bash
[sre@prod-server ~]$ getent group developers
developers:x:1000:jsmith,anotheruser
```

### **5. Additional User Management Commands**

#### **`su` – Switch User**

**Purpose**: Change the current user without logging out.

**SRE Context**: Used to test permissions as different users or perform tasks as root.

**Syntax:**

```bash
su [options] [username]
```

**Common options:**

- `-`: Start a login shell (loads the user's environment)
- `-c command`: Execute a single command as the specified user

**Examples:**

Switch to the root user:

```bash
[sre@prod-server ~]$ su -
Password: 
[root@prod-server ~]#
```

Run a command as another user:

```bash
[sre@prod-server ~]$ su - appuser -c "ls -la /opt/app/data"
```

#### **`sudo` – Execute Command as Another User (Typically Root)**

**Purpose**: Execute commands with elevated privileges.

**SRE Context**: Allows authorized users to perform specific administrative tasks without having the root password.

**Syntax:**

```bash
sudo [options] command
```

**Common options:**

- `-u user`: Execute command as a user other than root
- `-l`: List allowed commands
- `-i`: Simulate initial login (loads environment variables)

**Examples:**

Execute a command as root:

```bash
[sre@prod-server ~]$ sudo systemctl restart nginx
```

Execute a command as another user:

```bash
[sre@prod-server ~]$ sudo -u appuser /opt/app/bin/restart.sh
```

List allowed sudo commands:

```bash
[sre@prod-server ~]$ sudo -l
```

---

## 🔍 **SRE Perspective: User Management Best Practices**

### **1. Service Account Management**

SREs commonly create service accounts to run applications. Here's how to create one properly:

```bash
# Create system user with no login shell and no home directory
sudo useradd -r -s /sbin/nologin -c "App Service" appuser

# Set proper group membership
sudo usermod -a -G app_logs,app_data appuser

# Set application directory permissions
sudo mkdir -p /opt/app/{logs,data}
sudo chown -R appuser:appuser /opt/app
sudo chmod 750 /opt/app

# Verify setup
sudo -u appuser ls -la /opt/app
```

### **2. Implementing Least Privilege**

Proper group management helps implement the principle of least privilege:

```bash
# Create functional groups
sudo groupadd app_read
sudo groupadd app_write
sudo groupadd app_admin

# Assign users to appropriate groups
sudo usermod -a -G app_read viewer1
sudo usermod -a -G app_read,app_write editor1
sudo usermod -a -G app_read,app_write,app_admin admin1

# Set directory permissions
sudo mkdir -p /data/application
sudo chown root:app_read /data/application
sudo chmod 750 /data/application
sudo mkdir -p /data/application/config
sudo chown root:app_admin /data/application/config
sudo chmod 770 /data/application/config
```

### **3. User Onboarding and Offboarding**

Automation is key for consistent user management:

```bash
# Example onboarding script
newuser="jdoe"
fullname="John Doe"
primarygroup="staff"
additionalgroups="developers,docker,project42"

sudo useradd -m -c "$fullname" -g $primarygroup -G $additionalgroups $newuser
sudo passwd -e $newuser  # Force password change at first login
sudo mkdir -p /home/$newuser/.ssh
sudo cp /etc/skel/.bashrc /home/$newuser/
# Add SSH key, if provided
echo "ssh-rsa AAAA..." | sudo tee /home/$newuser/.ssh/authorized_keys
sudo chown -R $newuser:$newuser /home/$newuser/.ssh
sudo chmod 700 /home/$newuser/.ssh
sudo chmod 600 /home/$newuser/.ssh/authorized_keys

# Example offboarding script
olduser="exemployee"
sudo usermod -L $olduser  # Lock the account
sudo usermod -s /sbin/nologin $olduser  # Disable shell access
sudo find / -user $olduser -exec ls -la {} \; > /tmp/${olduser}_files.txt  # Audit files
# Archive home directory
sudo tar -czf /backup/home/${olduser}_$(date +%Y%m%d).tar.gz /home/$olduser
# Eventually, fully remove the account
# sudo userdel -r $olduser
```

---

## 🎯 **Practical Exercise: Setting Up a Multi-User Environment**

In this exercise, you'll practice creating and managing users and groups for a simulated application environment. You'll implement proper access controls and test the permissions.

1. **Set up the project groups**:

   ```bash
   sudo groupadd projectapp
   sudo groupadd projectapp_dev
   sudo groupadd projectapp_ops
   sudo groupadd projectapp_admin
   ```

2. **Create project users**:

   ```bash
   # Create a service account for the application
   sudo useradd -r -s /sbin/nologin -c "Project App Service" projectapp
   
   # Create a developer user
   sudo useradd -m -c "Developer User" -G projectapp_dev dev_user
   sudo passwd dev_user
   
   # Create an operations user
   sudo useradd -m -c "Operations User" -G projectapp_ops ops_user
   sudo passwd ops_user
   
   # Create an admin user
   sudo useradd -m -c "Admin User" -G projectapp_dev,projectapp_ops,projectapp_admin admin_user
   sudo passwd admin_user
   ```

3. **Set up the project directory structure**:

   ```bash
   # Create directory structure
   sudo mkdir -p /opt/projectapp/{bin,config,data,logs}
   
   # Set base directory ownership
   sudo chown projectapp:projectapp /opt/projectapp
   sudo chmod 755 /opt/projectapp
   
   # Set proper permissions for each directory
   sudo chown projectapp:projectapp /opt/projectapp/bin
   sudo chmod 755 /opt/projectapp/bin
   
   sudo chown projectapp:projectapp_admin /opt/projectapp/config
   sudo chmod 775 /opt/projectapp/config
   
   sudo chown projectapp:projectapp /opt/projectapp/data
   sudo chmod 770 /opt/projectapp/data
   
   sudo chown projectapp:projectapp_ops /opt/projectapp/logs
   sudo chmod 775 /opt/projectapp/logs
   ```

4. **Create test files in each directory**:

   ```bash
   sudo touch /opt/projectapp/bin/app.sh
   sudo chmod 755 /opt/projectapp/bin/app.sh
   
   sudo touch /opt/projectapp/config/settings.conf
   sudo chmod 664 /opt/projectapp/config/settings.conf
   
   sudo -u projectapp touch /opt/projectapp/data/data.db
   sudo chmod 660 /opt/projectapp/data/data.db
   
   sudo -u projectapp touch /opt/projectapp/logs/app.log
   sudo chmod 664 /opt/projectapp/logs/app.log
   ```

5. **Test access for each user**:

   ```bash
   # Test developer access
   sudo -u dev_user ls -la /opt/projectapp/bin/
   sudo -u dev_user ls -la /opt/projectapp/config/
   sudo -u dev_user ls -la /opt/projectapp/data/  # Should fail
   sudo -u dev_user ls -la /opt/projectapp/logs/  # Should fail
   
   # Test ops access
   sudo -u ops_user ls -la /opt/projectapp/bin/
   sudo -u ops_user ls -la /opt/projectapp/config/  # Should fail
   sudo -u ops_user ls -la /opt/projectapp/data/  # Should fail
   sudo -u ops_user ls -la /opt/projectapp/logs/
   
   # Test admin access (should work everywhere)
   sudo -u admin_user ls -la /opt/projectapp/bin/
   sudo -u admin_user ls -la /opt/projectapp/config/
   sudo -u admin_user touch /opt/projectapp/config/new.conf
   sudo -u admin_user ls -la /opt/projectapp/logs/
   ```

6. **Adjust permissions if needed**:

   ```bash
   # If you find issues, fix them
   sudo usermod -a -G projectapp_ops dev_user  # Give developer access to logs
   sudo chmod 775 /opt/projectapp/logs  # Ensure group members can write to logs
   ```

This exercise demonstrates how proper user and group management helps implement the principle of least privilege while enabling necessary access for different roles.

---

## 📝 **Quiz: User and Group Management**

Test your understanding of today's material:

1. How would you add a new user called `john` with a home directory?

   - a) `useradd john`
   - b) `useradd -h john`
   - c) `useradd -m john`
   - d) `usermod -m john`

2. Which command completely removes a user named `john` and their home directory?

   - a) `userdel john`
   - b) `userdel -r john`
   - c) `usermod -r john`
   - d) `rmuser -r john`

3. You need to add user `john` to the group `staff` without removing him from other groups. Which command would you use?

   - a) `usermod -aG staff john`
   - b) `usermod -g staff john`
   - c) `groupadd staff john`
   - d) `groupmod -a john staff`

4. Which file contains the encrypted passwords for user accounts?

   - a) `/etc/passwd`
   - b) `/etc/shadow`
   - c) `/etc/group`
   - d) `/etc/users`

5. To create a service account (system user) for running a web service, which command is most appropriate?

   - a) `useradd -m webservice`
   - b) `useradd -r -s /bin/false webservice`
   - c) `usermod -s /bin/nologin webservice`
   - d) `groupadd -r webservice`

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

For service accounts, using `-r` is usually safe since service accounts typically don't contain irreplaceable data.

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

---

## 🔄 **Real-World SRE Scenario: Setting Up a New Application**

**Situation:** You need to deploy a new application on a Linux server with proper user and permission setup. The application needs different permission levels for its components.

**SRE Response Using Today's Commands:**

1. Create appropriate groups for access control:

   ```bash
   sudo groupadd -r myapp
   sudo groupadd -r myapp_admin
   sudo groupadd -r myapp_logs
   ```

2. Create a service account for the application:

   ```bash
   sudo useradd -r -s /sbin/nologin -d /opt/myapp -c "My Application Service" myapp
   ```

3. Add appropriate administrators to the admin group:

   ```bash
   sudo usermod -a -G myapp_admin admin1
   sudo usermod -a -G myapp_admin admin2
   ```

4. Add operations staff to the logs group:

   ```bash
   sudo usermod -a -G myapp_logs operator1
   sudo usermod -a -G myapp_logs operator2
   ```

5. Set up the directory structure:

   ```bash
   sudo mkdir -p /opt/myapp/{bin,config,data,logs}
   ```

6. Set appropriate ownership and permissions:

   ```bash
   # Base application directory
   sudo chown root:root /opt/myapp
   sudo chmod 755 /opt/myapp
   
   # Executable directory - owned by root, readable by all
   sudo chown root:root /opt/myapp/bin
   sudo chmod 755 /opt/myapp/bin
   
   # Configuration - owned by service, writable by admins
   sudo chown myapp:myapp_admin /opt/myapp/config
   sudo chmod 770 /opt/myapp/config
   
   # Data directory - owned and only accessible by service
   sudo chown myapp:myapp /opt/myapp/data
   sudo chmod 700 /opt/myapp/data
   
   # Logs - owned by service, readable by log group
   sudo chown myapp:myapp_logs /opt/myapp/logs
   sudo chmod 750 /opt/myapp/logs
   sudo chmod g+s /opt/myapp/logs  # Set SGID to ensure new files maintain group
   ```

7. Configure sudo permissions for application management:

   ```bash
   echo "%myapp_admin ALL=(root) /bin/systemctl start myapp, /bin/systemctl stop myapp, /bin/systemctl restart myapp" | sudo tee /etc/sudoers.d/myapp
   sudo chmod 440 /etc/sudoers.d/myapp
   ```

8. Verify the setup:

   ```bash
   ls -la /opt/myapp/
   sudo -u myapp touch /opt/myapp/data/test.db
   sudo -u admin1 touch /opt/myapp/config/test.conf
   sudo -u operator1 ls -la /opt/myapp/logs/
   sudo -u operator1 touch /opt/myapp/logs/test.log  # Should fail
   ```

9. Create a systemd service file:

   ```bash
   sudo bash -c 'cat > /etc/systemd/system/myapp.service << EOF
   [Unit]
   Description=My Application Service
   After=network.target
   
   [Service]
   Type=simple
   User=myapp
   Group=myapp
   ExecStart=/opt/myapp/bin/myapp
   Restart=on-failure
   WorkingDirectory=/opt/myapp
   
   [Install]
   WantedBy=multi-user.target
   EOF'
   
   sudo systemctl daemon-reload
   ```

This comprehensive approach ensures:

- The application runs with minimal privileges (principle of least privilege)
- Different roles have appropriate access levels
- File permissions enforce the security model
- The setup is systematic and documented

---

## 🔒 **Security Best Practices for User Management**

As an SRE, follow these security best practices for user management:

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

Let me continue with the security best practices section for Day 8:

## 🔒 **Security Best Practices for User Management** (continued)

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

- [Linux User Administration (Red Hat Documentation)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/managing-users-groups-and-permissions_configuring-basic-system-settings)
- [User Management in Linux (DigitalOcean)](https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart)
- [Linux Permissions Advanced Concepts (Linux Journal)](https://www.linuxjournal.com/article/7727)
- [Google SRE Book - Chapter 5: Eliminating Toil](https://sre.google/sre-book/eliminating-toil/)
- [Essential System Administration, 3rd Edition (O'Reilly)](https://www.oreilly.com/library/view/essential-system-administration/0596003439/)
- [PAM (Pluggable Authentication Modules) Configuration](https://www.redhat.com/sysadmin/pluggable-authentication-modules-pam)

---

🎓 **Day 8 completed!** Tomorrow, we'll explore archiving, compression, and package management in Linux. You'll learn how to efficiently bundle and compress files, manage software installations, and keep your systems up to date – all critical skills for maintaining well-organized and current Linux environments.
