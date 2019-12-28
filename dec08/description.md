# HV19.08 - SmileNcryptor 4.0

| Author | Level | Categories |
|---|---|---|
| otaku | medium | crypto; reverse engineering |

## Given

### Description
You hacked into the system of very-secure-shopping.com and you found a SQL-Dump with $$-creditcards numbers. As a good hacker you inform the company from which you got the dump. The managers tell you that they don't worry, because the data is encrypted.

Dump-File: [dump.zip](c635204a-6347-45d7-91f8-bd7b94b111f1.zip)

### Goal
Analyze the "Encryption"-method and try to decrypt the flag.

### Hints
- CC-Numbers are valid ones.
- Cyber-Managers often doesn't know the difference between encoding and encryption.

### Additional info
In the SQL dump, the following entries could be found: 

```
# `creditcards` table
(1,'Sirius Black',		':)QVXSZUVY\ZYYZ[a'	,'12/2020'),
(2,'Hermione Granger',	':)QOUW[VT^VY]bZ_'	,'04/2021'),
(3,'Draco Malfoy',		':)SPPVSSYVV\YY_\\]','05/2020'),
(4,'Severus Snape',		':)RPQRSTUVWXYZ[\]^','10/2020'),
(5,'Ron Weasley',		':)QTVWRSVUXW[_Z`\b','11/2020');

# `flags` table
(1,'HV19{',':)SlQRUPXWVo\Vuv_n_\ajjce','}');
```

## Aproach
From the text it was clear that the ciphertext had to be reverted to a numeric string with a length of 14 to 19 positions (length of credit card numbers). It became also relatively clear from the quotation marks, that the encryption was more of an encoding and that it had to be some poor man's approach (which was also confirmed by `DrSchottkyd` later in the chat).

Looking at the given ciphertext with the algorithm being "SmileNcryptor 4.0", I simply dropped the prefixing smiley faces with them not adding any additional information (except that it's actually ciphertext).

An analysis of the ciphertext alphabet (of credit card numbers only) provides the following alphabet, which is already longer than the wanted 10 characters (0-9):

	[\]^_`abOPQRSTUVWXYZ

Other than that, it seems that characters that lay higher in the ASCII value space appear only later in the ciphertext. 

`multifred`, at some point (late at night/early in the morning), posted an incredible analysis that was a real eye opener (in the next morning) for me. He mapped ciphertext characters against an ASCII axis, which looks like this:

```
-----------------------------------------------------------------------------------------------
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
                         :
        )
                                                  S
                                               P
                                               P     
                                                     V
                                                  S
                                                  S
                                                        Y
                                                     V
                                                     V     
                                                           \
                                                        Y
                                                        Y
                                                              _
                                                           \
                                                           \
                                                            ]
```

This shows nicely, how a "decryption" algorithm needs to shift the characters to the left into the numeric part of the ASCII space.

It also shows, that the spectrum of cipher characters was wider than the spectrum of numeric characters. In combination with the fact that the distribution seems to drift to the right, which represents higher ASCII values, the of each character could have an influence. 

Let's script that... And indeed: By substracting from the character value a fixed offset and it's position's value, a printable, numeric ASCII character was produced.

Here's the code: 

```python
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

if __name__ == '__main__':
	for c in ciphertext:
		print("Decrypting %s" % c)
		cleartext = decrypt_string(c)
		print("%s (length: %s)" % (cleartext, len(cleartext)))

	print("Flag: HV19{%s}" % decrypt_string(flag))

```

Producing the output: 

```bash
$ python smilencryptor.py 
Decrypting QVXSZUVY\ZYYZ[a
378282246310005 (length: 15)
Decrypting QOUW[VT^VY]bZ_
30569309025904 (length: 14)
Decrypting SPPVSSYVV\YY_\\]
5105105105105100 (length: 16)
Decrypting RPQRSTUVWXYZ[\]^
4111111111111111 (length: 16)
Decrypting QTVWRSVUXW[_Z`\b
3566002020360505 (length: 16)
Flag: HV19{5M113-420H4-KK3A1-19801}

```

## Flag
`HV19{5M113-420H4-KK3A1-19801}`

## Credits
Massive credits to `multifred` who posted the above ASCII-analysis, which was a new approach to me and which finally helped to find the solution.
