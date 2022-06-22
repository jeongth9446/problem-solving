import sys

A = [1, 1, 2, 2, 2, 8]

B = list(map(int, sys.stdin.readline().split()))

for i in range(0, 6):
    print(A[i] - B[i], end=" ")
