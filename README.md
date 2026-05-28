Lab 02: Ransomware Analysis & Recovery

Objective: Reverse-engineer a basic encryption script to recover corrupted data.

---

Scenario

A simulated ransomware script (`ransomware.py`) has executed in this directory and scrambled our critical campus data file (`lab02data.txt`). 

Your task is to audit the `ransomware.py` file, figure out the exact mathematical formula used to alter the characters, and write a counter-script in Python or C# to reverse the process and restore `lab02data.txt` to plain text.

---

Tasks

  1. Analyze the Payload: Open `ransomware.py` and locate the line where the characters are modified.
  2. Write the Decryptor: Create a new file named `recover.py`. Write a script that reads the scrambled text from `lab02data.txt`, shifts the characters *backward* to undo the math, and saves the clean text back to the file.
  3. Verify Recovery: Run your recovery script and verify that `lab02data.txt` is readable again.

---

Python Reference Hints

To read a file in Python:
```python
with open("lab02data.txt", "r") as f:
    text = f.read()
```

To shift a single character code backward by 3 steps:
```python
original_char = chr(ord(scrambled_char) - 3)
```
