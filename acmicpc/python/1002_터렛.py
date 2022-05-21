n = int(input())

for a in range(0, n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist_pow = pow((x1 - x2), 2) + pow((y1 - y2), 2)
    r_plus_pow = pow(r1 + r2, 2)
    r_minus_pow = pow(r1 - r2, 2)

    if dist_pow == 0 and r_minus_pow == 0: print(-1)
    elif r_minus_pow < dist_pow < r_plus_pow: print(2)
    elif r_plus_pow == dist_pow or r_minus_pow == dist_pow: print(1)
    else: print(0)
