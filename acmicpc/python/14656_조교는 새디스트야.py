n = int(input())

arr = list(map(int, input().split()))

res = 0

for idx in range(n):
    if arr[idx] != idx + 1:
        res += 1

print(res)