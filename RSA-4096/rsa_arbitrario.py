import math

# Procedimento para geração das chaves

# Etapa 1 - Escolher p e q (números primos) para o cálculo de N = p.q
P = 4391
Q = 4219

N = P * Q

# Etapa 2 - Calcular a função totiente phi(N) = (p-1).(q-1)
PHI_N = (P-1)*(Q-1)

# Etapa 3 - Escolha 1 < e < phi(N), tal que e e phi(N) sejam primos entre si
E = 3
while math.gcd(PHI_N, E) > 1:
    E += 2

# Etapa 4 - Escolha d tal que e.d mod phi(N) =1
D = pow(E, -1, PHI_N)

# Chaves Assimétricas
MENSAGEM = "The information security is of significant importance to ensure the privacy of communications"

# Criptografar - Chave Pública (e,N) => C = P^e mod N
MENSAGEM_CIFRADA = [pow(char, E, N)
                    for char in [ord(char) for char in MENSAGEM]]

# Decriptografar - Chave Privada (d,N) => P = C^d mod N
MENSAGEM_DECIFRADA = ''.join(
    [chr(char) for char in [pow(char, D, N) for char in MENSAGEM_CIFRADA]])

print(MENSAGEM_DECIFRADA)