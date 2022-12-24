n = int(input())
b = 8
res = 1
while n >= b:
    res += 1
    b = b // res * (res + 1) * 2

print(res)
