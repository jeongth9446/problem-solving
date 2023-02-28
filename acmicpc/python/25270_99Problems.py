n = int(input())

res = 0
dif = 10000

for i in range(9999, 0, -100):
    if (abs(n - i) < dif):
        dif = abs(n - i)
        res = i

print(res)
