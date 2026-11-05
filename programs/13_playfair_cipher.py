# 13. Playfair Cipher
# Logic: 5x5 key matrix built using UID-derived keyword.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def get_uid_keyword(uid):
    u = str(uid)
    return "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))

def make_matrix(key):
    letters = ""
    for c in key.upper().replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c.isalpha() and c not in letters:
            letters += c
    return [letters[i:i+5] for i in range(0, 25, 5)]

def playfair(text, matrix, decrypt=False):
    t = "".join(c for c in text.upper().replace("J", "I") if c.isalpha())
    if not decrypt:
        pairs, i = [], 0
        while i < len(t):
            a = t[i]
            if i + 1 < len(t):
                b = t[i+1]
                if a == b: b = "X"; i += 1
                else: i += 2
            else:
                b = "X"; i += 1
            pairs.append(a + b)
    else:
        pairs = [t[i:i+2] for i in range(0, len(t), 2)]

    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    step = -1 if decrypt else 1
    ans = ""

    for a, b in pairs:
        r1, c1 = pos[a]; r2, c2 = pos[b]
        if r1 == r2:
            ans += matrix[r1][(c1 + step) % 5] + matrix[r2][(c2 + step) % 5]
        elif c1 == c2:
            ans += matrix[(r1 + step) % 5][c1] + matrix[(r2 + step) % 5][c2]
        else:
            ans += matrix[r1][c2] + matrix[r2][c1]
    return ans

uid_key = get_uid_keyword(UID)
print(f"Configured UID: {UID} -> Derived Keyword: '{uid_key}'")

key = input(f"Enter key (default '{uid_key}'): ") or uid_key
text = input("Enter text (default 'INSTRUMENTS'): ") or "INSTRUMENTS"

mat = make_matrix(key)
print("Matrix:")
for row in mat:
    print(" ".join(row))

enc = playfair(text, mat)
dec = playfair(enc, mat, decrypt=True)

print("Encrypted:", enc)
print("Decrypted:", dec)
