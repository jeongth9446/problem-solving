today = list(map(int, input().split()))
camp = list(map(int, input().split()))

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

res = 0

# 1000년 이상 예외 처리
if today[0] + 1000 < camp[0]:
    print("gg")
    exit()
elif today[0] + 1000 == camp[0]:
    if today[1] < camp[1]:
        print("gg")
        exit()
    elif today[1] == camp[1]:
        if today[2] <= camp[2]:
            print("gg")
            exit()

if today[0] % 4 == 0:
    month[2] = 29
    if today[0] % 100 == 0:
        month[2] = 28
        if today[0] % 400 == 0:
            month[2] = 29

while True:
    if today == camp:
        print("D-" + str(res))
        break

    res += 1
    today[2] += 1
    if today[2] > month[today[1]]:
        today[2] = 1
        today[1] += 1
        if today[1] > 12:
            today[1] = 1
            today[0] += 1

            if today[0] % 4 == 0:
                month[2] = 29
                if today[0] % 100 == 0:
                    month[2] = 28
                    if today[0] % 400 == 0:
                        month[2] = 29
            else:
                month[2] = 28
