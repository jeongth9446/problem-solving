n = int(input())

for i in range(1, n+1):
    if i <= 10:
        for _ in range(i*i):
            print("*", end="")
        print()
    else:
        for _ in range(100):
            print("*", end="")
        print("...")


