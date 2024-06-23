import sys

n = int(input())
a = list(map(int, input().split()))

posList = list()
negList = list()

posRes = list()
for i in range(n):
    posRes.append(0)

negRes = list()
for i in range(n):
    negRes.append(0)

totRes = list()
for i in range(n):
    totRes.append(0)

for i in range(n):
    if i == 0:
        posList.append(a[i])
        posRes[i] = 1
    else:
        s = 0
        e = len(posList) - 1
        while s <= e:
            m = (s + e) // 2

            if a[i] > posList[m]:
                s = m + 1
            else:
                e = m - 1

        if s == len(posList):
            posList.append(a[i])
        else:
            posList[s] = a[i]
        posRes[i] = s + 1

for i in reversed(range(n)):
    if i == n - 1:
        negList.append(a[i])
        negRes[i] = 1
    else:
        s = 0
        e = len(negList) - 1
        while s <= e:
            m = (s + e) // 2

            if a[i] > negList[m]:
                s = m + 1
            else:
                e = m - 1
        if s == len(negList):
            negList.append(a[i])
        else:
            negList[s] = a[i]
        negRes[i] = s + 1

res = 0

for i in range(n):
    totRes[i] = posRes[i] + negRes[i] - 1
    if res < totRes[i]:
        res = totRes[i]

print(res)


print(" @@@   @@@ ")
print("@   @ @   @")
print("@    @    @")
print("@         @")
print(" @       @ ")
print("  @     @  ")
print("   @   @   ")
print("    @ @    ")
print("     @     ")
