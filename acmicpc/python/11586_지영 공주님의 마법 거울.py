import sys

input = sys.stdin.readline

n = int(input())

board = list()

for _ in range(n):
    board.append(list(input().strip()))

k = int(input())

if k == 1:
    for item in board:
        print("".join(item))
elif k == 2:
    for item in board:
        print("".join(reversed(item)))
else:
    for item in board[-1::-1]:
        print("".join(item))
