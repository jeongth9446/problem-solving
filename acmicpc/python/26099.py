n = int(input())

res = 0
while n % 5:
    n -= 3
    res += 1

if n < 0:
    print(-1)
else:
    print(res + n // 5)