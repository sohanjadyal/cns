# 24. EC-ElGamal Encryption and Decryption
# Curve: y^2 = x^3 + 2x + 2 (mod 17), G = (5, 1), n = 19

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

p, a, b = 17, 2, 2
G = (5, 1); n = 19; O = None

def ec_add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return O
    if P == Q:
        m = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    else:
        m = ((y2 - y1) * pow((x2 - x1) % p, -1, p)) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def ec_mul(k, P):
    R = O
    while k > 0:
        if k % 2: R = ec_add(R, P)
        P = ec_add(P, P)
        k //= 2
    return R

d = sum(int(c) for c in str(UID)) % (n - 1) + 1
Q = ec_mul(d, G)
M = ec_mul(2, G)
k = 3

C1 = ec_mul(k, G)
C2 = ec_add(M, ec_mul(k, Q))

S = ec_mul(d, C1)
neg_S = (S[0], (-S[1]) % p)
dec = ec_add(C2, neg_S)

print(f"Configured UID: {UID} | Receiver Private Key d = {d}")
print("Original Message Point M: ", M)
print("Encrypted Ciphertext (C1):", C1)
print("Encrypted Ciphertext (C2):", C2)
print("Decrypted Message Point:  ", dec)
print("Verification Match:       ", dec == M)
