n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))
    res = a + b
    if res > 50:
        print(50)
    else:
        print(res - 1)
