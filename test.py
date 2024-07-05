from RSA import *

# example of usage

limit = 100000
min_size = 16
primes = sieve_erastothenes(limit)

public, private, correct_primes = generate_rsa_keys(primes, min_size)

message = ("NO MEIO DO CAMINHO TINHA UMA PEDRA. TINHA UMA PEDRA NO MEIO DO "
            "CAMINHO. TINHA UMA PEDRA. NO MEIO DO CAMINHO TINHA UMA PEDRA. "
            "NUNCA ME ESQUECEREI DESSE ACONTECIMENTO NA VIDA DE MINHAS RETINAS "
            "TAO FATIGADAS. NUNCA ME ESQUECEREI QUE NO MEIO DO CAMINHO TINHA "
            "UMA PEDRA. TINHA UMA PEDRA. TINHA UMA PEDRA NO MEIO DO CAMINHO. NO "
            "MEIO DO CAMINHO TINHA UMA PEDRA. POEMA DE CARLOS DRUMMOND DE "
            "ANDRADE.")

encrypted_message = encrypt(message, public)
decrypted_message = decrypt(encrypted_message, private)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)

incorrect_primes = select(primes, min_size)
incorrect_private_key = (mod_inverse(65537, (incorrect_primes[0] - 1) * (incorrect_primes[1] - 1)), incorrect_primes[0] * incorrect_primes[1])

try:
    incorrect_decrypted_message = decrypt(encrypted_message, incorrect_private_key)
except KeyError:
    incorrect_decrypted_message = "Decryption failed with incorrect primes."

print("Decrypted Message with Incorrect Primes:", incorrect_decrypted_message)