

for a in range(1, 101):
    for b in range(2, a+1):
        for c in range(b, a+1):
            for d in range(c, a+1):
                if pow(a, 3) == pow(b, 3) + pow(c, 3) + pow(d, 3):
#                    print(a, b, c, d, pow(a, 3), pow(b, 3), pow(c, 3), pow(d, 3))
                    print("Cube = " + str(a) + ", Triple = (" + str(b) + "," + str(c) + "," + str(d) + ")")