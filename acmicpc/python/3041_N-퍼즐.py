
comp = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', '.']]

board = list()

for _ in range(4):
    board.append(list(input()))

# print(board)

res = 0
for i in range(4):
    for j in range(4):
        for x in range(4):
            for y in range(4):
                if comp[x][y] == board[i][j] and comp[x][y] != '.':
                    res += abs(x-i) + abs(y-j)

print(res)