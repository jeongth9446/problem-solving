n = int(input())

board = list()

for _ in range(n):
    board.append(list(map(int, input().split())))

res1 = 0
res2 = 0

for idx in range(n):
    chk = [0 for _ in range(n)]
    for i in range(5):
        for j in range(n):
            if idx == j:
                continue
            if board[idx][i] == board[j][i]:
                chk[j] = 1

    if res1 < sum(chk):
        res1 = sum(chk)
        res2 = idx

print(res2 + 1)
