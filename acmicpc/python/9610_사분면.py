n = int(input())

Q1 = Q2 = Q3 = Q4 = AXIS = 0

for _ in range(n):
    x, y = list(map(int, input().split()))

    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    else:
        Q4 += 1

print("Q1: " + str(Q1))
print("Q2: " + str(Q2))
print("Q3: " + str(Q3))
print("Q4: " + str(Q4))
print("AXIS: " + str(AXIS))