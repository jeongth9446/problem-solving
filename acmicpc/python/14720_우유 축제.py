n = int(input())

A = list(map(int, input().split()))

next_milk = 0
idx = 0
res = 0

while idx < len(A):
    if A[idx] == 0:
        res += 1
        next_milk = 1
        break
    idx += 1

for i in range(idx, len(A)):
    if A[i] == next_milk:
        res += 1
        next_milk = (next_milk + 1) % 3

print(res)
