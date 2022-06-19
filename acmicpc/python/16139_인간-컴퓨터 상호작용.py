import sys

s = sys.stdin.readline().strip()

n = int(sys.stdin.readline())

list_s = list()
list_e = list()
acc = list()
char = ''
for i in range(0, n):
    k, start, end = list(map(str, sys.stdin.readline().split()))
    char = k
    list_s.append(int(start))
    list_e.append(int(end))

cnt = 0

for item in s:
    # print(item)
    if item == char:
        cnt += 1
    acc.append(cnt)

for i in range(0, n):
    if list_s[i] == 0:
        sys.stdout.write(str(acc[list_e[i]]) + "\n")
    else:
        sys.stdout.write(str(acc[list_e[i]] - acc[list_s[i]-1]) + "\n")

