Convert hex to base64:
```
This question is about converting a given hex string to base 64 value . Firstly ; we have to change the given hex to 
bytes and now we can encode it to base-64 using "base64.b64encode(l)" and now this will be decoded to ascii to get 
the exact format which we need

```
Fixed XOR:
```
This question is about xoring two strings which were hex decoded before xoring . Decoding was done by using unhexlify 
in the library binascii . And now using strxor ; we can xor two bytes easily .Now this was encoded to hex

```
Single-byte XOR cipher:
```
Single-byte XOR is about xoring a hex string ; after decoding it ; with all the numbers from 1 to 256 and finding a 
meaningful sentence from it . In this question; I have xored every byte with all the numbers till 256 and stored them
in an array . Now I have taken a string which contains the alphabets in lower case and another string which have 
space . If any decoded(into text) byte have only alphabets and spaces or which doesnot have any unmeaningful symbols;
can be taken as the answer and we can sort out the meaningful sentence from this .

```
Repeating key XOR:
```
Repeating key XOR is about xoring the given text with the key in a parallel way until the length of the text . So 
I have converted both the text and key into bytes and xored them and once again decoded them to hex to get the
desired answer .
```
