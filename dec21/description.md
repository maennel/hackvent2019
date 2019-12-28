# HV19.21 - Happy christmas 256

| Author | Level | Categories |
|---|---|---|
| hardlock | hard | fun; crypto |

## Given

Santa has improved since the last Cryptmas and now he uses harder algorithms to secure the flag.

This is his public key:

```
X: 0xc58966d17da18c7f019c881e187c608fcb5010ef36fba4a199e7b382a088072f
Y: 0xd91b949eaf992c464d3e0d09c45b173b121d53097a9d47c25220c0b4beb943c
```

To make sure this is safe, he used the NIST P-256 standard.

But we are lucky and an Elve is our friend. We were able to gather some details from our whistleblower:

- Santa used a password and SHA256 for the private key (d)
- His password was leaked 10 years ago
- The password is length is the square root of 256
- The flag is encrypted with AES256
- The key for AES is derived with `pbkdf2_hmac`, salt: "TwoHundredFiftySix", iterations: `256*256*256`

Phew - Santa seems to know his business - or can you still recover this flag?

```
Hy97Xwv97vpwGn21finVvZj5pK/BvBjscf6vffm1po0=
```

## Approach

The following image illustrates the problem at hand and shows, that the symmetric key used to encrypt the flag is protected via the elliptic curve key pair. In ECC, public and private keys are related through the given curve's (`NIST P-256`) base point `G`.

![Overview](./HV19.21_happy_christmas_256.jpg "Image inspired by https://cryptobook.nakov.com/asymmetric-key-ciphers/ecc-encryption-decryption")

The core problem here is, that the key generation with PBKDF2 HMAC and the given parameters is computationally expensive. So, we have to find a different way to find the right password/key.

To start, I tried to leverage the given information about the password.

A quick DuckDuckGo search for 10 year old password breaches brings up the RockYou breach, including over 30 Millions passwords. Since that name rang a bell, I checked the wordlists included with Kali, and indeed, there was a rockyou.txt. Filtering passwords with 16 characters results in \~118k single passwords.

After some trying around, I decided to check whether a curve can be constructed with the given parameters. To do so, I generated a [SHA256 hash](https://www.pycryptodome.org/en/latest/src/hash/sha256.html?highlight=sha256#Crypto.Hash.SHA256.SHA256Hash) for every 16-character password and attempted to construct an [ECC key](https://www.pycryptodome.org/en/latest/src/public_key/ecc.html?highlight=ecckey#Crypto.PublicKey.ECC.construct) in combination with the given public key for each of these. 

Passwords that produce an hash value that does not match the given public key will fail the curve construction.

Only one password did not throw an error: `santacomesatxmas` (what else...)

With that password, I generated a key using [PBKDF2](https://www.pycryptodome.org/en/latest/src/protocol/kdf.html?highlight=pbkdf2#Crypto.Protocol.KDF.PBKDF2).

To conclude, I decrypted the given ciphertext with [AES ECB-mode](https://www.pycryptodome.org/en/latest/src/cipher/classic.html#ecb-mode) (ECB mode does not require an IV or a nonce, so it's usually the first thing to try if nothing is given).

I liked this challenge a lot, since it allowed me to dive a bit deeper than usual into elliptic curve cryptography.

## Flag
```
HV19{sry_n0_crypt0mat_th1s_year}
```

## Foundation

- Curve p-256 defines a base point `G` (see https://safecurves.cr.yp.to/base.html)
- `n` is the private key and `n*G` is the public key (see https://www.embedded.com/an-introduction-to-elliptic-curve-cryptography/)
- A curve also defines a max value `p` that is prime.
- Encryption: Choose an ephemeral secret to produce another ephemeral public key, which is multiplied with the public key, producing an ephemeral public key: see https://cryptobook.nakov.com/asymmetric-key-ciphers/ecc-encryption-decryption#ecc-based-secret-key-derivation-example-in-python
- Decryption: multiply the encrypted emphemeral public key with the private key; get back the computed secret.
