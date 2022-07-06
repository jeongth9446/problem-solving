a = list(map(int, input().split()))
a.sort()

if a[0] - a[1] == a[1] - a[2]:
    print(a[2] + (a[2] - a[1]))
else:
    if a[1] - a[0] > a[2] - a[1]:
        print(int((a[1] + a[0]) / 2))
    else:
        print(int((a[2] + a[1]) / 2))
