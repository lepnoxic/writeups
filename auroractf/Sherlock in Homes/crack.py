decryptedText = ""
hex_arr = "0123456789abcdef"
new_cipherText = "c0969bceb5aedb9dc9ce99d88a96c4"
k = 6

for i in new_cipherText:
    if i in hex_arr:
        c = (hex_arr.index(i)-k)%16
        decryptedText += hex_arr[c]
    else:
        decryptedText += i

print(bytes.fromhex(decryptedText).decode())