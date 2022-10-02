n = int(input())

res = 0
for _ in range(n):
    m = list(map(int, input().split()))

    res += sum(m)

print(res)