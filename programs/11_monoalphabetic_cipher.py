# 11. Monoalphabetic Substitution Cipher
# Logic: Alphabet substitution key generated deterministically from UID seed.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_mono_key_from_uid(uid):
    letters = list(A)
    s = uid % 2**64
    for i in range(len(letters) - 1, 0, -1):
        s = (6364136223846793005 * s + 1442695040888963407) % 2**64
        j = (s >> 32) % (i + 1)
        letters[i], letters[j] = letters[j], letters[i]
    return "".join(letters)

key = get_mono_key_from_uid(UID)
print(f"Configured UID: {UID} -> Derived Substitution Key:\n{key}")

text = (input("Enter text (default 'ATTACK'): ") or "ATTACK").upper()

enc = "".join(key[A.index(c)] if c in A else c for c in text)
dec = "".join(A[key.index(c)] if c in key else c for c in enc)

print("Encrypted:", enc)
print("Decrypted:", dec)
