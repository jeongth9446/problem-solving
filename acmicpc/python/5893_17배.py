a = list(input())
res = 0
k = 1
for item in reversed(a):
    res = res + k * int(item)
    k *= 2
res *= 17
s = list()
while res != 0:
    s.append(str(res % 2))
    res = res // 2

print("".join(reversed(s)))