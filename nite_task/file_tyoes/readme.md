# File Types

Basic premise, bunch of file types, use `file` to check what file type, keep on decompressing according to the tool. So i have not given much comment, just mentioned the file type and tool used.

Shell script - changed permission and run
```
└─$ file Flag.pdf
Flag.pdf: shell archive text
└─$ chmod +x Flag.sh

└─$ ./Flag.sh
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
```

ar archive - binwalk
```
└─$ binwalk -e flag

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
100           0x64            bzip2 compressed data, block size = 900k
```

gzip
```
└─$ gzip -d 64.gz
```
lzip 
```
└─$ lzip -d 64
```
LZ4
```
└─$ chmod +x 64.out
└─$ lz4 -d 64.lz4
Decoding file 64
64.lz4               : decoded 264 bytes
```
lzma
```
└─$ lzma -d 64.lzma
```
lzop
```
└─$ lzop -d 64.lzop
```
lzip
```
└─$ lzip -d 64
```
xz
```
└─$ unxz 64.xz
```

Finally we get a ascii text which is hex. decoding it we get the flag
```
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f6630725f3062326375723137795f39353063346665657d0a

picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_950c4fee}
```