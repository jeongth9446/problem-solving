import sys

n = int(input())
while True:
    print("? 1")
    sys.stdout.flush()
    s = input()


    if s == "Y":
        print("! 1")
        sys.stdout.flush()
        exit()
