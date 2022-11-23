g, p, t = list(map(int, input().split()))

a = g * p
b = g + t * p

if a > b:
    print(2)
elif a < b:
    print(1)
else:
    print(0)
