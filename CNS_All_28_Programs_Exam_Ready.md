# CNS Lab (Cryptography and Network Security) – All 28 Programs
### Exam-Ready, Simple, Clean Python 3 Implementations
> **Strict Compliance**:
> - **ZERO external libraries**: No `numpy`, No `math` (`gcd` is written from scratch in pure Python).
> - **Standard hashing library**: `hashlib` is used exclusively for standard cryptographic hashing in Digital Signatures.
> - **Interactive & Standalone**: Every program runs directly with sensible defaults if you press Enter.

---

## Table of Contents
- **1. Number Theory**
  1. [Fermat Primality Test](#1-fermat-primality-test)
  2. [Euler Primality Test (Euler–Jacobi)](#2-euler-primality-test-eulerjacobi)
  3. [Miller–Rabin Primality Test](#3-millerrabin-primality-test)
  4. [Euclidean Algorithm (GCD)](#4-euclidean-algorithm-gcd)
  5. [Extended Euclidean Algorithm (Modular Inverse)](#5-extended-euclidean-algorithm-modular-inverse)
  6. [Euler's Totient Function](#6-eulers-totient-function)
  7. [Smallest Primitive Root](#7-smallest-primitive-root)
  8. [Discrete Logarithm](#8-discrete-logarithm)
  9. [Square-and-Multiply (Fast Modular Exponentiation)](#9-square-and-multiply-fast-modular-exponentiation)
- **2. Symmetric Ciphers**
  10. [Caesar Cipher](#10-caesar-cipher)
  11. [Monoalphabetic Substitution Cipher](#11-monoalphabetic-substitution-cipher)
  12. [Vigenère Cipher](#12-vigenère-cipher)
  13. [Playfair Cipher](#13-playfair-cipher)
  14. [Hill Cipher (2×2)](#14-hill-cipher-22)
  15. [Hill Cipher (3×3)](#15-hill-cipher-33)
  16. [Rail Fence Cipher](#16-rail-fence-cipher)
  17. [Columnar Transposition Cipher](#17-columnar-transposition-cipher)
  18. [Vernam Cipher / One-Time Pad](#18-vernam-cipher--one-time-pad)
  19. [Autokey Cipher](#19-autokey-cipher)
- **3. Asymmetric Ciphers**
  20. [RSA Encryption and Decryption](#20-rsa-encryption-and-decryption)
  21. [ElGamal Encryption and Decryption](#21-elgamal-encryption-and-decryption)
  22. [Diffie–Hellman Key Exchange](#22-diffiehellman-key-exchange)
  23. [ECC – Elliptic Curve Diffie–Hellman (ECDH)](#23-ecc--elliptic-curve-diffiehellman-ecdh)
  24. [EC-ElGamal Encryption and Decryption](#24-ec-elgamal-encryption-and-decryption)
- **4. Digital Signatures**
  25. [RSA Digital Signature](#25-rsa-digital-signature)
  26. [Digital Signature Algorithm (DSA)](#26-digital-signature-algorithm-dsa)
  27. [ECDSA (Elliptic Curve Digital Signature Algorithm)](#27-ecdsa-elliptic-curve-digital-signature-algorithm)
  28. [ElGamal Digital Signature](#28-elgamal-digital-signature)

---

# 1. Number Theory (9 Programs)

### 1. Fermat Primality Test
**Mathematical Principle:**
Fermat's Little Theorem states that if $p$ is prime and $\gcd(a, p) = 1$, then:
$$a^{p-1} \equiv 1 \pmod p$$
If $a^{p-1} \not\equiv 1 \pmod p$ for any base $a$, $p$ is composite.

```python
# 1. Fermat Primality Test (Zero imports)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def fermat(n, bases=[2, 3, 5]):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for a in bases:
        if a >= n:
            continue
        if gcd(a, n) != 1 or pow(a, n - 1, n) != 1:
            return False
    return True

n = int(input("Enter number to test (default 17): ") or 17)
print(f"{n} is {'Probably Prime' if fermat(n) else 'Composite'}")
```

---

### 2. Euler Primality Test (Euler–Jacobi)
**Mathematical Principle:**
The Euler–Jacobi test (Solovay–Strassen) checks whether:
$$a^{\frac{n-1}{2}} \equiv \left(\frac{a}{n}\right) \pmod n$$
where $\left(\frac{a}{n}\right)$ is the Jacobi symbol.

```python
# 2. Euler Primality Test (Zero imports)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def jacobi(a, n):
    ans = 1
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                ans = -ans
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            ans = -ans
        a %= n
    return ans if n == 1 else 0

def euler(n, bases=[2, 3, 5]):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for a in bases:
        if a >= n:
            continue
        if gcd(a, n) != 1:
            return False
        if pow(a, (n - 1) // 2, n) != jacobi(a, n) % n:
            return False
    return True

n = int(input("Enter number to test (default 17): ") or 17)
print(f"{n} is {'Probably Prime' if euler(n) else 'Composite'}")
```

---

### 3. Miller–Rabin Primality Test
**Mathematical Principle:**
Write $n - 1 = 2^s \cdot d$ where $d$ is odd. For base $a$, calculate $x = a^d \pmod n$.
If $x = 1$ or $x = n - 1$, $n$ passes for base $a$. Otherwise, square $x$ up to $s-1$ times. If $x$ becomes $n - 1$, it passes; otherwise, $n$ is composite.

```python
# 3. Miller-Rabin Primality Test (Zero imports)
def miller_rabin(n, bases=[2, 3, 5]):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in bases:
        if a >= n:
            continue
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

n = int(input("Enter number to test (default 17): ") or 17)
print(f"{n} is {'Probably Prime' if miller_rabin(n) else 'Composite'}")
```

---

### 4. Euclidean Algorithm (GCD)
**Mathematical Principle:**
Repeated division remainder: $\gcd(a, b) = \gcd(b, a \bmod b)$ until remainder becomes $0$.

```python
# 4. Euclidean Algorithm (GCD) (Zero imports)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter a (default 48): ") or 48)
b = int(input("Enter b (default 18): ") or 18)
print(f"GCD({a}, {b}) = {gcd(a, b)}")
```

---

### 5. Extended Euclidean Algorithm (Modular Inverse)
**Mathematical Principle:**
Computes integers $x, y$ such that:
$$a \cdot x + b \cdot y = \gcd(a, b)$$
If $\gcd(a, m) = 1$, then $x \pmod m$ is the modular multiplicative inverse $a^{-1} \pmod m$.

```python
# 5. Extended Euclidean Algorithm (Modular Inverse) (Zero imports)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

a = int(input("Enter a (default 7): ") or 7)
m = int(input("Enter modulus m (default 26): ") or 26)

g, x, y = extended_gcd(a, m)
if g == 1:
    inv = x % m
    print(f"gcd({a}, {m}) = {g}")
    print(f"Modular Inverse of {a} mod {m} = {inv}")
    print(f"Verification: ({a} * {inv}) % {m} = {(a * inv) % m}")
else:
    print(f"Inverse does not exist because gcd({a}, {m}) = {g} != 1")
```

---

### 6. Euler's Totient Function
**Mathematical Principle:**
$\phi(n)$ is the count of numbers $1 \le i \le n$ coprime to $n$ ($\gcd(i, n) = 1$).

```python
# 6. Euler's Totient Function (Zero imports - NO math.gcd)
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

n = int(input("Enter n (default 9): ") or 9)
print(f"phi({n}) = {phi(n)}")
```

---

### 7. Smallest Primitive Root
**Mathematical Principle:**
$g$ is a primitive root modulo $p$ if $\{g^1, g^2, \dots, g^{p-1}\} \pmod p$ generates all non-zero residue classes modulo $p$.

```python
# 7. Smallest Primitive Root (Zero imports)
def primitive_root(p):
    for g in range(2, p):
        values = set()
        for i in range(1, p):
            values.add(pow(g, i, p))
        if len(values) == p - 1:
            return g
    return None

p = int(input("Enter prime p (default 7): ") or 7)
g = primitive_root(p)
print(f"Smallest primitive root modulo {p} is {g}")
```

---

### 8. Discrete Logarithm
**Mathematical Principle:**
Given $g^x \equiv h \pmod p$, find integer $x$ in $0 \le x < p$.

```python
# 8. Discrete Logarithm (Zero imports)
def discrete_log(g, h, p):
    for x in range(p):
        if pow(g, x, p) == h:
            return x
    return None

g = int(input("Enter base g (default 5): ") or 5)
h = int(input("Enter result h (default 8): ") or 8)
p = int(input("Enter modulus p (default 23): ") or 23)

x = discrete_log(g, h, p)
if x is not None:
    print(f"Discrete log x = {x}  (since {g}^{x} mod {p} = {h})")
else:
    print("No solution found.")
```

---

### 9. Square-and-Multiply (Fast Modular Exponentiation)
**Mathematical Principle:**
Computes $a^b \pmod m$ in $O(\log b)$ by squaring the base on each step and multiplying by $a$ when the current binary bit is $1$.

```python
# 9. Square-and-Multiply (Fast Modular Exponentiation) (Zero imports)
def square_and_multiply(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

a = int(input("Enter base a (default 3): ") or 3)
b = int(input("Enter exponent b (default 13): ") or 13)
m = int(input("Enter modulus m (default 17): ") or 17)

ans = square_and_multiply(a, b, m)
print(f"{a}^{b} mod {m} = {ans}")
print(f"Built-in pow() verification: {pow(a, b, m)}")
```

---

# 2. Symmetric Ciphers (10 Programs)

### 10. Caesar Cipher
**Mathematical Principle:**
$$C \equiv (P + K) \pmod{26}, \quad P \equiv (C - K) \pmod{26}$$

```python
# 10. Caesar Cipher (Zero imports)
def caesar(text, key):
    ans = ""
    for c in text:
        if c.isupper():
            ans += chr((ord(c) - 65 + key) % 26 + 65)
        elif c.islower():
            ans += chr((ord(c) - 97 + key) % 26 + 97)
        else:
            ans += c
    return ans

text = input("Enter text (default 'HELLO'): ") or "HELLO"
key = int(input("Enter key shift (default 3): ") or 3)

enc = caesar(text, key)
dec = caesar(enc, -key)

print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 11. Monoalphabetic Substitution Cipher
**Mathematical Principle:**
Bijective mapping between the standard alphabet and a 26-character permuted key.

```python
# 11. Monoalphabetic Substitution Cipher (Zero imports)
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

text = (input("Enter text (default 'ATTACK'): ") or "ATTACK").upper()

# Encryption
enc = "".join(key[abc.index(c)] if c in abc else c for c in text)

# Decryption
dec = "".join(abc[key.index(c)] if c in key else c for c in enc)

print("Key:      ", key)
print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 12. Vigenère Cipher
**Mathematical Principle:**
Polyalphabetic key repetition:
$$C_i \equiv (P_i + K_{i \bmod m}) \pmod{26}, \quad P_i \equiv (C_i - K_{i \bmod m}) \pmod{26}$$

```python
# 12. Vigenère Cipher (Zero imports)
def vigenere(text, key, decrypt=False):
    ans, j = "", 0
    for c in text:
        if c.isalpha():
            k = ord(key[j % len(key)].upper()) - 65
            if decrypt:
                k = -k
            base = 65 if c.isupper() else 97
            ans += chr((ord(c) - base + k) % 26 + base)
            j += 1
        else:
            ans += c
    return ans

text = input("Enter text (default 'ATTACKATDAWN'): ") or "ATTACKATDAWN"
key = input("Enter keyword (default 'LEMON'): ") or "LEMON"

enc = vigenere(text, key)
dec = vigenere(enc, key, decrypt=True)

print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 13. Playfair Cipher
**Rules:**
1. Form $5 \times 5$ matrix combining I/J.
2. Group plaintext into digraphs (fill repeated letters with 'X', pad odd length with 'X').
3. Same Row: Shift right (enc) / left (dec) mod 5.
4. Same Column: Shift down (enc) / up (dec) mod 5.
5. Rectangle: Swap column indices.

```python
# 13. Playfair Cipher (Zero imports)
def make_matrix(key):
    letters = ""
    for c in key.upper().replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c.isalpha() and c not in letters:
            letters += c
    return [letters[i:i+5] for i in range(0, 25, 5)]

def playfair(text, matrix, decrypt=False):
    t = "".join(c for c in text.upper().replace("J", "I") if c.isalpha())
    if not decrypt:
        pairs = []
        i = 0
        while i < len(t):
            a = t[i]
            if i + 1 < len(t):
                b = t[i+1]
                if a == b:
                    b = "X"
                    i += 1
                else:
                    i += 2
            else:
                b = "X"
                i += 1
            pairs.append(a + b)
    else:
        pairs = [t[i:i+2] for i in range(0, len(t), 2)]

    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    step = -1 if decrypt else 1
    ans = ""

    for a, b in pairs:
        r1, c1 = pos[a]
        r2, c2 = pos[b]
        if r1 == r2:
            ans += matrix[r1][(c1 + step) % 5] + matrix[r2][(c2 + step) % 5]
        elif c1 == c2:
            ans += matrix[(r1 + step) % 5][c1] + matrix[(r2 + step) % 5][c2]
        else:
            ans += matrix[r1][c2] + matrix[r2][c1]
    return ans

key = input("Enter key (default 'MONARCHY'): ") or "MONARCHY"
text = input("Enter text (default 'INSTRUMENTS'): ") or "INSTRUMENTS"

matrix = make_matrix(key)
print("Matrix:")
for row in matrix:
    print(" ".join(row))

enc = playfair(text, matrix)
dec = playfair(enc, matrix, decrypt=True)

print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 14. Hill Cipher (2×2)
**Mathematical Principle:**
$C = P \cdot K \pmod{26}$, $P = C \cdot K^{-1} \pmod{26}$.
Adjugate inverse: $K^{-1} = \det(K)^{-1} \cdot \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \pmod{26}$.

```python
# 14. Hill Cipher 2x2 (Zero imports - NO numpy)
def hill2(text, K):
    t = "".join(c for c in text.upper() if c.isalpha())
    if len(t) % 2:
        t += "X"
    ans = ""
    for i in range(0, len(t), 2):
        p1, p2 = ord(t[i]) - 65, ord(t[i+1]) - 65
        ans += chr((K[0][0]*p1 + K[0][1]*p2) % 26 + 65)
        ans += chr((K[1][0]*p1 + K[1][1]*p2) % 26 + 65)
    return ans

def hill2_inverse(K):
    det = (K[0][0]*K[1][1] - K[0][1]*K[1][0]) % 26
    inv_det = pow(det, -1, 26)
    return [
        [(inv_det * K[1][1]) % 26, (-inv_det * K[0][1]) % 26],
        [(-inv_det * K[1][0]) % 26, (inv_det * K[0][0]) % 26]
    ]

key = [[3, 3], [2, 5]]
inv_key = hill2_inverse(key)

text = input("Enter text (default 'HELP'): ") or "HELP"

enc = hill2(text, key)
dec = hill2(enc, inv_key)

print("Key Matrix:        ", key)
print("Inverse Key Matrix:", inv_key)
print("Encrypted:         ", enc)
print("Decrypted:         ", dec)
```

---

### 15. Hill Cipher (3×3)
**Mathematical Principle:**
$C = P \cdot K \pmod{26}$, $P = C \cdot K^{-1} \pmod{26}$.
$3 \times 3$ determinant & cofactor matrix inverse calculated in pure Python (NO numpy).

```python
# 15. Hill Cipher 3x3 (Zero imports - NO numpy)
def hill3(text, K):
    t = "".join(c for c in text.upper() if c.isalpha())
    while len(t) % 3:
        t += "X"
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

key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]
inv_key = hill3_inverse(key)

text = input("Enter text (default 'ACT'): ") or "ACT"

enc = hill3(text, key)
dec = hill3(enc, inv_key)

print("Key Matrix:        ", key)
print("Inverse Key Matrix:", inv_key)
print("Encrypted:         ", enc)
print("Decrypted:         ", dec)
```

---

### 16. Rail Fence Cipher
**Mathematical Principle:**
Write text in a zigzag pattern of $n$ rails, read out row-wise.

```python
# 16. Rail Fence Cipher (Zero imports)
def rail_enc(text, rails):
    rows = ["" for _ in range(rails)]
    r, step = 0, 1
    for c in text:
        rows[r] += c
        if r == 0:
            step = 1
        elif r == rails - 1:
            step = -1
        r += step
    return "".join(rows)

def rail_dec(cipher, rails):
    pattern = []
    r, step = 0, 1
    for _ in cipher:
        pattern.append(r)
        if r == 0:
            step = 1
        elif r == rails - 1:
            step = -1
        r += step

    res = [""] * len(cipher)
    idx = 0
    for rail_idx in range(rails):
        for pos, p_rail in enumerate(pattern):
            if p_rail == rail_idx:
                res[pos] = cipher[idx]
                idx += 1
    return "".join(res)

text = input("Enter text (default 'DEFENDTHEEASTWALL'): ") or "DEFENDTHEEASTWALL"
rails = int(input("Enter number of rails (default 3): ") or 3)

enc = rail_enc(text, rails)
dec = rail_dec(enc, rails)

print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 17. Columnar Transposition Cipher
**Mathematical Principle:**
Arrange text into a grid whose width is the length of the key. Read out columns according to the alphabetical order of the key characters.

```python
# 17. Columnar Transposition Cipher (Zero imports)
def col_enc(text, key):
    n = len(key)
    while len(text) % n:
        text += "X"
    order = sorted(range(n), key=lambda i: key[i])
    return "".join(text[c::n] for c in order)

def col_dec(cipher, key):
    n = len(key)
    rows = len(cipher) // n
    order = sorted(range(n), key=lambda i: key[i])
    cols = {}
    for idx, c in enumerate(order):
        cols[c] = cipher[idx * rows:(idx + 1) * rows]
    return "".join(cols[c][r] for r in range(rows) for c in range(n))

text = input("Enter text (default 'HELLOFRIEND'): ") or "HELLOFRIEND"
key = input("Enter key word (default 'HACK'): ") or "HACK"

enc = col_enc(text, key)
dec = col_dec(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

### 18. Vernam Cipher / One-Time Pad
**Mathematical Principle:**
Key length equals message length:
$$C_i \equiv (P_i + K_i) \pmod{26}, \quad P_i \equiv (C_i - K_i) \pmod{26}$$

```python
# 18. Vernam Cipher / OTP (Zero imports)
def vernam(text, key, decrypt=False):
    ans = ""
    for a, b in zip(text.upper(), key.upper()):
        p = ord(a) - 65
        k = ord(b) - 65
        x = (p - k if decrypt else p + k) % 26
        ans += chr(x + 65)
    return ans

text = input("Enter text (default 'HELLO'): ") or "HELLO"
key = input("Enter key (same length, default 'XMCKL'): ") or "XMCKL"

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
**Mathematical Principle:**
The keystream begins with a keyword and is extended by appending the plaintext itself:
$$C_i \equiv (P_i + K_i) \pmod{26}, \quad P_i \equiv (C_i - K_i) \pmod{26}$$

```python
# 19. Autokey Cipher (Zero imports)
def autokey_enc(text, key):
    text = text.upper()
    full_key = (key + text).upper()
    ans = ""
    for i, c in enumerate(text):
        x = (ord(c) - 65 + ord(full_key[i]) - 65) % 26
        ans += chr(x + 65)
    return ans

def autokey_dec(cipher, key):
    cipher = cipher.upper()
    plain = ""
    full_key = key.upper()
    for i, c in enumerate(cipher):
        p = (ord(c) - 65 - (ord(full_key[i]) - 65)) % 26
        ch = chr(p + 65)
        plain += ch
        full_key += ch
    return plain

text = input("Enter text (default 'ATTACKATDAWN'): ") or "ATTACKATDAWN"
key = input("Enter primer key (default 'QUEEN'): ") or "QUEEN"

enc = autokey_enc(text, key)
dec = autokey_dec(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
```

---

# 3. Asymmetric Ciphers (5 Programs)

### 20. RSA Encryption and Decryption
**Mathematical Principle:**
- Key generation: $n = p \cdot q$, $\phi = (p-1)(q-1)$. Public key: $(e, n)$, Private key: $(d, n)$ where $e \cdot d \equiv 1 \pmod \phi$.
- Encryption: $C = M^e \bmod n$
- Decryption: $M = C^d \bmod n$

```python
# 20. RSA Encryption and Decryption (Zero imports)
p = 17
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = pow(e, -1, phi)

print("Public Key: ", (e, n))
print("Private Key:", (d, n))

m = int(input(f"Enter message number (0 < m < {n}, default 9): ") or 9)

c = pow(m, e, n)
dec = pow(c, d, n)

print("Encrypted Ciphertext:", c)
print("Decrypted Message:   ", dec)
```

---

### 21. ElGamal Encryption and Decryption
**Mathematical Principle:**
- Public key: $(p, g, y)$ where $y = g^x \bmod p$. Private key: $x$.
- Ephemeral key $k$.
- Encryption: $c_1 = g^k \bmod p, \quad c_2 = (M \cdot y^k) \bmod p$.
- Decryption: Shared secret $s = c_1^x \bmod p, \quad M = (c_2 \cdot s^{-1}) \bmod p$.

```python
# 21. ElGamal Encryption and Decryption (Zero imports)
p = 23
g = 5

x = 6               # Private key
y = pow(g, x, p)    # Public key

print(f"Public Parameters: p = {p}, g = {g}, y = {y}")
print(f"Private Key: x = {x}")

m = int(input("Enter message number (m < 23, default 10): ") or 10)
k = 7               # Ephemeral key

# Encryption
c1 = pow(g, k, p)
c2 = (m * pow(y, k, p)) % p

# Decryption
s = pow(c1, x, p)
dec = (c2 * pow(s, -1, p)) % p

print("Ciphertext (c1, c2):", (c1, c2))
print("Decrypted Message:  ", dec)
```

---

### 22. Diffie–Hellman Key Exchange
**Mathematical Principle:**
- Public: Prime $p$, generator $g$.
- Alice chooses private $a$, sends $A = g^a \bmod p$.
- Bob chooses private $b$, sends $B = g^b \bmod p$.
- Alice computes $K_A = B^a \bmod p$; Bob computes $K_B = A^b \bmod p$.
- $K_A \equiv K_B \equiv g^{ab} \pmod p$.

```python
# 22. Diffie-Hellman Key Exchange (Zero imports)
p = 23
g = 5

a = int(input("Enter Alice private key a (default 6): ") or 6)
b = int(input("Enter Bob private key b (default 15): ") or 15)

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Shared secrets
keyA = pow(B, a, p)
keyB = pow(A, b, p)

print("Alice Public Key (A):", A)
print("Bob Public Key (B):  ", B)
print("Alice Shared Key:    ", keyA)
print("Bob Shared Key:      ", keyB)
print("Keys Match:          ", keyA == keyB)
```

---

### 23. ECC – Elliptic Curve Diffie–Hellman (ECDH)
**Mathematical Principle:**
- Curve: $y^2 \equiv x^3 + ax + b \pmod p$. Base point $G$, order $n$.
- Alice private $d_A$, public $Q_A = d_A \cdot G$.
- Bob private $d_B$, public $Q_B = d_B \cdot G$.
- Shared secret point: $S = d_A \cdot Q_B = d_B \cdot Q_A$.

```python
# 23. ECC - Elliptic Curve Diffie-Hellman (ECDH) (Zero imports)
p = 17
a = 2
b = 2
G = (5, 1)
n = 19
O = None

def ec_add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return O
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
        if k % 2:
            R = ec_add(R, P)
        P = ec_add(P, P)
        k //= 2
    return R

alice_priv = int(input("Alice private key (1..18, default 5): ") or 5)
bob_priv = int(input("Bob private key (1..18, default 7): ") or 7)

pubA = ec_mul(alice_priv, G)
pubB = ec_mul(bob_priv, G)

sharedA = ec_mul(alice_priv, pubB)
sharedB = ec_mul(bob_priv, pubA)

print("Alice Public Key:", pubA)
print("Bob Public Key:  ", pubB)
print("Alice Shared Key:", sharedA)
print("Bob Shared Key:  ", sharedB)
print("Shared Keys Match:", sharedA == sharedB)
```

---

### 24. EC-ElGamal Encryption and Decryption
**Mathematical Principle:**
- Message mapped to curve point $M$. Private key $d$, Public key $Q = d \cdot G$.
- Encryption: $C_1 = k \cdot G, \quad C_2 = M + k \cdot Q$.
- Decryption: $M = C_2 - d \cdot C_1 = C_2 + (-(d \cdot C_1))$. Point negation: $-(x, y) = (x, -y \bmod p)$.

```python
# 24. EC-ElGamal Encryption and Decryption (Zero imports)
p = 17
a = 2
b = 2
G = (5, 1)
n = 19
O = None

def ec_add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return O
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
        if k % 2:
            R = ec_add(R, P)
        P = ec_add(P, P)
        k //= 2
    return R

private_key = 7
public_key = ec_mul(private_key, G)

# Message point M (e.g. 2*G = (6, 3))
M = ec_mul(2, G)
k = 3  # Ephemeral key

# Encryption
C1 = ec_mul(k, G)
C2 = ec_add(M, ec_mul(k, public_key))

# Decryption: M = C2 - d*C1 = C2 + (-(d*C1))
S = ec_mul(private_key, C1)
negative_S = (S[0], (-S[1]) % p)
decrypted_M = ec_add(C2, negative_S)

print("Original Message Point M: ", M)
print("Encrypted Ciphertext (C1):", C1)
print("Encrypted Ciphertext (C2):", C2)
print("Decrypted Message Point:  ", decrypted_M)
print("Matches Original:         ", decrypted_M == M)
```

---

# 4. Digital Signatures (4 Programs)

### 25. RSA Digital Signature
**Mathematical Principle:**
- Message hash $h = H(M) \bmod n$.
- Signing: $S = h^d \bmod n$
- Verification: $h' = S^e \bmod n$. Valid if $h' == h$.

```python
# 25. RSA Digital Signature (Uses standard hashlib)
import hashlib

p = 17
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = pow(e, -1, phi)

msg = input("Enter message to sign (default 'CNS Lab'): ") or "CNS Lab"

# Compute hash using standard hashlib
h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % n

# Signing
sig = pow(h, d, n)

# Verification
verified_h = pow(sig, e, n)

print("Message:   ", msg)
print("Hash mod n:", h)
print("Signature: ", sig)
print("Verified:  ", verified_h == h)
```

---

### 26. Digital Signature Algorithm (DSA)
**Mathematical Principle:**
- Key generation: $p, q$ ($q \mid p-1$), generator $g$. Private key $x$, Public key $y = g^x \bmod p$.
- Signing: $r = (g^k \bmod p) \bmod q, \quad s = k^{-1}(H(M) + x \cdot r) \bmod q$.
- Verification: $w = s^{-1} \bmod q, \quad u_1 = (H(M) \cdot w) \bmod q, \quad u_2 = (r \cdot w) \bmod q$.
  $$v = ((g^{u_1} y^{u_2}) \bmod p) \bmod q \stackrel{?}{=} r$$

```python
# 26. Digital Signature Algorithm (DSA) (Uses standard hashlib)
import hashlib

p = 23
q = 11
g = 4

x = 3               # Private key
y = pow(g, x, p)    # Public key

msg = input("Enter message to sign (default 'Exam'): ") or "Exam"
h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % q
if h == 0:
    h = 1

k = 2               # Ephemeral key (coprime to q)

# Signing
r = pow(g, k, p) % q
s = (pow(k, -1, q) * (h + x * r)) % q

# Verification
w = pow(s, -1, q)
u1 = (h * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

print("Message:   ", msg)
print(f"Signature: (r = {r}, s = {s})")
print("Verified:  ", v == r)
```

---

### 27. ECDSA (Elliptic Curve Digital Signature Algorithm)
**Mathematical Principle:**
- Private key $d$, Public key $Q = d \cdot G$.
- Signing: Ephemeral key $k$. $R = k \cdot G = (x_1, y_1)$, $r = x_1 \bmod n$, $s = k^{-1}(H(M) + r \cdot d) \bmod n$.
- Verification: $w = s^{-1} \bmod n, \quad u_1 = (H(M) \cdot w) \bmod n, \quad u_2 = (r \cdot w) \bmod n$.
  Compute point $P = u_1 \cdot G + u_2 \cdot Q = (x_v, y_v)$. Valid if $x_v \bmod n == r$.

```python
# 27. ECDSA (Uses standard hashlib)
import hashlib

p = 17
a = 2
b = 2
G = (5, 1)
n = 19
O = None

def ec_add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return O
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
        if k % 2:
            R = ec_add(R, P)
        P = ec_add(P, P)
        k //= 2
    return R

private_key = 7
public_key = ec_mul(private_key, G)

msg = input("Enter message (default 'CNS'): ") or "CNS"
h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % n
if h == 0:
    h = 1

k = 3  # Ephemeral key

# Signing
R = ec_mul(k, G)
r = R[0] % n
s = (pow(k, -1, n) * (h + r * private_key)) % n

# Verification
w = pow(s, -1, n)
u1 = (h * w) % n
u2 = (r * w) % n
P = ec_add(ec_mul(u1, G), ec_mul(u2, public_key))

valid = P is not None and (P[0] % n == r)

print(f"Signature: (r = {r}, s = {s})")
print("Valid:     ", valid)
```

---

### 28. ElGamal Digital Signature
**Mathematical Principle:**
- Key: Private $x$, Public $(p, g, y)$ where $y = g^x \bmod p$.
- Signing: Choose $k$ with $\gcd(k, p-1) = 1$.
  $$r = g^k \bmod p, \quad s = k^{-1}(H(M) - x \cdot r) \bmod (p-1)$$
- Verification:
  $$g^{H(M)} \equiv y^r \cdot r^s \pmod p$$

```python
# 28. ElGamal Digital Signature (NO math.gcd - uses custom gcd and hashlib)
import hashlib

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

p = 23
g = 5

x = 6               # Private key
y = pow(g, x, p)    # Public key

msg = input("Enter message (default 'Secure'): ") or "Secure"
h = int(hashlib.sha256(msg.encode()).hexdigest(), 16) % (p - 1)
if h == 0:
    h = 1

k = 7  # Must be coprime to p - 1 = 22
assert gcd(k, p - 1) == 1

# Signing
r = pow(g, k, p)
s = ((h - x * r) * pow(k, -1, p - 1)) % (p - 1)

# Verification
left = pow(g, h, p)
right = (pow(y, r, p) * pow(r, s, p)) % p

print(f"Signature: (r = {r}, s = {s})")
print("Verified:  ", left == right)
```

