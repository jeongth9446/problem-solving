n = int(input())

res = 0
for i in range(1, n + 1):
    for j in range(i, (n - i) // 2 + 1):
        k = n - i - j
        if max(i, j, k) < i + j + k - max(i, j, k):
            # print(i, j, k)
            res += 1

print(res)
