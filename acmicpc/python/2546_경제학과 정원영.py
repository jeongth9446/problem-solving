t = int(input())


def average(v: list):
    k = 0
    for item in v:
        k += item
    return k / len(v)


for _ in range(t):
    _ = input()
    n, m = list(map(int, input().split()))
    niq = list(map(int, input().split()))
    miq = list(map(int, input().split()))

    avg_n = average(niq)
    avg_m = average(miq)

    # print(avg_n, avg_m)
    res = 0
    for item in niq:
        if avg_n > item > avg_m:
            res += 1

    print(res)
