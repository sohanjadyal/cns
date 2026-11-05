# CNS Lab Programs Tailored for UID: 2024300089
### Zero External Libraries (`math` / `numpy` excluded) | Pure Python 3 & `hashlib` only

---

## UID Configuration Summary (UID = `2024300089`)

| Parameter / Key | Derivation Formula from UID | Computed Value for `2024300089` |
| :--- | :--- | :--- |
| **Sum of Digits** | $\sum d_i = 2+0+2+4+3+0+0+0+8+9$ | **`28`** |
| **UID Bases (Primality)** | Lab formulas: $b_1 \dots b_5$ | **`[91, 30, 78, 17, 15]`** |
| **Caesar Key** | $(\sum d_i \bmod 25) + 1 = (28 \bmod 25) + 1$ | **`4`** |
| **Vigenère Keyword** | 5 pairs mod 26: `[20, 24, 30, 00, 89]` $\to$ Letters | **`"UYEAL"`** |
| **Hill 2×2 Key Matrix** | Derived from pairs `[20, 24], [30, 00]` & fixed mod 26 | **`[[21, 24], [4, 1]]`** ($\det = 3$) |
| **Hill 2×2 Inverse** | $K^{-1} \pmod{26}$ in pure Python | **`[[9, 18], [16, 7]]`** |
| **Rail Fence Rails** | $(\sum d_i \bmod 3) + 2 = (28 \bmod 3) + 2$ | **`3` rails** |
| **Columnar Keyword** | UID keyword | **`"UYEAL"`** |
| **Playfair Matrix Key**| Built from UID keyword | **`"UYEAL"`** |
| **RSA Message** | Default $\sum d_i$ | **`28`** |
| **DSA / ElGamal / ECC**| Private keys & messages | Derived from UID digits & `2024300089` |

All 28 standalone executable files are located in the [`programs_uid_2024300089/`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089) folder.

---

## 1. Number Theory (9 Programs)

### 1. Fermat Primality Test
- **File**: [`01_fermat_primality.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/01_fermat_primality.py)
- **Logic**: Tests $a^{n-1} \equiv 1 \pmod n$ for UID bases `[91, 30, 78, 17, 15]`. Default candidate is $89$ (last 2 digits of UID, which is prime).

```python
# 1. Fermat Primality Test (UID: 2024300089)
UID = 2024300089

def gcd(a, b):
    while b: a, b = b, a % b
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
print(f"UID: {UID} -> Derived Bases: {bases}")

n = int(input("Enter number to test (default 89): ") or 89)
print(f"Result: {n} is {'Probably Prime' if fermat(n, bases) else 'Composite'}")
```

---

### 2. Euler Primality Test (Euler–Jacobi)
- **File**: [`02_euler_primality.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/02_euler_primality.py)
- **Logic**: $a^{(n-1)/2} \equiv \left(\frac{a}{n}\right) \pmod n$ using Jacobi symbol without external libraries.

```python
# 2. Euler Primality Test (Euler-Jacobi) (UID: 2024300089)
UID = 2024300089

def gcd(a, b):
    while b: a, b = b, a % b
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

def jacobi(a, n):
    ans = 1
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): ans = -ans
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: ans = -ans
        a %= n
    return ans if n == 1 else 0

def euler_test(n, bases):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False

    for a in bases:
        if a >= n:
            a = (a % (n - 2)) + 2
        if gcd(a, n) != 1:
            return False
        if pow(a, (n - 1) // 2, n) != jacobi(a, n) % n:
            return False
    return True

bases = get_uid_bases(UID)
print(f"UID: {UID} -> Derived Bases: {bases}")

n = int(input("Enter number to test (default 89): ") or 89)
print(f"Result: {n} is {'Probably Prime' if euler_test(n, bases) else 'Composite'}")
```

---

### 3. Miller–Rabin Primality Test
- **File**: [`03_miller_rabin.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/03_miller_rabin.py)
- **Logic**: Write $n - 1 = 2^s \cdot d$. Check $a^d \equiv 1 \pmod n$ or square $s-1$ times.

```python
# 3. Miller-Rabin Primality Test (UID: 2024300089)
UID = 2024300089

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
print(f"UID: {UID} -> Derived Bases: {bases}")

n = int(input("Enter number to test (default 89): ") or 89)
print(f"Result: {n} is {'Probably Prime' if miller_rabin(n, bases) else 'Composite'}")
```

---

### 4. Euclidean Algorithm (GCD)
- **File**: [`04_euclidean_gcd.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/04_euclidean_gcd.py)
- **Inputs**: $a = 2024$ (first 4 digits), $b = 89$ (last 2 digits).

```python
# 4. Euclidean Algorithm (GCD) (UID: 2024300089)
UID = 2024300089

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def_a = int(str(UID)[:4])   # 2024
def_b = int(str(UID)[-2:])  # 89

a = int(input(f"Enter a (default from UID = {def_a}): ") or def_a)
b = int(input(f"Enter b (default from UID = {def_b}): ") or def_b)

print(f"GCD({a}, {b}) = {gcd(a, b)}")
```

---

### 5. Extended Euclidean Algorithm (Modular Inverse)
- **File**: [`05_extended_euclidean.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/05_extended_euclidean.py)
- **Inputs**: $a = 28$ ($\sum d_i$), $m = 89$ (prime from UID).

```python
# 5. Extended Euclidean Algorithm (Modular Inverse) (UID: 2024300089)
UID = 2024300089

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def_a = sum(int(d) for d in str(UID))  # 28
def_m = int(str(UID)[-2:])             # 89

a = int(input(f"Enter a (default sum of digits = {def_a}): ") or def_a)
m = int(input(f"Enter modulus m (default last digits = {def_m}): ") or def_m)

g, x, y = extended_gcd(a, m)
if g == 1:
    inv = x % m
    print(f"gcd({a}, {m}) = {g}")
    print(f"Modular Inverse of {a} mod {m} = {inv}")
    print(f"Verification: ({a} * {inv}) % {m} = {(a * inv) % m}")
else:
    print(f"Inverse does not exist: gcd({a}, {m}) = {g} != 1")
```

---

### 6. Euler's Totient Function $\phi(n)$
- **File**: [`06_euler_totient.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/06_euler_totient.py)
- **Input**: $n = 28$ ($\sum d_i$).

```python
# 6. Euler's Totient Function phi(n) (UID: 2024300089)
UID = 2024300089

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def phi(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1
    return count

def_n = sum(int(d) for d in str(UID))  # 28
n = int(input(f"Enter n (default sum of digits = {def_n}): ") or def_n)
print(f"phi({n}) = {phi(n)}")
```

---

### 7. Smallest Primitive Root
- **File**: [`07_primitive_root.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/07_primitive_root.py)
- **Input**: $p = 89$ (prime from UID).

```python
# 7. Smallest Primitive Root (UID: 2024300089)
UID = 2024300089

def primitive_root(p):
    for g in range(2, p):
        values = set()
        for i in range(1, p):
            values.add(pow(g, i, p))
        if len(values) == p - 1:
            return g
    return None

def_p = int(str(UID)[-2:])  # 89
p = int(input(f"Enter prime p (default from UID = {def_p}): ") or def_p)
print(f"Smallest primitive root modulo {p} is {primitive_root(p)}")
```

---

### 8. Discrete Logarithm
- **File**: [`08_discrete_logarithm.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/08_discrete_logarithm.py)
- **Logic**: Solves $g^x \equiv h \pmod p$.

```python
# 8. Discrete Logarithm (UID: 2024300089)
UID = 2024300089

def discrete_log(g, h, p):
    for x in range(p):
        if pow(g, x, p) == h:
            return x
    return None

def_g = 5
def_p = 23
def_h = sum(int(d) for d in str(UID)) % def_p  # 28 % 23 = 5

g = int(input(f"Enter base g (default {def_g}): ") or def_g)
h = int(input(f"Enter target h (default {def_h}): ") or def_h)
p = int(input(f"Enter modulus p (default {def_p}): ") or def_p)

x = discrete_log(g, h, p)
print(f"Discrete log x = {x}" if x is not None else "No solution exists.")
```

---

### 9. Square-and-Multiply (Fast Modular Exponentiation)
- **File**: [`09_square_and_multiply.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/09_square_and_multiply.py)
- **Inputs**: $a = 3$, $b = 28$ ($\sum d_i$), $m = 89$ (UID last 2 digits).

```python
# 9. Square-and-Multiply (UID: 2024300089)
UID = 2024300089

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
def_b = sum(int(d) for d in str(UID))  # 28
def_m = int(str(UID)[-2:])             # 89

a = int(input(f"Enter base a (default {def_a}): ") or def_a)
b = int(input(f"Enter exponent b (default sum of digits = {def_b}): ") or def_b)
m = int(input(f"Enter modulus m (default last digits = {def_m}): ") or def_m)

ans = square_and_multiply(a, b, m)
print(f"{a}^{b} mod {m} = {ans}")
print(f"Verification using pow(): {pow(a, b, m)}")
```

---

## 2. Symmetric Ciphers (10 Programs)

### 10. Caesar Cipher
- **File**: [`10_caesar_cipher.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/10_caesar_cipher.py)
- **Key Formula**: $(\sum d_i \bmod 25) + 1 = (28 \bmod 25) + 1 = 4$.

```python
# 10. Caesar Cipher (UID: 2024300089)
UID = 2024300089

def caesar(text, key):
    ans = ""
    for c in text:
        if c.isupper():   ans += chr((ord(c) - 65 + key) % 26 + 65)
        elif c.islower(): ans += chr((ord(c) - 97 + key) % 26 + 97)
        else:             ans += c
    return ans

uid_key = (sum(int(d) for d in str(UID)) % 25) + 1  # 4
text = input("Enter text (default 'HELLO'): ") or "HELLO"
key = int(input(f"Enter shift key (default derived from UID = {uid_key}): ") or uid_key)

enc = caesar(text, key)
dec = caesar(enc, -key)
print(f"UID: {UID} -> Shift Key: {key}")
print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 11. Monoalphabetic Substitution Cipher
- **File**: [`11_monoalphabetic_cipher.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/11_monoalphabetic_cipher.py)
- **Logic**: Alphabet deterministically shuffled using UID seed.

```python
# 11. Monoalphabetic Substitution Cipher (UID: 2024300089)
UID = 2024300089
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_mono_key_from_uid(uid):
    letters = list(A)
    s = uid % 2**64
    for i in range(len(letters) - 1, 0, -1):
        s = (6364136223846793005 * s + 1442695040888963407) % 2**64
        j = (s >> 32) % (i + 1)
        letters[i], letters[j] = letters[j], letters[i]
    return "".join(letters)

key = get_mono_key_from_uid(UID)
print(f"UID: {UID} -> Derived Substitution Key:\n{key}")

text = (input("Enter text (default 'ATTACK'): ") or "ATTACK").upper()
enc = "".join(key[A.index(c)] if c in A else c for c in text)
dec = "".join(A[key.index(c)] if c in key else c for c in enc)

print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 12. Vigenère Cipher
- **File**: [`12_vigenere_cipher.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/12_vigenere_cipher.py)
- **Keyword Formula**: Pairs of UID digits mod 26 $\to$ `"UYEAL"`.

```python
# 12. Vigenère Cipher (UID: 2024300089)
UID = 2024300089

def get_vig_key_from_uid(uid):
    u = str(uid)
    return "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))

def vigenere(text, key, decrypt=False):
    ans, j = "", 0
    for c in text:
        if c.isalpha():
            k = ord(key[j % len(key)].upper()) - 65
            if decrypt: k = -k
            base = 65 if c.isupper() else 97
            ans += chr((ord(c) - base + k) % 26 + base)
            j += 1
        else:
            ans += c
    return ans

uid_key = get_vig_key_from_uid(UID)
print(f"UID: {UID} -> Derived Keyword: '{uid_key}'")

text = input("Enter text (default 'ATTACKATDAWN'): ") or "ATTACKATDAWN"
key = (input(f"Enter keyword (default derived from UID = '{uid_key}'): ") or uid_key).upper()

enc = vigenere(text, key)
dec = vigenere(enc, key, decrypt=True)
print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 13. Playfair Cipher
- **File**: [`13_playfair_cipher.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/13_playfair_cipher.py)
- **Matrix Key**: Built from UID keyword `"UYEAL"`.

```python
# 13. Playfair Cipher (UID: 2024300089)
UID = 2024300089

def get_uid_keyword(uid):
    u = str(uid)
    return "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))

def make_matrix(key):
    letters = ""
    for c in key.upper().replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c.isalpha() and c not in letters:
            letters += c
    return [letters[i:i+5] for i in range(0, 25, 5)]

def playfair(text, matrix, decrypt=False):
    t = "".join(c for c in text.upper().replace("J", "I") if c.isalpha())
    if not decrypt:
        pairs, i = [], 0
        while i < len(t):
            a = t[i]
            if i + 1 < len(t):
                b = t[i+1]
                if a == b: b = "X"; i += 1
                else: i += 2
            else:
                b = "X"; i += 1
            pairs.append(a + b)
    else:
        pairs = [t[i:i+2] for i in range(0, len(t), 2)]

    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    step = -1 if decrypt else 1
    ans = ""
    for a, b in pairs:
        r1, c1 = pos[a]; r2, c2 = pos[b]
        if r1 == r2:
            ans += matrix[r1][(c1 + step) % 5] + matrix[r2][(c2 + step) % 5]
        elif c1 == c2:
            ans += matrix[(r1 + step) % 5][c1] + matrix[(r2 + step) % 5][c2]
        else:
            ans += matrix[r1][c2] + matrix[r2][c1]
    return ans

uid_key = get_uid_keyword(UID)
key = input(f"Enter key (default '{uid_key}'): ") or uid_key
text = input("Enter text (default 'INSTRUMENTS'): ") or "INSTRUMENTS"

mat = make_matrix(key)
enc = playfair(text, mat)
dec = playfair(enc, mat, decrypt=True)
print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 14. Hill Cipher (2×2)
- **File**: [`14_hill_cipher_2x2.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/14_hill_cipher_2x2.py)
- **Matrix Key**: `[[21, 24], [4, 1]]` (derived from UID pairs `[20, 24], [30, 00]` & fixed to $\det = 3$).
- **Inverse Matrix**: `[[9, 18], [16, 7]]` (computed in pure Python, NO numpy).

```python
# 14. Hill Cipher (2x2) (UID: 2024300089)
UID = 2024300089

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def get_hill2_key(uid):
    u = str(uid)
    g = [int(u[i:i+2]) for i in range(0, 8, 2)]
    K = [[g[0] % 26, g[1] % 26], [g[2] % 26, g[3] % 26]]
    tries = 0
    while gcd((K[0][0]*K[1][1] - K[0][1]*K[1][0]) % 26, 26) != 1:
        K[1][1] = (K[1][1] + 1) % 26
        tries += 1
        if tries % 26 == 0:
            K[0][0] = (K[0][0] + 1) % 26
    return K

def hill2_inverse(K):
    det = (K[0][0]*K[1][1] - K[0][1]*K[1][0]) % 26
    inv_det = pow(det, -1, 26)
    return [
        [(inv_det * K[1][1]) % 26, (-inv_det * K[0][1]) % 26],
        [(-inv_det * K[1][0]) % 26, (inv_det * K[0][0]) % 26]
    ]

def hill2(text, K):
    t = "".join(c for c in text.upper() if c.isalpha())
    if len(t) % 2: t += "X"
    ans = ""
    for i in range(0, len(t), 2):
        p1, p2 = ord(t[i]) - 65, ord(t[i+1]) - 65
        ans += chr((K[0][0]*p1 + K[0][1]*p2) % 26 + 65)
        ans += chr((K[1][0]*p1 + K[1][1]*p2) % 26 + 65)
    return ans

key = get_hill2_key(UID)
inv_key = hill2_inverse(key)
text = input("Enter text (default 'HELP'): ") or "HELP"

enc = hill2(text, key)
dec = hill2(enc, inv_key)
print(f"UID: {UID} -> Key Matrix: {key}")
print(f"Inverse Key Matrix: {inv_key}")
print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 15. Hill Cipher (3×3)
- **File**: [`15_hill_cipher_3x3.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/15_hill_cipher_3x3.py)
- **Logic**: Pure Python 3×3 matrix multiplication and cofactor inverse without numpy.

```python
# 15. Hill Cipher (3x3) (UID: 2024300089)
UID = 2024300089

def hill3(text, K):
    t = "".join(c for c in text.upper() if c.isalpha())
    while len(t) % 3: t += "X"
    ans = ""
    for i in range(0, len(t), 3):
        v = [ord(c) - 65 for c in t[i:i+3]]
        for row in K:
            ans += chr(sum(row[j]*v[j] for j in range(3)) % 26 + 65)
    return ans

def hill3_inverse(K):
    det = (K[0][0]*(K[1][1]*K[2][2] - K[1][2]*K[2][1])
         - K[0][1]*(K[1][0]*K[2][2] - K[1][2]*K[2][0])
         + K[0][2]*(K[1][0]*K[2][1] - K[1][1]*K[2][0])) % 26
    inv_det = pow(det, -1, 26)
    adj = [
        [(K[1][1]*K[2][2] - K[1][2]*K[2][1]) % 26, (K[0][2]*K[2][1] - K[0][1]*K[2][2]) % 26, (K[0][1]*K[1][2] - K[0][2]*K[1][1]) % 26],
        [(K[1][2]*K[2][0] - K[1][0]*K[2][2]) % 26, (K[0][0]*K[2][2] - K[0][2]*K[2][0]) % 26, (K[0][2]*K[1][0] - K[0][0]*K[1][2]) % 26],
        [(K[1][0]*K[2][1] - K[1][1]*K[2][0]) % 26, (K[0][1]*K[2][0] - K[0][0]*K[2][1]) % 26, (K[0][0]*K[1][1] - K[0][1]*K[1][0]) % 26]
    ]
    return [[(adj[r][c] * inv_det) % 26 for c in range(3)] for r in range(3)]

key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
inv_key = hill3_inverse(key)
text = input("Enter text (default 'ACT'): ") or "ACT"

enc = hill3(text, key)
dec = hill3(enc, inv_key)
print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 16. Rail Fence Cipher
- **File**: [`16_rail_fence_cipher.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/16_rail_fence_cipher.py)
- **Rails Formula**: $(\sum d_i \bmod 3) + 2 = (28 \bmod 3) + 2 = 3$ rails.

```python
# 16. Rail Fence Cipher (UID: 2024300089)
UID = 2024300089

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

uid_rails = (sum(int(d) for d in str(UID)) % 3) + 2  # 3
text = input("Enter text (default 'DEFENDTHEEASTWALL'): ") or "DEFENDTHEEASTWALL"
rails = int(input(f"Enter rails (default from UID = {uid_rails}): ") or uid_rails)

enc = rail_enc(text, rails)
dec = rail_dec(enc, rails)
print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 17. Columnar Transposition Cipher
- **File**: [`17_columnar_transposition.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/17_columnar_transposition.py)
- **Keyword**: `"UYEAL"` (from UID).

```python
# 17. Columnar Transposition Cipher (UID: 2024300089)
UID = 2024300089

def get_uid_key(uid):
    u = str(uid)
    return "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))

def col_enc(text, key):
    n = len(key)
    while len(text) % n: text += "X"
    order = sorted(range(n), key=lambda i: key[i])
    return "".join(text[c::n] for c in order)

def col_dec(cipher, key):
    n = len(key)
    rows = len(cipher) // n
    order = sorted(range(n), key=lambda i: key[i])
    cols = {c: cipher[idx * rows:(idx + 1) * rows] for idx, c in enumerate(order)}
    return "".join(cols[c][r] for r in range(rows) for c in range(n))

uid_key = get_uid_key(UID)  # "UYEAL"
text = input("Enter text (default 'HELLOFRIEND'): ") or "HELLOFRIEND"
key = (input(f"Enter key word (default '{uid_key}'): ") or uid_key).upper()

enc = col_enc(text, key)
dec = col_dec(enc, key)
print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 18. Vernam Cipher / One-Time Pad
- **File**: [`18_vernam_cipher.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/18_vernam_cipher.py)
- **Key**: Matches plaintext length based on UID keyword `"UYEAL"`.

```python
# 18. Vernam Cipher / OTP (UID: 2024300089)
UID = 2024300089

def vernam(text, key, decrypt=False):
    ans = ""
    for a, b in zip(text.upper(), key.upper()):
        p, k = ord(a) - 65, ord(b) - 65
        x = (p - k if decrypt else p + k) % 26
        ans += chr(x + 65)
    return ans

u = str(UID)
uid_keyword = "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))
text = (input("Enter text (default 'HELLO'): ") or "HELLO").upper()
def_key = (uid_keyword * ((len(text) // len(uid_keyword)) + 1))[:len(text)]
key = (input(f"Enter key of length {len(text)} (default '{def_key}'): ") or def_key).upper()

if len(text) != len(key):
    print("Error: Key length must match text length!")
else:
    enc = vernam(text, key)
    dec = vernam(enc, key, decrypt=True)
    print("Encrypted:", enc)
    print("Decrypted:", dec)
```

---

### 19. Autokey Cipher
- **File**: [`19_autokey_cipher.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/19_autokey_cipher.py)
- **Primer Key**: `"UYEAL"` (from UID).

```python
# 19. Autokey Cipher (UID: 2024300089)
UID = 2024300089

def get_uid_primer(uid):
    u = str(uid)
    return "".join(chr(int(u[i:i+2]) % 26 + 65) for i in range(0, 10, 2))

def autokey_enc(text, key):
    text = text.upper()
    full_key = (key + text).upper()
    return "".join(chr((ord(c) - 65 + ord(full_key[i]) - 65) % 26 + 65) for i, c in enumerate(text))

def autokey_dec(cipher, key):
    cipher = cipher.upper()
    plain, full_key = "", key.upper()
    for i, c in enumerate(cipher):
        p = (ord(c) - 65 - (ord(full_key[i]) - 65)) % 26
        ch = chr(p + 65)
        plain += ch
        full_key += ch
    return plain

uid_primer = get_uid_primer(UID)  # "UYEAL"
text = input("Enter text (default 'ATTACKATDAWN'): ") or "ATTACKATDAWN"
key = (input(f"Enter primer key (default '{uid_primer}'): ") or uid_primer).upper()

enc = autokey_enc(text, key)
dec = autokey_dec(enc, key)
print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

## 3. Asymmetric Ciphers (5 Programs)

### 20. RSA Encryption and Decryption
- **File**: [`20_rsa_cipher.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/20_rsa_cipher.py)
- **Message**: $M = 28$ ($\sum d_i$). $p = 17, q = 11, n = 187, e = 7, d = 23$.

```python
# 20. RSA Encryption and Decryption (UID: 2024300089)
UID = 2024300089

p, q = 17, 11
n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = pow(e, -1, phi)

def_m = sum(int(d) for d in str(UID))  # 28
print(f"UID: {UID} | Public Key (e, n): {(e, n)} | Private Key (d, n): {(d, n)}")

m = int(input(f"Enter message number (0 < m < {n}, default sum of digits = {def_m}): ") or def_m)
c = pow(m, e, n)
dec = pow(c, d, n)

print("Encrypted Ciphertext:", c)
print("Decrypted Message:   ", dec)
print("Verification Match:  ", dec == m)
```

---

### 21. ElGamal Encryption and Decryption
- **File**: [`21_elgamal_cipher.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/21_elgamal_cipher.py)
- **Private Key**: $x = (\sum d_i \bmod 10) + 2 = 10$.

```python
# 21. ElGamal Encryption and Decryption (UID: 2024300089)
UID = 2024300089

p, g = 23, 5
x = sum(int(d) for d in str(UID)) % 10 + 2  # 10
y = pow(g, x, p)

m = int(input("Enter message number (m < 23, default 10): ") or 10)
k = 7

# Encryption
c1 = pow(g, k, p)
c2 = (m * pow(y, k, p)) % p

# Decryption
s = pow(c1, x, p)
dec = (c2 * pow(s, -1, p)) % p

print(f"UID: {UID} | Private x = {x}, Public y = {y}")
print("Ciphertext (c1, c2):", (c1, c2))
print("Decrypted Message:  ", dec)
print("Verification Match: ", dec == m)
```

---

### 22. Diffie–Hellman Key Exchange
- **File**: [`22_diffie_hellman.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/22_diffie_hellman.py)
- **Alice Private Key**: $a = 10$ (derived from UID).

```python
# 22. Diffie-Hellman Key Exchange (UID: 2024300089)
UID = 2024300089

p, g = 23, 5
def_a = sum(int(d) for d in str(UID)) % 10 + 2  # 10
def_b = 15

a = int(input(f"Enter Alice private key a (default from UID = {def_a}): ") or def_a)
b = int(input(f"Enter Bob private key b (default {def_b}): ") or def_b)

A = pow(g, a, p)
B = pow(g, b, p)

keyA = pow(B, a, p)
keyB = pow(A, b, p)

print("Alice Computed Shared Key:", keyA)
print("Bob Computed Shared Key:  ", keyB)
print("Shared Keys Match:        ", keyA == keyB)
```

---

### 23. ECC – Elliptic Curve Diffie–Hellman (ECDH)
- **File**: [`23_ecc_ecdh.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/23_ecc_ecdh.py)
- **Curve**: $y^2 \equiv x^3 + 2x + 2 \pmod{17}$, $G = (5, 1)$, order $n = 19$.
- **Alice Private**: $d_A = (28 \bmod 18) + 1 = 11$.

```python
# 23. ECC - Elliptic Curve Diffie-Hellman (ECDH) (UID: 2024300089)
UID = 2024300089

p, a, b = 17, 2, 2
G = (5, 1); n = 19; O = None

def ec_add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return O
    if P == Q:
        m = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    else:
        m = ((y2 - y1) * pow((x2 - x1) % p, -1, p)) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def ec_mul(k, P):
    R = O
    while k > 0:
        if k % 2: R = ec_add(R, P)
        P = ec_add(P, P)
        k //= 2
    return R

def_alice = sum(int(d) for d in str(UID)) % (n - 1) + 1  # 11
def_bob = 7

alice_priv = int(input(f"Alice private key (default from UID = {def_alice}): ") or def_alice)
bob_priv = int(input(f"Bob private key (default {def_bob}): ") or def_bob)

pubA = ec_mul(alice_priv, G)
pubB = ec_mul(bob_priv, G)

sharedA = ec_mul(alice_priv, pubB)
sharedB = ec_mul(bob_priv, pubA)

print("Alice Shared Key Point:", sharedA)
print("Bob Shared Key Point:  ", sharedB)
print("Shared Keys Match:     ", sharedA == sharedB)
```

---

### 24. EC-ElGamal Encryption and Decryption
- **File**: [`24_ec_elgamal.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/24_ec_elgamal.py)
- **Receiver Key**: $d = 11$ (from UID). Message point $M = 2G$.

```python
# 24. EC-ElGamal Encryption and Decryption (UID: 2024300089)
UID = 2024300089

p, a, b = 17, 2, 2
G = (5, 1); n = 19; O = None

def ec_add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return O
    if P == Q:
        m = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    else:
        m = ((y2 - y1) * pow((x2 - x1) % p, -1, p)) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def ec_mul(k, P):
    R = O
    while k > 0:
        if k % 2: R = ec_add(R, P)
        P = ec_add(P, P)
        k //= 2
    return R

d = sum(int(c) for c in str(UID)) % (n - 1) + 1  # 11
Q = ec_mul(d, G)
M = ec_mul(2, G)
k = 3

C1 = ec_mul(k, G)
C2 = ec_add(M, ec_mul(k, Q))

S = ec_mul(d, C1)
neg_S = (S[0], (-S[1]) % p)
dec = ec_add(C2, neg_S)

print(f"UID: {UID} | Receiver Private Key d = {d}")
print("Original Message Point M: ", M)
print("Encrypted Ciphertext (C1):", C1)
print("Encrypted Ciphertext (C2):", C2)
print("Decrypted Message Point:  ", dec)
print("Verification Match:       ", dec == M)
```

---

## 4. Digital Signatures (4 Programs)

### 25. RSA Digital Signature
- **File**: [`25_rsa_signature.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/25_rsa_signature.py)
- **Message**: `"UID: 2024300089"` hashed using `hashlib.sha256`.

```python
# 25. RSA Digital Signature (UID: 2024300089)
import hashlib

UID = 2024300089

p, q = 17, 11
n = p * q
phi = (p - 1) * (q - 1)
e = 7
d = pow(e, -1, phi)

def_msg = f"UID: {UID}"
msg = input(f"Enter message to sign (default '{def_msg}'): ") or def_msg

h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % n
sig = pow(h, d, n)
verified_h = pow(sig, e, n)

print("Message:           ", msg)
print("SHA-256 Hash mod n:", h)
print("Signature:         ", sig)
print("Verification Result:", verified_h == h)
```

---

### 25b. RSA-PSS (Probabilistic Signature Scheme)
- **File**: [`25b_rsa_pss.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/25b_rsa_pss.py)
- **Concept**: Unlike deterministic textbook RSA, PSS introduces a **Salt** (probabilistic) and an **MGF** (Mask Generation Function) based on `hashlib.sha256`.
- **Parameters**: $p = 61, q = 53, n = 3233, e = 17, d = 2753$, Message: `'HELLO'`.

```python
# RSA-PSS (Probabilistic Signature Scheme) (UID: 2024300089)
import hashlib

p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi)

msg = "HELLO"
UID = 2024300089

def mgf(seed_int, length=2):
    return hashlib.sha256(f"MGF:{seed_int}".encode()).digest()[:length]

# Step 1: Base message hash
m_hash = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % n

# Step 2: Salt (derived from UID or random: 29)
salt = (sum(int(c) for c in str(UID)) % 50) + 1

# Step 3: Compute H = Hash(m_hash || salt) mod n
H = int(hashlib.sha256(f"{m_hash}:{salt}".encode()).hexdigest(), 16) % n

# Step 4: Mask the salt using MGF(H)
mask = int.from_bytes(mgf(H), "big") % 100
masked_salt = salt ^ mask

# Step 5: Sign the PSS hash H
pss_sig = pow(H, d, n)

# --- VERIFICATION ---
recovered_H = pow(pss_sig, e, n)
verifier_mask = int.from_bytes(mgf(recovered_H), "big") % 100
recovered_salt = masked_salt ^ verifier_mask
expected_H = int(hashlib.sha256(f"{m_hash}:{recovered_salt}".encode()).hexdigest(), 16) % n

print("PSS Signature:  ", pss_sig)
print("Masked Salt:    ", masked_salt)
print("Recovered Salt: ", recovered_salt, f"(matches: {recovered_salt == salt})")
print("Verified:       ", recovered_H == expected_H)
```

---

### 26. Digital Signature Algorithm (DSA)
- **File**: [`26_dsa_signature.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/26_dsa_signature.py)
- **Parameters**: $p = 23, q = 11, g = 4$. Private key $x = 9$ (from UID). Message: `"UID: 2024300089"`.

```python
# 26. Digital Signature Algorithm (DSA) (UID: 2024300089)
import hashlib

UID = 2024300089

p, q, g = 23, 11, 4
x = sum(int(d) for d in str(UID)) % (q - 1) + 1  # 9
y = pow(g, x, p)

def_msg = f"UID: {UID}"
msg = input(f"Enter message to sign (default '{def_msg}'): ") or def_msg

h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % q or 1
k = 2

r = pow(g, k, p) % q
s = (pow(k, -1, q) * (h + x * r)) % q

w = pow(s, -1, q)
u1 = (h * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

print(f"UID: {UID} | Private x = {x}, Public y = {y}")
print(f"Signature: (r = {r}, s = {s})")
print("Verification Result:", v == r)
```

---

### 27. ECDSA (Elliptic Curve Digital Signature Algorithm)
- **File**: [`27_ecdsa_signature.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/27_ecdsa_signature.py)
- **Curve**: $y^2 \equiv x^3 + 2x + 2 \pmod{17}$, $G = (5, 1)$, order $n = 19$. Private key $d = 11$. Message: `"UID: 2024300089"`.

```python
# 27. ECDSA (UID: 2024300089)
import hashlib

UID = 2024300089

p, a, b = 17, 2, 2
G = (5, 1); n = 19; O = None

def ec_add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0: return O
    if P == Q:
        m = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    else:
        m = ((y2 - y1) * pow((x2 - x1) % p, -1, p)) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def ec_mul(k, P):
    R = O
    while k > 0:
        if k % 2: R = ec_add(R, P)
        P = ec_add(P, P)
        k //= 2
    return R

d = sum(int(c) for c in str(UID)) % (n - 1) + 1  # 11
Q = ec_mul(d, G)

def_msg = f"UID: {UID}"
msg = input(f"Enter message to sign (default '{def_msg}'): ") or def_msg

h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % n or 1
k = 3

R = ec_mul(k, G)
r = R[0] % n
s = (pow(k, -1, n) * (h + r * d)) % n

w = pow(s, -1, n)
u1 = (h * w) % n
u2 = (r * w) % n
P_ver = ec_add(ec_mul(u1, G), ec_mul(u2, Q))

valid = P_ver is not None and (P_ver[0] % n == r)
print(f"UID: {UID} | Private d = {d}, Public Q = {Q}")
print(f"Signature: (r = {r}, s = {s})")
print("Verification Result:", valid)
```

---

### 28. ElGamal Digital Signature
- **File**: [`28_elgamal_signature.py`](file:///d:/Desktop/0_For%20immediate%20use/CNS/programs_uid_2024300089/28_elgamal_signature.py)
- **Parameters**: $p = 23, g = 5$. Private key $x = 10$. Message: `"UID: 2024300089"`.
- Zero `math.gcd` – custom `gcd(a, b)` and `hashlib` only.

```python
# 28. ElGamal Digital Signature (UID: 2024300089)
import hashlib

UID = 2024300089

def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

p, g = 23, 5
x = sum(int(d) for d in str(UID)) % 10 + 2  # 10
y = pow(g, x, p)

def_msg = f"UID: {UID}"
msg = input(f"Enter message to sign (default '{def_msg}'): ") or def_msg

h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % (p - 1) or 1
k = 7
assert gcd(k, p - 1) == 1

# Signing
r = pow(g, k, p)
s = ((h - x * r) * pow(k, -1, p - 1)) % (p - 1)

# Verification: g^h = y^r * r^s (mod p)
left = pow(g, h, p)
right = (pow(y, r, p) * pow(r, s, p)) % p

print(f"UID: {UID} | Private x = {x}, Public y = {y}")
print(f"Signature: (r = {r}, s = {s})")
print("Verification Result:", left == right)
```

