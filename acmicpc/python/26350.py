n = int(input())

for i in range(n):
    a = list(map(str, input().split()))
    a = a[1:]

    print("Denominations:", " ".join(a))

    flag = 0
    for j in range(len(a) - 1):
        v = int(a[j])
        w = int(a[j + 1])

        if w < v * 2:
            flag = 1

    if (flag == 0):
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()
