# HV19.03 - Hodor, Hodor, Hodor

| Author | Level | Categories |
|---|---|---|
| otaku feat. trolli101 | easy | fun; programming |

## Given

![Hodor!!](b3e6e692-e685-4804-9d4f-dfa873ce80d9.jpg)

The following text was given:

```
$HODOR: hhodor. Hodor. Hodor!?  = `hodor?!? HODOR!? hodor? Hodor oHodor. hodor? , HODOR!?! ohodor!?  dhodor? hodor odhodor? d HodorHodor  Hodor!? HODOR HODOR? hodor! hodor!? HODOR hodor! hodor? ! 

hodor?!? Hodor  Hodor Hodor? Hodor  HODOR  rhodor? HODOR Hodor!?  h4Hodor?!? Hodor?!? 0r hhodor?  Hodor!? oHodor?! hodor? Hodor  Hodor! HODOR Hodor hodor? 64 HODOR Hodor  HODOR!? hodor? Hodor!? Hodor!? .

HODOR?!? hodor- hodorHoOodoOor Hodor?!? OHoOodoOorHooodorrHODOR hodor. oHODOR... Dhodor- hodor?! HooodorrHODOR HoOodoOorHooodorrHODOR RoHODOR... HODOR!?! 1hodor?! HODOR... DHODOR- HODOR!?! HooodorrHODOR Hodor- HODORHoOodoOor HODOR!?! HODOR... DHODORHoOodoOor hodor. Hodor! HoOodoOorHodor HODORHoOodoOor 0Hooodorrhodor HoOodoOorHooodorrHODOR 0=`;
hodor.hod(hhodor. Hodor. Hodor!? );
```

## Approach
Once again, I was on a completely wrong track to start with. Trying to find out about obfuscation possibilities in bash and or perl did not lead anywhere.

And once again, the break-through idea came while not being in front of the screen, but doing something else.

A quick DuckDuckGo for "Hodor Programming Language" lead to a page describing the syntax: http://www.hodor-lang.org/. An online interpreter could be found at https://tio.run/#hodor (this, btw, seems like a cool page for this kind of challenges... bookmarking...).

The output produced was:

```
Awesome, you decoded Hodors language! 

As sis a real h4xx0r he loves base64 as well.

SFYxOXtoMDFkLXRoMy1kMDByLTQyMDQtbGQ0WX0=

```

And with a little CyberChef magic, this challenge was solvable entirely on the phone. 

## Flag
`HV19{h01d-th3-d00r-4204-ld4Y}`
