# 노래 곡수 : N
# 여행길 : K
import collections
import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, k = list(map(int, input().split()))

seta = set()

cnt = 0
dic = collections.defaultdict(int)
chk = collections.defaultdict(bool)
max_len = 0
max_str = ""

a = list()

def dfs(idx):
    global dic
    global chk
    global cnt
    global seta
    global a, cur_len, cur_str, max_len, max_str

    # print("init", cnt)

    if cnt == k:
        # print("good")
        max_len = cur_len
        max_str = cur_str
        # print(seta)
        return
    elif cnt > k:
        return
    else:
        for item in range(idx+1, len(a)):
            t = max_len-1
            while t <= len(cur_str) and t <= len(a[item][0]) and cur_str[0:t] == a[item][0][0:t]:
                t += 1
            tmp_len = cur_len
            tmp_str = cur_str
            cur_len = t-1
            cur_str = cur_str[0:t-1]

            if (a[item][0] not in seta) and (chk[a[item][0]] == False):
                if (cur_len > max_len) or (cur_len == max_len and cur_str < max_str):
                    cnt += a[item][1]
                    seta.add(a[item][0])
                    # print("before", cnt)
                    dfs(item)
                    cnt -= a[item][1]
                    seta.remove(a[item][0])

            cur_len = tmp_len
            cur_str = tmp_str


for _ in range(n):
    s, l = list(map(str, input().split()))
    l = int(l)
    a.append([s, l])

a.sort()
# print(a)
for idx in range(len(a)):
    cur_len = len(a[idx][0])
    cur_str = a[idx][0]
    if (cur_len > max_len) or (cur_len == max_len and cur_str < max_str):
        chk[a[idx][0]] = True
        # print("start : " + a[idx][0])
        cnt += a[idx][1]
        seta.add(a[idx][0])
        # print(idx)
        dfs(idx)
        cnt -= a[idx][1]
        seta.remove(a[idx][0])


print(max_len, max_str)

