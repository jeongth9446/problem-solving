s = list(input())
if len(s) == 2:
    print(int(s[0]) + int(s[1]))
elif len(s) == 3:
    if int(s[1]) == 0:
        print(int(s[2]) + 10)
    else:
        print(int(s[0]) + 10)
else:
    print(20)