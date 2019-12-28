# HV19.05 - Santa Parcel Tracking

| Author | Level | Categories |
|---|---|---|
| inik | easy | fun |

## Given 
To handle the huge load of parcels Santa introduced this year a parcel tracking system. He didn't like the black and white barcode, so he invented a more solemn barcode. Unfortunately the common barcode readers can't read it anymore, it only works with the pimped models santa owns. Can you read the barcode.

![Barcode](157de28f-2190-4c6d-a1dc-02ce9e385b5c.png)

## Approach
During breakfast, the moment I started, retr0id already sloved the challenge. What does that mean? Once more, probbably that I again overthink the challenge. But here we are... 

"Not the solution" is what you get, no matter what color layer you filter out. Looking at the image, it's no wonder. Each bar has a component of all the three RGB colors.

In addition, there's that misleading SP Tracking number: 1337-9999-4555-9. It's go the same length as "Not the solution", so it must be useful in some way, right?
But what if not. What if everything that I got was just plain distractors and misleading hints...

Together with my colleagues at work, we started looking more closely at the barcode's colors. Decoding the color of each bar of the barcode, we quickly found the pattern "HV19{" by looking only at the value of the blue RGB layer, being also the least significant byte of each value. Unfortunately, in the middle we confused the "_a_" for an "_=_" (can happen). After some back and forth, we still found the flag.

Credits to Jean-Eudes, mcia, and the entire FAIRTIQ crew.

## Flag
`HV19{D1fficult_to_g3t_a_SPT_R3ader}`
