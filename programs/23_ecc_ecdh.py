# 23. ECC - Elliptic Curve Diffie-Hellman (ECDH)
# Curve: y^2 = x^3 + 2x + 2 (mod 17), Base G = (5, 1), order n = 19

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

def_alice = sum(int(d) for d in str(UID)) % (n - 1) + 1
def_bob = 7

alice_priv = int(input(f"Alice private key (default from UID = {def_alice}): ") or def_alice)
bob_priv = int(input(f"Bob private key (default {def_bob}): ") or def_bob)

pubA = ec_mul(alice_priv, G)
pubB = ec_mul(bob_priv, G)

sharedA = ec_mul(alice_priv, pubB)
sharedB = ec_mul(bob_priv, pubA)

print("Alice Public Key Point:", pubA)
print("Bob Public Key Point:  ", pubB)
print("Alice Shared Key Point:", sharedA)
print("Bob Shared Key Point:  ", sharedB)
print("Shared Keys Match:     ", sharedA == sharedB)
