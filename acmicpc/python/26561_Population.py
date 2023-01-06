n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))

    print(a + b // 4 - b // 7)
