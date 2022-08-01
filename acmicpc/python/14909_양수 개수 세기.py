a = list(map(int, input().split()))

res = 0

for item in a:
    if item > 0:
        res += 1

print(res)