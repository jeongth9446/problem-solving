n = input()

for _ in range(3):
    if len(n) % 3 != 0:
        n = "0" + n

for i in range(0, len(n), 3):
    k = n[i:i+3]
    if (k == '000'): print("0",end="")
    if (k == '001'): print("1",end="")
    if (k == '010'): print("2",end="")
    if (k == '011'): print("3",end="")
    if (k == '100'): print("4",end="")
    if (k == '101'): print("5",end="")
    if (k == '110'): print("6",end="")
    if (k == '111'): print("7",end="")
