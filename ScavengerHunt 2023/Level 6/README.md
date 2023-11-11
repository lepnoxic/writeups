# Level 6: Airlock

## Problem

At last, the Wormhole activates and the starship plunges into the wormhole. However, the transition is not as smooth as you expected, causing multiple system failures on the Odysseus. Yet, the starship makes its way back to the original trajectory but not in the intended state.
The Odysseus descends through the atmosphere, its sleek exterior glowing brightly as it fights against the friction. Inside the cabin, you anxiously monitor the systems, your eyes fixed on a series of flashing lights. As the Odysseus approaches the planet's surface, a cacophony of alarms blares throughout the cabin. Continuous warning signs light up as each system fails. You realize the ship is in a dire situation, which is threatening the ship’s safe landing.
SPOCK informs you that the Radiation shields on the hull of the ship have been damaged, you need to go out and replace the bridge, but you don’t have the authorized access to open the airlock and go out. As you catch your breath and survey the wreckage, SPOCK informs you that the Communication System and the Navigation System have also been damaged, which means you can no longer send or receive messages from UNSC headquarters.
The airlock is locked out. To unlock the airlock, you need to find a way to bypass the locked system.

## Writeup

Given a cipher java file. In the checkpassword function we can see it takes the given string, xors it with `_scavenger__hunt_` and base64's it and checks if it is equal to `LBAXBw1VHlQLLSw6G0EDRyI=`. So we just go reverse, decode this base64 to bytes, and xor the two and get the password

```python
from Crypto.Util.strxor import strxor
import base64

base64_bytes = "LBAXBw1VHlQLLSw6G0EDRyI=".encode()
expected_bytes = base64.b64decode(base64_bytes)

key = "_scavenger__hunt_".encode()
print(strxor(key, expected_bytes).decode())
```

`sctf{0p3n_ses4m3}`