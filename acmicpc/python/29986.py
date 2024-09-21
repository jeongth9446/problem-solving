n, h = list(map(int, input().split()))

a = list(map(int, input().split()))

res = 0

for i in a:
    if i <= h:
        res += 1

print(res)