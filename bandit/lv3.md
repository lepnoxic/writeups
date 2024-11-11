# Level 3

seeing directory
```
bandit3@bandit:~$ ls
inhere
```
so i change directory and check
```
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls
```
there is no file found, so i try to find hidden files
```
bandit3@bandit:~/inhere$ find
.
./.hidden
bandit3@bandit:~/inhere$ cat ./.hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```