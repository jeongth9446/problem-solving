bag = [0] * 5005
bag[3] = 1
bag[5] = 1

for i in range(6, 5004):
    m = 10000
    if bag[i-3] != 0 and m > bag[i-3] + 1:
        m = bag[i-3] + 1
    if bag[i-5] != 0 and m > bag[i-5] + 1:
        m = bag[i-5] + 1
    bag[i] = m

n = int(input())

if bag[n] == 0 or bag[n] >= 10000:
    print(-1)
else:
    print(bag[n])
