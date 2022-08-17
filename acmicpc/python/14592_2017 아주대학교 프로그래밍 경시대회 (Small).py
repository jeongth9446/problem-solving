import sys

input = sys.stdin.readline

n = int(input())

board = list()
for i in range(1, n + 1):
    a, b, c = list(map(int, input().split()))
    board.append([i, a, b, c])

board.sort(key=lambda x: (-x[1], x[2], x[3]))

# print(board)
print(board[0][0])
