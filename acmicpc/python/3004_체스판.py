n = int(input())

res = 0
flag = 0
cnt = 2
for i in range(1, n+1):
    res += cnt
    if i != 1:
        flag += 1

    if(flag == 2):
        flag = 0
        cnt += 1

print(res)