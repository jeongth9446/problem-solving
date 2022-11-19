n = int(input())

k = list(map(float, input().split()))

res = 0
for item in k:
    res += pow(item, 3)

print(pow(res, 1/3))