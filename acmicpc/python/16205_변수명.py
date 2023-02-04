a, b = list(map(str, input().split()))
b = list(b)
flag = 0
for idx in range(len(b)):
    if idx == 0:
        print(b[idx].lower(), end="")
    elif b[idx] == "_":
        flag = 1
    elif flag == 1:
        print(b[idx].upper(), end="")
        flag = 0
    else:
        print(b[idx], end="")
print()

for idx in range(len(b)):
    if idx == 0:
        print(b[idx].lower(), end="")
    elif b[idx] == "_":
        print(b[idx], end="")
    elif b[idx].isupper():
        print("_", end="")
        print(b[idx].lower(), end="")
    else:
        print(b[idx], end="")
print()

for idx in range(len(b)):
    if idx == 0:
        print(b[idx].upper(), end="")
    elif b[idx] == "_":
        flag = 1
    elif flag == 1:
        print(b[idx].upper(), end="")
        flag = 0
    else:
        print(b[idx], end="")
print()