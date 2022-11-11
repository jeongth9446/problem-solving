p1, q1, p2, q2 = list(map(int, input().split()))

res = p1 / q1 * p2 / q2 / 2

if res == int(res):
    print(1)
else:
    print(0)
