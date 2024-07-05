import random
from simpy import mod_inverse, isprime

# Implementation of RSA Cryptography

# Sieve of Eratosthenes implementation
def sieve_erastothenes(max):
    primos = [True] * (max + 1)
    p = 2
    while p * p <= max:
        if primos[p]:
            for i in range(p * p, max + 1, p):
                primos[i] = False

        p += 1

    return [p for p in range(2, max + 1) if primos[p]]

# Pre-encryption
def pre_encryption(message):
    def char_to_code(char):
        if 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 10
        elif char == ' ':
            return 36
        elif char == '.':
            return 37
        else:
            return None

    code = [char_to_code(char) for char in message.upper() if char_to_code(char) is not None]

    return code

# Prime Selection
def select(primes, min_size):
    large_primes = [prime for prime in primes if prime.bit_length() >= min_size]
    if len(large_primes) < 2:
        raise ValueError("Not enough large primes found. Increase the limit or lower the min_size.")
    p = random.choice(large_primes)
    q = random.choice(large_primes)
    while p == q:
        q = random.choice(large_primes)
    return p, q

# Key generation
def generate_rsa_keys(primes, min_size):
    p, q = select(primes, min_size)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi_n)
    return (e, n), (d, n), (p, q)

def encrypt(message, public_key):
    e, n = public_key
    pre_encrypted = pre_encryption(message)
    encrypted = [pow(char, key, n) for char in pre_encrypted]
    return encrypted

def decrypt(message, private_key):
    d, n = private_key
    decrypted = [pow(char, key, n) for char in message]

    code_to_char = {10 + i: chr(65 + i) for i in range(26)}
    code_to_char[36] = ' '
    code_to_char[37] = '.'

    decoded = [code_to_char[char] for char in decrypted]
    return ''.join(decoded)




