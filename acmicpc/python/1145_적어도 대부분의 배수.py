arr = list(map(int, input().split()))

idx = 1

while True:
    cnt = 0
    for item in arr:
        if idx % item == 0:
            cnt += 1

    if cnt >= 3:
        print(idx)
        break
    idx += 1
