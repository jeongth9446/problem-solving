n = int(input())

for i in range(1, n * 2):
    for j in range(min(i, n * 2 - i)):
        print("*", end="")
    for j in range(abs(n - i) * 2):
        print(" ", end="")
    for j in range(min(i, n * 2 - i)):
        print("*", end="")

    print()
