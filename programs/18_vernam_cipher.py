# 18. Vernam Cipher / One-Time Pad
# Logic: Key length must equal text length.
# Encryption: C = (P + K) mod 26, Decryption: P = (C - K) mod 26

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def vernam(text, key, decrypt=False):
    ans = ""
    for a, b in zip(text.upper(), key.upper()):
        p = ord(a) - 65
        k = ord(b) - 65
        x = (p - k if decrypt else p + k) % 26
        ans += chr(x + 65)
    return ans

u = str(UID)
uid_keyword = "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))

text = (input("Enter text (default 'HELLO'): ") or "HELLO").upper()
def_key = (uid_keyword * ((len(text) // len(uid_keyword)) + 1))[:len(text)]

key = (input(f"Enter key of length {len(text)} (default '{def_key}'): ") or def_key).upper()

if len(text) != len(key):
    print("Error: Key length must match text length!")
else:
    enc = vernam(text, key)
    dec = vernam(enc, key, decrypt=True)
    print("Encrypted:", enc)
    print("Decrypted:", dec)
