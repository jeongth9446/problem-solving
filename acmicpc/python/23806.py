n = int(input())

for i in range(n):
    print("".join(["@" for _ in range(n * 5)]))

for i in range(3 * n):
    print("".join("@" for _ in range(n)), end="")
    print("".join(" " for _ in range(n * 3)), end="")
    print("".join("@" for _ in range(n)))

for i in range(n):
    print("".join(["@" for _ in range(n * 5)]))
