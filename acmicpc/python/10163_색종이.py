import sys

input = sys.stdin.readline
n = int(input())
board = [[0 for i in range(1001)] for j in range(1001)]
res = [0 for i in range(1001)]
for k in range(1, n+1):
    x, y, w, h = list(map(int, input().split()))

    for i in range(x, x+w):
        for j in range(y, y+h):
            board[i][j] = k

for i in range(1001):
    for j in range(1001):
        res[board[i][j]] += 1

for i in range(1, n+1):
    print(res[i])