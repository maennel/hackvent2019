# HV19.10 - Guess what

| Author | Level | Categories |
|---|---|---|
| inik | medium | fun |

## Given
The flag is right, of course

[HV10.10-guess3.zip](d658ab66-6859-416d-8554-9a4ee0105794.zip)

### Hints
- New binary (v3) released at 20:00 CET
- Time for full points will be extended for additional 24 hours
- No asm needed
- run it on linux

## Approach
As the description says, there were two other binaries published before this one. I found the fact that everyone struggled (well, almost - kudos to @hardlock for fixing the binary and finding the flag) not too bad actually. 
It let me excercise a bit with `strace` and `ltrace`, which came in handy as soon as the real challenge was published. 

With the following command, the flag was printed out:

```bash
$ strace -e trace=execve -x -y -f -s10024  ./guess3
execve("./guess3", ["./guess3"], 0x7ffdd43f0c80 /* 66 vars */) = 0
execve("/bin/bash", ["./guess3", "-c", "exec './guess3' \"$@\"", "./guess3"], 0x5567ea44c290 /* 67 vars */) = 0
execve("/home/manu/Documents/hackvent19/dec10/_d658ab66-6859-416d-8554-9a4ee0105794.zip.extracted/guess3", ["./guess3"], 0x55ede84f3460 /* 66 vars */) = 0
execve("/bin/bash", ["./guess3", "-c", "       
        [ some whitespaces removed... ]
 #!/bin/bash\n\nread -p \"Your input: \" input\n\nif [ $input = \"HV19{Sh3ll_0bfuscat10n_1s_fut1l3}\" ] \nthen\n  echo \"success\"\nelse \n  echo \"nooooh. try harder!\"\nfi\n\n", "./guess3"], 0x7ffe99f75548 /* 65 vars */) = 0
Your input: HV19{Sh3ll_0bfuscat10n_1s_fut1l3}
success
+++ exited with 0 +++
```

So after all, the executable called itself a couple of times, only to run some script testing for whether or not the flag was entered.  

## Flag
`HV19{Sh3ll_0bfuscat10n_1s_fut1l3}`
