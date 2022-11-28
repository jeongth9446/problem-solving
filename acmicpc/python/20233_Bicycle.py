a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

res1 = a + max(t - 30, 0) * x * 21
res2 = b + max(t - 45, 0) * y * 21

print(res1, res2)
