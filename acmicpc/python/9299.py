t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    n = a[0]
    a = a[1:]
    print("Case " + str(i + 1) + ":", end=" ")
    print(n - 1, end=" ")

    for i in range(n):
        print(a[i] * (n - i), end=" ")

    print()
