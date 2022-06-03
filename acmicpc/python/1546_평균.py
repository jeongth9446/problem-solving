n = int(input())

input_arr = list(map(int, input().split()))

M = max(input_arr)
res = list()
sum = 0.0

for item in input_arr:
    sum += item/M * 100.0

print(sum / n)
