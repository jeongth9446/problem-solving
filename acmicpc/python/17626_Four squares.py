import sys

n = int(sys.stdin.readline())

S = list()

res = [99999 for item in range(50001)]
res[0] = 0
res[1] = 1
res[2] = 2

for i in range(1, int(pow(50000, 0.5))+1):
    S.append(i*i)

S.sort(reverse=True)

for i in range(1, n+1):
    for item in S:
        if item > i:
            pass
        else:
            res[i] = min(res[i], res[i-item]+1)
sys.stdout.write(str(res[n]))

S.sort()