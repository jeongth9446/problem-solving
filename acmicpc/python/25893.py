n = int(input())

for i in range(n):
    a, b, c = list(map(int, input().split()))

    print(a, b, c)

    res = 0
    if a >= 10:
        res += 1
    if b >= 10:
        res += 1
    if c >= 10:
        res += 1

    if res == 0:
        print("zilch")
    elif res == 1:
        print("double")
    elif res == 2:
        print("double-double")
    elif res == 3:
        print("triple-double")

    print()