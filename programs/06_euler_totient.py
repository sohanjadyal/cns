# 6. Euler's Totient Function phi(n)
# Logic: Counts numbers 1 <= i <= n such that gcd(i, n) == 1 (Zero imports).

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def phi(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1
    return count

def_n = sum(int(d) for d in str(UID))  # Sum of UID digits
n = int(input(f"Enter n (default sum of digits = {def_n}): ") or def_n)
print(f"phi({n}) = {phi(n)}")
