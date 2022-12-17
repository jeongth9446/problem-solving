def f2(v: int):
    c = 0

    global n, s, k

    for item in s:
        c += item // v
        if c >= k:
            return True
    return False


def f():
    l = 0
    h = 10000000000000000

    while h >= l:
        m = (l + h) // 2
        if f2(m):
            l = m + 1
        else:
            h = m - 1
    return h


n, k = list(map(int, input().split()))

s = list()

for _ in range(n):
    s.append(int(input()))

res = f()
if res == -1:
    print(0)
else:
    print(res)
