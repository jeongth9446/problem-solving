t = int(input())

for _ in range(t):
    n = int(input())

    for i in range(n):
        if i == 0 or i == n - 1:
            print("".join(["#" for _ in range(n)]))
        else:
            print("#", end="")
            print("".join(["J" for _ in range(n - 2)]), end="")
            print("#")

    print()
