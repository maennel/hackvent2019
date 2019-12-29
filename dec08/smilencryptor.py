#!/usr/bin/env python

DEFAULT_OFFSET = 30

ciphertext = [
	"QVXSZUVY\\ZYYZ[a",
	"QOUW[VT^VY]bZ_",
	"SPPVSSYVV\\YY_\\\\]",
	"RPQRSTUVWXYZ[\\]^",
	"QTVWRSVUXW[_Z`\\b"
]
flag = "SlQRUPXWVo\\Vuv_n_\\ajjce"


def decrypt_char(character, index):
	character_val = ord(character) - DEFAULT_OFFSET - index
	try:
		return chr(character_val)	
	except Exception as e:
		print("Character %x could not be decrypted" % ord(character))
		return "X"
	
def decrypt_string(ciphertext):
	dec = ""
	for i in range(len(ciphertext)):
		dec += decrypt_char(ciphertext[i], i)
	return dec


def encrypt_char(character, index):
	character_val = ord(character)
	return chr(character_val + DEFAULT_OFFSET + index)


def encrypt_string(cleartext):
	enc = ""
	for i in range(len(cleartext)):
		enc += encrypt_char(cleartext[i], i)
	return enc


if __name__ == '__main__':
	for c in ciphertext:
		print("Decrypting %s" % c)
		cleartext = decrypt_string(c)
		print("%s (length: %s)" % (cleartext, len(cleartext)))

	print("Flag: HV19{%s}" % decrypt_string(flag))

	print("%s" % encrypt_string("378282246310005"))

#HV19{5M113-420H4-KK3A1-19801}
