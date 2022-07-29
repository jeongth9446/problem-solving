l, r, a = list(map(int, input().split()))

while a > 0:
    if l > r:
        r += 1
        a -= 1
    else:
        l += 1
        a -= 1

print(min(l, r) * 2)
