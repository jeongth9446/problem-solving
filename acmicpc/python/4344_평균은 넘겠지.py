n = int(input())

for t in range(0, n):
    tmp = list(map(int, input().split()))
    m = tmp[0]
    arr = tmp[1:]
    avg = float(sum(arr))/float(m)
    cnt = 0
    for item in arr:
        if item > avg:
            cnt += 1
    print("{0:0.3f}".format(float(cnt)/float(m)*100.0) + "%")


