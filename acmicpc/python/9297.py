n = int(input())

for i in range(n):
    a, b = list(map(int, input().split()))

    print("Case " + str(i + 1) + ":", end="")

    if a == 0:
        print(" 0", end="")
    else:
        if a >= b:
            print(" " + str(a // b), end="")
        if a % b != 0:
            print(" " + str(a % b) + "/" + str(b), end="")
    print()
