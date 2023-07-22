def checker(s: str):
    # print(s)

    if diff(s, '000000') <= 1:
        return 'A'
    if diff(s, '001111') <= 1:
        return 'B'
    if diff(s, '010011') <= 1:
        return 'C'
    if diff(s, '011100') <= 1:
        return 'D'
    if diff(s, '100110') <= 1:
        return 'E'
    if diff(s, '101001') <= 1:
        return 'F'
    if diff(s, '110101') <= 1:
        return 'G'
    if diff(s, '111010') <= 1:
        return 'H'
    else:
        return 'X'


def diff(a: str, b: str):
    x = 0
    y = list(map(int, list(a)))
    z = list(map(int, list(b)))
    for i in range(len(y)):
        if y[i] != z[i]:
            x += 1
    return x


n = int(input())

s = input()

res = ''

for i in range(n):
    p = checker(s[i * 6:(i + 1) * 6])
    if p == 'X':
        print(i + 1)
        exit()
    else:
        res = res + p

print(res)
