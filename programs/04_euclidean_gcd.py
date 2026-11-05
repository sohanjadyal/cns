# 4. Euclidean Algorithm (GCD)
# Logic: gcd(a, b) = gcd(b, a % b) until b becomes 0.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def_a = int(str(UID)[:4])   # e.g. 2024
def_b = int(str(UID)[-2:])  # e.g. 89

a = int(input(f"Enter a (default from UID = {def_a}): ") or def_a)
b = int(input(f"Enter b (default from UID = {def_b}): ") or def_b)

print(f"GCD({a}, {b}) = {gcd(a, b)}")
