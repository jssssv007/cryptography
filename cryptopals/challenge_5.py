import binascii
k="Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
l=bytes(k,'utf-8')
f="ICE"*len(l)
d=bytes(f,'utf-8')
p=b''
for i in range(len(l)):
	p+=bytes([l[i]^d[i]])
print(binascii.hexlify(p).decode('ascii'))