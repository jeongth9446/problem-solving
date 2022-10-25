n = int(input())

board = list()
board_a = list()
board_b = list()

for idx in range(n):
    board.append(list(input()))
    board_a.append(board[idx].copy())
    board_b.append(board[idx].copy())

# print(board)
a = 0
for i in range(n):
    for j in range(n - 1):
        if board_a[i][j] == '.' and board_a[i][j + 1] == '.' and \
                (j == 0 or board_a[i][j - 1] == 'X' or j == n - 3 or board_a[i][j + 2] == 'X'):
            a += 1
            for k in range(j, n):
                if board_a[i][k] == '.':
                    board_a[i][k] = '?'
                else:
                    break
    # print(a)
# print(board_a)
# print(board_b)
b = 0
for i in range(n):
    for j in range(n - 1):
        if board_b[j][i] == '.' and board_b[j + 1][i] == '.' and \
                (j == 0 or board_b[j - 1][i] == 'X' or j == n - 3 or board_b[j + 2][i] == 'X'):
            b += 1
            for k in range(j, n):
                if board_b[k][i] == '.':
                    board_b[k][i] = '?'
                else:
                    break
    # print(b)
print(a, b)
