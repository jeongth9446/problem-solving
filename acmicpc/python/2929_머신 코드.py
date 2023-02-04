s = list(input())

res = 0
p = 0
for idx in range(len(s)):
    if s[idx].isupper():
        if (idx + res) % 4 == 0:
            pass
        else:
            while (idx+res) % 4 != 0:
                res += 1

print(res)