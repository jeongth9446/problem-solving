a = input()

x = int(a[0])
y = int(a[4])
z = int(a[8])

p = a[2]

if p == "+":
    if x + y == z:
        print("YES")
    else:
        print("NO")
if p == "-":
    if x - y == z:
        print("YES")
    else:
        print("NO")
if p == "/":
    if x / y == z:
        print("YES")
    else:
        print("NO")
if p == "*":
    if x * y == z:
        print("YES")
    else:
        print("NO")
