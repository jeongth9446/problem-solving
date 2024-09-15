n = int(input())

s = 0
res = 0

for i in range(1, n + 1):
    s += i
    res += 1
    if s > n:
        res -= 1
        break

print(res)
