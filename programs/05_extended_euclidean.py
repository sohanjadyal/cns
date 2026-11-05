# 5. Extended Euclidean Algorithm (Modular Inverse)
# Logic: Finds integers x, y such that a*x + m*y = gcd(a, m).

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def_a = sum(int(d) for d in str(UID))  # Sum of digits
def_m = int(str(UID)[-2:])             # Last 2 digits

a = int(input(f"Enter a (default sum of UID digits = {def_a}): ") or def_a)
m = int(input(f"Enter modulus m (default last digits = {def_m}): ") or def_m)

g, x, y = extended_gcd(a, m)

if g == 1:
    inv = x % m
    print(f"gcd({a}, {m}) = {g}")
    print(f"Modular Inverse of {a} mod {m} = {inv}")
    print(f"Verification: ({a} * {inv}) % {m} = {(a * inv) % m}")
else:
    print(f"Inverse does not exist because gcd({a}, {m}) = {g} != 1")
