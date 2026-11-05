# 14. Hill Cipher (2x2)
# Logic: Key matrix derived from UID digit pairs and fixed for invertibility mod 26.
# C = P * K mod 26, P = C * K^-1 mod 26 (Zero imports - NO numpy)

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def get_hill2_key(uid):
    u = str(uid)
    g = [int(u[i:i+2]) for i in range(0, 8, 2)]
    K = [[g[0] % 26, g[1] % 26], [g[2] % 26, g[3] % 26]]
    tries = 0
    while gcd((K[0][0]*K[1][1] - K[0][1]*K[1][0]) % 26, 26) != 1:
        K[1][1] = (K[1][1] + 1) % 26
        tries += 1
        if tries % 26 == 0:
            K[0][0] = (K[0][0] + 1) % 26
    return K

def hill2_inverse(K):
    det = (K[0][0]*K[1][1] - K[0][1]*K[1][0]) % 26
    inv_det = pow(det, -1, 26)
    return [
        [(inv_det * K[1][1]) % 26, (-inv_det * K[0][1]) % 26],
        [(-inv_det * K[1][0]) % 26, (inv_det * K[0][0]) % 26]
    ]

def hill2(text, K):
    t = "".join(c for c in text.upper() if c.isalpha())
    if len(t) % 2: t += "X"
    ans = ""
    for i in range(0, len(t), 2):
        p1, p2 = ord(t[i]) - 65, ord(t[i+1]) - 65
        ans += chr((K[0][0]*p1 + K[0][1]*p2) % 26 + 65)
        ans += chr((K[1][0]*p1 + K[1][1]*p2) % 26 + 65)
    return ans

key = get_hill2_key(UID)
inv_key = hill2_inverse(key)

print(f"Configured UID: {UID} -> Derived Invertible Key Matrix: {key}")
print(f"Inverse Key Matrix: {inv_key}")

text = input("Enter text (default 'HELP'): ") or "HELP"

enc = hill2(text, key)
dec = hill2(enc, inv_key)

print("Encrypted:", enc)
print("Decrypted:", dec)
