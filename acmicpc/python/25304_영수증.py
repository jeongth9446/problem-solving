res = int(input())

n = int(input())

for i in range(n):
    a, b = list(map(int, input().split()))

    res -= a*b

if res == 0:
    print("Yes")
else:
    print("No")