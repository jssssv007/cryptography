x="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
y=bytes.fromhex(x).decode("utf-8")
k=bytes(y,'utf-8')
#print(k)
e=b'crypto{'
f=b''
for i in range(len(e)):
	f+=bytes([k[i]^e[i]])
h=f.decode('utf-8')+'y'
h+=h*6
l=h.encode()
u=b''

for i in range(len(k)):
	u+=bytes([k[i]^l[i]])
print(u.decode('utf-8'))
