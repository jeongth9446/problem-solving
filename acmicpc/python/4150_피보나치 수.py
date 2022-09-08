n = int(input())

a = 0
b = 1

for _ in range(n):
    c = a + b
    a = b
    b = c

print(a)
