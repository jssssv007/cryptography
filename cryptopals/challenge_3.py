import binascii
k="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
l=binascii.unhexlify(k)
p=b''
arr=[]
brr=[]
s="abcdefghijklmnopqrstuvwxyz"
d=" "
t=0
for i in range(256):
	for j in l:
		p+=bytes([j^i])
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
kh=brr.index(max(brr))
print(arr[kh])