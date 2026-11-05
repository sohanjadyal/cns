# 3. Miller-Rabin Primality Test
# Logic: Write n-1 = 2^s * d. Check a^d mod n == 1 or -1, then square s-1 times.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

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

def miller_rabin(n, bases):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False

    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in bases:
        if a >= n:
            a = (a % (n - 2)) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

bases = get_uid_bases(UID)
print(f"Configured UID: {UID} -> Derived Bases: {bases}")

def_n = int(str(UID)[-2:]) if int(str(UID)[-2:]) > 1 else 17
n = int(input(f"Enter number to test (default {def_n}): ") or def_n)

if miller_rabin(n, bases):
    print(f"Result: {n} is Probably Prime (Passed Miller-Rabin Test)")
else:
    print(f"Result: {n} is Composite")
