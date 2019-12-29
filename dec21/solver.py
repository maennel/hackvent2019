#!/usr/bin/env python

from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256
from Cryptodome.Cipher import AES
from Cryptodome.PublicKey import ECC
import base64

ciphertext = b'Hy97Xwv97vpwGn21finVvZj5pK/BvBjscf6vffm1po0='

# Eliptic curve parameters
x = 0xc58966d17da18c7f019c881e187c608fcb5010ef36fba4a199e7b382a088072f
y = 0xd91b949eaf992c464d3e0d09c45b173b121d53097a9d47c25220c0b4beb943c

# Key computation parameters
salt = b'TwoHundredFiftySix'
iterations = 256*256*256

def decrypt_ciphertext(ciphertext, key):
	aes = AES.new(key, mode=AES.MODE_ECB)
	plaintext = aes.decrypt(base64.b64decode(ciphertext))
	print("##################### FLAG ########################")
	print("    " + str(plaintext))
	print("###################################################")

def compute_key(pwd):
	# https://www.pycryptodome.org/en/latest/src/protocol/kdf.html
	key = PBKDF2(pwd, salt, dkLen=32, count=iterations, hmac_hash_module=SHA256)
	print("Key: " + hex(int.from_bytes(key, byteorder='big')))
	return key

def get_ecc_key(pwd):
	# https://www.pycryptodome.org/en/latest/src/public_key/ecc.html
	pwd_bytes = bytes(pwd, 'utf-8')
	sha = SHA256.new(pwd_bytes)
	d = int.from_bytes(sha.digest(), byteorder='big')
	ecc_key = ECC.construct(curve='p256', point_x=x, point_y=y, d=d)

def find_password():
	with open('rockyou.16.txt', 'r') as f:
		pwd = f.readline()
		while pwd:
			try:
				pwd = pwd.strip()
				get_ecc_key(pwd)
				print("Password: " + pwd)
				return pwd
			except ValueError as e:
				# print(type(e))
				# print("What? " + pwd)
				pwd = f.readline()
	raise Exception("No pwd found")

def main():
	pwd = find_password()
	# pwd = "santacomesatxmas"
	key = compute_key(pwd)
	# key_int = 0xeb1e0442ca6566e5d687740d246caea6db3b2851f774140d153c848d59515705
	# key = key_int.to_bytes(32, byteorder='big')
	decrypt_ciphertext(ciphertext, key)

if __name__ == '__main__':
	main()
