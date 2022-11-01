t = int(input())

for _ in range(t):

    res = 0

    a, b = list(map(int, input().split()))

    for k in range(a, b + 1):
        s = list(str(k))

        for item in s:
            if item == '0':
                res += 1

    print(res)
   