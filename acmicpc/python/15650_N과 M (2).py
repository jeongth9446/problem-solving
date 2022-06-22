import sys

n, m = list(map(int, sys.stdin.readline().split()))

arr = [0 for item in range(0, 10)]


def func(n: int, m: int, k: int, c: int):
    if m == k:
        for i in range(1, n+1):
            if arr[i] == 1:
                print(i, end=" ")

        print()
        return

    for i in range(c, n+1):
        if arr[i] == 0:
            arr[i] = 1
            func(n, m, k+1, i+1)
            arr[i] = 0


func(n, m, 0, 1)
