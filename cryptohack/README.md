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

XOR:


```
XOR Starter:
For this question ; we can just apply a for loop and xor every element of the string "label" with 13 . This gives
us the answer .

XOR Properties:
For the question xor properties ;We will be xoring key2^key3 and key1 And now we will be xoring flag^key1^key2^key3
with key1^key2^key3 which we will be getting in the above step to get the flag

Favourite byte:
In this question ; firstly I have decoded the string from hex and changed it to bytes . These bytes were xored with 
all the numbers from 1 to 256 and stored in an array and now our task is to decode these bytes and search for a 
string which contains "crypto" in it and if it was meaningful . I have used try and except because while decoding ; 
some of the bytes were not decoded properly and they were giving errors . We can even use "ignore" while decoding 
the byte which ignores the error and continues with the positive outputs . And now we will get the flag .

You Either Know XOR , you dont:
In this question ; I have decoded the given hex string and converted it into bytes . According to the question ; By
decoding the given string ; we will get the flag . So , the first 7 elements of the string should be "crypto{" . 
Now if we xor the first seven elements of the byte with "crypto{" ; we will get a flag "myXORke" but this is not 
sufficient for getting the answer as it gives some errors while decoding the string using this key . So we have to
assume that the key will be "myXORkey" as the key for xoring will always be meaningful . Now we can decode and get
the flag using this key.

Lemur XOR:
Here we will be given two images and we have to get the flag with these two images . In the question they have 
already stated that both the images were xored with the same key . So by xoring these two images in a bitwise 
way ; we will get an image and it contains the flag "crypto{X0Rly_n0t!}".
```
