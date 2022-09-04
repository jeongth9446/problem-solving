a, b = list(map(str, input().split()))

a = int("".join(reversed(list(a))))
b = int("".join(reversed(list(b))))
c = str(a + b)
c = int("".join(reversed(list(c))))

print(c)
