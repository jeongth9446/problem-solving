t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))

    print(m - (n - m), n - m)
