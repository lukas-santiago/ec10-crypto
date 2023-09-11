from random import SystemRandom
from math import gcd
from time import time

BIT_LENGTH = 4096
system_random = SystemRandom()


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_prime(bits):
    max_value = 2**bits - 1
    min_value = 2**(bits - 1)

    prime = system_random.randint(min_value, max_value)
    while not miller_rabin(prime):
        prime = system_random.randint(min_value, max_value)
    return prime


def miller_rabin(n, k=40):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = system_random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Procedimento para geração das chaves
start = time()

# Etapa 1 - Escolher p e q (números primos) para o cálculo de N = p.q
P, Q = generate_prime(BIT_LENGTH // 2), generate_prime(BIT_LENGTH // 2)
while P == Q:
    Q = generate_prime(BIT_LENGTH // 2)

N = P * Q

checkpoint_1 = time()

# Etapa 2 - Calcular a função totiente phi(N) = (p-1).(q-1)
PHI_N = (P-1)*(Q-1)

# Etapa 3 - Escolha 1 < e < phi(N), tal que e e phi(N) sejam primos entre si
E = 3
while gcd(PHI_N, E) > 1:
    E += 2

checkpoint_2 = time()

# Etapa 4 - Escolha d tal que e.d mod phi(N) =1
D = pow(E, -1, PHI_N)

checkpoint_3 = time()

# Chaves Assimétricas
MENSAGEM = "The information security is of significant importance to ensure the privacy of communications"

# Criptografar - Chave Pública (e,N) => C = P^e mod N
MENSAGEM_CIFRADA = [pow(char, E, N)
                    for char in [ord(char) for char in MENSAGEM]]

checkpoint_4 = time()

# Decriptografar - Chave Privada (d,N) => P = C^d mod N
MENSAGEM_DECIFRADA = ''.join(
    [chr(char) for char in [pow(char, D, N) for char in MENSAGEM_CIFRADA]])

checkpoint_5 = time()

print(MENSAGEM_DECIFRADA)

print(f"Checkpoint 1: {checkpoint_1 - start}")
print(f"Checkpoint 2: {checkpoint_2 - start}")
print(f"Checkpoint 3: {checkpoint_3 - start}")
print(f"Checkpoint 4: {checkpoint_4 - start}")
print(f"Tempo de execução: {checkpoint_5 - start}")
