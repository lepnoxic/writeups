# Play Fair

in the given python file there is a wikipedia page which shows description about the cipher that is being used. We can see that cipher uses swapping places in the matrix. 

![Alt text](Playfair_Cipher_01_HI_to_BM_(cropped).png)

So for to decrypt the given message we just need to decrement whatever has been incremented in the positions to get back the decrypt character. So the lines we need to change is just 

```python
def encrypt_pair(pair, matrix):
	...
	if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] + 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] + 1)  % SQUARE_SIZE]
	elif p1[1] == p2[1]:
		return matrix[(p1[0] + 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] + 1)  % SQUARE_SIZE][p2[1]]
	...
```

to

```python
def decrypt_pair(pair, matrix):
	...
    if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] - 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1)  % SQUARE_SIZE]
	elif p1[1] == p2[1]:
		return matrix[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1)  % SQUARE_SIZE][p2[1]]
	...
```

that's it. We input the given string into our decrypt function and we get the flag

```
└─$ nc mercury.picoctf.net 40742
Here is the alphabet: irlgektq8ayfp5zu037nov1m9xbc64shwjd2
Here is the encrypted message: h5a1sqeusdi38obzy0j5h3ift7s2r2
What is the plaintext message? xqyvhtg02jkplzo8eyhu25ktip2dkh
Congratulations! Here's the flag: 25a0ea7ff711f17bddefe26a6354b2f3
```