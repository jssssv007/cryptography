import binascii
from Crypto.Util.strxor import strxor
k="1c0111001f010100061a024b53535009181c"
l="686974207468652062756c6c277320657965"
k1=binascii.unhexlify(k)
l1=binascii.unhexlify(l)
print((strxor(k1,l1)).hex())