# Bit-O-Assembly

I have combined all 4 Bit-O-Assembly Challenges into this one writeup. Each challenge deals with understanding x86 assembly and trying to find what is stored in the eax register.

# Bit-O-Assembly 1

```
<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```

We can see that value of `0x30` is being mov into `eax`. Thus our required answer is `0x30` = 48

`picoCTF{48}`

# Bit-O-Assembly 2

```
<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
```

at line 22 the value at `0x4` position in `rbp`. And in line 15, value `0x9fe1a` is moved into `0x4`. So our answer is `0x9fe1a` = 654874

`picoCTF{654874}`

# Bit-O-Assembly 3

```
<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
```

Arthemetic calculations. At the end what goes in eax is 

```
[rbp-0xc] * [rbp-0x8] + 0x1f5
0x9fe1a * 0x4 + 0x1f5
654874 * 4 + 501
2619997
``` 

`picoCTF{2619997}`

# Bit-O-Assembly 4

```
<+0>:     endbr64
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
```

`jle` if the previous comparision if less than then it jumps to the given address. As `0x9fe1a` is actually more than `0x2710`, so it won't jump on line 29. so our output will be 

```
0x9f1a - 0x65 
654874 - 101
654773
```
`picoCTF{654773}`