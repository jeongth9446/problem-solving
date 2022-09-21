import sys


def chk(x: int, y: int, k: int):
    global board
    global blue_paper
    global white_paper

    # one paper
    if k == 1:
        if board[x][y] == 0:
            white_paper += 1
        else:
            blue_paper += 1
        return

    # check all 1
    flag = 0
    for i in range(x, x + k):
        for j in range(y, y + k):
            if board[i][j] == 0:
                flag = 1
    if flag == 0:
        blue_paper += 1
        return

    # check all 0
    flag = 0
    for i in range(x, x + k):
        for j in range(y, y + k):
            if board[i][j] == 1:
                flag = 1
    if flag == 0:
        white_paper += 1
        return

    chk(x, y, int(k / 2))
    chk(x, y + int(k / 2), int(k / 2))
    chk(x + int(k / 2), y, int(k / 2))
    chk(x + int(k / 2), y + int(k / 2), int(k / 2))


input = sys.stdin.readline

n = int(input())
blue_paper = 0
white_paper = 0

board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))

chk(0, 0, n)

print(white_paper)
print(blue_paper)
