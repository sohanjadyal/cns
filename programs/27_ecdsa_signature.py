# 27. ECDSA (Elliptic Curve Digital Signature Algorithm)
# Curve: y^2 = x^3 + 2x + 2 (mod 17), G = (5, 1), order n = 19
import hashlib

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

def_msg = f"UID: {UID}"
msg = input(f"Enter message to sign (default '{def_msg}'): ") or def_msg

h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % n or 1
k = 3

R = ec_mul(k, G)
r = R[0] % n
s = (pow(k, -1, n) * (h + r * d)) % n

w = pow(s, -1, n)
u1 = (h * w) % n
u2 = (r * w) % n
P_ver = ec_add(ec_mul(u1, G), ec_mul(u2, Q))

valid = P_ver is not None and (P_ver[0] % n == r)

print(f"Configured UID: {UID} | Private d = {d}, Public Q = {Q}")
print(f"Signature: (r = {r}, s = {s})")
print("Verification Result:", valid)
