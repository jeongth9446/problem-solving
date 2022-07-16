import sys

input = sys.stdin.readline

n = int(input())

x_list = list()
y_list = list()

for _ in range(n):
    x, y = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)

x_list.sort()
y_list.sort()

print(abs((x_list[0] - x_list[n-1]) * (y_list[0] - y_list[n-1])))