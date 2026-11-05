# 1. Fermat Primality Test
# Logic: If p is prime and gcd(a, p) = 1, then a^(p-1) = 1 (mod p)

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def get_uid_bases(uid):
    u = str(uid)
    ds = [int(c) for c in u]
    return [
        int(u[-2:]) % 97 + 2,
        sum(ds) % 97 + 2,
        (int(u[:4]) + int(u[-4:])) % 97 + 2,
        sum(ds[0::2]) % 97 + 2,
        sum(ds[1::2]) % 97 + 2
    ]

def fermat(n, bases):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False

    for a in bases:
        if a >= n:
            a = (a % (n - 2)) + 2
        if gcd(a, n) != 1 or pow(a, n - 1, n) != 1:
            return False
    return True

bases = get_uid_bases(UID)
print(f"Configured UID: {UID} -> Derived Bases: {bases}")

# Default test candidate: prime from last 2 digits of UID or standard prime
def_n = int(str(UID)[-2:]) if int(str(UID)[-2:]) > 1 else 17
n = int(input(f"Enter number to test (default {def_n}): ") or def_n)

if fermat(n, bases):
    print(f"Result: {n} is Probably Prime (Passed Fermat Test)")
else:
    print(f"Result: {n} is Composite")
