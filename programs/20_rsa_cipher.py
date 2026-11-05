# 20. RSA Encryption and Decryption
# Logic: Public Key (e, n), Private Key (d, n)
# n = p * q, phi = (p-1)*(q-1), e*d = 1 (mod phi)

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

def_m = sum(int(d) for d in str(UID))

print(f"Configured UID: {UID}")
print(f"Public Key (e, n):  {(e, n)}")
print(f"Private Key (d, n): {(d, n)}")

m = int(input(f"Enter message number (0 < m < {n}, default sum of digits = {def_m}): ") or def_m)

c = pow(m, e, n)
dec = pow(c, d, n)

print("Encrypted Ciphertext:", c)
print("Decrypted Message:   ", dec)
print("Verification Match:  ", dec == m)
