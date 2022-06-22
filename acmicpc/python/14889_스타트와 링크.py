import sys

input = sys.stdin.readline

S = set()

n = int(input())

a = list()
min = 1000000000
for i in range(0, n):
    a.append(list(map(int, input().split())))


def func(k: int, m: int):
    global min
    if k == n / 2:  # 다 골랐다면

        res1 = 0
        res2 = 0

        for j in range(0, n):
            for i in range(0, n):
                if i in S and j in S:
                    res1 += a[i][j]
                if i not in S and j not in S:
                    res2 += a[i][j]
        # print(S, res1, res2)
        if min > abs(res1 - res2):
            min = abs(res1 - res2)
            # print(min, S)
    else:
        for i in range(m, n):
            S.add(i)
            func(k + 1, i + 1)
            S.remove(i)


func(0, 0)

print(min)
