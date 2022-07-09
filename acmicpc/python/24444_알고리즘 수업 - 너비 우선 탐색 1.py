import collections
import queue
import sys

input = sys.stdin.readline

q = queue.Queue()

n, m, r = list(map(int, input().split()))

grp = collections.defaultdict(list)
visited = [False for item in range(100001)]
res = [0 for item in range(100001)]

for _ in range(m):
    u, v = list(map(int, input().split()))
    grp[u].append(v)
    grp[v].append(u)

for idx in range(1, n+1):
    grp[idx].sort()

q.put(r)
res[r] = 1
visited[r] = True
cnt = 1

while not q.empty():
    t = q.get()
    for item in grp[t]:
        if visited[item]:
            pass
        else:
            cnt += 1
            res[item] = cnt
            visited[item] = True
            q.put(item)

for i in range(1, n+1):
    print(res[i])
