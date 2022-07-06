n = int(input())

for i in range(n * 2 - 1):
    for j in range(abs(n - i - 1)):
        print(" ", end="")
    for j in range((n - (abs(n - i - 1))) * 2 - 1):
        print("*", end="")
    print()
