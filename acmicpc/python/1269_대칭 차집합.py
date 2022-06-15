import sys

n, m = list(map(int, sys.stdin.readline().split()))

arr_n = list(map(int, sys.stdin.readline().split()))
arr_m = list(map(int, sys.stdin.readline().split()))

A = set()
B = set()
for i in arr_n:
    A.add(i)

for i in arr_m:
    B.add(i)

print(len(A) + len(B) - 2 * len(A.intersection(B)))
