a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

res = 0
k = a/c + b/d

for i in range(1, 4):
    a, b, c, d = c, a, d, b
    if k < a/c + b/d:
        k = a/c + b/d
        res = i

print(res)