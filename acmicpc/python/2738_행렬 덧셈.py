import sys

A = [[0 for col in range(0, 101)] for row in range(0, 101)]
B = [[0 for col in range(0, 101)] for row in range(0, 101)]

N, M = list(map(int, sys.stdin.readline().split()))

for i in range(0, N):
    A[i] = list(map(int, sys.stdin.readline().split()))

for i in range(0, N):
    B[i] = list(map(int, sys.stdin.readline().split()))

for i in range(0, N):
    for j in range(0, M):
        print(A[i][j] + B[i][j], end=" ")
    print()
