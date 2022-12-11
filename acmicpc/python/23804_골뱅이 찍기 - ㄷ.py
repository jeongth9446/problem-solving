n = int(input())


def a(x):
    for _ in range(x):
        for _ in range(x * 5):
            print("@", end="")
        print()


def b(x):
    for _ in range(x):
        for _ in range(x):
            print("@", end="")
        print()
a(n)
b(n)
b(n)
b(n)
a(n)

