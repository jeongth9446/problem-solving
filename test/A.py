# 한 붓 그리기 문제.
import collections
import sys

sys.setrecursionlimit(500005)

input = sys.stdin.readline

n, m = list(map(int, input().split()))

chk = [0 for _ in range(500005)]

chk2 = [0 for _ in range(500005)]

grp = collections.defaultdict(list)

grp_cnt = 0

odd_cnt = [0 for _ in range(500005)]


def dfs(k: int):
    global grp
    global grp_cnt
    global chk
    global chk2
    global n, m

    for item in grp[k]:
        if chk2[item] == 0:
            chk2[item] = 1
            if chk[item] % 2 == 1:
                odd_cnt[grp_cnt] += 1
            dfs(item)


for _ in range(m):
    u, v = list(map(int, input().split()))
    chk[u] += 1
    chk[v] += 1
    grp[u].append(v)
    grp[v].append(u)

for idx in range(1, n + 1):
    if chk[idx] == 0:  # 연결되지 않은 노드 --- 무시
        pass
    elif chk2[idx] == 1:  # 이미 처리한 노드 --- 무시
        pass
    else:
        chk2[idx] = 1
        grp_cnt += 1
        if chk[idx] % 2 == 1:
            odd_cnt[grp_cnt] += 1
        dfs(idx)

if grp_cnt == 0:  # 없으면
    print(0)
    exit()
else:
    odd = odd_cnt[1]
    # print(odd)
    # print (odd_cnt[2:grp_cnt+1])
    if grp_cnt > 1:
        for idx in range(2, grp_cnt + 1):
            if odd > 0 and odd_cnt[idx] > 0:  # 홀수인 게 둘 다 있으면
                odd = odd + odd_cnt[idx] - 2
            elif odd > 0 and odd_cnt[idx] == 0:
                pass
            elif odd == 0 and odd_cnt[idx] > 0:
                odd = odd_cnt[idx]
            else:
                odd = odd + odd_cnt[idx] + 2
            # print(odd)

    print((odd // 2) + grp_cnt - 1)
