t = int(input())
s = int(input())
h = int(input())

for _ in range(t):
    print("*", end="")
    for _ in range(s):
        print(" ", end="")
    print("*", end="")
    for _ in range(s):
        print(" ", end="")
    print("*")

for _ in range(s * 2 + 3):
    print("*", end="")
print()
for _ in range(h):
    for _ in range(s + 1):
        print(" ", end="")
    print("*")
