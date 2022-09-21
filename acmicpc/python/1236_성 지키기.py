n, m = list(map(int, input().split()))

row = [0 for _ in range(n)]
col = [0 for _ in range(m)]

for idx in range(n):
    a = list(input())
    for i in range(m):
        if a[i] == 'X':
            row[idx] = 1
            col[i] = 1

print(max(len(row) - sum(row), len(col) - sum(col)))