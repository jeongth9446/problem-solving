def multiply(k: list):
    res = 1
    for item in k:
        res *= item
    return res


n = list(map(int, list(input())))

for i in range(len(n) - 1):
    if multiply(n[0:i + 1]) == multiply(n[i + 1: len(n)]):
        print("YES")
        exit(0)

print("NO")
