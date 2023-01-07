h = int(input())

if h == 0:
    print(1)
elif h == 1:
    print(0)
else:
    if (h % 2 == 0):
        for _ in range(h // 2):
            print(8, end="")
    else:
        print(4, end="")
        for _ in range(h // 2):
            print(8, end="")
