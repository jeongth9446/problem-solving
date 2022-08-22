t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    if n < 12:
        print(-1)
    elif m < 4:
        print(-1)
    else:
        print(m*11 + 4)
