n = int(input())


def a(x):
    for _ in range(x):
        for j in range(x):
            print("@", end="")
        for _ in range(3):
            for j in range(x):
                print(" ", end="")
        for j in range(x):
            print("@", end="")
        print()


def b(x):
    for _ in range(x):
        for j in range(x * 5):
            print("@", end="")
        print()


a(n)
b(n)
a(n)
b(n)
a(n)
