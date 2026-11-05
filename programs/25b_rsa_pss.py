# 25b. RSA-PSS (Probabilistic Signature Scheme)
# Logic: Adds Salt and MGF (Mask Generation Function) to make signatures probabilistic.
import hashlib

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

# 1. Key Generation
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi)

msg = "HELLO"

def mgf(seed_val, length=2):
    return hashlib.sha256(f"MGF:{seed_val}".encode()).digest()[:length]

# Step 1: Base message hash
m_hash = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % n

# Step 2: Salt (Probabilistic component — derived from UID or random)
salt = (sum(int(c) for c in str(UID)) % 50) + 1

# Step 3: Compute H = Hash(m_hash || salt) mod n
H = int(hashlib.sha256(f"{m_hash}:{salt}".encode()).hexdigest(), 16) % n

# Step 4: Mask the salt using MGF(H)
mask = int.from_bytes(mgf(H), "big") % 100
masked_salt = salt ^ mask

# Step 5: Sign the PSS hash H
pss_sig = pow(H, d, n)

# ----------------- VERIFICATION -----------------
recovered_H = pow(pss_sig, e, n)
verifier_mask = int.from_bytes(mgf(recovered_H), "big") % 100
recovered_salt = masked_salt ^ verifier_mask
expected_H = int(hashlib.sha256(f"{m_hash}:{recovered_salt}".encode()).hexdigest(), 16) % n

print(f"Configured UID: {UID}")
print(f"PSS Signature:  {pss_sig}")
print(f"Masked Salt:    {masked_salt}")
print(f"Recovered Salt: {recovered_salt} (matches original: {recovered_salt == salt})")
print(f"Verified:       {recovered_H == expected_H}")
