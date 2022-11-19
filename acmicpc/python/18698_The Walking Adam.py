n = int(input())

for _ in range(n):
    s = list(input())

    flag = 0
    for idx in range(len(s)):
        if s[idx] == 'D':
            print(idx)
            flag = 1
            break

    if flag == 0:
        print(len(s))
