n = int(input())

res = 0

for i in range(n):
    if int(input()) % 2 == 1:
        res += 1

print(res)