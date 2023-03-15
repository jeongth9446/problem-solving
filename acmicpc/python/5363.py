n = int(input())

for _ in range(n):
    t = list(map(str, input().split()))

    for i in range(2, len(t)):
        print(t[i], end=" ")
    print(t[0], end=" ")
    print(t[1])