# HV19.H03 - Hidden three

| Author | Level | Categories |
|---|---|---|
| M./inik | novice | fun; penetration testing |

## Given
"Not each quote is compl"

Hidden three appeared together with HV19.11.

## Approach
- Scan whale.hacking-lab.com.
- Discover port 17, ("Quote of the day") is open.
- Netcat to the port, check what's returned.
- Be disappointed that there's only 1 character and not a flag.
- Be bored and check again later only to notice the character changed.
- Use an AWS EC2 instance to poll the port.
- See that there's a new character every hour (\*sigh\*).
- Record characters for 24h.
- Get the flag.

In other news, the flag was commented as follows (as tweeted by [@Cac0nym](https://twitter.com/Cac0nym)):

![Waitiiing...](./ELiCu05WkAA_hb9.png)


## Flag
```
HV19{an0ther_DAILY_fl4g}
```
