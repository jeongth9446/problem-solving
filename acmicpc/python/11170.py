t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))

    res = 0
    for j in range(n, m+1):
        res += str(j).count('0')

    print(res)
