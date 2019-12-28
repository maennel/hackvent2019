# HV19.12 - back to basic

| Author | Level | Categories |
|---|---|---|
| hardlock | medium | fun; reverse engineering |

## Given
Santa used his time machine to get a present from the past. get your rusty tools out of your cellar and solve this one!

[HV19.12-BackToBasic.zip](67e6c6c2-1119-4c1e-a9b5-85f118173a40.zip)

## Approach

"Rusty tools"? In my case, they were never shiny or even existing. But anyways...

Being a beginner in reverse eingineering I decided to proceed with Ghidra and OllyDbg side by side, as it was clear that we deal with a Windows PE binary and Ghidra provided a decompiled view, which is handy.

Let's have a look at the program. Apparently, the UI will display "Status: wrong" as long as we don't enter the correct flag.

It turns out, the program rejects all strings that have a length other than 33 characters. 

Looking at what Ghidra was able to decompile, one can see there's a suspicious looking XOR function somewhere in the middle of the part that we end up in, when a 33-character string is entered. 

![Ghidra screenshot](HV19.12_ghidra.png)

In OllyDbg, I then tried to observe what happened right before that XOR by setting breakpoints and investigating memory.


Eventually, I was able to find the key used for XORing.

TODO

## Credits
- *mcia* for keeping me in front of the screen with tiny, non-revealing but very teasing hints.

## Flag
```
HV19{0ldsch00l_Revers1ng_Sess10n}
```
