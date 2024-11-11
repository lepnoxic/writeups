# PcapPoisoning

2 ways:

First is to open the given pcap file in wireshark. Filter the packets by the given data and the remaining packet will have the flag.

The other way is just to cat, string, grep

```
└─$ cat trace.pcap | strings | grep pico
picoCTF{P64P_4N4L7S1S_SU55355FUL_0f2d7dc9}6~
```
