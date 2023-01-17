a, b, c, d = list(map(int, input().split()))

m = a * b
p = c * d

if m > p:
    print("M")
elif m < p:
    print("P")
else:
    print("E")
