n = int(input())
res = 0

for i in range(1, n+1):
    k = str(i)
    # print(list(map(int, list(map(str, k)))))
    s = sum(list(map(int, list(map(str, k)))))

    if i % s == 0:
        res += 1

print(res)