import collections

n, p = list(map(int, input().split()))

s = collections.defaultdict(int)
k = n
cnt = 0
while True:
    # print(s)
    if s[k] != 0:
        print(cnt - s[k] + 1)
        break
    else:
        cnt += 1
        s[k] = cnt
        k = k * n % p
