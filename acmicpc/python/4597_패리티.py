import sys

input = sys.stdin.readline

while True:
    k = list(input())
    flag = 1 # 1:even, -1:odd
    if k[0] == "#":
        break

    for item in k:
        if item == "1":
            flag *= -1
            print(item, end="")
        elif item == "0":
            print(item, end="")
        elif item == "e":
            if flag > 0:
                print("0")
            else:
                print("1")
        elif item == "o":
            if flag < 0:
                print("0")
            else:
                print("1")
