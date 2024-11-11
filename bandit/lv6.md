# Level 6

Problem says to find again with given conditions but this time it says somewhere in the server so we search from the route directory

```
bandit6@bandit:~$ cd ../..
bandit6@bandit:/$ find -user bandit7 -group bandit6 -size 33c
find: ‘./etc/ssl/private’: Permission denied
find: ‘./etc/polkit-1/localauthority’: Permission denied
find: ‘./etc/sudoers.d’: Permission denied
find: ‘./etc/multipath’: Permission denied
...
```

we are finding many errors because we don't have permission for which we can null those outputs by using `2>/dev/null` where we take stderr outputs (`2`) and we stdout it (`>`) to null (`/dev/null`)

```
bandit6@bandit:/$ find -user bandit7 -group bandit6 -size 33c 2>/dev/null
./var/lib/dpkg/info/bandit7.password
bandit6@bandit:/$ cat ./var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
```