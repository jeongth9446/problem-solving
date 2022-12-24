s = list(input())
a = 0
b = 0
for item in s:
    if item == "A":
        a += 1
    else:
        b += 1

print(a, ":", b)
