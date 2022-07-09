n = int(input())
res = 0

for i in range(1, n+1):
    res += int(i*(i+1)*(1+0.5))

print(res)