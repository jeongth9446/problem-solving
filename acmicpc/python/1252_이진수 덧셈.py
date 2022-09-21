x, y = list(map(str, input().split()))
x = list(x)
y = list(y)
x.reverse()
y.reverse()
z = list()

p = 0
flag = 0

while(len(x) < len(y)):
    x.append("0")
while(len(y) < len(x)):
    y.append("0")

x.append("0")
y.append("0")

while p < len(x):
    if x[p] == "1" and y[p] == "1":
        if flag == 1:
            z.append("1")
            flag = 1
        else:
            z.append("0")
            flag = 1
    elif x[p] == y[p] == "0":
        if flag == 1:
            z.append("1")
            flag = 0
        else:
            z.append("0")
            flag = 0
    else:
        if(flag == 1):
            z.append("0")
            flag = 1
        else:
            z.append("1")
            flag = 0
    p += 1
while len(z) > 1 and z[-1] == "0":
    z.pop()

z.reverse()

print("".join(z))
