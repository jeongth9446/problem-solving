N = 20
n = int(input())

s = list(input())

pw = [['0' for _ in range(N)] for _ in range(N)]

for idx in range(len(s)):
    if (idx // n) % 2 == 0:
        pw[idx // n][idx % n] = s[idx]
    else:
        pw[idx // n][n - idx % n - 1] = s[idx]

# print(pw)

for i in range(n):
    for j in range(len(s) // n):
        print(pw[j][i], end='')

print()
