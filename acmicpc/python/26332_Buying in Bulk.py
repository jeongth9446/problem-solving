n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))
    print(a, b)
    print(a * b - (a - 1) * 2)
