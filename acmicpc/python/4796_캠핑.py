# 4796 캠핑

case = 1
while True:
    L, P, V = list(map(int, input().split()))

    # break condition
    if L == P == V == 0:
        break

    print("Case " + str(case) + ": " + str((V // P) * L + min((V % P), L)))
    case += 1