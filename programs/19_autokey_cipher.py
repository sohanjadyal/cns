# 19. Autokey Cipher
# Logic: Keystream starts with UID-derived primer keyword then appends plaintext.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def get_uid_primer(uid):
    u = str(uid)
    return "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))

def autokey_enc(text, key):
    text = text.upper()
    full_key = (key + text).upper()
    return "".join(chr((ord(c) - 65 + ord(full_key[i]) - 65) % 26 + 65) for i, c in enumerate(text))

def autokey_dec(cipher, key):
    cipher = cipher.upper()
    plain, full_key = "", key.upper()
    for i, c in enumerate(cipher):
        p = (ord(c) - 65 - (ord(full_key[i]) - 65)) % 26
        ch = chr(p + 65)
        plain += ch
        full_key += ch
    return plain

uid_primer = get_uid_primer(UID)
print(f"Configured UID: {UID} -> Derived Primer: '{uid_primer}'")

text = input("Enter text (default 'ATTACKATDAWN'): ") or "ATTACKATDAWN"
key = (input(f"Enter primer key (default '{uid_primer}'): ") or uid_primer).upper()

enc = autokey_enc(text, key)
dec = autokey_dec(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
