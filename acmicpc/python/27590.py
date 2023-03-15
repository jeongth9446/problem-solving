s1, s2 = list(map(int, input().split()))
m1, m2 = list(map(int, input().split()))

s = -s1
m = -m1

while s != m:
    if m < s:
        m += m2
    else:
        s += s2

print(s)
