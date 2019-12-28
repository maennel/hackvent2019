# HV19.22 - The command... is lost

| Author | Level | Categories |
|---|---|---|
| inik | leet | fun; reverse engineering |

## Given
Introduction
Santa bought this gadget when it was released in 2010. He did his own DYI project to control his sledge by serial communication over IR. Unfortunately Santa lost the source code for it and doesn't remember the command needed to send to the sledge. The only thing left is this file: [thecommand7.data](a97ef12f-c583-4c54-84e4-68eaa2737bd9.data)

Santa likes to start a new DYI project with more commands in January, but first he needs to know the old command. So, now it's on you to help out Santa.

## Approach

Many things seemed possible with this bunch of strangely connected strings. The pattern, however, is recurring: a colon in the beginning of the line and then some 42 hex characters.

Searching for the first line of this file revealed that it was a so-called hex file. 

Searching a bit further, I found out that one could dump an Arduino's flash memory and the resulting data was a hex-file. Things also worked the other way around. So, I tried flashing my Arduino with that program - and things worked... I think, at least. Because effectively I did not get any output, neither on the serial interface, nor on any board LED (I did not wire anything).

For flashing the hex program on my Arduino, I used the following command: 
```bash
avrdude -C/usr/share/arduino/hardware/tools/avrdude.conf -v -v -v -v -patmega328p -carduino -P/dev/ttyACM0 -b115200 -D -Uflash:w:./thecommand7.data:i
```

This has got to work in a different way...

### Static analysis

I tried disassembling/decmpiling the program in a static way: 

With Ghidra...
```
89e 44f -> 0
89f 227 -> ?
8a0 450 -> 1
8a1 228 -> ...
...
```

With avr-objdump (produces wrong output):
```
avr-objdump -D -m avr5 thecommand7.data > thecommand7.asm
```

With little success. So I proceeded:

### Debugging

Debugging the program seemed more promising. As I'm not equipped to do HW debugging. I had to look for a simulator. I found the following tool: 

OshonSoft.com AVR Simulator IDE (see https://www.oshonsoft.com/avr.html)

By closely observing memory mutations, I noticed that there were printable characters at 0x100. Right after that section, things were initialized to 0x20. However, when keeping an eye on that part of the memory, things suddenly started changing. Thanks to the OshonSoft simulator, execution speed could be slowed down, so that I could stop the program at the right point.

There was the flag, starting at *Internal data SRAM* address 0x117(-0x142):
```
48 56 31 39 7b 48 33 79 5f 53 6c 33 64 67 33 5f 6d 33 33 74 5f 6d 33 5f 61 74 5f 74 68 33 5f 6e 33 78 74 5f 63 30 72 6e 33 72 7d
```

This data got loaded into memory starting at address 0x0357 in the .text section.

### Additional info

ATmega328 is an `avr5` architecture (see https://www.microchip.com/webdoc/AVRLibcReferenceManual/using_tools_1using_avr_gcc_mach_opt.html)

Side note on the AVR "abbreviation": 
```
Atmel says that the name AVR is not an acronym and does not stand for anything in particular. The creators of the AVR give no definitive answer as to what the term "AVR" stands for.[3] However, it is commonly accepted that AVR stands for Alf and Vegard's RISC processor.[7] Note that the use of "AVR" in this article generally refers to the 8-bit RISC line of Atmel AVR Microcontrollers.
```
Source: https://en.wikipedia.org/wiki/AVR_microcontrollers

Conclusion: Stumbling over the solution is a way, too.

## Credits

Credits to *mcia* for helping me in keeping short the search for a suitable AVR/Arduino simulation/debugging tool.

## Flag
```
HV19{H3y_Sl3dg3_m33t_m3_at_th3_n3xt_c0rn3r}
```
