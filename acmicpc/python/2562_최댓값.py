arr = []

for i in range(0, 9):
    arr.append(int(input()))

_max = max(arr)

for i in range(0, 9):
    if arr[i] == _max:
        print(_max)
        print(i+1)
