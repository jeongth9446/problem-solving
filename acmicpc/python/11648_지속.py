n = int(input())

res = 0

while True:
    if n < 10:
        break
    res += 1

    k = list(map(int, list(str(n))))
    n = 1
    for item in k:
        n *= item

print(res)