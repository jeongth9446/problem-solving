a, b, c = list(map(int, input().split()))

if a + b == c:
    print(str(a)+"+"+str(b) + "="+str(c))
elif a - b == c:
    print(str(a) + "-" + str(b) + "=" + str(c))
elif a * b == c:
    print(str(a) + "*" + str(b) + "=" + str(c))
elif a / b == c:
    print(str(a) + "/" + str(b) + "=" + str(c))
elif a == b + c:
    print(str(a) + "=" + str(b) + "+" + str(c))
elif a == b - c:
    print(str(a) + "=" + str(b) + "-" + str(c))
elif a == b * c:
    print(str(a) + "=" + str(b) + "*" + str(c))
elif a == b / c:
    print(str(a) + "=" + str(b) + "/" + str(c))

