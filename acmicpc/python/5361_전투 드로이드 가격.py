
price = [350.34, 230.90, 190.55, 125.30, 180.90]


n = int(input())

for _ in range(n):
    s = list(map(int, input().split()))

    res = sum(list(map(lambda x, y: x*y, price, s)))

    print("$" + "{0:.2f}".format(res))