#following RSA n, e, d generation create and test RSA key blocks
from Crypto.PublicKey.RSA import construct
from Crypto.PublicKey import RSA

#n = modulus, e = exponent, d - such that 1 < d < phi where ed ≡ 1 mod phi 

#RSA construct expects longs
key_params = (long(n), long(e), long(d))
#feed the beast
key = RSA.construct(key_params)

#print the private block. Keep this safe
print key.exportKey()
#print the public block.
print key.publickey().exportKey()

message = 'your test text goes here'
secret = key.encrypt(message,'')

#check it worked
print secret
print key.decrypt(secret)
