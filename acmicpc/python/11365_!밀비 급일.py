while True:
    s = list(input())
    if s[0] == 'E' and s[1] == 'N' and s[2] == 'D':
        exit()
    else:
        print("".join(reversed(s)))
