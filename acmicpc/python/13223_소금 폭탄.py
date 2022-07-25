h, m, s = list(map(int, input().split(":")))
hh, mm, ss = list(map(int, input().split(":")))

d = h * 60 * 60 + m * 60 + s
dd = hh * 60 * 60 + mm * 60 + ss

if dd <= d:
    dd += 24 * 60 * 60

k = dd - d

h = int(k / 3600)
k %= 3600
m = int(k / 60)
k %= 60
s = k

print("{0:02d}:{1:02d}:{2:02d}".format(h, m, s))
