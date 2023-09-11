import random
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_prime(min, max):
    prime = random.randint(min, max)
    while not is_prime(prime):
        prime = random.randint(min, max)
    return prime


def mod_inverse(e, phi):
    for d in range(3, phi):
        if (e * d) % phi == 1:
            return d
    raise ValueError("Modular inverse does not exist")


p, q = generate_prime(2, 100), generate_prime(2, 100)
# p, q = 3, 5

while p == q:
    q = generate_prime(2, 100)

N = p * q
phi_n = (p - 1) * (q - 1)


e = random.randint(3, phi_n - 1)

while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

d = mod_inverse(e, phi_n)


print("Public key: ", e)
print("Private key: ", d)
print("N: ", N)
print("Phi N: ", phi_n)
print("p: ", p)
print("q: ", q)


MENSAGEM = "The information security is of significant importance to ensure the privacy of communications"
print('MENSAGEM', MENSAGEM)

MENSAGEM_CODIFICADA = [ord(char) for char in MENSAGEM]
print('MENSAGEM_CODIFICADA', MENSAGEM_CODIFICADA)

MENSAGEM_CIFRADA = [pow(char, e, N) for char in MENSAGEM_CODIFICADA]
print('MENSAGEM_CIFRADA', MENSAGEM_CIFRADA)
print('MENSAGEM_CIFRADA_LEGIVEL', ''.join(
    [chr(char) for char in MENSAGEM_CIFRADA]))

MENSAGEM_DECIFRADA = [pow(char, d, N) for char in MENSAGEM_CIFRADA]
print('MENSAGEM_DECIFRADA', MENSAGEM_DECIFRADA)

MENSAGEM_DECIFRADA_LEGIVEL = ''.join(
    [chr(char) for char in MENSAGEM_DECIFRADA])
print('MENSAGEM_DECIFRADA_LEGIVEL', MENSAGEM_DECIFRADA_LEGIVEL)
