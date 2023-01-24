n = int(input())

arr = list("BABCBCDCDADAB")

for _ in range(n):
    k = int(input())
    print(arr[k % 12])
