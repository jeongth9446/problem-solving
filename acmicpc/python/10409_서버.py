n, T = list(map(int, input().split()))

s = list(map(int, input().split()))

res = 0
m = 0
for item in s:
    m += item
    if m <= T:
        res += 1
    else:
        break

print(res)