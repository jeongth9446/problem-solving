
arr = list()
m = 0

for i in range(9):
    arr.append(list(map(int, input().split())))
    m = max(m, max(arr[i]))
print(m)

for i in range(9):
    for j in range(9):
        if arr[i][j] == m:
            print(i+1, j+1)
            exit()
