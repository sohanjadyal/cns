# 05b. Chinese Remainder Theorem (CRT)
# Logic: Solves system of simultaneous congruences:
#   x = a_1 (mod m_1)
#   x = a_2 (mod m_2)
#   ...
#   x = a_k (mod m_k)
# where moduli m_i are pairwise coprime (gcd(m_i, m_j) = 1 for all i != j).
# Zero external libraries (NO math, NO numpy).

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a, m):
    # Modular multiplicative inverse using extended Euclidean algorithm
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def chinese_remainder_theorem(rems, mods):
    # Step 1: Verify that all moduli are pairwise coprime
    k = len(mods)
    for i in range(k):
        for j in range(i + 1, k):
            if gcd(mods[i], mods[j]) != 1:
                print(f"Error: Moduli {mods[i]} and {mods[j]} are not coprime!")
                return None, None

    # Step 2: Calculate total modulus product M = m_1 * m_2 * ... * m_k
    M = 1
    for m in mods:
        M *= m

    # Step 3: Compute x = sum(a_i * M_i * y_i) mod M
    # where M_i = M // m_i and y_i = (M_i)^(-1) mod m_i
    x = 0
    print("\n--- CRT Computation Table ---")
    print(f"{'i':<4} {'a_i':<6} {'m_i':<6} {'M_i':<8} {'y_i = M_i^-1 mod m_i':<24} {'Term = a_i * M_i * y_i':<24}")
    print("-" * 75)

    for i, (a, m) in enumerate(zip(rems, mods), 1):
        Mi = M // m
        yi = modinv(Mi, m)
        term = a * Mi * yi
        x = (x + term) % M
        print(f"{i:<4} {a:<6} {m:<6} {Mi:<8} {yi:<24} {term:<24}")

    print("-" * 75)
    return x, M

print(f"Configured UID: {UID}")

# Default textbook system:
# x = 2 (mod 3)
# x = 3 (mod 5)
# x = 2 (mod 7)
def_rems = "2, 3, 2"
def_mods = "3, 5, 7"

rems_input = input(f"Enter remainders a_i separated by commas (default '{def_rems}'): ") or def_rems
mods_input = input(f"Enter moduli m_i separated by commas (default '{def_mods}'): ") or def_mods

rems = [int(x.strip()) for x in rems_input.split(",")]
mods = [int(x.strip()) for x in mods_input.split(",")]

if len(rems) != len(mods):
    print("Error: The number of remainders must equal the number of moduli!")
else:
    sol_x, sol_M = chinese_remainder_theorem(rems, mods)
    if sol_x is not None:
        print(f"\nUnique Solution modulo M = {sol_M}:")
        print(f"  x = {sol_x} (mod {sol_M})")

        print("\n--- Verification Phase ---")
        all_correct = True
        for a, m in zip(rems, mods):
            actual_rem = sol_x % m
            match = actual_rem == (a % m)
            if not match: all_correct = False
            print(f"  {sol_x} mod {m} = {actual_rem} (Expected: {a % m}) -> {match}")

        print(f"\nAll Congruences Satisfied: {all_correct}")

        # UID-based application demo
        uid_rems = [UID % m for m in mods]
        uid_x, _ = chinese_remainder_theorem(uid_rems, mods)
        print(f"\n[Optional UID Application]")
        print(f"For UID = {UID}, remainders mod {mods} are {uid_rems}")
        print(f"CRT recovers UID mod {sol_M}: {uid_x} (UID % {sol_M} = {UID % sol_M})")
