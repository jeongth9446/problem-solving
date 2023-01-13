n = int(input())
a = list(map(int, input().split()))

k = 0
p = 2
res = 0
for item in a:
    if k != item:
        p = 2
    else:
        p *= 2
    if res + p >= 100:
        res = 0
        p = 1
    else:
        res += p
    # print(res)
    k = item

print(res)
