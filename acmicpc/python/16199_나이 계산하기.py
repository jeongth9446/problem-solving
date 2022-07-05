y, m, d = list(map(int, input().split()))
yy, mm, dd = list(map(int, input().split()))

res2 = yy - y + 1
res3 = yy - y

if m > mm:
    res1 = 0
elif m < mm:
    res1 = 1
else:
    if d > dd:
        res1 = 0
    elif d < dd:
        res1 = 1
    else:
        res1 = 1

res1 += yy-y-1


print(res1)
print(res2)
print(res3)