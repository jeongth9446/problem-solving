n = int(input())
t = list(map(int, input().split()))

res = -8

for i in t:
    res += i + 8

print(res // 24, res % 24)
