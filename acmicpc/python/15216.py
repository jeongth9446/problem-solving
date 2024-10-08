h, w, n = list(map(int, input().split()))

a = list(map(int, input().split()))

x, y = 0, 0

for i in a:
    if x == w:
        x = 0
        y += 1
    if y == h:
        print("YES")
        exit(0)
    if x + i <= w:
        x += i
    else:
        print("NO")
        exit(0)

if x == w:
    x = 0
    y += 1
if y == h:
    print("YES")
    exit(0)
else:
    print("NO")
    exit(0)
