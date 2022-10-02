i, j, k = list(map(int, input().split()))
s = list(input())

a = min(i, j, k)
c = max(i, j, k)
b = sum([i, j, k]) - a - c

for item in s:
    if item == 'A':
        print(a, end=" ")
    elif item == 'B':
        print(b, end=" ")
    elif item == 'C':
        print(c, end=" ")
