# 8. Discrete Logarithm
# Logic: Given g^x = h (mod p), find exponent x in 0 <= x < p.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def discrete_log(g, h, p):
    for x in range(p):
        if pow(g, x, p) == h:
            return x
    return None

def_g = 5
def_p = 23
def_h = sum(int(d) for d in str(UID)) % def_p

g = int(input(f"Enter base g (default {def_g}): ") or def_g)
h = int(input(f"Enter target h (default {def_h}): ") or def_h)
p = int(input(f"Enter modulus p (default {def_p}): ") or def_p)

x = discrete_log(g, h, p)
if x is not None:
    print(f"Discrete log x = {x}  (Verification: {g}^{x} mod {p} = {pow(g, x, p)})")
else:
    print("No solution exists.")
