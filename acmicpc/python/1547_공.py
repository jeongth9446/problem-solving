n = int(input())

arr = [0, 1, 2, 3]

for i in range(n):
    a, b = list(map(int, input().split()))

    if a == b:
        pass
    else:
        if arr[1] == a:
            x = 1
        elif arr[2] == a:
            x = 2
        elif arr[3] == a:
            x = 3
        if arr[1] == b:
            y = 1
        elif arr[2] == b:
            y = 2
        elif arr[3] == b:
            y = 3
        arr[x], arr[y] = arr[y], arr[x]


print(arr[1])