h, m, s = list(map(int, input().split(":")))
hh, mm, ss = list(map(int, input().split(":")))

resh, resm, ress = hh-h, mm-m, ss-s

if ress < 0:
    resm -= 1
    ress += 60

if resm < 0:
    resh -= 1
    resm += 60

if resh < 0:
    resh += 24

if resh == 0 and resm == 0 and ress == 0:
    resh = 24

print("{0:02d}:{1:02d}:{2:02d}".format(resh, resm, ress))