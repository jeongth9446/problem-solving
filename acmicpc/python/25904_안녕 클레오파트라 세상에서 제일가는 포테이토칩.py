n, x = list(map(int, input().split()))
t = list(map(int, input().split()))

while True:
    for idx in range(n):
        if t[idx] < x:
            print(idx + 1)
            exit(0)
        x += 1
