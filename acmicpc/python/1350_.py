n = int(input())

a = list(map(int, input().split()))

k = int(input())

res = 0

for item in a:
    if item % k == 0:
        res += item
    else:
        res += ((item // k) + 1) * k

print(res)
