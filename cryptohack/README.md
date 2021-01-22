Encoding:


`For the Ascii question ; we should just change those ascii values 
to their corresponding charecters to get the flag . I have just printed
the charecters in a line .`

`For the Hex question ; I have just converted the hex to text using the following command 
print(bytes.fromhex(arr).decode('utf-8'))`
















`For the question xor properties ;

We will be xoring key2^key3 and key1 

And now we will be xoring flag^key1^key2^key3 with key1^key2^key3 

which we will be getting in the above step to get the flag`
