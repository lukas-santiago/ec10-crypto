from math import gcd
import time

# def isPrimeNumber(num):
#     if num==2 or num==3: return True
#     if num%2==0 or num<2: return False
#     for i in range(3, int(num**0.5)+1, 2):
#         if num%i==0:
#             return False
#     return True

def isPrimeNumber(num):
    i = 2
    while i < N:
        R = N % i
        if R == 0:
            return False
        i += 1
    else:
        return True

p = 4391
q = 4219

N = p * q

print('p = %s\nq = %s'%(p,q))
print('N = %s * %s = %s' %(p, q, N))
# ф(N) = (p-1).(q-1)
phi =	(p-1)*(q-1)
print('ф(%s) = (%s-1).(%s-1) = %s'%(N, p, q, phi))

e = 3
while(gcd(phi, e) > 1): e+= 2 
print('e = %s' % e)

d = 1
while((e * d) % phi != 1): 
    d+= 2
print('d = %s' % d)

