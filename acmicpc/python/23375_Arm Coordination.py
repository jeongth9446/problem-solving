x, y = list(map(int, input().split()))
r = int(input())

a, b = x - r, y - r
c, d = x + r, y + r

print(a, b)
print(a, d)
print(c, d)
print(c, b)
