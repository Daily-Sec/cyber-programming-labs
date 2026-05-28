Lab 03: Digital Forensics & Log Parsing

Objective: Write an automation script to parse a massive log file and isolate a cyber attack.

---

Scenario:

Our campus web server was breached sometime in the last 24 hours. The IT Help Desk has dumped the network logs into a file named `server_access.log`. 

The file contains 1,000 lines of traffic, making a manual audit impossible. Your team must write a Python or C# script to parse the data, detect the attacker's footprint, and answer the incident response questions.

---

Tasks:
  1. **Analyze the Format:** Open `server_access.log` and note how the timestamps, IP addresses, and HTTP status codes are structured.
  2. **Write the Parser:** Create a Python script (`parse_logs.py`) or a C# equivalent that reads the file line-by-line. 
  3. **Isolate the Attacker:** Filter the data to find any IP address hitting `/portal/admin_login` and returning multiple `401` (Unauthorized) errors followed by a `200` (Success) error.
  4. **Identify the Breach Time:** Print out the exact timestamp of the successful `200` breach.

---

Python Reference Hints:

To search for a specific word inside a line of text in Python:

```python
with open("server_access.log", "r") as f:
    for line in f:
        if "admin_login" in line:
            print(line.strip())
```
