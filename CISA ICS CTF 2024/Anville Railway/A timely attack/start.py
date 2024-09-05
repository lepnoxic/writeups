import time
import subprocess

wordlist = 'abcdefghijklmnopqrstuvwxyz0123456789'
password = ''
time_count = {}

for a in range(8):
    for i in wordlist:
        current = []
        for b in range(3):
            start_time = time.perf_counter()
            subprocess.run(['./time_attack1', password + i + '0' * (7 - len(password))])
            end_time = time.perf_counter()
            current.append(end_time - start_time)
        time_count[i] = sum(current) / len(current)
    char_found = max(time_count, key=time_count.get)
    print('char found: ', char_found)
    password += char_found

print(password)
subprocess.run(['./time_attack1', password])
