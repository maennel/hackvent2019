#!/usr/bin/env python

from Cryptodome.Cipher import Salsa20
import base64



nonce = base64.b16decode(b'11458fe7a8d032b1', casefold=True) # <-- 
# nonce = base64.b16decode(b'a8d032b111458fe7', casefold=True)

secret = base64.b16decode(b'0320634661b63caffb2f7097214fd04c79730ff4ec0c406badf16c63456a5ef1', casefold=True)
# secret = base64.b16decode(b'46632003af3cb66197702ffb4cd04f21f40f73796b400cec636cf1adf15e6a45', casefold=True)
# secret = base64.b16decode(b'61b63caf03206346214fd04cfb2f7097ec0c406b79730ff4456a5ef1adf16c63', casefold=True)
# secret = base64.b16decode(b'af3cb661466320034cd04f2197702ffb6b400cecf40f7379f15e6a45636cf1ad', casefold=True)

# secret = base64.b16decode(b'0320634661b63cafaa76c27eea00659bfb2f7097214fd04cb257ac2904efee46', casefold=True)
# secret = base64.b16decode(b'46632003af3cb6617ec276aa9b6500ea97702ffb4cd04f2129ac57b246eeef04', casefold=True)
# secret = base64.b16decode(b'af3cb661466320039b6500ea7ec276aa4cd04f2197702ffb46eeef0429ac57b2', casefold=True)
# secret = base64.b16decode(b'61b63caf03206346ea00659baa76c27e214fd04cfb2f709704efee46b257ac29', casefold=True)

# With AArch64
secret = base64.b16decode(b'0320634661b63cafaa76c27eea00b59bfb2f7097214fd04cb257ac2904efee46', casefold=True)
# secret = base64.b16decode(b'46632003af3cb6617ec276aa9bb500ea97702ffb4cd04f2129ac57b246eeef04', casefold=True)



cipher = Salsa20.new(key=secret, nonce=nonce)

test_cleartext = b"fakeflagfakeflag"
test_ciphertext = base64.b16decode(b'275b8e1af6e0e0442a8e2c99dd7032231a', casefold=True)
print(cipher.decrypt(test_ciphertext))
# print(cipher.encrypt(test_ciphertext))


ciphertext = base64.b16decode(b'096CD446EBC8E04D2FDE299BE44F322863F7A37C18763554EEE4C99C3FAD15', casefold=True)
# ciphertext = base64.b16decode(b'096CD446EBC8E04D2FDE299BE44F322863F7A37C18763554EEE4C99C3FAD15', casefold=True)
cipher = Salsa20.new(key=secret, nonce=nonce)
print(str(cipher.decrypt(ciphertext)))
# Flag: HV19{Danc1ng_Salsa_in_ass3mbly}


# Self test
cipher = Salsa20.new(key=secret, nonce=nonce)
c = cipher.encrypt(test_cleartext)
print(c)
cipher = Salsa20.new(key=secret, nonce=nonce)
print(cipher.decrypt(c))

# 30:
# 03 20 63 46 61 b6 3c af aa 76 c2 7e ea 00 b5 9b 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
# 50:
# 03 20 63 46 61 b6 3c af aa 76 c2 7e ea 00 b5 9b 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
# 70:
# 03 20 63 46 61 b6 3c af aa 76 c2 7e ea 00 b5 9b fb 2f 70 97 21 4f d0 4c b2 57 ac 29 04 ef ee 46  <-- KEY
# 90:
# 79 73 0f f4 ec 0c 40 6b fd 91 c9 1f e7 04 00 a8 ad f1 6c 63 45 6a 5e f1 ed 9d 79 46 9d a2 a0 b5
# -- 79730ff4ec0c406bfd91c91fe70400a8adf16c63456a5ef1ed9d79469da2a0b5

# 03 20 63 46 61 b6 3c af aa 76 c2 7e ea 00 b5 9b fb 2f 70 97 21 4f d0 4c b2 57 ac 29 04 ef ee 46 79 73 0f f4 ec 0c 40 6b fd 91 c9 1f e7 04 00 a8 ad f1 6c 63 45 6a 5e f1 ed 9d 79 46 9d a2 a0 b5