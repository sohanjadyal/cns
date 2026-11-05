# 15. Hill Cipher (3x3)
# Logic: 3x3 Hill cipher with pure Python determinant and inverse (NO numpy).

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def hill3(text, K):
    t = "".join(c for c in text.upper() if c.isalpha())
    while len(t) % 3: t += "X"
    ans = ""
    for i in range(0, len(t), 3):
        v = [ord(c) - 65 for c in t[i:i+3]]
        for row in K:
            ans += chr(sum(row[j]*v[j] for j in range(3)) % 26 + 65)
    return ans

def hill3_inverse(K):
    det = (K[0][0]*(K[1][1]*K[2][2] - K[1][2]*K[2][1])
         - K[0][1]*(K[1][0]*K[2][2] - K[1][2]*K[2][0])
         + K[0][2]*(K[1][0]*K[2][1] - K[1][1]*K[2][0])) % 26
    inv_det = pow(det, -1, 26)
    adj = [
        [(K[1][1]*K[2][2] - K[1][2]*K[2][1]) % 26, (K[0][2]*K[2][1] - K[0][1]*K[2][2]) % 26, (K[0][1]*K[1][2] - K[0][2]*K[1][1]) % 26],
        [(K[1][2]*K[2][0] - K[1][0]*K[2][2]) % 26, (K[0][0]*K[2][2] - K[0][2]*K[2][0]) % 26, (K[0][2]*K[1][0] - K[0][0]*K[1][2]) % 26],
        [(K[1][0]*K[2][1] - K[1][1]*K[2][0]) % 26, (K[0][1]*K[2][0] - K[0][0]*K[2][1]) % 26, (K[0][0]*K[1][1] - K[0][1]*K[1][0]) % 26]
    ]
    return [[(adj[r][c] * inv_det) % 26 for c in range(3)] for r in range(3)]

key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]
inv_key = hill3_inverse(key)

print(f"Configured UID: {UID}")
print(f"Key Matrix (3x3):         {key}")
print(f"Inverse Key Matrix (3x3): {inv_key}")

text = input("Enter text (default 'ACT'): ") or "ACT"

enc = hill3(text, key)
dec = hill3(enc, inv_key)

print("Encrypted:", enc)
print("Decrypted:", dec)
