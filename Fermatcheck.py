from Crypto.Util import number
from Crypto.PublicKey.RSA import construct
from Crypto.PublicKey import RSA
import sympy

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        if verbose:
            print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    print('a=',a)
    print('b=',b)
    print('p=',p)
    print('q=',q)
    print('pq=',p*q)
    return p, q

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

n = #n value goes here
e = #e value goes here

p, q = fermat(n)

#let's use those to make the key blocks
n = p*q 
phi = (p-1)*(q-1) 
gcd, d, b = egcd(e, phi) 

key_params = (long(n), long(e), long(d))
key = RSA.construct(key_params)
print key.exportKey()
print key.publickey().exportKey()
