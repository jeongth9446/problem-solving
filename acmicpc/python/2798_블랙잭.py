n, m = map(int, input().split())

in_arr = list(map(int, input().split()))

diff = m
for i, item_i in enumerate(in_arr):
    for j, item_j in enumerate(in_arr):
        for k, item_k in enumerate(in_arr):
            if i == j or i == k or j == k:
                continue
            else:
                if item_i + item_j + item_k <= m and m - (item_i + item_j + item_k) < diff:
                    diff = m - (item_i + item_j + item_k)

print(m - diff)
