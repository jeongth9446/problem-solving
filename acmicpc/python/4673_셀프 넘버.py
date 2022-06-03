def d(n: int) -> int:
    tmp = list(map(int, list(str(n))))
    return n + sum(tmp)


dic = dict()

for i in range(1, 10001):
    dic[d(i)] = True

for i in range(1, 10000):
    if i in dic:
        pass
    else:
        print(i)
