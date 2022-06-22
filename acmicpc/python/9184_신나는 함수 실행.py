import sys

N = 20
W = [[[0 for x in range(0, N+1)] for y in range(0, N+1)] for z in range(0, N+1)]


for i in range(0, N+1):
    for j in range(0, N+1):
        for k in range(0, N+1):
            if i == 0 or j == 0 or k == 0:
                W[i][j][k] = 1
            elif i < j < k:
                W[i][j][k] = W[i][j][k-1] + W[i][j-1][k-1] - W[i][j-1][k]
            else:
                W[i][j][k] = W[i-1][j][k] + W[i-1][j-1][k] + W[i-1][j][k-1] - W[i-1][j-1][k-1]


def func(x: int, y: int, z: int):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    elif x > 20 or y > 20 or z > 20:
        return W[20][20][20]
    else:
        return W[x][y][z]


while True:
    x, y, z = list(map(int, sys.stdin.readline().split()))

    if x == y == z == -1:
        break

    print("w(", x, ", ", y, ", ", z, ") = ", func(x, y, z), sep="")
