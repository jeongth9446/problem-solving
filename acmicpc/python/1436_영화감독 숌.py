n = int(input())

cnt = 0

for i in range(1, 100000000):
    t = str(i)
    if t.find("666") != -1:
        cnt += 1

    if cnt == n:
        print (i)
        exit()

