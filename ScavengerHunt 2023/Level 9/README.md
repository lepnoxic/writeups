# Level 9: Enter The Ship

## Problem

You make your way back inside the ship having fixed the shields and you realize that the captain is unconscious in the ship’s bridge. But, you don’t have the authorized access to enter the ship. Use the bridge passcode database provided by SPOCK to find the right passcode for entering the ship.

## Writeup

We are given an sql file with a bunch of flags already inserted in it waiting for a value to fetch at what index which is the one. As there are not that many flags, so we can manually put each one as an input as flag. To do the intended way taking the base64 data given and decoding it we get a list of ascii numbers, we take the ascii numbers and decode as bytes to get a message at which position the flag is.

```python
from base64 import b64decode
given = "MTE2IDEwNCAxMDEgMzIgNTIgMTE2IDEwNCAzMiAxMTIgOTcgMTE1IDExNSAxMTkgMTExIDExNCAxMDAgMzIgMTA1IDExMCAzMiAxMTYgMTA0IDEwMSAzMiAxMDAgOTcgMTE2IDk3IDk4IDk3IDExNSAxMDE=".encode("ascii")
listOfNumbers = b64decode(given).decode("ascii")
listOfNumbers = list(map(int, listOfNumbers.split(" ")))
print(bytes(listOfNumbers).decode("ascii"))
```
`the 4th password in the database`
```
-- Insert critical information into the table
INSERT INTO critical_information (info_text)
VALUES 
    ('sctf{passw0rd_cr4ck}'),
    ('sctf{p@ssw0rd_cr4ck}'),
    ('sctf{password_cr4ck}'),
    ('sctf{p@ssw0rd_h@ck}'),  <---------
    ('sctf{p@ssw0rd_hack}'),
    ('sctf{Pa$$w0rd_Cr4ck}'),
    ('sctf{P@$$W0rd_Cr4ck}'),
    ('sctf{P@ssw0rd_H@ck}'),
    ('sctf{p@ssW0rd_Cr4ck}'),
    ('sctf{P@ssw0rd_Hack}');
```

`sctf{p@ssw0rd_h@ck}`