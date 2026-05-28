Lab 01: Repository Code Audit

Objective: Internal code review and history analysis.

---

Scenario:

During a recent security audit of our internal project history, it was discovered that a junior engineer accidentally committed a production database credential to this repository. 

Although they quickly realized their mistake, deleted the file, and pushed a secondary commit to remove it, the sensitive data remains accessible within the Git history metadata. 

Your job is to locate and extract this credential before the repository is marked for external deployment.

---

Tasks:
1. Analyze the History: Use your terminal to audit the commit logs of this repository.
2. Isolate the Leak: Pinpoint the exact commit where the configuration file was introduced.
3. Extract the Key: Check out that specific moment in time and recover the password string (formatted as `FLAG{...}`).

---

Technical Reference Sheet

*If your terminal text viewer gets stuck or shows an `(END)` marker, press **`q`** to return to your normal prompt.*

1. View the Commit Log
Display the simplified chronological history of all changes made to this branch:
```bash
git log --oneline
```
*(Identify the unique 7-character alphanumeric hash code to the left of the commit message where the file was originally added.)*

2. Check Out the Target Commit
Temporarily move your local directory back to that specific snapshot in time. Replace `1234abc` with your discovered hash code:
```bash
git checkout 1234abc
```

3. Read the Configuration File
Open your file directory or use the terminal to read the contents of the restored file:
```bash
cat config.env
```

---

Resetting Your Workspace
Once you have successfully logged the credential, return your terminal back to the live branch timeline by running:
```bash
git checkout main
```

