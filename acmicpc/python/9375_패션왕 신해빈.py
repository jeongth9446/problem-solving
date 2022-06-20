import collections
import sys

t = int(sys.stdin.readline())

for _ in range(0, t):
    n = int(sys.stdin.readline())
    clothes = collections.defaultdict(int)
    for i in range(0, n):
        item, category = list(map(str, sys.stdin.readline().split()))
        clothes[category] += 1

    m = 1

    for item in clothes:
        m *= (clothes[item] + 1)

    print(m-1)
