a = list(map(int, list(input())))

k = 1
a.reverse()
flag = 0
res = list()
p = 0
for item in a:
    flag += 1
    p += item * k
    k *= 2
    if flag == 3:
        res.append(str(p))
        p = 0
        k = 1
        flag = 0
if flag != 0:
    res.append(str(p))

res.reverse()
print("".join(res))