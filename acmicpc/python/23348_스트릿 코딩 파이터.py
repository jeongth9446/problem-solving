a, b, c = list(map(int, input().split()))

n = int(input())

res = 0
for _ in range(n):
    p = 0
    for k in range(3):
        s = list(map(int, input().split()))
        p += s[0] * a + s[1] * b + s[2] * c

    res = max(res, p)

print(res)
