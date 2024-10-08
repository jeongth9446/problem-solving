a, b = list(map(int, input().split()))

if (a * b / 4840 % 5 == 0):
    print(int(a * b / 4840 // 5))
else:
    print(int(a * b / 4840 // 5) + 1)
