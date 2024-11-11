# Level 5: L3 Wormhole

## Problem

Finally, with the machine whirring to life and the right timestamp in hand, all you need to do is open the wormhole. SPOCK displays the document for the Wormhole KEY which has the information that needs to be used to activate the wormhole generator.

![Alt text](q5Key.jpg)

## Writeup

Running exiftool provided in the metadata the flag

```
└─$ exiftool q5Key.jpg
ExifTool Version Number         : 12.63
File Name                       : q5Key.jpg
Directory                       : .
File Size                       : 122 kB
File Modification Date/Time     : 2023:11:11 11:28:58+05:30
File Access Date/Time           : 2023:11:11 11:29:19+05:30
File Inode Change Date/Time     : 2023:11:11 11:29:10+05:30
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 96
Y Resolution                    : 96
Exif Byte Order                 : Big-endian (Motorola, MM)
Copyright                       : sctf{T3mp0r4l_R1ft};
Padding                         : (Binary data 2050 bytes, use -b option to extract)
About                           : uuid:faf5bdd5-ba3d-11da-ad31-d33d75182f1b
Rights                          : sctf{T3mp0r4l_R1ft};
Image Width                     : 1024
Image Height                    : 1024
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1024x1024
Megapixels                      : 1.0
```

`sctf{T3mp0r4l_R1ft}`