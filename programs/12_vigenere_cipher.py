# 12. Vigenère Cipher
# Logic: Keyword derived from pairs of UID digits: (pair % 26) -> letter

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def get_vig_key_from_uid(uid):
    u = str(uid)
    return "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))

def vigenere(text, key, decrypt=False):
    ans, j = "", 0
    for c in text:
        if c.isalpha():
            k = ord(key[j % len(key)].upper()) - 65
            if decrypt:
                k = -k
            base = 65 if c.isupper() else 97
            ans += chr((ord(c) - base + k) % 26 + base)
            j += 1
        else:
            ans += c
    return ans

uid_key = get_vig_key_from_uid(UID)
print(f"Configured UID: {UID} -> Derived Keyword: '{uid_key}'")

text = input("Enter text (default 'ATTACKATDAWN'): ") or "ATTACKATDAWN"
key = (input(f"Enter keyword (default derived from UID = '{uid_key}'): ") or uid_key).upper()

enc = vigenere(text, key)
dec = vigenere(enc, key, decrypt=True)

print("Encrypted:", enc)
print("Decrypted:", dec)
