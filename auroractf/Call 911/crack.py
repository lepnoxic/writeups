a = "djcj{mbbs_sludok_ki_sfxpegzng}"
p = "379411500469" * 3

alpha = "abcdefghijklmnopqrstuvwxyz"

offset = 0

for i in range(len(a)):
    if a[i] in "{}_": 
        print(a[i], end="")
        offset += 1
        continue
    print(alpha[(alpha.find(a[i]) - int(p[i - offset]) ) % 26], end="")
