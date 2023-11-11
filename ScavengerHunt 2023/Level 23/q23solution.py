key = {};
current = 300;
for i in "abcdefghijklmnopqrstuvwxyz":
    key[current] = i;
    current += 100;
cipher = [1000, 700, 1400, 1400, 1700, 2200, 2000, 300, 2400, 700, 1400, 1400, 700, 2000]
for i in cipher:
    print(key[i], end="")