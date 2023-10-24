# Level 4

checking inner directory
```
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
```
we see that there are many files which we have to check to find that password. One method can be to cat all files together by using the following command by using iterator `[0-9]` or `*`
```
bandit4@bandit:~/inhere$ cat ./-file0[0-9]
QRrtZ�i�     �H
                  |��ȧ����^��7L3��Y�ͯ Ŵ����E�Y�ܚ      �V&��h�F���y���O̫��`�\�-⃐�Hx��2��K��i�x�#e�>�VO��p{�      ���MUb4���gQ��eE}:�g���j8�����<.�e��S��e 0�����]7�������b�<�~G=1�������B׃�"
                                                                                     ���W��9ؽ5lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
���K�~�+��9"T���*Z$���"�r�
�Z�\�������ж�q���7����/�n��n
```
another method is to use the file command on all the files to find the ascii file that stores the password
```
bandit4@bandit:~/inhere$ file ./-*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
```
