n = int(input())

for _ in range(n):
    t = int(input())
    if t % 2 == 0:
        print(str(t) + " is even")
    else:
        print(str(t) + " is odd")
