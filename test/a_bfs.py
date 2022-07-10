# 한 붓 그리기 문제.
import collections
import queue
import sys


input = sys.stdin.readline

n, m = list(map(int, input().split()))


chk2 = [0 for _ in range(500005)]

grp = collections.defaultdict(list)
q = queue.Queue(maxsize=500005)

grp_cnt = 0

odd_cnt = [0 for _ in range(500005)]

for _ in range(m):
    u, v = list(map(int, input().split()))
    grp[u].append(v)
    grp[v].append(u)

for idx in range(1, n + 1):
    if len(grp[idx]) == 0:  # 연결되지 않은 노드 --- 무시
        pass
    elif chk2[idx] == 1:  # 이미 처리한 노드 --- 무시
        pass
    else:
        chk2[idx] = 1
        grp_cnt += 1
        if len(grp[idx]) % 2 == 1:
            odd_cnt[grp_cnt] += 1
        q.put(idx)

        while not q.empty():
            t = q.get()
            if t > 100:
                pass
            for item in grp[t]:
                if chk2[item] == 0:
                    chk2[item] = 1
                    if len(grp[item]) % 2 == 1:
                        odd_cnt[grp_cnt] += 1
                    q.put(item)

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