n = int(input())

for _ in range(n):
    k = int(input())

    res = 0
    for j in range(1, k):
        if k % j == 0:
            res += j

    if res == k:
        print(k, "is a perfect number.")
    elif res < k:
        print(k, "is a deficient number.")
    else:
        print(k, "is an abundant number.")
    print()
