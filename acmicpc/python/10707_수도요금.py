a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

ax = a * p
bx = b + max(0, p - c) * d

print(min(ax, bx))