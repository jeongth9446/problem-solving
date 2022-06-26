a, b, c = list(map(int, input().split()))

m = max(a, b, c)

if a == b == c:
    print("2")
elif a * a + b * b + c * c == 2 * m * m:
    print("1")
else:
    print("0")
