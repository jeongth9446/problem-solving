s = input()

n = int(input())
res = 0
for _ in range(n):
    k = input()

    if s == k:
        res += 1

print(res)
