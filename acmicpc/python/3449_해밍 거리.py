t = int(input())

for _ in range(t):
    a = list(input())
    b = list(input())

    cnt = 0

    for idx in range(len(a)):
        if a[idx] != b[idx]:
            cnt += 1

    print("Hamming distance is {0:d}.".format(cnt))
