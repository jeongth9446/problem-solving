t = int(input())

for _ in range(t):
    a, b, c = list(map(int, input().split()))

    res = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                if i % j == j % k == k % i:
                    res += 1

    print(res)
