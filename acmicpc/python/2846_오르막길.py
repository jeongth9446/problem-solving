n = int(input())

road = list(map(int, input().split()))
road.append(0)

acc = 0
res = 0

for i in range(1, n + 1):
    if road[i] > road[i - 1]:
        acc += road[i] - road[i - 1]
    else:
        if res < acc:
            res = acc
        acc = 0

print(res)