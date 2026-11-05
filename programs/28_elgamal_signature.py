# 28. ElGamal Digital Signature
# Logic: Public (p, g, y), Private x. Hash with hashlib.sha256.
import hashlib

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

p = 23
g = 5

x = sum(int(d) for d in str(UID)) % 10 + 2
y = pow(g, x, p)

def_msg = f"UID: {UID}"
msg = input(f"Enter message to sign (default '{def_msg}'): ") or def_msg

h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % (p - 1) or 1
k = 7
assert gcd(k, p - 1) == 1

r = pow(g, k, p)
s = ((h - x * r) * pow(k, -1, p - 1)) % (p - 1)

left = pow(g, h, p)
right = (pow(y, r, p) * pow(r, s, p)) % p

print(f"Configured UID: {UID} | Private x = {x}, Public y = {y}")
print(f"Signature: (r = {r}, s = {s})")
print("Verification Result:", left == right)
