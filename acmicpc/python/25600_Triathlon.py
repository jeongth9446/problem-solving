n = int(input())

res = 0

for _ in range(n):
    a, d, g = list(map(int, input().split()))

    k = a * (d + g)
    if a == d + g:
        k *= 2
    if res < k:
        res = k

print(res)
