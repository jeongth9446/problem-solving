n, k = list(map(int, input().split()))

res = 0

for i in range(n):
    a = int(input())
    if i == 0:
        p = a
    else:
        if p - k >= a:
            res += 1
            # print(p, a)
        p = a

print(res)
