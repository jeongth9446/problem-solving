a, b, c = list(map(int, input().split()))

if a + b + c - max(a, b, c) <= max(a, b, c):
    print((a + b + c - max(a, b, c))*2 - 1)
else:
    print(a+b+c)