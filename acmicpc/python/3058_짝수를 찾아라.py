t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    m = 101
    s = 0
    for item in arr:
        if item % 2 == 0:
            s += item
            m = min(m, item)

    print(s, m)
