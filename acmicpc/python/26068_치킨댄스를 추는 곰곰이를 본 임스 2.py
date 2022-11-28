n = int(input())

res = 0

for _ in range(n):
    k = list(map(str, input().split("-")))
    if int(k[1]) <= 90:
        res += 1

print(res)
