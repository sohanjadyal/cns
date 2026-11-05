# 26. Digital Signature Algorithm (DSA)
# Logic: Hash msg with hashlib.sha256. Sign: r = (g^k mod p) mod q, s = k^-1*(h + x*r) mod q.
import hashlib

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

p = 23
q = 11
g = 4

x = sum(int(d) for d in str(UID)) % (q - 1) + 1
y = pow(g, x, p)

def_msg = f"UID: {UID}"
msg = input(f"Enter message to sign (default '{def_msg}'): ") or def_msg

h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % q or 1
k = 2

r = pow(g, k, p) % q
s = (pow(k, -1, q) * (h + x * r)) % q

w = pow(s, -1, q)
u1 = (h * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

print(f"Configured UID: {UID} | Private x = {x}, Public y = {y}")
print(f"Signature: (r = {r}, s = {s})")
print("Verification Result:", v == r)
