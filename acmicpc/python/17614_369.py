n = int(input())


def clap(s: list):
    res = 0
    for l in s:
        if l == '3' or l == '6' or l == '9':
            res += 1
    return res


res = 0

for item in range(n + 1):
    k = list(str(item))

    res += clap(k)

print(res)
