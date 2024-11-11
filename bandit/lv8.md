# Level 8

Given to find 1 unique line so i tried to use uniq command and giving the count option and used grep to find which had count 1

```
bandit8@bandit:~$ cat data.txt | uniq -c | grep 1
      1 kjIuqjobFBhKw9Mmfj2wAnWbXB2VxSfv
      1 5Y76FifuxKStZi4CVovF2uPhgLrZnLzG
      1 AiYd84lOOVTA4gqJPX7f6DH8eG3zwq1W
      1 A16BW831T94qcsYcGDSkgzYhxnX2xUdK
      1 vlsSKqk3yVx2PZxIkBuZPR3KKIf8hGi1
      1 cEqNrEqHVIIi9fQKdcvAxaip1brmsSxT
      1 FQIgwPiuPKftkFhIy9Nzm94sWdNGTlHd
      1 P8jd7Kr8GXVKTLhe1Y7cVYAARwh4lN4A
      ...
```

it turns out that uniq only works for the consecutive occurences so i used the sort command to first sort the text

```
bandit8@bandit:~$ sort data.txt | uniq -u -c | grep 1
      1 EN632PlfYiZbn3PhVK3XOGSlNInNE00t
```