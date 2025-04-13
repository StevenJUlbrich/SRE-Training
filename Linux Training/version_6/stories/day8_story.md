# Day 8: Taylor's Identity Management

*09:00 EST - San Francisco, USA*

Taylor arrived at CloudCrest's San Francisco headquarters feeling like an entirely different person from the nervous wreck who had stepped through these doors just a week ago. She'd spent the weekend binging old episodes of "The IT Crowd" and couldn't help but grin at how her first-day panic now seemed like something from a sitcom.

Her desk—initially stark and impersonal—now sported a small potted succulent (a gift from the team after her first successful day), a "Keep Calm and Grep On" mug she'd impulse-bought online, and a framed photo of her golden retriever, Kernel Panic, who was undoubtedly still sleeping on her unmade bed at home.

Growing up in rural Minnesota, Taylor had been the only tech enthusiast in a family of farmers. She'd built her first computer at 12 from parts rescued from the town dump, earning the nickname "Trash Tech Taylor" from her siblings—a moniker that had evolved from teasing to grudging respect when she started fixing everyone's devices. College had been a revelation; suddenly she wasn't the odd one out but part of a community that spoke her language. Still, nothing in her education had prepared her for the real-world pressure of that first day at CloudCrest.

Now, a week later, she opened her laptop and saw Mina's handoff:

> **@Taylor:** I've completed the integration of all our team's improvements from this week. The analytics platform is now stable, secure, and well-monitored:
> 
> 1. All networking connections are verified and functional
> 2. Created a comprehensive dashboard that shows system health, available via SSH tunnel
> 3. Verified that all scheduled maintenance scripts are running properly
> 4. Created detailed documentation of all improvements
> 
> The system has come a long way since your first day! The runaway logs that you discovered led us to uncover and fix several deeper issues. The platform is now in much better shape, with proper permissions, process management, log standardization, and monitoring.
> 
> I've attached instructions for accessing the dashboard in an email. Let me know if you have any questions when you start your shift.

"From accidental hero to... well, still a newbie, but at least a less panicked one," Taylor murmured, scrolling through the handoff and additional documentation.

Sophia, her team lead, stopped by her desk. "Morning, Taylor! Quite the week you've had, huh? How's it feel to have kickstarted the Great Analytics Renovation of 2025?"

Taylor laughed. "Like I accidentally pushed a domino and somehow fixed an entire Rube Goldberg machine. I've been studying everyone's notes all weekend—I still can't believe how many issues were hiding under that one log problem."

"That's SRE life for you," Sophia replied. "One thread always leads to another. Today's task should be right up your alley—we need to implement proper user and group management for the new analytics deployment. The new code is ready, but we need someone to set up all the service accounts and permissions. Think you can handle that?"

"Actually implementing the stuff Luis documented? Yes, please!" Taylor nodded eagerly.

"Perfect. The deployment docs are in Confluence. I'll check back in a few hours to see how you're doing."

As Sophia walked away, Taylor couldn't help but notice how different this felt from her first day. A week ago, she'd been thrown into an emergency. Today, she was being trusted with a planned deployment. Progress!

She connected to the staging server first, where she'd set up the users and groups before applying the same configuration to production:

```bash
$ ssh taylor@analytics-staging-01
```

First, she wanted to see the current users and groups on the system:

```bash
$ grep analytics /etc/passwd
analytics:x:1001:1001:Analytics Service:/home/analytics:/bin/bash

$ grep analytics /etc/group
analytics:x:1001:analytics
```

There was only a single user and group for all the analytics services, which explained some of the permission issues they'd encountered. According to Luis's notes and the new deployment plan, they needed to separate these into distinct service accounts to improve security.

Taylor pulled up the documentation and began planning the new user structure:

1. **analytics-admin**: Administrative account for the platform (already exists as "analytics")
2. **analytics-upload**: Service account for the upload component
3. **analytics-process**: Service account for the processing component
4. **analytics-archive**: Service account for the archival component
5. **analytics-api**: Service account for the API component

She also needed to create corresponding groups and properly set up membership.

First, Taylor decided to rename the existing analytics user to analytics-admin:

```bash
$ sudo usermod -l analytics-admin analytics
$ sudo groupmod -n analytics-admin analytics
```

She verified the change:

```bash
$ grep analytics-admin /etc/passwd
analytics-admin:x:1001:1001:Analytics Service:/home/analytics:/bin/bash
```

"Oops," Taylor realized, "the home directory still shows the old name." She corrected this:

```bash
$ sudo usermod -d /home/analytics-admin -m analytics-admin
```

Now she could create the service accounts. Since these would be system accounts that didn't need login capabilities, she used the `-r` flag and specified `/sbin/nologin` as the shell:

```bash
$ sudo useradd -r -s /sbin/nologin analytics-upload
$ sudo useradd -r -s /sbin/nologin analytics-process
$ sudo useradd -r -s /sbin/nologin analytics-archive
$ sudo useradd -r -s /sbin/nologin analytics-api
```

She verified the new accounts:

```bash
$ grep analytics /etc/passwd
analytics-admin:x:1001:1001:Analytics Service:/home/analytics-admin:/bin/bash
analytics-upload:x:999:999::/home/analytics-upload:/sbin/nologin
analytics-process:x:998:998::/home/analytics-process:/sbin/nologin
analytics-archive:x:997:997::/home/analytics-archive:/sbin/nologin
analytics-api:x:996:996::/home/analytics-api:/sbin/nologin
```

"Wait, do these service accounts even need home directories?" Taylor wondered. She decided to check the docs again. According to best practices, service accounts didn't need home directories, so she removed them:

```bash
$ for user in upload process archive api; do
    sudo usermod -d / analytics-$user
done
```

She double-checked:

```bash
$ grep analytics /etc/passwd
analytics-admin:x:1001:1001:Analytics Service:/home/analytics-admin:/bin/bash
analytics-upload:x:999:999::/:/sbin/nologin
analytics-process:x:998:998::/:/sbin/nologin
analytics-archive:x:997:997::/:/sbin/nologin
analytics-api:x:996:996::/:/sbin/nologin
```

Next, Taylor needed to set up the groups for managing shared access. She created additional groups:

```bash
$ sudo groupadd analytics-readers
$ sudo groupadd analytics-writers
```

Now she needed to set up group memberships. The analytics-admin user needed to be in all groups for administrative access:

```bash
$ sudo usermod -a -G analytics-upload,analytics-process,analytics-archive,analytics-api,analytics-readers,analytics-writers analytics-admin
```

She also needed to add appropriate group memberships for each service account:

```bash
$ sudo usermod -a -G analytics-readers,analytics-writers analytics-upload
$ sudo usermod -a -G analytics-readers,analytics-writers analytics-process
$ sudo usermod -a -G analytics-readers analytics-archive
$ sudo usermod -a -G analytics-readers analytics-api
```

Taylor checked the group memberships:

```bash
$ groups analytics-admin
analytics-admin : analytics-admin analytics-upload analytics-process analytics-archive analytics-api analytics-readers analytics-writers
```

Next, she wanted to verify that the directory structure Aanya created was ready for the new user permissions:

```bash
$ ls -la /var/app/uploads/
total 20
drwxr-xr-x 5 root          root            4096 Apr 13 15:30 .
drwxr-xr-x 8 root          root            4096 Apr 13 15:30 ..
drwxrwsr-x 2 analytics     analytics       4096 Apr 13 15:30 archive
drwxr-s--- 2 analytics     analytics       4096 Apr 13 15:30 incoming
drwxr-s--- 2 analytics     analytics       4096 Apr 13 15:30 processing
```

She needed to update these to use the new service accounts and groups:

```bash
$ sudo chown analytics-upload:analytics-writers /var/app/uploads/incoming
$ sudo chown analytics-process:analytics-writers /var/app/uploads/processing
$ sudo chown analytics-archive:analytics-readers /var/app/uploads/archive
```

Taylor also set the proper permissions to ensure the right access:

```bash
$ sudo chmod 770 /var/app/uploads/incoming
$ sudo chmod 770 /var/app/uploads/processing
$ sudo chmod 750 /var/app/uploads/archive
```

She rechecked the directory permissions:

```bash
$ ls -la /var/app/uploads/
total 20
drwxr-xr-x 5 root             root                4096 Apr 13 15:30 .
drwxr-xr-x 8 root             root                4096 Apr 13 15:30 ..
drwxr-x--- 2 analytics-archive analytics-readers  4096 Apr 13 15:30 archive
drwxrwx--- 2 analytics-upload  analytics-writers  4096 Apr 13 15:30 incoming
drwxrwx--- 2 analytics-process analytics-writers  4096 Apr 13 15:30 processing
```

To maintain the permission inheritance that Aanya set up, Taylor ensured the setgid bit was set on the directories:

```bash
$ sudo chmod g+s /var/app/uploads/incoming
$ sudo chmod g+s /var/app/uploads/processing
$ sudo chmod g+s /var/app/uploads/archive
```

Next, Taylor needed to handle the password policies for these accounts. Since they were service accounts, they shouldn't have regular passwords but should use SSH keys or other authentication methods. However, she wanted to ensure the analytics-admin account had proper password policies:

```bash
$ sudo chage -l analytics-admin
Last password change                                    : Apr 13, 2025
Password expires                                        : never
Password inactive                                       : never
Account expires                                         : never
Minimum number of days between password change          : 0
Maximum number of days between password change          : 99999
Number of days of warning before password expires       : 7
```

"That's not secure enough," Taylor thought. She updated the password policies:

```bash
$ sudo chage -M 90 -m 1 -W 7 -I 30 analytics-admin
```

This set:
- Maximum password age: 90 days
- Minimum password age: 1 day
- Warning period: 7 days
- Account inactive after password expiration: 30 days

She verified the changes:

```bash
$ sudo chage -l analytics-admin
Last password change                                    : Apr 13, 2025
Password expires                                        : Jul 12, 2025
Password inactive                                       : Aug 11, 2025
Account expires                                         : never
Minimum number of days between password change          : 1
Maximum number of days between password change          : 90
Number of days of warning before password expires       : 7
```

For the service accounts, Taylor locked them to prevent traditional password authentication:

```bash
$ for user in upload process archive api; do
    sudo passwd -l analytics-$user
done
```

She checked the status:

```bash
$ sudo passwd -S analytics-upload
analytics-upload L 04/13/2025 0 99999 7 -1 (Password locked.)
```

Next, Taylor needed to update the sudo permissions to align with the new user structure. She checked the current sudo configuration:

```bash
$ sudo cat /etc/sudoers.d/analytics
# Restricted permissions for analytics users
analytics ALL=(root) NOPASSWD: /bin/mv /var/app/uploads/processing/* /var/app/uploads/archive/*
www-data ALL=(root) NOPASSWD: /bin/cp /tmp/* /var/app/uploads/incoming/*
```

She updated the sudoers file to use the new service accounts:

```bash
$ sudo cp /etc/sudoers.d/analytics /etc/sudoers.d/analytics.bak
$ sudo visudo -f /etc/sudoers.d/analytics
```

And modified it to:

```
# Restricted permissions for analytics service accounts
analytics-admin ALL=(ALL:ALL) ALL
analytics-process ALL=(analytics-archive) NOPASSWD: /bin/mv /var/app/uploads/processing/* /var/app/uploads/archive/*
www-data ALL=(analytics-upload) NOPASSWD: /bin/cp /tmp/* /var/app/uploads/incoming/*
```

This gave analytics-admin full sudo access but restricted the other accounts to only the specific operations they needed.

To ensure these changes worked with the existing automation scripts, Taylor updated Aanya's maintenance script:

```bash
$ sudo cp /home/aanya/scripts/analytics_maintenance.sh /home/aanya/scripts/analytics_maintenance.sh.bak
$ sudo vim /home/aanya/scripts/analytics_maintenance.sh
```

She updated the script to use the new user and group names, then saved it.

Finally, Taylor created a README to document the new user structure:

```bash
$ sudo vim /var/app/uploads/USER_PERMISSIONS.md
```

```markdown
# Analytics Platform User & Group Structure

## Service Accounts

- **analytics-admin**: Administrative user with full access to all components
- **analytics-upload**: Service account for handling file uploads
- **analytics-process**: Service account for processing analytics data
- **analytics-archive**: Service account for archiving processed data
- **analytics-api**: Service account for the API component

## Groups

- **analytics-readers**: Users that need read access to analytics data
- **analytics-writers**: Users that need write access to analytics data

## Directory Permissions

- **/var/app/uploads/incoming**: Owned by analytics-upload:analytics-writers (770)
- **/var/app/uploads/processing**: Owned by analytics-process:analytics-writers (770)
- **/var/app/uploads/archive**: Owned by analytics-archive:analytics-readers (750)

## Security Notes

- Service accounts are locked and use /sbin/nologin shell
- Setgid bit is set on all directories to preserve group ownership
- Sudo permissions are restricted to specific operations
- Password policies are enforced for human accounts

Last updated: April 13, 2025 by Taylor
```

Satisfied with her work on the staging server, Taylor created a deployment script to apply these changes to production:

```bash
$ vim ~/scripts/deploy_user_setup.sh
```

```bash
#!/bin/bash
# deploy_user_setup.sh - Created by Taylor
# Deploys the user and group structure to production

# Exit on any error
set -e

echo "Starting user and group deployment..."

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Use sudo."
    exit 1
fi

# Rename existing analytics user/group
usermod -l analytics-admin analytics
groupmod -n analytics-admin analytics
usermod -d /home/analytics-admin -m analytics-admin

# Create service accounts
useradd -r -s /sbin/nologin analytics-upload
useradd -r -s /sbin/nologin analytics-process
useradd -r -s /sbin/nologin analytics-archive
useradd -r -s /sbin/nologin analytics-api

# Remove unnecessary home directories
for user in upload process archive api; do
    usermod -d / analytics-$user
done

# Create groups
groupadd analytics-readers
groupadd analytics-writers

# Set up group memberships
usermod -a -G analytics-upload,analytics-process,analytics-archive,analytics-api,analytics-readers,analytics-writers analytics-admin
usermod -a -G analytics-readers,analytics-writers analytics-upload
usermod -a -G analytics-readers,analytics-writers analytics-process
usermod -a -G analytics-readers analytics-archive
usermod -a -G analytics-readers analytics-api

# Update directory ownership
chown analytics-upload:analytics-writers /var/app/uploads/incoming
chown analytics-process:analytics-writers /var/app/uploads/processing
chown analytics-archive:analytics-readers /var/app/uploads/archive

# Set directory permissions
chmod 770 /var/app/uploads/incoming
chmod 770 /var/app/uploads/processing
chmod 750 /var/app/uploads/archive

# Ensure setgid bit
chmod g+s /var/app/uploads/incoming
chmod g+s /var/app/uploads/processing
chmod g+s /var/app/uploads/archive

# Set password policies
chage -M 90 -m 1 -W 7 -I 30 analytics-admin

# Lock service accounts
for user in upload process archive api; do
    passwd -l analytics-$user
done

# Create README
cat > /var/app/uploads/USER_PERMISSIONS.md << 'EOF'
# Analytics Platform User & Group Structure

## Service Accounts

- **analytics-admin**: Administrative user with full access to all components
- **analytics-upload**: Service account for handling file uploads
- **analytics-process**: Service account for processing analytics data
- **analytics-archive**: Service account for archiving processed data
- **analytics-api**: Service account for the API component

## Groups

- **analytics-readers**: Users that need read access to analytics data
- **analytics-writers**: Users that need write access to analytics data

## Directory Permissions

- **/var/app/uploads/incoming**: Owned by analytics-upload:analytics-writers (770)
- **/var/app/uploads/processing**: Owned by analytics-process:analytics-writers (770)
- **/var/app/uploads/archive**: Owned by analytics-archive:analytics-readers (750)

## Security Notes

- Service accounts are locked and use /sbin/nologin shell
- Setgid bit is set on all directories to preserve group ownership
- Sudo permissions are restricted to specific operations
- Password policies are enforced for human accounts

Last updated: April 13, 2025 by Taylor
EOF

echo "User and group deployment completed successfully!"
```

She made the script executable:

```bash
$ chmod +x ~/scripts/deploy_user_setup.sh
```

Before running it on production, Taylor tested it on a clean staging server to ensure it worked correctly. Once verified, she scheduled a deployment window with Sophia.

Later that afternoon, with approval from Sophia, Taylor connected to the production server and deployed the changes:

```bash
$ ssh taylor@analytics-prod-03
$ sudo ~/scripts/deploy_user_setup.sh
```

The script ran successfully, completing her task of properly implementing the user and group management structure.

"Look at me now, setting up users and groups like a pro," Taylor chuckled to herself. "A week ago I was panicking over a single log file. If only Kernel Panic could see me now—he'd still be unimpressed, but that's cats for you."

As her shift was ending, Taylor prepared a handoff for Noah in Australia:

> **@Noah:** I've implemented the new user and group structure for the analytics platform:
> 
> 1. Created separate service accounts for each component (upload, process, archive, api)
> 2. Set up appropriate groups (readers, writers) for access control
> 3. Updated directory permissions and ownership to match the new structure
> 4. Locked service accounts and enforced password policies for human accounts
> 5. Created documentation in /var/app/uploads/USER_PERMISSIONS.md
> 
> The changes have been deployed to both staging and production. The system is now ready for the new code deployment scheduled for tomorrow.
> 
> Also, I can't believe how much we've accomplished as a team in just one week! From that first disk space alert to a completely restructured, properly secured platform. I might actually sleep tonight without dreaming of runaway log files!

Sophia stopped by as Taylor was packing up. "How'd it go?"

"All done," Taylor replied with a smile. "Users created, groups set up, permissions assigned. It's amazing how much more confident I feel after just a week."

"That's because you're now officially battle-tested," Sophia grinned. "In the SRE world, that's worth more than any certification. Ready for week two?"

Taylor laughed. "As long as it doesn't start with another disk space emergency."

"No promises in our line of work," Sophia winked. "But whatever comes up, I think you've proven you can handle it."

As Taylor walked out of the office, she reflected on how much had changed in a single week. She'd gone from panicking over a simple log issue to implementing a complex user management structure. The whole team had transformed a problematic system into something robust and secure, using their complementary skills across different time zones.

Her phone pinged with a message from her roommate: "Kernel Panic knocked over your coffee mug again. Your desk is a disaster zone."

"Some things never change," Taylor laughed to herself as she headed home. But she had changed—from nervous newcomer to confident contributor. And tomorrow would bring new challenges to solve, all part of the never-ending, follow-the-sun adventure of being an SRE.

*[End of Day 8]*