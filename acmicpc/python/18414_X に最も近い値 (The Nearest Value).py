x, l, r = list(map(int, input().split()))

if l <= x <= r:
    print(x)
elif x > r:
    print(r)
elif x < l:
    print(l)
