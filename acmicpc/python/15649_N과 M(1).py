import sys

n, m = list(map(int, sys.stdin.readline().split()))

arr = [0 for item in range(0, 10)]


def func(n: int, m: int, k: int):
    if m == k:
        for j in range(1, m+1):
            for i in range(1, n+1):
                if arr[i] == j:
                    print(i, end=" ")

        print()
        return

    for i in range(1, n+1):
        if arr[i] == 0:
            arr[i] = k+1
            func(n, m, k+1)
            arr[i] = 0


func(n, m, 0)
