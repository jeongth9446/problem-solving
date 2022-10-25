n = int(input())

print("int a;")

for idx in range(1, n + 1):
    print("int ", end="")
    for _ in range(idx):
        print("*", end="")

    print("ptr", end="")

    if idx != 1:
        print(idx, end="")
    print(" = &", end="")

    if idx != 1:
        print("ptr", end="")
    else:
        print("a", end="")

    if idx > 2:
        print(idx - 1, end="")
    print(";")
