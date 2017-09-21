from Crypto.Util import number
from Crypto.PublicKey.RSA import construct
from Crypto.PublicKey import RSA
import sympy


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def getPQ():
    n_length =512 #generates a 1024bit key, use n=1024 for 2048 bit key.
    p = number.getPrime(n_length)
    q = number.getPrime(n_length)
    return p, q #it might not like it if q < p. Check this.

e = 65537
p, q = getPQ()
n = p*q
phi = (p-1)*(q-1)
gcd, d, b = egcd(e, phi)

key_params = (long(n), long(e), long(d))
key = RSA.construct(key_params)
print key.exportKey()
print key.publickey().exportKey()
#keep the pre-shared key below 100 bytes. 
message = 'message goes here'

print(message)
secret = key.encrypt(message,'') #check the encryption works
print secret
print key.decrypt(secret)


with open('key.priv', 'w') as file: #this is your private key. Don't lose it.
    file.write(key.exportKey())
with open('key.pub', 'w') as file: #this is your public key
    file.write(key.publickey().exportKey())
with open('secret.txt', 'wb') as file:
    file.write(str(secret)) #this is your ciphertext
with open('flag.txt', 'wb') as file:
    file.write(message) #this is your plaintext
