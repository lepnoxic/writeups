# Tell me baby, do you recognize me? (150)

Category - Misc

Challenge Question

Well, it's been a year (a lot actually), it doesn't surprise me.

The Flag should be wrapped in actf{}

Hints
1) BARCODE OR VISUAL TRANSFER OF INFORMATION.
2) https://www.microsoft.com/en-us/research/project/high-capacity-color-barcodes-hccb/

## Solution

We have an image which is an old barcode technology by microsoft which was discontinued in 2013. Observing closely we are dealing with 8 colors, primary colors, secondary colors, black and white. We tried to install microsoft tag app from an apk library out there and tried to scan this, that didn't work. But it worked on the other barcodes we found on the internet. 

So, each of these colors black, white, primary, secondary have one thing in common, there rgb is either 255 or 0. This means they can signify 1 and 0. So we write all the colors, get them in 1 and 0 format, that's the binary we need, and convert it into string.

```python
from Crypto.Util.number import long_to_bytes

white = "111"
black = "000"
red = "100"
green = "010"
blue = "001"
cyan = "011"
yellow = "110"
magenta = "101"

pattern = [
    cyan, black, green, yellow, blue, magenta, yellow, red, cyan, blue, red, white, magenta, magenta, magenta, black, blue, red, black, white, cyan, magenta, cyan, white, cyan, blue, black, cyan, black, magenta, red, red, green, white, yellow, white, green, magenta, cyan, white, cyan, blue, yellow, cyan, blue, magenta, yellow, red, green, white, yellow, yellow, red, black, yellow, cyan, cyan, red, red, cyan, blue, magenta, white, magenta
]

print(long_to_bytes(int("".join(pattern), 2)).decode())
```

`actf{h0w_d1d_u_g3t_h3r3}`