n = int(input())


def a(x):
    for _ in range(x):
        for _ in range(x * 3):
            print("@", end="")
        for _ in range(x):
            print(" ", end="")
        for _ in range(x):
            print("@", end="")
        print()


def b(x):
    for _ in range(x):
        for _ in range(x):
            print("@", end="")
        for _ in range(x):
            print(" ", end="")
        for _ in range(x):
            print("@", end="")
        for _ in range(x):
            print(" ", end="")
        for _ in range(x):
            print("@", end="")
        print()


def c(x):
    for _ in range(x):
        for _ in range(x):
            print("@", end="")
        for _ in range(x):
            print(" ", end="")
        for _ in range(x * 3):
            print("@", end="")
        print()


a(n)
b(n)
b(n)
b(n)
c(n)
