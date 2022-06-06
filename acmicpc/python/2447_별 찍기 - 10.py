def nf(k: int) -> list:
    t = list()
    for i in range(0, 3 ** k):
        t.append(list())
        for j in range(0, 3 ** k):
            t[i].append(False)
    return t


def f(k: int) -> list:
    if k == 1:
        return [[True, True, True], [True, False, True], [True, True, True]]
    else:
        tmp = list(map(list.__add__, f(k - 1), f(k - 1)))
        tmp = list(map(list.__add__, tmp, f(k - 1)))
        tmp2 = list(map(list.__add__, f(k - 1), nf(k - 1)))
        tmp2 = list(map(list.__add__, tmp2, f(k - 1)))

        return tmp + tmp2 + tmp


n = int(input())
m = n
k = 0

while m != 1:
    k += 1
    m /= 3
arr = f(k)

for i in range(0, n):
    for j in range(0, n):
        if arr[i][j]:
            print("*", end="")
        else:
            print(" ", end="")
    print()
