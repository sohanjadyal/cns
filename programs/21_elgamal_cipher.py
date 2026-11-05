# 21. ElGamal Encryption and Decryption
# Logic: Public Key (p, g, y), Private Key x where y = g^x mod p

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

p = 23
g = 5

x = sum(int(d) for d in str(UID)) % 10 + 2
y = pow(g, x, p)

print(f"Configured UID: {UID}")
print(f"Public Parameters: p = {p}, g = {g}, Public Key y = {y}")
print(f"Private Key: x = {x}")

m = int(input("Enter message number (m < 23, default 10): ") or 10)
k = 7

c1 = pow(g, k, p)
c2 = (m * pow(y, k, p)) % p

s = pow(c1, x, p)
dec = (c2 * pow(s, -1, p)) % p

print("Ciphertext (c1, c2):", (c1, c2))
print("Decrypted Message:  ", dec)
print("Verification Match: ", dec == m)
