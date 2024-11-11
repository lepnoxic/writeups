from Crypto.Util.strxor import strxor
import base64

base64_bytes = "LBAXBw1VHlQLLSw6G0EDRyI=".encode()
expected_bytes = base64.b64decode(base64_bytes)

key = "_scavenger__hunt_".encode()
print(strxor(key, expected_bytes).decode())