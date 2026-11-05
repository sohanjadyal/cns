# 9. Square-and-Multiply (Fast Modular Exponentiation)
# Logic: Compute a^b mod m by squaring the base each step and multiplying when bit is 1.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def square_and_multiply(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

def_a = 3
def_b = sum(int(d) for d in str(UID))
def_m = int(str(UID)[-2:])

a = int(input(f"Enter base a (default {def_a}): ") or def_a)
b = int(input(f"Enter exponent b (default sum of digits = {def_b}): ") or def_b)
m = int(input(f"Enter modulus m (default last digits = {def_m}): ") or def_m)

ans = square_and_multiply(a, b, m)
print(f"{a}^{b} mod {m} = {ans}")
print(f"Verification using pow(): {pow(a, b, m)}")
