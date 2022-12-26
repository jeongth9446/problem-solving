n = int(input())

for _ in range(n):
    s = list(map(float, input().split()))

    k = 1
    for item in s:
        k *= item

    print("$" + format(k, "0.2f"))
