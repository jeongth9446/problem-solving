res1 = 0
res2 = 0

for i in range(1, 5+1):
    t = sum(list(map(int, input().split())))

    if res1 < t:
        res1 = t
        res2 = i

print(res2, res1)