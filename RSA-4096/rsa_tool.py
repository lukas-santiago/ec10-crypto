from random import SystemRandom
from math import gcd
import sys
from time import time

import json
import os

BIT_LENGTH = 4096
SYSTEM_RANDOM = SystemRandom()
RSA_KEYS_FILE = "rsa_keys.json"


def generate_prime(bits):
    max_value = 2**bits - 1
    min_value = 2**(bits - 1)

    prime = SYSTEM_RANDOM.randint(min_value, max_value)
    while not miller_rabin(prime):
        prime = SYSTEM_RANDOM.randint(min_value, max_value)
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
        a = SYSTEM_RANDOM.randrange(2, n - 1)
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


def generate_keys():
    P, Q = generate_prime(BIT_LENGTH // 2), generate_prime(BIT_LENGTH // 2)
    while P == Q:
        Q = generate_prime(BIT_LENGTH // 2)

    N = P * Q

    PHI_N = (P-1)*(Q-1)

    E = 3
    while gcd(PHI_N, E) > 1:
        E += 2

    D = pow(E, -1, PHI_N)

    return P, Q, N, PHI_N, E, D


def generate_keys_and_save_to_json():
    P, Q, N, PHI_N, E, D = generate_keys()
    rsa_keys_object = {
        "P": P,
        "Q": Q,
        "N": N,
        "PHI_N": PHI_N,
        "E": E,
        "D": D
    }

    rsa_keys_json = json.dumps(rsa_keys_object, indent=4)
    with open(RSA_KEYS_FILE, "w", encoding="utf-8") as outfile:
        outfile.write(rsa_keys_json)


def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]


def decrypt(message, d, n):
    return ''.join([chr(pow(char, d, n)) for char in message])


def get_keys():
    if not os.path.exists(RSA_KEYS_FILE):
        print("Arquivo de chaves 'rsa_keys.json' não encontrado, gerando...")
        start = time()
        generate_keys_and_save_to_json()
        end = time()
        print("Arquivo de chaves gerado com sucesso. Time: ", end - start)
    try:
        with open(RSA_KEYS_FILE, "r", encoding="utf-8") as infile:
            json_keys = json.load(infile)
            print("Arquivo de chaves recuperado com sucesso")
            return json_keys
    except:
        print("Precisa excluir o rsa_keys.json")
        sys.exit()
