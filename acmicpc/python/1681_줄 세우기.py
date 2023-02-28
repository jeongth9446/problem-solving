n, l = list(map(int, input().split()))

c = 0
res = 0
for i in range(1, 10000000):
    t = list(str(i))
    if t.count(str(l)) == 0:
        # print(i)
        c += 1

    if c == n:
        res = i
        break

print(res)
