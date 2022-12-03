import math

n = int(input())

p = int(math.sqrt(n))

a = p
b = p

if a * b < n:
    a += 1
    if a * b < n:
        b += 1

print(a, b)
