# HV19.H04 - Hidden Four

| Author | Level | Categories |
|---|---|---|
| M. | novice | fun; programming |


## Given
Not much; 

Hidden 04 appeared together with HV19.14.

## Approach

Take the flag from HV19.14 and "run" it:
```
HV19{s@@jSfx4gPcvtiwxPCagrtQ@,y^p-za-oPQ^a-z\x20\n^&&s[(.)(..)][\2\1]g;s%4(...)%"p$1t"%ee}
```

### How I've done it
And split it up into multiple regexes. 

```perl
$a="";
$a=~s@@jSfx4gPcvtiwxPCagrtQ@; # s-function: substitute
print "${a}\n";
$a=~y^p-za-oPQ^a-z\x20\n^;  # y-function: transliterate
print "${a}\n";
$a=~ s[(.)(..)][\2\1]g; # substitute globally (modifier: g)
print "${a}\n";
# Prints "Squ4ring the Circle"
$a=~s%4(...)%"p$1t"%ee; # modifier: ee - evaluate the right side as a string then eval the result
print "${a}\n";
# Prints "Squ1g the Circle"
```

Investigating on modifers, the last expression obviously was meant to print out the flag.

When run as a script, however, this does not work. So, I've taken the intermediary string to submit as a flag.


### How it could've been done

After a quick chat with M. (the author of the challenge), I learned that this kind of things can be run directly inline:

```bash
perl -e 's@@jSfx4gPcvtiwxPCagrtQ@,y^p-za-oPQ^a-z\x20\n^&&s[(.)(..)][\2\1]g;s%4(...)%"p$1t"%ee'
```

## Credits
Thanks *M.* for being patient with me.

## Flag
```
HV19{Squ4ring the Circle}
```
