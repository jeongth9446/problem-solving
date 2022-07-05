import collections
import heapq
import sys

input = sys.stdin.readline

t = int(input())

for k in range(t):
    n = int(input())

    dic = collections.defaultdict(int)
    min_hq = []
    max_hq = []
    cnt = 0
    for i in range(n):
        a, b = list(map(str, input().split()))
        c = int(b)
        if a == "I":
            heapq.heappush(min_hq, c)
            heapq.heappush(max_hq, -c)
            dic[c] += 1
            cnt += 1
        else:
            if cnt == 0:
                pass
            else:
                if c == 1:
                    while len(max_hq) > 0:
                        t = -heapq.heappop(max_hq)
                        if dic[t] != 0:
                            dic[t] -= 1
                            break
                else:
                    while len(min_hq) > 0:
                        t = heapq.heappop(min_hq)
                        if dic[t] != 0:
                            dic[t] -= 1
                            break
                cnt -= 1
            if cnt == 0:
                while len(max_hq) != 0:
                    heapq.heappop(max_hq)
                while len(min_hq) != 0:
                    heapq.heappop(min_hq)

    if cnt == 0:
        print("EMPTY")
    else:
        while len(max_hq) > 0:
            t = -heapq.heappop(max_hq)
            if dic[t] != 0:
                break
        while len(min_hq) > 0:
            kk = heapq.heappop(min_hq)
            if dic[kk] != 0:
                break
        print(t, kk)
