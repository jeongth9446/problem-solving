n = int(input())
arr = input().split()

arr_set = set()

for i in range(0, n):
    arr[i] = int(arr[i])
    arr_set.add(arr[i])

if len(arr_set) >= 3:
    print("YES")
else:
    print("NO")