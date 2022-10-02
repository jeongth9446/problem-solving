t = int(input())

for _ in range(t):
    n = input()
    arr = list(map(int, input().split()))
    print(min(arr), max(arr))

