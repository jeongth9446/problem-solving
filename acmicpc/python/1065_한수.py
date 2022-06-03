n = int(input())

cnt = 0


def func_han_num(n: int) -> bool:
    tmp = list(map(int, list(str(n))))

    for i in range(0, len(tmp)-2):
        if tmp[i] - tmp[i + 1] is not tmp[i + 1] - tmp[i + 2]:
            return False

    return True


for i in range(1, n + 1):
    if func_han_num(i): cnt += 1

print(cnt)