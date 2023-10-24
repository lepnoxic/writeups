# Level 5

entering directory
```
bandit5@bandit:~$ cd inhere
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
```
we are given conditions that the file is 
    "human-readable,
    1033 bytes in size,
    not executable"
which on inspection are all options of the find command in it's man page. They have asked for size which will be given in c, they asked not executable and `-executable` is an option. So we use `!` infront of it to get files which are false for it.
```
bandit5@bandit:~/inhere$ find -readable -size 1033c ! -executable
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
```