n = int(input())
k = list(input())

s = 0
t = 0

for i in k:
    if i == 's':
        s += 1
    if i == 't':
        t += 1

for idx in range(len(k)):
    if s == t:
        print("".join(k[idx:]))
        break
    else:
        if k[idx] == 's':
            s -= 1
        if k[idx] == 't':
            t -= 1
