n = int(input())

for t in range(0, n):
    arr = list(input())
    cnt = 0
    res = 0
    for i in arr:
        if i == 'O':
            cnt += 1
            res += cnt
        else:
            cnt = 0

    print(res)

