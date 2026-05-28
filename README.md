Lab 04: Digital Forensics & Data Carving

**Objective:** Programmatically scan a raw data payload to extract a hidden, embedded file structure.

---

Scenario:

Network defense systems intercepted a suspicious, massive binary file named `intercepted_payload.dat` being exfiltrated from our servers. Initial string scans show only scrambled raw bytes, but threat intelligence suspects a compressed archive is hidden inside it.

Your mission is to perform digital "data carving." You must write a Python script that opens the file in binary mode, scans the raw bytes for the standard binary signature of a ZIP file, and extracts the hidden contents.

---

Tasks
  1. **Understand Binary Signatures:** All files start with universal magic bytes. A ZIP archive *always* starts with the exact hex signature: `50 4b 03 04` (which stands for the ASCII letters `PK..` after the format inventor, Phil Katz).
  2. **Write the Carver:** Create a script named `carve.py`. It must open `intercepted_payload.dat` in **Read Binary (`rb`)** mode and find the starting index location of the bytes `b'PK\x03\x04'`.
  3. **Extract the Archive:** Once your script finds the starting index, slice the data from that index all the way to the end of the file, and save those extracted bytes into a brand new file named `extracted.zip`.
  4. **Unzip the Flag:** Open your newly carved ZIP file to recover the plaintext flag!

---

Python Reference Hints

To search for raw bytes inside a binary data stream:
```python
with open("intercepted_payload.dat", "rb") as f:
    data = f.read()

# Find the starting position of the magic bytes
start_index = data.find(b'PK\x03\x04')
print(f"ZIP file magic bytes found at index: {start_index}")
```
