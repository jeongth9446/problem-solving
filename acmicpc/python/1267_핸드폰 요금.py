n = int(input())

arr = list(map(int, input().split()))

Y = 0
M = 0
for item in arr:
    Y += 10 * (item//30 + 1)
    M += 15 * (item // 60 + 1)

if Y == M:
    print("Y M " + str(Y))
elif Y < M:
    print("Y " + str(Y))
else:
    print("M " + str(M))
