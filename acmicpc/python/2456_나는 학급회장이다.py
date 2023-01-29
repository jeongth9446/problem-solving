n = int(input())

a = [0 for _ in range(4)]
b = [0 for _ in range(4)]
c = [0 for _ in range(4)]
for _ in range(n):
    x, y, z = list(map(int, input().split()))
    a[0] += x
    b[0] += y
    c[0] += z
    a[x] += 1
    b[y] += 1
    c[z] += 1

s = list()
s.append([1, a])
s.append([2, b])
s.append([3, c])

# print(s)

s.sort(key=lambda x: [-x[1][0], -x[1][3], -x[1][2]])

if s[0][1] == s[1][1]:
    print(0, s[0][1][0])
else:
    print(s[0][0], s[0][1][0])
# print(s)
