board = [[0 for i in range(101)] for j in range(101)]

# print(board)

for _ in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

res = 0

for i in range(101):
    for j in range(101):
        res += board[i][j]

print(res)
