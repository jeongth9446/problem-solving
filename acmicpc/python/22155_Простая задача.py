n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))
    if (a <= 2 and b <= 1) or (a <= 1 and b <= 2):
        print("Yes")
    else:
        print("No")
