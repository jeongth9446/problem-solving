import math

n = int(input())

x = (-0.5 + (0.25 + 2 * n)**0.5)

x_end = math.floor(x)

a = x_end * (x_end+1) / 2

m = int(n - a)

if m == 0:
    if x_end % 2 != 0:
        print("1/" + str(x_end))
    else:
        print(str(x_end) +"/1")
else:
    if x_end % 2 == 0:
        print(str(x_end+2-m)+ "/" + str(m))
    else:
        print(str(m) +"/" + str(x_end+2-m))
