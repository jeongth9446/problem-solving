n, m = list(map(int, input().split()))

S = set()

for i in range(n):
    S.add(input())

res = 0
for i in range(m):
    t = input()
    if t in S:
        res += 1

print(res)
