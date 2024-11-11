for i in cipherText:
    if i in hex_arr:
        c = (hex_arr.index(i)+k)%16
        new_cipherText += hex_arr[c]
    else:
        new_cipherText += i