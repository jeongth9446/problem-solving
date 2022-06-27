import sys

input = sys.stdin.readline
n = int(input())

S = list()

for i in range(n):
    a, b = input().split()
    S.append([i + 1, float(a), int(b), int(float(a) * int(b) * 10) / 10, 1])

# print(S[i])

S.sort(key=lambda x: (-x[3], x[0]))

for i in range(n):
    print(S[i][0], end=" ")