n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    zack = 0
    mack = 0

    for j in a:
        print(j, end=" ")
        if j == 18:
            mack += 1
        if j == 17:
            zack += 1
    print()
    if mack + zack == 2:
        print("both")
    elif mack == 1:
        print("mack")
    elif zack == 1:
        print("zack")
    else:
        print("none")
    print()
