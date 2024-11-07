n = int(input())

for i in range(n):
    a, b, c = list(map(str, input().split()))
    b, c = int(b), int(c)

    for j in range(len(a)):
        if j < b or j >= c:
            print(a[j], end="")
    print()
