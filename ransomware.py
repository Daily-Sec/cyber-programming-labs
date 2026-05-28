import os

def encryptFile(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    with open(filename, 'r') as f:
        originalText = f.read()

    scrambledText = "".join(chr(ord(char) + 3) for char in originalText)

    with open(filename, 'w') as f:
        f.write(scrambledText)

    print(f"SUCCESS: {filename} has been encrypted by simulation virus.")

encryptFile("lab02data.txt")
