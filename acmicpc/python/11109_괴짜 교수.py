import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    d, n, s, p = list(map(int, input().split()))

    if d + p * n > n * s:  # 병렬이 더 오래 걸린다
        print("do not parallelize")
    elif d + p * n < n * s:  # 직렬이 더 오래 걸린다
        print("parallelize")
    else:
        print("does not matter")
