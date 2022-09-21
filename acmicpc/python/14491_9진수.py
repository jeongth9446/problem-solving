n = int(input())

k = list()
while n > 0:
    k.append(n % 9)
    n = int(n/9)

k.reverse()
l = map(str, k)
print("".join(l))