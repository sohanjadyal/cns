# CNS Lab – Cryptography & Network Security Python Programs

This repository contains clean, standalone, exam-ready Python implementations for all **Cryptography and Network Security (CNS)** lab algorithms.

---

## 📌 How to Set Your UID (`20243000xx`)
Every script in the [`programs/`](programs/) directory is pre-configured with a simple, standard instruction block at the top:

```python
# ==============================================================================
# INSTRUCTION: Change 'xx' below to your roll number (e.g. "2024300089")
# ==============================================================================
uid_str = "20243000xx"  # <-- CHANGE 'xx' HERE to your roll number
UID = int(uid_str.replace("xx", "89"))  # Fallback to 89 if unchanged
```

### Where to make changes:
1. Open any `.py` file from [`programs/`](programs/).
2. On line 6, change `"20243000xx"` to your actual UID (e.g. `"2024300012"`).
3. Save and run! All keys, bases, and parameters will automatically recalculate for your UID.
4. If you leave it as `"20243000xx"`, it automatically defaults to `2024300089`.

---

## ⚙️ Key Constraints
- **ZERO External Libraries**: No `numpy`, No `math` module (pure Python custom `gcd`, `egcd`, matrix inversion, etc.).
- **Hashing Libraries Only**: Standard library `hashlib` is used exclusively for standard cryptographic hashing in Digital Signatures.
- **Interactive & Standalone**: Every script runs standalone, prompts for input, and uses standard default values if you press `Enter`.

---

## 📂 Programs Index

### 1. Number Theory (10 Programs)
| File | Algorithm | Description |
| :--- | :--- | :--- |
| [`01_fermat_primality.py`](programs/01_fermat_primality.py) | **Fermat Primality Test** | Tests $a^{n-1} \equiv 1 \pmod n$ using UID-derived bases. |
| [`02_euler_primality.py`](programs/02_euler_primality.py) | **Euler Primality Test** | Euler–Jacobi (Solovay–Strassen) with pure Python Jacobi symbol. |
| [`03_miller_rabin.py`](programs/03_miller_rabin.py) | **Miller–Rabin Primality Test** | $n - 1 = 2^s \cdot d$ probabilistic test. |
| [`04_euclidean_gcd.py`](programs/04_euclidean_gcd.py) | **Euclidean Algorithm (GCD)** | Greatest Common Divisor without `math.gcd`. |
| [`05_extended_euclidean.py`](programs/05_extended_euclidean.py) | **Extended Euclidean Algorithm** | Computes Bézout coefficients and modular multiplicative inverse. |
| [`05b_chinese_remainder_theorem.py`](programs/05b_chinese_remainder_theorem.py) | **Chinese Remainder Theorem (CRT)** | Solves simultaneous congruences $x \equiv a_i \pmod{m_i}$ for coprime moduli. |
| [`06_euler_totient.py`](programs/06_euler_totient.py) | **Euler's Totient Function $\phi(n)$** | Counts coprimes $1 \le i \le n$. |
| [`07_primitive_root.py`](programs/07_primitive_root.py) | **Smallest Primitive Root** | Finds generator $g$ of cyclic group $\mathbb{Z}_p^*$. |
| [`08_discrete_logarithm.py`](programs/08_discrete_logarithm.py) | **Discrete Logarithm** | Solves $g^x \equiv h \pmod p$. |
| [`09_square_and_multiply.py`](programs/09_square_and_multiply.py) | **Square-and-Multiply** | Fast modular exponentiation in $O(\log b)$. |

### 2. Symmetric Ciphers (10 Programs)
| File | Cipher | Description |
| :--- | :--- | :--- |
| [`10_caesar_cipher.py`](programs/10_caesar_cipher.py) | **Caesar Cipher** | Shift key derived from UID digits: $(\sum d_i \bmod 25) + 1$. |
| [`11_monoalphabetic_cipher.py`](programs/11_monoalphabetic_cipher.py) | **Monoalphabetic Cipher** | Alphabet substitution keyed deterministically by UID. |
| [`12_vigenere_cipher.py`](programs/12_vigenere_cipher.py) | **Vigenère Cipher** | Keyword derived from UID digit pairs. |
| [`13_playfair_cipher.py`](programs/13_playfair_cipher.py) | **Playfair Cipher** | $5 \times 5$ matrix generated from UID keyword. |
| [`14_hill_cipher_2x2.py`](programs/14_hill_cipher_2x2.py) | **Hill Cipher (2×2)** | Invertible key matrix mod 26 and pure Python matrix inversion. |
| [`15_hill_cipher_3x3.py`](programs/15_hill_cipher_3x3.py) | **Hill Cipher (3×3)** | Pure Python determinant & adjugate inverse (NO `numpy`). |
| [`16_rail_fence_cipher.py`](programs/16_rail_fence_cipher.py) | **Rail Fence Cipher** | Zigzag transposition cipher. |
| [`17_columnar_transposition.py`](programs/17_columnar_transposition.py) | **Columnar Transposition** | Grid transposition ordered by UID keyword. |
| [`18_vernam_cipher.py`](programs/18_vernam_cipher.py) | **Vernam / One-Time Pad** | Modulo 26 addition/subtraction with key matching text length. |
| [`19_autokey_cipher.py`](programs/19_autokey_cipher.py) | **Autokey Cipher** | Self-extending keystream with primer keyword. |

### 3. Asymmetric Ciphers (5 Programs)
| File | Algorithm | Description |
| :--- | :--- | :--- |
| [`20_rsa_cipher.py`](programs/20_rsa_cipher.py) | **RSA Encryption/Decryption** | $C = M^e \bmod n, M = C^d \bmod n$. |
| [`21_elgamal_cipher.py`](programs/21_elgamal_cipher.py) | **ElGamal Encryption/Decryption** | Ephemeral key encryption over finite field $\mathbb{Z}_p^*$. |
| [`22_diffie_hellman.py`](programs/22_diffie_hellman.py) | **Diffie–Hellman Key Exchange** | Shared secret establishment $K_A = K_B = g^{ab} \bmod p$. |
| [`23_ecc_ecdh.py`](programs/23_ecc_ecdh.py) | **ECC – ECDH** | Elliptic Curve Diffie–Hellman key exchange over $y^2 = x^3 + 2x + 2 \pmod{17}$. |
| [`24_ec_elgamal.py`](programs/24_ec_elgamal.py) | **EC-ElGamal Encryption** | Curve point encryption $C_1 = kG, C_2 = M + kQ$. |

### 4. Digital Signatures (5 Programs)
| File | Scheme | Description |
| :--- | :--- | :--- |
| [`25_rsa_signature.py`](programs/25_rsa_signature.py) | **RSA Digital Signature** | Hash-and-sign using standard SHA-256 and private key. |
| [`25b_rsa_pss.py`](programs/25b_rsa_pss.py) | **RSA-PSS** | Probabilistic Signature Scheme with Salt and MGF1 masking. |
| [`26_dsa_signature.py`](programs/26_dsa_signature.py) | **Digital Signature Algorithm (DSA)** | FIPS 186 signature generation $(r, s)$ and verification. |
| [`27_ecdsa_signature.py`](programs/27_ecdsa_signature.py) | **ECDSA** | Elliptic Curve DSA with SHA-256 and point verification. |
| [`28_elgamal_signature.py`](programs/28_elgamal_signature.py) | **ElGamal Digital Signature** | Verification equation $g^h \equiv y^r r^s \pmod p$. |

---

## 🚀 How to Run
Run any program directly with Python 3:
```bash
python programs/10_caesar_cipher.py
python programs/14_hill_cipher_2x2.py
python programs/25b_rsa_pss.py
```
Press `Enter` at the prompt to use the default configured values, or type your own custom input!

