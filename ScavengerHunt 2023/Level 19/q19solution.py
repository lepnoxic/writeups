from Crypto.Util.strxor import strxor
from binascii import unhexlify
hex_data = "5a8bf3f7e01a00e7ee83180cd8eb61cfa90ef9e99e0f627ce02d86371bd75b94232109f3"
hex_data_2 = "6e9ae2f0ef6e25ffe2f27034dbf21efaa503edf797290179e839bc5611c01e8f35615daf"
msg = bytes("Great Job. You finally made it here!", "utf-8")

output = unhexlify(hex_data.encode())
output_2 = unhexlify(hex_data_2.encode())
final_output = strxor(strxor(output, output_2), msg)
print(final_output.decode())