# 10. Caesar Cipher
# Logic: Key derived from UID: (sum of digits % 25) + 1
# C = (P + key) mod 26, P = (C - key) mod 26

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def caesar(text, key):
    ans = ""
    for c in text:
        if c.isupper():
            ans += chr((ord(c) - 65 + key) % 26 + 65)
        elif c.islower():
            ans += chr((ord(c) - 97 + key) % 26 + 97)
        else:
            ans += c
    return ans

uid_key = (sum(int(d) for d in str(UID)) % 25) + 1

text = input("Enter text (default 'HELLO'): ") or "HELLO"
key = int(input(f"Enter shift key (default derived from UID = {uid_key}): ") or uid_key)

enc = caesar(text, key)
dec = caesar(enc, -key)

print(f"Configured UID: {UID} -> Shift Key: {key}")
print("Encrypted:", enc)
print("Decrypted:", dec)
