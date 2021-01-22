def sol():
	for i in range(len(arr)):
		try:
			k=bytes.fromhex(arr[i]).decode("utf-8")
			if("crypto" in k):
				print(k)
				print(arr[i])
		except:
			print("",end="")
x="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
y=bytes.fromhex(x).decode("utf-8")
k=bytes(y,'utf-8')
print(k)
arr=[]
s=b''
for j in range(1,256):
	for i in k:
		s+=bytes([i^j])
	arr.append(s.hex())
	s=b''
sol()
