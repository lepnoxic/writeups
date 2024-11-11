from Crypto.Cipher import ARC4
from secret import key, flag
from binascii import hexlify


def encrypt(data):
	assert(len(key) > 128)
	cipher = ARC4.new(key)
	cipher.encrypt("0"*1024)
	return cipher.encrypt(data)

msg = "" #msg corresponds to the message obtained from video.mp4

print (hexlify(encrypt(msg)).decode())
print (hexlify(encrypt(flag)).decode())