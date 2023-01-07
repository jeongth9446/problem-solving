n = int(input())

for _ in range(n):
    a, b = list(map(float, input().split()))
    print(format(abs(a-b), ".1f"))