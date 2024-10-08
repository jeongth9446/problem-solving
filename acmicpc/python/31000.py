n = int(input())

res = 0

for a in range(-n, n + 1):
    for b in range(-n, n + 1):
        if -n <= 1 - a - b <= n and a != 0:
            res += 1

res += ((n + 1) * 2 - 1) * ((n + 1) * 2 - 1)

print(res)
