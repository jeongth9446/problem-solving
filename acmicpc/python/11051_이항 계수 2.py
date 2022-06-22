import sys

n, k = list(map(int, sys.stdin.readline().split()))

ncr = [[00 for col in range(1001)] for row in range(1001)]

ncr[0][0] = 1

for i in range(1, 1001):
    for j in range(0, i+1):
        if j == 0:
            ncr[i][j] = 1
        elif j == i:
            ncr[i][j] = 1
        else:
            ncr[i][j] = (ncr[i-1][j] + ncr[i-1][j-1]) % 10007

print(ncr[n][k])
