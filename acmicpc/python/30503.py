n = int(input())

a = list(map(int, input().split()))

q = int(input())

for _ in range(q):
    b = list(map(int, input().split()))

    if b[0] == 1:
        res = 0
        for i in range(b[1] - 1, b[2]):
            if b[3] == a[i]:
                res += 1
        print(res)
    else:
        for i in range(b[1] - 1, b[2]):
            a[i] = 0
