n = int(input())

res = 0

for _ in range(n):
    k = input()

    res = max(k.count('for') + k.count('while'), res)

print(res)
