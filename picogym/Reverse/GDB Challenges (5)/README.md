# GDB Challenges

This writeup includes all challenges that are to learn how to use GDB

# GDB Test Drive

This is just a test drive, so run the given commands.

```
└─$ gdb gdbme
gef➤  break *(main+99)
Breakpoint 1 at 0x132a
gef➤  r
Starting program: /home/user1/picoCTF/gdb/gdbme
Breakpoint 1, 0x000055555555532a in main ()
gef➤  jump *(main+104)
Continuing at 0x55555555532f.
picoCTF{d3bugg3r_dr1v3_7776d758}
```

when dissasembling we can find out we are doing this to exit the instruction that puts the program to sleep

```
gef➤  disass main
Dump of assembler code for function main:
   ...
   0x0000555555555325 <+94>:    mov    edi,0x186a0
   0x000055555555532a <+99>:    call   0x555555555110 <sleep@plt>
   0x000055555555532f <+104>:   lea    rax,[rbp-0x30]
   ...
   0x000055555555538a <+195>:   ret
End of assembler dump.
```
# GDB baby step 1
Find what is loaded into eax
```
└─$ gdb debugger0_a
gef➤  disass main
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   rbp
   0x000000000000112e <+5>:     mov    rbp,rsp
   0x0000000000001131 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000001134 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000001138 <+15>:    mov    eax,0x86342
   0x000000000000113d <+20>:    pop    rbp
   0x000000000000113e <+21>:    ret
End of assembler dump.
```
`0x86342 => 549698`

`picoCTF{549698}`

# GDB baby step 2
Find what is loaded into eax
```
└─$ gdb debugger0_b
gef➤  disass main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x1e0da
   0x000000000040111c <+22>:    mov    DWORD PTR [rbp-0xc],0x25f
   0x0000000000401123 <+29>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040112a <+36>:    jmp    0x401136 <main+48>
   0x000000000040112c <+38>:    mov    eax,DWORD PTR [rbp-0x8]
   0x000000000040112f <+41>:    add    DWORD PTR [rbp-0x4],eax
   0x0000000000401132 <+44>:    add    DWORD PTR [rbp-0x8],0x1
   0x0000000000401136 <+48>:    mov    eax,DWORD PTR [rbp-0x8]
   0x0000000000401139 <+51>:    cmp    eax,DWORD PTR [rbp-0xc]
   0x000000000040113c <+54>:    jl     0x40112c <main+38>
   0x000000000040113e <+56>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401141 <+59>:    pop    rbp
   0x0000000000401142 <+60>:    ret
End of assembler dump.
gef➤  break *0x401141
Breakpoint 1 at 0x401141
gef➤  r
Starting program: /home/user1/picoCTF/gdb/debugger0_b
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0000000000401141 in main ()
gef➤  display $eax
1: $eax = 0x4af4b
```
`0x4af4b => 307019`

`picoCTF{307019}`

# GDB baby step 3
This time we see the 4 bytes of the address where `0x2262c96b` is loaded. 
```
└─$ gdb debugger0_c
gef➤  disass main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040111f <+25>:    pop    rbp
   0x0000000000401120 <+26>:    ret
End of assembler dump.
gef➤  b *0x40111c
Breakpoint 1 at 0x40111c
gef➤  r
Starting program: /home/user1/picoCTF/gdb/debugger0_c
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000000000040111c in main ()
gef➤  x/4xb $rbp-0x4
0x7fffffffdd8c: 0x6b    0xc9    0x62    0x22
```

Realization hitting that it is just storing the value in that address and viewing it backwards by 2 bytes. So it's just `0x2262c96b`but reverse every 2 bytes.

`picoCTF{0x6bc96222}`

# GDB baby step 4
Given we have a constant being multiplied to eax in the function call. So we look in the eax value before and after the function call and divide them.

```
└─$ gdb debugger0_d
gef➤  disass main
Dump of assembler code for function main:
   0x000000000040111c <+0>:     endbr64
   0x0000000000401120 <+4>:     push   rbp
   0x0000000000401121 <+5>:     mov    rbp,rsp
   0x0000000000401124 <+8>:     sub    rsp,0x20
   0x0000000000401128 <+12>:    mov    DWORD PTR [rbp-0x14],edi
   0x000000000040112b <+15>:    mov    QWORD PTR [rbp-0x20],rsi
   0x000000000040112f <+19>:    mov    DWORD PTR [rbp-0x4],0x28e
   0x0000000000401136 <+26>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040113d <+33>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401140 <+36>:    mov    edi,eax
   0x0000000000401142 <+38>:    call   0x401106 <func1>
   0x0000000000401147 <+43>:    mov    DWORD PTR [rbp-0x8],eax
   0x000000000040114a <+46>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040114d <+49>:    leave
   0x000000000040114e <+50>:    ret
End of assembler dump.
gef➤  b *0x401142
Breakpoint 1 at 0x401142
gef➤  b *0x401147
Breakpoint 2 at 0x401147
gef➤  r
Starting program: /home/user1/picoCTF/gdb/debugger0_d
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0000000000401142 in main ()
gef➤  display $eax
1: $eax = 0x28e
gef➤  c
Continuing.

Breakpoint 2, 0x0000000000401147 in main ()
gef➤  display $eax
2: $eax = 0x80c83e
```

```
80c83e / 28e
=> 8439870 / 654
=> 12905
```


`picoCTF{12905}`