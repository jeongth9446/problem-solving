n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))

    res = a - b // 7 + b // 4

    print(res)