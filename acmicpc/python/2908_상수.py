x, y = map(list, (input().split()))

x.reverse()
y.reverse()

if x > y:
    print("".join(x))
else:
    print("".join(y))
