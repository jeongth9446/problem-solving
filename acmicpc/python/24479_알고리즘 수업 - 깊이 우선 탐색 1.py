import collections
import sys
sys.setrecursionlimit(100001)

input = sys.stdin.readline

n, m, r = list(map(int, input().split()))

grp = collections.defaultdict(list)
visited = [False for col in range(100001)]
res = [0 for col in range(100001)]
cnt = 0

def dfs(r: int):
    global grp
    global visited
    global cnt

    cnt += 1
    res[r] = cnt
    for item in grp[r]:
        if visited[item]:
            pass
        else:
            visited[item] = True
            dfs(item)

for _ in range(m):
    u, v = list(map(int, input().split()))
    grp[u].append(v)
    grp[v].append(u)

for idx in range(1, n+1):
    grp[idx].sort()

# print(grp)

visited[r] = True
dfs(r)

for i in range(1, n+1):
    print(res[i])