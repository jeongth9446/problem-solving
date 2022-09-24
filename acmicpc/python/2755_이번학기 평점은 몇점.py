n = int(input())

res = 0
k = 0
for _ in range(n):
    a, b, c = list(map(str, input().split()))
    b = int(b)
    k += b
    c = list(c)
    d = 0
    if c[0] == "F":
        d = 0
    else:
        if c[0] == "A":
            d = 4.0
        elif c[0] == "B":
            d = 3.0
        elif c[0] == "C":
            d = 2.0
        elif c[0] == "D":
            d = 1.0

        if c[1] == "+":
            d += 0.3
        elif c[1] == "0":
            d += 0.0
        elif c[1] == "-":
            d -= 0.3
    res += d * b

p = res / k * 1000

if p % 10 >= 5:
    p = p - p % 10 + 10
else:
    p = p - p % 10

print("{0:0.2f}".format(p / 1000))
