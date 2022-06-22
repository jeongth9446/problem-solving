import collections

board = collections.defaultdict(int)

for i in range(0, 28):
    t = int(input())
    board[t] = 1


for i in range(1, 31):
    if board[i] == 0:
        print(i)

