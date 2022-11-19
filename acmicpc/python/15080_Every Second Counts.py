a, b, c = list(map(int, input().split(" : ")))
x, y, z = list(map(int, input().split(" : ")))

n = a * 3600 + b * 60 + c
m = x * 3600 + y * 60 + z

if m >= n:
    print(m - n)
else:
    print(m - n + 3600 * 24)
