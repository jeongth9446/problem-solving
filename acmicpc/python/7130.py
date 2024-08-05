m, h = list(map(int, input().split()))
n = int(input())

res = 0
for i in range(n):
    c, b = list(map(int, input().split()))
    res += max(c*m, b*h)

print(res)