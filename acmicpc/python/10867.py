a = [0 for _ in range(10001)]

n = int(input())

p = list(map(int, input().split()))
for item in p:
    a[item + 5000] = 1

for i in range(3000, 10000):
    if a[i] != 0:
        print(i - 5000, end=" ")
