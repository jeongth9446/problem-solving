h, m, s = list(map(int, input().split()))

amount = int(input())

s += amount

m += s // 60
s = s % 60
h += m // 60
m = m % 60
h %= 24

print(h, m, s)