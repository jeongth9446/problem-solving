n, t, p = list(map(int, input().split()))

input_table = list()
zeros_t = [0 for _ in range(t)]
ones_n = list()
score_n = [0 for _ in range(n)]

for idx in range(n):
    input_table.append(list(map(int, input().split())))
    ones_n.append(sum(input_table[idx]))

for score_p in range(t):
    for j in range(n):
        if input_table[j][score_p] == 0:
            zeros_t[score_p] += 1

for score_p in range(n):
    for j in range(t):
        score_n[score_p] += input_table[score_p][j] * zeros_t[j]

p -= 1

res = 1
ones_p = ones_n[p]
score_p = score_n[p]

for idx in range(n):
    if score_n[idx] > score_p:
        res += 1
    if score_n[idx] == score_p and ones_n[idx] > ones_p:
        res += 1
    if score_n[idx] == score_p and ones_n[idx] == ones_p and idx < p:
        res += 1

print(score_p, res)
