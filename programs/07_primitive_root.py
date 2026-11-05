# 7. Smallest Primitive Root
# Logic: g is a primitive root mod p if powers {g^1, g^2, ..., g^(p-1)} mod p contain all 1..p-1.

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def primitive_root(p):
    for g in range(2, p):
        values = set()
        for i in range(1, p):
            values.add(pow(g, i, p))
        if len(values) == p - 1:
            return g
    return None

def_p = int(str(UID)[-2:])  # e.g. 89
p = int(input(f"Enter prime p (default from UID = {def_p}): ") or def_p)
print(f"Smallest primitive root modulo {p} is {primitive_root(p)}")
