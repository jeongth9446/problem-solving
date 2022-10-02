n, m = list(map(int, input().split()))

res = 1

arr = list(map(int, input().split()))

for item in arr:
    res *= item % m
    res %= m

print(res)
