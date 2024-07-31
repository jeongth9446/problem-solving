n = int(input())

s = list(input())

chk = [0 for i in range(1000)]

for i in s:
    chk[ord(i)] += 1

p = 'u'
res = 0
while True:
    if chk[ord(p)] >= 1:
        chk[ord(p)] -= 1
        if p == 'u':
            p = 'o'
        elif p == 'o':
            p = 's'
        elif p == 's':
            p = 'p'
        elif p == 'p':
            p = 'c'
        elif p == 'c':
            res += 1
            p = 'u'
    else:
        break
print(res)