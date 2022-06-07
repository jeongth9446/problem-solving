n, m = map(int, input().split())

board = list()

for t in range(0, n):
    board.append(list(input()))

res = n * m
for i in range(0, n):
    for j in range(0, m):
        if i + 8 > n or j + 8 > m:
            continue
        cnt = 0
        for k in range(0, 8):
            for l in range(0, 8):
                if (k + l) % 2:
                    flag = True
                else:
                    flag = False

                if board[i + k][j + l] == 'W' and flag == False:
                    cnt += 1
                elif board[i + k][j + l] == 'B' and flag == True:
                    cnt += 1

        if cnt < res:
            res = cnt

        cnt = 0
        for k in range(0, 8):
            for l in range(0, 8):
                if (k + l) % 2:
                    flag = False
                else:
                    flag = True

                if board[i + k][j + l] == 'W' and flag == False:
                    cnt += 1
                elif board[i + k][j + l] == 'B' and flag == True:
                    cnt += 1

        if cnt < res:
            res = cnt

print(res)
