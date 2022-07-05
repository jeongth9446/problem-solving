import collections
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = collections.defaultdict(list)
chk = collections.defaultdict(bool)


def dfs(k: int):
    global graph
    global chk

    t = graph[k]
    # print(t)
    for item in t:
        if chk[item]:
            pass
        else:
            chk[item] = True
            dfs(item)


res = 0

for i in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if chk[i]:
        pass
    else:
        res += 1
        chk[i] = True
        dfs(i)

print(res)
