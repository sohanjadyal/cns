# 22. Diffie-Hellman Key Exchange
# Logic: Alice computes B^a mod p, Bob computes A^b mod p.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

p = 23
g = 5

def_a = sum(int(d) for d in str(UID)) % 10 + 2
def_b = 15

print(f"Configured UID: {UID} | Public: p = {p}, g = {g}")
a = int(input(f"Enter Alice private key a (default from UID = {def_a}): ") or def_a)
b = int(input(f"Enter Bob private key b (default {def_b}): ") or def_b)

A = pow(g, a, p)
B = pow(g, b, p)

keyA = pow(B, a, p)
keyB = pow(A, b, p)

print("Alice Public Key (A):", A)
print("Bob Public Key (B):  ", B)
print("Alice Computed Shared Key:", keyA)
print("Bob Computed Shared Key:  ", keyB)
print("Shared Keys Match:        ", keyA == keyB)
