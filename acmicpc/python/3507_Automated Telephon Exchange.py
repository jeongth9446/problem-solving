n = int(input())

res = 0

for i in range(100):
    for j in range(100):
        if n - j - i == 0:
            res += 1
print(res)
