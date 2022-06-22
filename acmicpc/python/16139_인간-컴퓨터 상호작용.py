import collections
import sys

s = sys.stdin.readline().strip()

board = collections.defaultdict()

for i in range(ord('a'), ord('z')+1):
    board[chr(i)] = list()


for index, item in enumerate(s):
    t = ord(item)
    for i in range(ord('a'), ord('z') + 1):
        if i == t:
            if index == 0:
                board[chr(i)].append(1)
            else:
                board[chr(i)].append(board[chr(i)][-1] + 1)
        else:
            if index == 0:
                board[chr(i)].append(0)
            else:
                board[chr(i)].append(board[chr(i)][-1])

n = int(sys.stdin.readline())

# print(board)
for i in range(0, n):
    k, start, end = list(map(str, sys.stdin.readline().split()))
    if int(start) == 0:
        sys.stdout.write(str(board[k][int(end)]) + "\n")
    else:
        sys.stdout.write(str(board[k][int(end)] - board[k][int(start)-1]) + "\n")
