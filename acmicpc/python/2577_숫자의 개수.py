arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

a = int(input())
b = int(input())
c = int(input())

res = list(str(a * b * c))

for i in res:
    arr[int(i)] += 1

for i in range(0, 10):
    print(arr[i])
