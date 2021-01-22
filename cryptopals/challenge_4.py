import binascii
from Crypto.Util.strxor import strxor
f=open("challenge_4.txt","r")
f1=f.readlines()
for i in range(len(f1)):
	if(f1[i][len(f1[i])-1]=='\n'):
		f1[i]=f1[i][:len(f1[i])-1]
	f1[i]=binascii.unhexlify(f1[i])
s="abcdefghijklmnopqrstuvwxyz"
d=" "
t=0
arr=[]
brr=[]
p=b''
for i in range(256):
	for j in f1:
		for k in j:
			p+=bytes([k^i])
		try:
			arr.append(bytes.fromhex(p.hex()).decode("utf-8"))
		except:
			print("",end="")
		p=b''
for i in arr:
	for j in i:
		if(j in s or j in d):
			t+=1
	brr.append(t)
	t=0
print(arr[brr.index(max(brr))])
