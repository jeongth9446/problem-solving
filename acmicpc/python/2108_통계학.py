import sys

n = int(sys.stdin.readline())

# 초기화
mode_arr = [0] * 8001
min_ = 4000
max_ = -4000
acc = 0

mode1_i = 0
mode1_n = 0
mode2_i = 4000
mode2_n = 0

for i in range(0, n):
    #input
    t = int(sys.stdin.readline())

    # 누적한다
    acc += t

    # 최소값 갱신
    if min_ > t:
        min_ = t
    # 최대값 갱신
    if max_ < t:
        max_ = t

    # 빈도 수 누적
    mode_arr[t+4000] += 1
    if mode1_n < mode_arr[t+4000]: # 새로운 큰 빈도의 숫자 등장
        mode2_i = 4000 # 초기화
        mode2_n = 0 # 초기화
        mode1_i = t # 갱신
        mode1_n = mode_arr[t+4000] # 갱신
    elif mode1_n == mode_arr[t+4000]: # 현재 최대 빈도와 같은 숫자 등장
        if t < mode1_i:
            mode2_i = mode1_i
            mode2_n = mode1_n
            mode1_i = t
            mode1_n = mode_arr[t+4000]
        elif t < mode2_i:
            mode2_i = t
            mode2_n = mode_arr[t+4000]

ab = 0
for i, item in enumerate(mode_arr):
    ab += item
    if ab >= (n+1)/2:
        ab = i
        break


print(round(float(acc) / float(n)))
print(ab - 4000)
if mode2_n == 0:
    print(mode1_i)
else:
    print(mode2_i)
print(max_ - min_)
