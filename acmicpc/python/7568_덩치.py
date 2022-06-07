n = int(input())

arr_weight = [0] * 51
arr_height = [0] * 51
arr_res = [0] * 51
for k in range(0, n):
    arr_weight[k], arr_height[k] = map(int, input().split())

for k in range(0, n):
    weight = arr_weight[k]
    height = arr_height[k]
    cnt = 0
    for j in range(0, n):
        if weight < arr_weight[j] and height < arr_height[j]:
            cnt += 1

    arr_res[k] = cnt + 1

for k in range(0, n):
    print(arr_res[k], "", end="")
