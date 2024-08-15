def printLine(col, w, x, y):
    print(x, end="")
    for i in range(col):
        for j in range(w):
            print(y, end="")
        print(x, end="")
    print()


n = int(input())

for t in range(1, n + 1):
    row, col, w, h = list(map(int, input().split()))

    print("Case #" + str(t) + ":")
    printLine(col, w, "+", "-")
    for _ in range(row):
        for i in range(h):
            printLine(col, w, "|", "*")
        printLine(col, w, "+", "-")
