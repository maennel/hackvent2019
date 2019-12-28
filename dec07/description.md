# HV19.07 - Santa rider

| Author | Level | Categories |
|---|---|---|
| inik | easy | fun |

## Given

"Santa is prototyping a new gadget for his sledge. Unfortunately it still has some glitches, but look for yourself."

An embedded video from https://academy.hacking-lab.com/api/media/challenge/mp4/13e4f1a0-bb71-44ec-be54-3f5f23991033.mp4
For easy download, get it here: [HV19-SantaRider.zip](3dbe0c12-d794-4f79-ae67-09ac27bd099d.zip)

## Approach

Decode, frame by frame, all bytes that can be seen in the film. This results in:

```
01001000
01010110
00110001
00111001
01111011
00110001
01101101
01011111
01100001
01101100
01110011
00110000
01011111
01110111
00110000
01110010
01101011
00110001
01101110
01100111
01011111
00110000
01101110
01011111
01100001
01011111
01110010
00110011
01101101
00110000
01110100
00110011
01011111
01100011
00110000
01101110
01110100
01110010
00110000
01101100
01111101
```

Which can be converted to ASCII, producing the flag.

## Flag
`HV19{1m_als0_w0rk1ng_0n_a_r3m0t3_c0ntr0l}`
