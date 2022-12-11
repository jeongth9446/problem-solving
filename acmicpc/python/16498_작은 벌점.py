import sys


def b_search(x: int, arr: []):
    start = 0
    end = len(arr) - 1
    while True:
        # print(start, end)
        p = (start + end) // 2
        if start == p:
            if p == end:
                return arr[p]
            else:
                return arr[p]

        if arr[p] == x:
            return x
        elif arr[p] < x:
            start = p
            continue
        elif arr[p] > x:
            end = p
            continue


input = sys.stdin.readline

t = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

penalty = 1000000000 * 2

for i in a:
    j = b_search(i, b)
    k = b_search(i, c)
    # print("Res", j, k)
    # print(i, j, k)
    penalty = min(penalty, abs(max(i, j, k) - min(i, j, k)))

for i in b:
    j = b_search(i, c)
    k = b_search(i, a)
    # print("Res", j, k)
    # print(i, j, k)
    penalty = min(penalty, abs(max(i, j, k) - min(i, j, k)))

for i in c:
    j = b_search(i, a)
    k = b_search(i, b)
    # print("Res", j, k)
    # print(i, j, k)
    penalty = min(penalty, abs(max(i, j, k) - min(i, j, k)))

print(penalty)
