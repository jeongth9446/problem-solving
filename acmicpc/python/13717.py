n = int(input())

rc = 0
res2 = 0

for i in range(n):
    p = input()

    k, m = list(map(int, input().split()))

    c = 0
    while m >= k:
        c += m // k
        m = m - (m // k) * k + (m // k) * 2
    res2 += c

    if c > rc:
        rc = c
        res = p

print(res2)
print(res)
