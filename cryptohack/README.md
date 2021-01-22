Encoding:


```
Ascii:
For the Ascii question ; we should just change those ascii values to their corresponding charecters to get the flag .
I have just printed the charecters in a line .

Hex:
For the Hex question ; I have just converted the hex to text using the following command 
print(bytes.fromhex(arr).decode('utf-8'))

Base64:
For this question ; using unhexlify we can decode the given hex string to bytes and from that we will use b2a_base64
to change those bytes to base 64 value

Bytes and Big Integers:
In this question ; I have converted the given number to it's hex form . Now while decoding ; it will be a problem if 
we leave the "0x" in the hex form while converting to text . So I have started the decoding from the second element . 
Now we can use "bytes.fromhex(k[2:]).decode('utf-8')" for the decoding purpose .

```


















For the question xor properties ;

We will be xoring key2^key3 and key1 

And now we will be xoring flag^key1^key2^key3 with key1^key2^key3 

which we will be getting in the above step to get the flag
