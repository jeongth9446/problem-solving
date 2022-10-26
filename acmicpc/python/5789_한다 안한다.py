t = int(input())

for _ in range(t):
    a = list(input())

    res = "Do-it"

    start = 0
    end = len(a) - 1

    while start < end:
        if a[start] == a[end]:
            res = "Do-it"
        else:
            res = "Do-it-Not"
        start += 1
        end -= 1

    print(res)
