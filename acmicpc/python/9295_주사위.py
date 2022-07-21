n = int(input())

for idx in range(1, n + 1):
    a, b = list(map(int, input().split()))
    print("Case " + str(idx) + ": " + str(a + b))

