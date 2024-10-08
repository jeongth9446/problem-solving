x = int(input())

s = [64, 32, 16, 8, 4, 2, 1]
res = 0

for i in range(len(s)):
    if x >= s[i]:
        res += 1
        x -= s[i]

    if x == 0:
        break

print(res)
