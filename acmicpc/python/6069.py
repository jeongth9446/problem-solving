n, m = list(map(int, input().split()))

lst = [0 for _ in range(n)]

for _ in range(m):
    a, b, c = list(map(int, input().split()))

    if a == 0:
        for j in range(b - 1, c):
            lst[j] = abs(lst[j] - 1)
        # print(lst)
    elif a == 1:
        res = 0
        for j in range(b - 1, c):
            if lst[j] == 1:
                res += 1
        print(res)
