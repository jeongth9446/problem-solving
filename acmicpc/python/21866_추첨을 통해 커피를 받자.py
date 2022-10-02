arr = list(map(int, input().split()))

max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

hacker_flag = 0
for idx in range(9):
    if arr[idx] > max_score[idx]:
        hacker_flag = 1

draw_flag = 0

if sum(arr) >= 100:
    draw_flag = 1

if hacker_flag == 1:
    print("hacker")
elif draw_flag == 1:
    print("draw")
else:
    print("none")