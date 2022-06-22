import sys

n, m = list(map(int, sys.stdin.readline().split()))

arr = [0 for item in range(0, 10)]


def func(n: int, m: int, k: int, c: int):
    if m == k:
        for i in range(1, m+1):
            print(arr[i], end=" ")

        print()
        return

    for i in range(c, n+1):
        arr[k+1] = i
        func(n, m, k+1, i)
        arr[k+1] = 0


func(n, m, 0, 1)
