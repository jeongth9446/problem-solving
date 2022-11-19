n = int(input())

for _ in range(n):
    mack = False
    zack = False

    k = list(map(int, input().split()))

    for item in k:
        print(item, end=" ")
        if item == 18:
            mack = True
        elif item == 17:
            zack = True
    print()
    if mack and zack:
        print("both", end="\n\n")
    elif mack:
        print("mack", end="\n\n")
    elif zack:
        print("zack", end="\n\n")
    else:
        print("none", end="\n\n")
