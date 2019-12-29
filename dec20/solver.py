#!/usr/bin/env python
import base64

# From game:0x229b
v = base64.b16decode(b'0f1f4400000fb614014188140648ffc04883f81a75ef488b0548', casefold=True)
# From game:0x2000
v = base64.b16decode(b'ce55954e38c589a51b6f5e25d21d2a2b5e7b39148ed0f0f8f8a5', casefold=True)

print(base64.b16encode(v))

# File needs to have md5 f86d4f9d2c049547bd61f942151ffb55
# find it at http://wololo.net/2018/05/28/how-to-update-your-ps4-to-firmware-5-05/
filename = 'PS4UPDATE.PUP'

pos = 0x1337
with open(filename, mode='rb') as f:
	while pos != 0x1714908:
		f.seek(pos)
		bs = f.read(0x1a)
		v = bytes([a ^ b for a,b in zip(v, bs)])
		pos += 0x1337

print(v)
print(base64.b16encode(bytes(v)))
