# 25. RSA Digital Signature
# Logic: Hash message using hashlib.sha256. Sign: S = h^d mod n. Verify: S^e mod n == h.
import hashlib

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

p = 17
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = pow(e, -1, phi)

def_msg = f"UID: {UID}"
msg = input(f"Enter message to sign (default '{def_msg}'): ") or def_msg

h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % n
sig = pow(h, d, n)
verified_h = pow(sig, e, n)

print("Message:           ", msg)
print("SHA-256 Hash mod n:", h)
print("Signature:         ", sig)
print("Verification Result:", verified_h == h)
