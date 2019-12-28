# HV19.04 - Password Policy Circumvention

| Author | Level | Categories |
|---|---|---|
| DanMcFly | easy | fun |

## Given
Santa released a new password policy (more than 40 characters, upper, lower, digit, special).

The elves can't remember such long passwords, so they found a way to continue to use their old (bad) password:

Copied to clipboard

    merry christmas geeks

File: [HV19-PPC.zip](6473254e-1cb3-444e-9dac-5baeaaaf6d11.zip)

## Approach
Extracting the zip file resulted in a .ahk file.

AHK?? What is that? That's how I started...

After learning about what it actually is and considering the script, I decided to re-activate my Windows 10 box I still had around.

With AutoHotkey installed, I only had to type in the given string into a Notepad editor (however, I noticed elves must be very slow typers).

The produced output was the flag below.

## Flag
`HV19{R3memb3r, rem3mber - the 24th 0f December}`
