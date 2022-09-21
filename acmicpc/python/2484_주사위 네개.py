n = int(input())

res = 0

for _ in range(n):
    a, b, c, d = list(map(int, input().split()))
    k = 0
    if a == b == c == d:
        k = 50000 + a*5000
    elif a == b == c:
        k = 10000 + a*1000
    elif b == c == d:
        k = 10000 + b * 1000
    elif c == d == a:
        k = 10000 + c * 1000
    elif d == a == b:
        k = 10000 + d * 1000
    elif a == b and c == d:
        k = 2000 + a * 500 + c * 500
    elif a == c and b == d:
        k = 2000 + a * 500 + b * 500
    elif a == d and b == c:
        k = 2000 + a * 500 + b * 500
    elif a == b or a == c or a == d:
        k = 1000 + a * 100
    elif b == c or b == d:
        k = 1000 + b * 100
    elif c == d:
        k = 1000 + c * 100
    else:
        k = max(a, b, c, d)*100

    if res < k:
        res = k

print(res)

