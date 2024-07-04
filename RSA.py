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

# Pre-encryption implementation
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


