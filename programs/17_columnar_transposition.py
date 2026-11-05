# 17. Columnar Transposition Cipher
# Logic: Key word derived from UID: read columns in alphabetical order.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def get_uid_key(uid):
    u = str(uid)
    return "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))

def col_enc(text, key):
    n = len(key)
    while len(text) % n: text += "X"
    order = sorted(range(n), key=lambda i: key[i])
    return "".join(text[c::n] for c in order)

def col_dec(cipher, key):
    n = len(key)
    rows = len(cipher) // n
    order = sorted(range(n), key=lambda i: key[i])
    cols = {c: cipher[idx * rows:(idx + 1) * rows] for idx, c in enumerate(order)}
    return "".join(cols[c][r] for r in range(rows) for c in range(n))

uid_key = get_uid_key(UID)
print(f"Configured UID: {UID} -> Derived Key Word: '{uid_key}'")

text = input("Enter text (default 'HELLOFRIEND'): ") or "HELLOFRIEND"
key = (input(f"Enter key word (default '{uid_key}'): ") or uid_key).upper()

enc = col_enc(text, key)
dec = col_dec(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
