# 16. Rail Fence Cipher
# Logic: Rails derived from UID sum of digits: (sum(digits) % 3) + 2

# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged

def rail_enc(text, rails):
    rows = ["" for _ in range(rails)]
    r, step = 0, 1
    for c in text:
        rows[r] += c
        if r == 0: step = 1
        elif r == rails - 1: step = -1
        r += step
    return "".join(rows)

def rail_dec(cipher, rails):
    pattern, r, step = [], 0, 1
    for _ in cipher:
        pattern.append(r)
        if r == 0: step = 1
        elif r == rails - 1: step = -1
        r += step

    res = [""] * len(cipher)
    idx = 0
    for rail_idx in range(rails):
        for pos, p_rail in enumerate(pattern):
            if p_rail == rail_idx:
                res[pos] = cipher[idx]
                idx += 1
    return "".join(res)

uid_rails = (sum(int(d) for d in str(UID)) % 3) + 2

text = input("Enter text (default 'DEFENDTHEEASTWALL'): ") or "DEFENDTHEEASTWALL"
rails = int(input(f"Enter rails (default from UID = {uid_rails}): ") or uid_rails)

enc = rail_enc(text, rails)
dec = rail_dec(enc, rails)

print("Encrypted:", enc)
print("Decrypted:", dec)
