import sys

input = sys.stdin.readline

t = int(input().strip())


for _ in range(t):
    n = int(input().strip())
    A, B, C = list(), list(), list()
    res = 0
    for i in range(n):
        a, b, c = list(map(int, input().split()))
        A.append(a)
        B.append(b)
        C.append(c)

    for idx in range(n):
        # print(max(A[idx], B[idx], C[idx], 0))
        res += max(A[idx], B[idx], C[idx], 0)

    print(res)
