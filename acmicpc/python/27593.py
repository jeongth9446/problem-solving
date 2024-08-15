t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    if a[0] != 0:
        a = [0] + a
    a.append(1440)

    res = 0
    for i in range(1, len(a)):
        res += (a[i] - a[i - 1]) // 120

    if res >= 2:
        print("YES")
    else:
        print("NO")
