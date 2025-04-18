# 🔐 Prompt: *Follow-the-Sun Chronicles* – Day 6: Fatima & the Fortress of Access Control

> You're continuing the serialized global SRE training series **The Follow-the-Sun Chronicles**, where each day is led by a fictional character from a different region.
>
> For **Day 6**, your character is:
> - **Name:** Fatima  
> - **Location:** UAE (Dubai)  
> - **Time:** 08:30 GST  
> - **Role:** Security-focused SRE and permission architect  
> - **Personality:** Disciplined, sharp, rules-driven. Will revoke your privileges mid-sentence if you're careless. Lives by the Principle of Least Privilege. Speaks with precise, measured words that carry the weight of experience.
>
> You're rewriting the **Day 6 SRE Database Training Module**, focused on:
> - Database user management (creating users, assigning roles)  
> - Privileges: system vs object  
> - Role-based access control (RBAC)  
> - GRANT and REVOKE  
> - User activity monitoring  
> - Security best practices (passwords, auditing, encryption)  
> - SRE response to permission-related outages
>
> **Constraints & Style:**
> 1. Maintain the structure from the original Day 6 training document, including numbered sections:  
>    - 🔍 Beginner → 🧩 Intermediate → 💡 Advanced/SRE Learning Objectives  
>    - Core concepts, technical explanations, SQL examples, and system impact  
>    - Real-world SRE use cases, security tradeoffs, and recovery examples  
>    - The "Observe, Test, Evaluate, and Take Action" framework  
> 2. Narrate everything from **Fatima's point of view** and maintain her voice consistently throughout:  
>    - She approaches access control like building a digital fortress  
>    - Her tone should be polite but firm, with zero tolerance for permission sprawl  
>    - Each section should include her personal commentary on why careless privilege assignments are dangerous  
>    - Use phrases like "I've revoked more privileges than most DBAs have granted" or "In my experience, over-privileged accounts are ticking time bombs"  
> 3. Begin with a **real incident**: a read-only service account was silently dropped from a critical table's GRANT list, breaking an app in production. Fatima investigates and locks it down.  
> 4. Use **Mermaid diagrams** to illustrate:  
>    - User-role-privilege relationships  
>    - Privilege escalation paths  
>    - SRE response workflow during access failures  
>    - Use `&commat;` for email addresses, and `autonumber` for all `sequenceDiagram` blocks  
> 5. For each concept (system privilege, object privilege, GRANT/REVOKE, auditing):  
>    - Give a real-world analogy (e.g., "System privileges = master keys")  
>    - Include Mermaid visuals  
>    - Add SQL examples (Oracle, Postgres, SQL Server)  
>    - Explain the performance and security impact  
>    - Include common mistakes and how Fatima handles them (with her specific perspective)  
> 6. Create **"Fatima's Security Rules"** as visually distinct blocks after key sections:
>    ```
>    🔒 Fatima's Rule #2: All privileges must be documented, justified, and regularly audited.
>    ```
> 7. Include a detailed section on **permissions and performance interactions**:
>    - Show concrete examples with metrics of how over-privileged users can degrade system performance
>    - Include a specific example: a user accidentally running a `SELECT *` with no WHERE across a 1M-row table
>    - Show CPU/memory spike visuals or AWR sample plans to demonstrate impact
>    - Have Fatima explain how a security audit helped identify and resolve performance issues
>    - Emphasize that **security lapses are performance issues too**
> 8. Include a **sequenceDiagram** showing an SRE response to an access outage caused by a revoked privilege  
> 9. Include a **flowchart** showing how to decide whether a user needs a new role or should be granted existing permissions  
> 10. Expand the **Hands-On Advanced/SRE Exercises** section:
>     - Keep the existing three exercises
>     - Add a fourth stretch goal: "Design a permission escalation alert using audit logs + external alerting (e.g., Prometheus + Slack)"
>     - Include a redacted snippet of suspicious query logs as an example
>     - Have Fatima comment on what patterns she looks for in these logs
> 11. Include a **"Golden RBAC Template"** table as a quick reference:
>     
>     | Role | Privileges | Use Case |
>     |------|------------|----------|
>     | `dev_user` | SELECT, INSERT on test_* | Developer test environment |
>     | `app_user` | SELECT, INSERT, UPDATE on prod.orders | Production write path |
>     | `reporting` | SELECT only, read-only replica | Dashboards, BI tools |
>     | `dba_ro` | SELECT on all objects, SHOW commands | Non-invasive troubleshooting |
>     | `sre_admin` | Elevated privileges with audit trail | Emergency response only |
>     
>     With Fatima's commentary on why this template provides both security and operational efficiency
> 12. Preserve the practical examples from the original document:
>     - Permission matrix examples
>     - Database security syntax comparison 
>     - SRE monitoring dashboard elements
>     - Real-world reliability considerations
> 13. Conclude with a **summary of security red flags Fatima watches for**, and tips for access policy hygiene  
> 14. End with a **handoff to Mina in Lagos**, who will take over Day 7 by assessing the performance impact of too many indexes on those well-secured tables.
>
> **Tone:**  
> - Precise and protective  
> - Each technical section should reveal Fatima's expertise through specific anecdotes and warnings  
> - No chaos allowed—only clarity, containment, and command  
> - When giving examples, Fatima should occasionally mention "I once had to revoke..." or "I've seen this mistake too many times..."
>
> This should be a **professional training document** that maintains all the technical content from the original, but is narrated consistently through Fatima's security-conscious lens, where every permission decision carries weight and consequence.

The revised prompt addresses all three feedback points:

1. **Deeper exploration of permissions and performance interaction** (Point #7)
   - Added specific examples showing how security issues become performance problems
   - Required CPU/memory spike visuals or AWR sample plans
   - Connected security audits to performance improvements

2. **Expanded hands-on advanced exercises** (Point #10)
   - Added the suggested fourth "stretch goal" exercise
   - Included requirements for suspicious query log examples
   - Added Fatima's commentary on what patterns to watch for

3. **Golden RBAC Template** (Point #11)
   - Added a quick-reference table with role definitions, privileges, and use cases
   - Expanded to include more role types (added `dba_ro` and `sre_admin`)
   - Required Fatima's commentary on the balance of security and operational efficiency

