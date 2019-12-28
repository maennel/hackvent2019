# HV19.20 - i want to play a game

| Author | Level | Categories |
|---|---|---|
| hardlock | hard | fun |

## Given

Santa was spying you on Discord and saw that you want something weird and obscure to reverse?

your wish is my command.

[HV19-game.zip](e22163c8-e0a4-475b-aef5-6a8aba51fd93.zip)

## Aproach
It looks like this is a Playstation 4 binary, running - well - something.

Opening it with Hopper resulted in a bunch of garbage. Ghidra provided a much better disassembly out of the box, but still with some issues. For example, the `.rdata` section was incorrectly addressed with `0x229b` instead of `0x2000`. I'm still unsure why this happened.

Looking at the main routine, a file was being hashed with an MD5 hash. The result was compared with some expected value. 

After that, values were read in from specific positions in the file, starting at `0x1337` and incrementing by `0x1337`. These values were used to repeatedly XOR a value that originally was `0xce55954e38c589a51b6f5e25d21d2a2b5e7b39148ed0f0f8f8a5`, taken from address `0x2000`.

To find the file that was read, I had a look at the `.rdata` section. There was only one more string that satisfies an MD5 string, which is always 32 characters long.

Also, an analysis with `strings` lead to the conclusion, that the MD5 hash had something to do with the `PS4UPDATE.PUP` file:

```bash
$ strings game | head -n 45 | tail -n 10
libkernel.sprx
sceKernelGetIdPs
sceKernelGetOpenPsIdForSystem
/mnt/usb0/PS4UPDATE.PUP
%02x
f86d4f9d2c049547bd61f942151ffb55
GCC: (GNU) 7.4.0
.file
main.c
rSyscall
```

Indeed, a quick DuckDuckGo search for `f86d4f9d2c049547bd61f942151ffb55 PS4UPDATE.PUP` popped the following page: http://wololo.net/2018/05/28/how-to-update-your-ps4-to-firmware-5-05/

I re-implemented the algo with a small python script:

```python
#!/usr/bin/env python
import base64

# From game:0x2000
v = base64.b16decode(b'ce55954e38c589a51b6f5e25d21d2a2b5e7b39148ed0f0f8f8a5', casefold=True)

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
# Prints "b'HV19{C0nsole_H0mebr3w_FTW}'"
```

This was a really cool challenge, as one thing lead to another in a really smooth way.

## Flag: 
```
HV19{C0nsole_H0mebr3w_FTW}
```
